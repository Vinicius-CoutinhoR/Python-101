const url = 'https://api.gorents.com.br/1/active-debt/302?situation=CANCELADO';
const headerKey = 'rent-header-key';
const headerValue = 'vcQmJ7fjUHds3n5UDYBXesZB8gMxPAtaCLNGD1Qgghsux516LUuq9A9kdTEV';


const requestOptions = {
    method: 'PUT',
    headers: {
        'Content-Type': 'application/json',
        [headerKey]: headerValue
    }
};

fetch(url, requestOptions)
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error('Erro:', error));
