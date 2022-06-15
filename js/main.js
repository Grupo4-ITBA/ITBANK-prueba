const createElement = infoDollar => {
  const elementList = document.getElementById('list-group');
  elementList.innerHTML += ` 
  <div class="col ">
  <div class="card">
    <div class="card-body">
      <h5 class="card-title">${infoDollar.nombre}</h5>
      <small class="buy mb-1"><strong>Compra:</strong>${infoDollar.compra}</small>
      <small class="sell"><strong>Venta:</strong> ${infoDollar.venta}</small>
    </div>
  </div>
</div>`;
};

function getInformation() {
  fetch('https://www.dolarsi.com/api/api.php?type=valoresprincipales')
    .then(resp => resp.json())
    .then(data => {
      document.getElementById('loading').hidden = true;
      data.forEach(element => {
        console.log(element.casa);
        if (element.casa.compra != 'No Cotiza') {
          createElement(element.casa);
        }
      });
    });
}

getInformation();
