const submitBtn = document.querySelector('.btn-primary');
const values = document.querySelectorAll('.form-control');

submitBtn.addEventListener('click', (e) => {
    e.preventDefault();
    
    let recent_activity = values[0].value;
    let flower_quantity = values[1].value;
    let equipment_id = values[2].value;
    let farmland_address = values[3].value;
    let person_pesel = values[4].value;

    return fetch('/update/harvest', {
      method: 'PUT',
      headers: { 'Content-type': 'application/json' },
      body: JSON.stringify({ recent_activity, flower_quantity, equipment_id, farmland_address, person_pesel })
    });
});