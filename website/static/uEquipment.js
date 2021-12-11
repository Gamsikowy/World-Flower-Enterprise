const submitBtn = document.querySelector('.btn-primary');
const values = document.querySelectorAll('.form-control');

submitBtn.addEventListener('click', (e) => {
    e.preventDefault();
    
    let name = values[0].value;
    let model = values[1].value;
    let warranty_validity = values[2].value;
    let id = values[3].value;

    return fetch('/update/equipment', {
      method: 'PUT',
      headers: { 'Content-type': 'application/json' },
      body: JSON.stringify({ name, model, warranty_validity, id })
    });
});