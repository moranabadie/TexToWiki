function parser(to) {
	if (to ==0) {
        return "NAMECORE"
    }
	TOREPLACE
	return "";
}
function parserName(to) {
	if (to ==0) {
        return "Intro"
    }
	TRPLPA
	return "";
}

function bottomLink(id_obj) {

    var inside_elem = "";

    if (id_obj > 0) {
        inside_elem = inside_elem +
            '<font class="button fakelink" to="' +
            (id_obj - 1).toString() +
            '"><img src="img/prev.png" style="width:18px; position:relative; top:3px;" /> ' + parserName(id_obj - 1) + "</font>";
    }
    var nameNext = parserName(id_obj + 1);
    if (nameNext != "") {
        inside_elem = inside_elem +
            '<div style="float:right;"><font class="button fakelink" to="' +
            (id_obj + 1).toString() +
            '">' + nameNext + ' <img src="img/next.png" style="width:18px; position:relative; top:3px;" /></font></div>';
    }

    $("#linkAuto").html(inside_elem);
}

function linkReplace(id_obj) {
    var li = window.location.href.split("?");
    if (li.length > 1) {
        return li[0] + "#" + id_obj.toString();
    }
    li = window.location.href.split("#");
    return li[0] + "?" + id_obj.toString();
}



function f(th) {

    
    var id_obj = parseInt(th.attr('to'));
    
    faux(id_obj, th.attr('link'));
    

}

function faux(id_obj, thlink) {
	faux2(id_obj, thlink, true);
}
function faux2(id_obj, thlink, push) {

    var currenth = $("#content").height();
    initialLink = id_obj;

    bottomLink(id_obj);
    $("#content").load(parser(id_obj), function() {

        $("#fullbody").height(currenth);
        if (push) {
        	 history.pushState({}, '', linkReplace(id_obj));
        }
       
        if (thlink != null) {
            history.pushState({}, '', linkReplace(id_obj) + thlink);
            var v = $(thlink).offset().top - 40;
            if (v < 0) {
                v = $(thlink).offset().top;
            }
            simpleBz.getScrollElement().scrollTop = v;
        }


        $(".clink").click(function() {

            f($(this));

        });
        $(".fakelink").click(function() {

            f($(this));

        });
    });

}



$(".button").click(function() {

    f($(this));

});


function updateLink()  {
	
	var idd = getID();
	if (idd != null) {
		if (initialLink != idd) {
	
			faux2(idd, null, false);
	
		}
	}
	
}
function getID() {
	var li = window.location.href.split("?");
    if (li.length > 1) {
        return parseInt(li[1]);
    }
    li = window.location.href.split("#");
    if (li.length > 1) {
    	return parseInt(li[1]);
    }
    return null;
	
}


