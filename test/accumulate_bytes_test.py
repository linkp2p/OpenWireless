import unittest
import mock
import sys
import os

sys.path.insert(0, os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    "..", "routerapi"))

import accumulate_bytes
from fake_uci import FakeUci

@mock.patch('accumulate_bytes.common.reset_wifi')
@mock.patch('accumulate_bytes.uci', new_callable = FakeUci)
class AccumulateBytesTest(unittest.TestCase):
    def with_usage_in_mb(self, uci, usage):
        uci.set("openwireless.use_before_last_reset", "0")
        uci.set("openwireless.use_since_last_reset", float(usage) * 1024 * 1024)
        uci.set("openwireless.use_at_last_ui_reset", "0")
        uci.commit("openwireless")

    def test_turn_on_adapter_if_off_and_sufficient_bandwidth(self, uci, reset):
        uci.set("openwireless.maxmonthlybandwidth", "20")
        uci.set("wireless.@wifi-iface[1].disabled", "1")
        self.with_usage_in_mb(uci, "0")
        uci.commit("openwireless")
        uci.commit("wireless")

        accumulate_bytes.update_network_availability()

        self.assertEquals(uci.get("wireless.@wifi-iface[1].disabled"), "0")
        reset.assert_called_with()

    def test_turn_off_adapter_if_on_and_insufficient_bandwidth(self, uci, reset):
        self.with_usage_in_mb(uci, "20")
        uci.set("openwireless.maxmonthlybandwidth", "20")
        uci.set("wireless.@wifi-iface[1].disabled", "0")
        uci.commit("openwireless")
        uci.commit("wireless")

        accumulate_bytes.update_network_availability()

        self.assertEquals(uci.get("wireless.@wifi-iface[1].disabled"), "1")
        reset.assert_called_with()

    def test_do_not_reset_when_not_changing_on_state(self, uci, reset):
        self.with_usage_in_mb(uci, "20")
        uci.set("openwireless.maxmonthlybandwidth", "40")
        uci.set("wireless.@wifi-iface[1].disabled", "0")
        uci.commit("openwireless")
        uci.commit("wireless")

        accumulate_bytes.update_network_availability()

        self.assertFalse(reset.called)

    def test_do_not_reset_when_not_changing_off_state(self, uci, reset):
        self.with_usage_in_mb(uci, "20")
        uci.set("openwireless.maxmonthlybandwidth", "10")
        uci.set("wireless.@wifi-iface[1].disabled", "1")
        uci.commit("openwireless")
        uci.commit("wireless")

        accumulate_bytes.update_network_availability()

        self.assertFalse(reset.called)
