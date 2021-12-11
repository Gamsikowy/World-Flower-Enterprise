const submitBtn = document.querySelector('.btn-primary');
const values = document.querySelectorAll('.form-control');

submitBtn.addEventListener('click', (e) => {
    e.preventDefault();
    
    let flowerQuantity = values[0].value;
    let seedQuantity = values[1].value;
    let flowerPrice = values[2].value;
    let seedPrice = values[3].value;
    let address = values[4].value;

    return fetch('/update/warehouse', {
      method: 'PUT',
      headers: { 'Content-type': 'application/json' },
      body: JSON.stringify({ flowerQuantity, seedQuantity, flowerPrice, seedPrice, address })
    });
});