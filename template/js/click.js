function parser(to) {
	if (to ==0) {
        return "NAMECORE"
    }
	TOREPLACE

}

function f(th) {
var currenth = $( "#content" ).height();
	$( "#content" ).load(parser(parseInt(th.attr( 'to' ))) , function() {
		
		$( "#fullbody" ).height(currenth);
			
			if (th.attr( 'link' ) != null){
				
				simpleBz.getScrollElement().scrollTop = $(th.attr( 'link' ) ).offset().top;
			}
		   
		
  $( ".clink" ).click(function() {

  f($(this));
  
});
  $( ".button" ).click(function() {
		
	  f($(this));

	 });
});
}

$( ".button" ).click(function() {
	
 f($(this));

});


