let i = 0;
var today = new Date();
var dd = String(today.getDate()).padStart(2, '0');
var mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
var yyyy = today.getFullYear();
today = dd + '/' + mm + '/' + yyyy;

getInformation();

const createElement = infoDollar => {
  const elementList = document.getElementById('list-group');
  elementList.innerHTML += ` 
    <div class="col ">
      <div class="card">
        <div class="card-header text-bg-dark mb-3">
        ${infoDollar.nombre}
        </div>
        <div class="card-body">
        <div class="row">
          <div class="col-8" >
              <p>Compra: ${infoDollar.compra} </p> 
              <p>Venta: ${infoDollar.venta} </p> 
            </div>
            <div class="col-1  w-auto" id="cotiz${i}">
            </div>
          </div>
        </div>
        <div class="card-footer text-muted">
            Ultima Consulta: ${today}
          </div>
      </div>
    </div>`;
  
    const cotizDolar = document.createElement("p");
  if( infoDollar.variacion.includes("-")){
    cotizDolar.classList.add("text-danger");
    cotizDolar.textContent = infoDollar.variacion;
  }else{
    cotizDolar.classList.add("text-success");
    cotizDolar.textContent = infoDollar.variacion;
  }
  const divCotiz = document.getElementById("cotiz"+i);
  divCotiz.appendChild(cotizDolar);
  i++;
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

