const brandsSelect = document.getElementById('brands');
const modelsSelect = document.getElementById('models');

function apiRequest(brandId) {
    fetch(`https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformake/${brandId}?format=json`)
    .then(response => {
        if (!response.ok) {
            throw new Error("Solicitud fallida");
        }
        return response.json();
    })
    .then(data => {
        modelsSelect.innerHTML = '';

        data.Results.forEach(res => {
            option = document.createElement('option');
            option.value = res.Model_Name;
            option.classList.add('model');
            option.textContent = res.Model_Name;

            modelsSelect.appendChild(option);
        })
    })
    .catch(error => {
        console.error('Error en la solicitud:', error);
    })
}

brandsSelect.addEventListener('change', function() {
    const selectedBrandId = brandsSelect.value;
    apiRequest(selectedBrandId);
});