const submitBtn = document.querySelector('.btn-primary');
const values = document.querySelectorAll('.form-control');

submitBtn.addEventListener('click', (e) => {
    e.preventDefault();
    
    let address = values[0].value;

    return fetch('/delete/farmland', {
      method: 'DELETE',
      headers: { 'Content-type': 'application/json' },
      body: JSON.stringify({ address })
    });
});