const checkElement=(element)=>{
     element < 0 ? element.style.color = "red" : element.style.color= 'green'
}

const createElement = infoDollar => {
  const element = document.getElementById('newCard');
  element.innerHTML += `   
  <div
  class="col-lg-3 mx-6 mt-2 "
>
  <div class="icon-box">
    <h5 class'text-secondary'>${infoDollar.nombre}</h5>
    <small class="buy mb-1"><strong>Compra:</strong>${infoDollar.compra}</small>
    <small class="sell"><strong>Venta:</strong> ${infoDollar.venta}</small>
    
  </div>
</div>`;
};

function getInformation() {
  fetch('https://www.dolarsi.com/api/api.php?type=valoresprincipales')
    .then(resp => resp.json())
    .then(data => {
      document.getElementById('loading').hidden = true;
      data.forEach(element => {
        if (element.casa.compra != 'No Cotiza') {
          createElement(element.casa);
          console.log(element.casa)
        }
      });
    });
}

getInformation();
