/* Radio & Checkbox */
$(function(){
    $('input').checkBox();

    $('.slider').slider({
        range: true,
        values: [17, 67]
    });
    $('.ui-slider').each(function() {
        $('.ui-slider-handle:first', this).addClass('ui-slider-handle-left');
        $('.ui-slider-handle:last', this).addClass('ui-slider-handle-right');
    });
    $(".selection .filter .slider").bind("slide", function(event, ui){
        $(this).next(".from").val(ui.values[0]).next(".to").val(ui.values[1]);
    });
    $("select").selectBox();

    $(".buyform input.text").addClass("default");
});

