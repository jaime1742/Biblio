$(document).ready(function() {
    $('#id_marca').change(function() {
        var selectedMarca = $(this).find("option:selected").text();
        if (selectedMarca) {
            console.log(selectedMarca); 
            var apiUrl = `https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformake/${encodeURIComponent(selectedMarca)}?format=json`;
            console.log(apiUrl)
            $.ajax({
                url: apiUrl,
                type: 'GET',
                success: function(data) {
                    console.log(data)
                    // Lógica para manejar la respuesta de la API
                    $('#id_modelo').empty();

                    // Llenar las opciones con los modelos de la API
                    $.each(data.Results, function(index, value) {
                        $('#id_modelo').append('<option value="' + value.Model_Name + '">' + value.Model_Name + '</option>');
                    });
                },
                error: function(error) {
                    console.log('Error al llamar a la API:', error);
                }
            });
        }
    });
});