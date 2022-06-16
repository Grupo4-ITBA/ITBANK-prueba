const createElement = infoDollar => {
  const element = document.getElementById('newCard');
  element.innerHTML += `   
  <div
  class="col-lg-4 mt-2"
>
  <div class="icon-box">
    <h4><a href="">${infoDollar.nombre}</a></h4>
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
        }
      });
    });
}

getInformation();
