$(function() {

  setCheckboxSelectLabels();

  $('.toggle-next').click(function() {
    $(this).next('.checkboxes').slideToggle(400);
  });

  $('.ckkBox').change(function() {
    toggleCheckedAll(this);
    setCheckboxSelectLabels();
  });

});


function setCheckboxSelectLabels(elem) {
  var wrappers = $('.wrapper');
  $.each( wrappers, function( key, wrapper ) {
    var checkboxes = $(wrapper).find('.ckkBox');
    var label = $(wrapper).find('.checkboxes').attr('id');
    var prevText = '';
    $.each( checkboxes, function( i, checkbox ) {
      var button = $(wrapper).find('button');
      if( $(checkbox).prop('checked') == true) {
        var text = $(checkbox).next().html();
        var btnText = prevText + text;
        var numberOfChecked = $(wrapper).find('input.val:checkbox:checked').length;
        if(numberOfChecked >= 4) {
           btnText = numberOfChecked +' '+ label + ' selected';
        }
        $(button).text(btnText);
        prevText = btnText + ', ';
      }
    });
  });
}

function toggleCheckedAll(checkbox) {
  var apply = $(checkbox).closest('.wrapper').find('.apply-selection');
  apply.fadeIn('slow');

  var val = $(checkbox).closest('.checkboxes').find('.val');
  var all = $(checkbox).closest('.checkboxes').find('.all');
  var ckkBox = $(checkbox).closest('.checkboxes').find('.ckkBox');

  if( $(checkbox).hasClass('all') ) {
    $(val).prop('checked', false);
  } else {
    $(all).prop('checked', false);
  }
}



function product_select(id) {
  var wrappers = $('.wrapper');
  $.each( wrappers, function( key, wrapper ) {
    var checkboxes = $(wrapper).find('.ckkBox');
    var label = $(wrapper).find('.checkboxes').attr('id');
    var prevText = '';
    $.each( checkboxes, function( i, checkbox ) {
      var button = $(wrapper).find('button');
      if( $(checkbox).prop('checked') == true) {
        var val = $(checkbox).val();
        if (val !=  id){
            $(checkbox).prop('checked', false);
        }
      }
    });
  });
}


function change_select(id){
    product_select(id)
}
