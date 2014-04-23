describe("Change password page", function() {
	beforeEach(function() {
		$('body').append("<div id='test'><input type='password' id='newPassword'></input><input type='password' id='retypePassword'></input></div>");
	});

	afterEach(function() {
		$('#test').remove();
	});

	it("should return false when new password field is empty", function() {
        var newPassword = $("#newPassword");
		spyOn(newPassword, "val").andReturn(" ");
        checkForm();
		expect(checkForm()).toBeFalsy();
	});

//	it("should submit AJAX request with proper data", function() {
//		var loginData = "{\"jsonrpc\":\"2.0\",\"method\":\"login\",\"params\":[\"root\",\"asdf1234\"],\"id\":1}";
//		$('#username').val("root");
//		$('#password').val("asdf1234");
//		spyOn($, "ajax");
//		login();
//		expect($.ajax.mostRecentCall.args[0]["data"]).toEqual(loginData);
//	});
//
//	afterEach(function() {
//		$('#test').remove();
//	});
});

//describe("SSID page", function() {
//	beforeEach(function() {
//		$("body").append("<div id='test'><input type='text' id='ssid'></input></div>");
//  });
//
//	it("should submit AJAX request to proper URL", function() {
//		authorizationToken = "abcdef123456";
//		spyOn($, "ajax");
//		setSSID();
//		expect($.ajax.mostRecentCall.args[0]["url"]).toEqual("http://192.168.1.1/cgi-bin/luci/rpc/uci?auth="+authorizationToken);
//	});
//
//	it("should submit AJAX request with proper data", function() {
//		var ssidData = "{\"jsonrpc\":\"2.0\",\"method\":\"set\",\"params\":[\"wireless.@wifi-iface[0].ssid=myPrivateNetwork\"],\"id\":1}";
//		$('#ssid').val("myPrivateNetwork");
//		spyOn($, "ajax");
//		setSSID();
//		expect($.ajax.mostRecentCall.args[0]["data"]).toEqual(ssidData);
//	});
//
//	afterEach(function() {
//		$('#test').remove();
//	});
//});
