const submitBtn = document.querySelector('.btn-primary');
const values = document.querySelectorAll('.form-control');

submitBtn.addEventListener('click', (e) => {
    e.preventDefault();
    
    let name = values[0].value;
    let surname = values[1].value;
    let phone = values[2].value;
    let birth = values[3].value;
    let salary = values[4].value;
    let role = values[5].value;
    let lodgingAddress = values[6].value;
    let pesel = values[7].value;

    return fetch('/update/employee', {
      method: 'PUT',
      headers: { 'Content-type': 'application/json' },
      body: JSON.stringify({ name, surname, phone, birth, salary, role, lodgingAddress, pesel })
    });
});