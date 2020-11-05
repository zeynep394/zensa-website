$('#right-arrow').click(function() {
    	var currentContainer= $('.container.active');
    	var nextContainer=currentContainer.next();

    	currentContainer.fadeOut(300).removeClass('active');
    	nextContainer.fadeIn(300).addClass('active');

    	if (nextContainer.length==0){
    		$('.container').first().fadeIn(300).addClass('active');
    	}
});

$('#left-arrow').click(function() {
    	var currentContainer= $('.container.active');
    	var prevContainer=currentContainer.prev();

    	currentContainer.fadeOut(300).removeClass('active');
    	prevContainer.fadeIn(300).addClass('active');

    	if (prevContainer.length==0){
    		$('.container').last().fadeIn(300).addClass('active');
    	}
});