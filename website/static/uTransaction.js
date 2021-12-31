const submitBtn = document.querySelector('.btn-primary');
const values = document.querySelectorAll('.form-control');

submitBtn.addEventListener('click', (e) => {
    e.preventDefault();
    
    let id = values[0].value;
    let flower_quantity = values[1].value;
    let seed_quantity = values[2].value;
    let payment = values[3].value;
    let date_of_transaction = values[4].value;
    let client_pesel = values[5].value;
    let warehouse_address = values[6].value;
    let person_pesel = values[7].value;

    return fetch('/update/transaction', {
      method: 'PUT',
      headers: { 'Content-type': 'application/json' },
      body: JSON.stringify({ id, flower_quantity, seed_quantity, payment, date_of_transaction, client_pesel, warehouse_address,person_pesel })
    });
});