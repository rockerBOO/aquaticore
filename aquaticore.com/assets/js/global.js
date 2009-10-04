var onloads = new Array();
function addLoadEvent(func) {
	onloads[onloads.length] = func;
}
window.onload = function() {
	for (var i = 0; i < onloads.length; i++) {
		onloads[i]();
	}
}