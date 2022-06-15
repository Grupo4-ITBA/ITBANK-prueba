const createElement = infoDollar => {
  const element = document.getElementById('newCard');
  element.innerHTML += `   
  <div
  class="align-items-center w-40 mt-4 mh-20"
  data-aos="zoom-in"
  data-aos-delay="300"
>
  <div class="icon-box">
    <div class="icon"><i class="bx bx-tachometer"></i></div>
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
        console.log(element.casa);
        if (element.casa.compra != 'No Cotiza') {
          createElement(element.casa);
        }
      });
    });
}

getInformation();
