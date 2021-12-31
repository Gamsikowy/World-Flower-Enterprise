const submitBtn = document.querySelector('.btn-update');
const lowerBtn = document.querySelector('.btn-lower');
const increaseBtn = document.querySelector('.btn-increase');
const lowerPercentage = document.querySelector('.form-control-l');
const increasePercentage = document.querySelector('.form-control-i');
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

lowerBtn.addEventListener('click', (e) => {
    e.preventDefault();
    
    let percentage = lowerPercentage.value;
    let action = 'lower'

    return fetch('/update/warehouse', {
      method: 'POST',
      headers: { 'Content-type': 'application/json' },
      body: JSON.stringify({ percentage, action })
    });
});

increaseBtn.addEventListener('click', (e) => {
    e.preventDefault();
    
    let percentage = increasePercentage.value;
    let action = 'increase'

    return fetch('/update/warehouse', {
      method: 'POST',
      headers: { 'Content-type': 'application/json' },
      body: JSON.stringify({ percentage, action })
  });
});