//
// Script to grab the image, encode it and return
//
// http://stackoverflow.com/questions/22554313/send-captured-images-from-python-server-to-javascript-client

var img = document.getElementById("liveIRImg");
var arrayBuffer;

var ws = new WebSocket("ws://uowebsite.cloudapp.net/ws");
var $message = $("#message");

ws.binaryType = 'arraybuffer';

ws.onopen = function(){
    $message.attr("class", 'label label-info');
    $message.text("Connecting");
    console.log("connection was established");
    img.src = "images/connecting.svg"
};

ws.onmessage = function(evt){
    arrayBuffer = evt.data;
    $message.attr("class", 'label label-success')
    $message.text("Live")
    img.src = "data:image/jpeg;base64," + encode(new Uint8Array(arrayBuffer));
};

function encode (input) {
    var keyStr = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=";
    var output = "";
    var chr1, chr2, chr3, enc1, enc2, enc3, enc4;
    var i = 0;

    while (i < input.length) {
	chr1 = input[i++];
	chr2 = i < input.length ? input[i++] : Number.NaN; // Not sure if the index
	chr3 = i < input.length ? input[i++] : Number.NaN; // checks are needed here

	enc1 = chr1 >> 2;
	enc2 = ((chr1 & 3) << 4) | (chr2 >> 4);
	enc3 = ((chr2 & 15) << 2) | (chr3 >> 6);
	enc4 = chr3 & 63;

	if (isNaN(chr2)) {
	    enc3 = enc4 = 64;
	} else if (isNaN(chr3)) {
	    enc4 = 64;
	}
	output += keyStr.charAt(enc1) + keyStr.charAt(enc2) +
	    keyStr.charAt(enc3) + keyStr.charAt(enc4);
    }
    return output;
}

ws.onclose = function(ev){
    $message.attr("class", 'label label-important');
    $message.text('Not Live');
};
ws.onerror = function(ev){
    $message.attr("class", 'label label-warning');
    $message.text('error occurred');
};
