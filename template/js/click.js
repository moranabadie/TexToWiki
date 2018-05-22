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
		'<font class="button fakelink" to="'
		+ (id_obj - 1).toString() + 
		'"><img src="img/prev.png" style="width:18px; position:relative; top:3px;" /> ' + parserName(id_obj - 1) + "</font>";
	}
	var nameNext =parserName(id_obj + 1);
	if (nameNext != "") {
		inside_elem = inside_elem + 
		'<div style="float:right;"><font class="button fakelink" to="'
		+ (id_obj + 1).toString() + 
		'">' + nameNext + ' <img src="img/next.png" style="width:18px; position:relative; top:3px;" /></font></div>';
	}

	$( "#linkAuto" ).html(inside_elem);
}
function f(th) {

var currenth = $( "#content" ).height();
var id_obj = parseInt(th.attr( 'to' ));

bottomLink(id_obj);
	$( "#content" ).load(parser(id_obj) , function() {
		
		$( "#fullbody" ).height(currenth);
			
			if (th.attr( 'link' ) != null){
				var v = $(th.attr( 'link' ) ).offset().top - 40;
				if (v < 0) {
					v = $(th.attr( 'link' ) ).offset().top;
				}
				simpleBz.getScrollElement().scrollTop = v;
			}
		   
		
  $( ".clink" ).click(function() {

  f($(this));
  
});
  $( ".fakelink" ).click(function() {
	
	  f($(this));

	 });
});
}

$( ".button" ).click(function() {
	
 f($(this));

});


