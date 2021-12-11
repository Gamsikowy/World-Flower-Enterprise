const submitBtn = document.querySelector('.btn-primary');
const values = document.querySelectorAll('.form-control');

submitBtn.addEventListener('click', (e) => {
    e.preventDefault();
    
    let apartments = values[0].value;
    let address = values[1].value;

    return fetch('/update/lodging', {
      method: 'PUT',
      headers: { 'Content-type': 'application/json' },
      body: JSON.stringify({ apartments, address })
    });
});