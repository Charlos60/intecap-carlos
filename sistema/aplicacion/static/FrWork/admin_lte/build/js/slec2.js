


// Luego de cargar jQuery y Select2, puedes incluir tu código de Select2
jQuery(document).ready(function() {
    jQuery(".select2").select2({
        placeholder: "Selecciona un sector",
        minimumInputLength: 2,
        ajax: {
            url: function (params) {
                return jQuery(this).data('url') + '?search=' + params.term;
            },
            dataType: 'json',
            processResults: function (data) {
                return {
                    results: data
                };
            }
        }
    });
});
