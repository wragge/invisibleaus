$(function(){
    $('input:radio[name=record_date_type]').change(function() {
        var date_type = $('input:radio[name=record_date_type]:checked').val();
        if (date_type == 'single') {
            $('#id_end_date_year').parent().hide();
        } else if (date_type == 'range') {
            $('#id_end_date_year').parent().show();
        }
    });
    $('#id_end_date_year').parent().hide();
    $('#id_category').change(function() {

        $('.form-field').hide();
        $('.naa').show();
    });
});
