const submitBtn = document.querySelector('.btn-primary');
const values = document.querySelectorAll('.form-control');

submitBtn.addEventListener('click', (e) => {
    e.preventDefault();
    
    let name = values[0].value;
    let surname = values[1].value;
    let company = values[2].value;
    let pesel = values[3].value;

    return fetch('/update/client', {
      method: 'PUT',
      headers: { 'Content-type': 'application/json' },
      body: JSON.stringify({ name, surname, company, pesel })
    });
});