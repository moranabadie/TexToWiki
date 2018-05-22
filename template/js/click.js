function parser(to) {
	if (to ==0) {
        return "NAMECORE"
    }
	TOREPLACE

}

function f(th) {
	console.log("yo");
var currenth = $( "#content" ).height();
	$( "#content" ).load(parser(parseInt(th.attr( 'to' ))) , function() {
		
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


