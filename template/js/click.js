function parser(to) {
	TOREPLACE

}

function f(th) {
$( "#content" ).load(parser(parseInt(th.attr( 'to' ))) , function() {
  $( ".clink" ).click(function() {

  f($(this));

});
});
}

$( ".button" ).click(function() {
 f($(this));

});


