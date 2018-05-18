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
  $( ".clink" ).click(function() {

  f($(this));

});
});
}

$( ".button" ).click(function() {
 f($(this));

});


