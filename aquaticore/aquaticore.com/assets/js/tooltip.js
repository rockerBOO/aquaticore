//Sigrie Tooltips (External)
// var URL_BASE = '^http://db\\.mmo-champion\\.com'
// var URL_REGEX =  URL_BASE + '/(i|s|a|c|q|is)/([A-Za-z0-9-]+).*'

var URL_BASE = '^http://aquaticore\\.com'
var URL_REGEX =  URL_BASE + '/taxa/(species|genus)/([A-Za-z0-9-]+).*'

// FIXME should be in settings.js
var TOOLTIP_RETRIEVING_HTML = "<span class='tt-retrieving'>Retrieving tooltip...</span>"
var TOOLTIP_MAX_WIDTH = 310;

var DOMAIN = 'aquaticore.com:31337';

var ttlib = {
	init: function() {
		var jstooltip = document.createElement("div");
		jstooltip.id = "tooltip";
		jstooltip.className = "tooltip tt-hover";
		var jstooltipdata = document.createElement("div");
		jstooltipdata.id = "tooltipdata";
		jstooltip.appendChild(jstooltipdata);
		document.getElementsByTagName("body")[0].appendChild(jstooltip);
		ttlib.jstooltip = jstooltip
		ttlib.jstooltipdata = jstooltipdata
		ttlib.hide();
		ttlib.parseDocument();
		ttlib.queue = new Array();
		ttlib.currentRequest = null;
		ttlib.currentMouseover = '';
		ttlib.cache = new Object();
		document.onmousemove = ttlib.mouseMove;
	},
	
	mouseMove: function(e) {
		if (ttlib.jstooltip.style.visibility == "hidden") return;
		var cursor = ttlib.cursorPosition(e);
		var de = document.documentElement;
		var body = document.body;
		var y = cursor.y - 15;
		var x = cursor.x + 20;
		if (cursor.y + ttlib.jstooltip.offsetHeight > de.clientHeight + body.scrollTop + de.scrollTop) {
			var diff = (de.clientHeight+body.scrollTop+de.scrollTop)-(cursor.y+ttlib.jstooltip.offsetHeight);
			y += diff;
		}
		ttlib.jstooltip.style.left = "" + (x) + "px";
		ttlib.jstooltip.style.top = "" + (y) + "px";
	},
	
	request: function(url) {
		var script = document.createElement("script");
		script.type = "text/javascript";
		script.src = url;
		ttlib.currentRequest["tag"] = script;
		document.getElementsByTagName("head")[0].appendChild(script);
	},
	
	queueRequest: function(url) {
		var req = new Object();
		req["url"] = url;
		req["cache"] = url;
		ttlib.queue.push(req);
		ttlib.processQueue();
	},
	
	processQueue: function() {
		if (ttlib.queue.length > 0 && ttlib.currentRequest == null) {
			ttlib.currentRequest = ttlib.queue.pop();
			ttlib.request(ttlib.currentRequest["url"]);
		}
	},
	
	getValid: function(url) {
		if (url.href.match(URL_REGEX)) return url + "/tooltip/js";
		return false; // Disabled wh/wowdb tooltips
		if (url.href.match(WH_URL_REGEX)) {
			var match = url.href.match(WH_URL_REGEX);
			return "http://" + DOMAIN + "/" + match[2][0] + match[3] + "/tooltip/js";
		}
		if (url.href.match(OW_URL_REGEX)) {
			var match = url.href.match(OW_URL_REGEX);
			return "http://" + DOMAIN + "/" + match[2][0] + match[3] + "/tooltip/js";
		}
		return false;
	},
	
	startTooltip: function(atag) {
		ttlib.currentMouseover = atag["rel"];
		if (ttlib.cache[atag["rel"]]) {
			ttlib.jstooltipdata.innerHTML = ttlib.cache[atag["rel"]];
		} else {
			ttlib.jstooltipdata.innerHTML = TOOLTIP_RETRIEVING_HTML;
			ttlib.queueRequest(atag["rel"]);
		}
		ttlib.show();
	},
	
	parseDocument: function() {
		var links = document.getElementsByTagName("a");
		var upval;
		for(var i = 0; i<links.length; i++) {
			if(ttlib.getValid(links[i]) != "") {
				links[i]["rel"] = ttlib.getValid(links[i]);
				links[i].onmouseover = function(evt) { ttlib.startTooltip(this); }
				links[i].onmouseout = function(evt) { ttlib.hide(); }
			}
		}
	},
	
	cursorPosition: function(e) {
		e = e || window.event;
		var cursor = {x:0, y:0};
		if (e.pageX || e.pageY) {
			cursor.x = e.pageX;
			cursor.y = e.pageY;
		} else {
			var de = document.documentElement;
			var b = document.body;
			cursor.x = e.clientX + (de.scrollLeft || b.scrollLeft) - (de.clientLeft || 0);
			cursor.y = e.clientY + (de.scrollTop || b.scrollTop) - (de.clientTop || 0);
		}
		return cursor;
	},
	
	show: function() {
		if(ttlib.jstooltipdata.style.width > TOOLTIP_MAX_WIDTH || ttlib.jstooltip.style.width > TOOLTIP_MAX_WIDTH
			|| ttlib.jstooltipdata.offsetWidth > TOOLTIP_MAX_WIDTH || ttlib.jstooltip.offsetWidth > TOOLTIP_MAX_WIDTH) {
			ttlib.jstooltip.style.width = TOOLTIP_MAX_WIDTH;
		} else {
			ttlib["jstooltip"]["style"]["width"] = ttlib["jstooltipdata"]["style"]["width"];
		}
		ttlib.jstooltip.style.visibility = "visible";
	},
	
	hide: function() {
		ttlib.jstooltip.style.visibility = "hidden";
		ttlib.currentMouseover = null;
	},
	
	removeChildren: function() {
		var scripts = document.getElementsByTagName("script");
		var head = document.getElementsByTagName("head").item(0);
		for (var i=0; i<scripts.length; i++) {
			var script = scripts[i];
			var src = script.getAttribute("src");
			if(src!=null && src.indexOf("tooltip/js") > 0 && src.indexOf(DOMAIN) > 0) {
				head.removeChild(script);
				return;
			}
		}	
	}
}

function registertooltip(str) {
	ttlib.cache[ttlib.currentRequest["cache"]] = str.tooltip;
	try {
		setTimeout("ttlib.removeChildren()", 0);
	} catch (e) {}
	if (ttlib.currentMouseover == ttlib.currentRequest["cache"]) {
		ttlib.jstooltipdata.innerHTML = str.tooltip;
		ttlib.show();
	}
	ttlib.currentRequest = null;
	ttlib.processQueue();
}

addLoadEvent(ttlib.init);