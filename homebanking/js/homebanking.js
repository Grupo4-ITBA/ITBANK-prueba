//Declaración de variables
var nombreUsuario = "grupo4";
var saldoCuenta = 8000;
var montoAnterior = saldoCuenta;
var limiteExtraccion = 5000;
var monto;
var cotizacionDolar = 20.64;
//Variables para transferir
var cuenta;
var cuentaAmiga1 = 1;
var cuentaAmiga2 = 2;
/*/ variables de inicio de sesion
var password = 12345;
var usuarioIntroducido;
var passwordIntroducida;*/
//Variables de pago servicios
var agua = 700;
var telefono = 900;
var luz = 2100;
var internet = 2500;
//Ejecución de las funciones que actualizan los valores de las variables en el HTML
cargarNombreEnPantalla();
actualizarSaldoEnPantalla();
actualizarLimiteEnPantalla();

//funciones de suma y resta
function sumar(monto) {
    saldoCuenta += monto;
}

function restar(monto) {
    saldoCuenta -= monto;
}

//funcion de validación, tanto de monto como de formato.

function haySaldo() {
    if (isNaN(monto)) {
        alert("ingrese un monto númerico");
    } else if (monto > limiteExtraccion) {
            alert("Limite de extracción superado");
        } else if (monto % 100 != 0) {
            alert("Solo se pueden extraer billetes de 100");
        } else  {
            if (!isNaN(monto) && monto != null) {
                return true;
            }
        }
} 

// Función de extracción de dinero

function extraerDinero() {
    monto = parseInt(prompt("Ingrese monto"));
	if (haySaldo()) {
        restar(monto);
        alert("Has Extraído " + monto + "\nsaldo anterior " +
            montoAnterior + "\nsaldo actual " + saldoCuenta);

    }
    actualizarSaldoEnPantalla();
}
// Función de depósito de dinero

function depositarDinero() {
    monto = parseInt(prompt("Ingrese monto"));
    if (haySaldo()) {
        sumar(monto);
        //saldoCuenta += monto; 
        alert("Has depositado " + monto + "\nsaldo anterior " + montoAnterior + "\nsaldo actual " + saldoCuenta);

        actualizarSaldoEnPantalla();
    }
}

// Función de pago de servicios

function pagarServicio() {
    var pago = parseInt(prompt("Ingrese el número que corresponde con el servicio que queres pagar: " + "\n1- Agua" + "\n2- teléfono" + "\n3- Luz" + "\n4- internet"));
    switch (pago) {
        case 1:
            restar(agua);
            alert("Has depositado " + agua + " correspondientes al servicio de Agua" + "\nsaldo anterior " + montoAnterior + "\nsaldo actual " + saldoCuenta);
            break;
        case 2:
            restar(telefono);
            alert("Has depositado " + telefono + " correspondientes al servicio de Telefonía" + "\nsaldo anterior " + montoAnterior + "\nsaldo actual " + saldoCuenta);
            break;
        case 3:
            restar(luz);
            alert("Has depositado " + luz + " correspondientes al servicio de Electricidad" + "\nsaldo anterior " + montoAnterior + "\nsaldo actual " + saldoCuenta);
            break;
        case 4:
            restar(internet);
            alert("Has depositado " + internet + " correspondientes al servicio de Internet" + "\nsaldo anterior " + montoAnterior + "\nsaldo actual " + saldoCuenta);
            break;
        default:
            alert("Opción incorrecta. Ingrese una de los opciones mostradas en pantalla")

    }
    actualizarSaldoEnPantalla();
}


// Función de transferencia de dinero*/

function transferirDinero() {
    var transferir = parseInt(prompt("Ingrese monto a transferir"));
    if (isNaN(transferir)) {

        alert("Ingrese un monto correcto");
    } else if (transferir <= saldoCuenta) {
        //cuenta = parseInt(prompt());
        cuenta = parseInt(prompt("Ingrese el número que corresponde con la cuenta a la que quiere transferir:" + "\n1- cuentaAmiga1" + "\n2- cuentaAmiga2"));
        if (isNaN(cuenta) && not(null)) {
            alert("ingrese una opción correcta")

        } else if (cuenta === 1) {
            restar(transferir);
            actualizarSaldoEnPantalla();
            alert("Has Transferido " + transferir + " a la cuenta " + cuentaAmiga1 + "\nSu saldo anterior: " + montoAnterior + "\nsaldo actual: " + saldoCuenta);


        } else if (cuenta === 2) {
            restar(transferir);
            actualizarSaldoEnPantalla();
            alert("Has Transferido " + transferir + " a la cuenta " + cuentaAmiga2 + "\nSu saldo anterior: " + montoAnterior + "\nsaldo actual: " + saldoCuenta);
        } else if (isNaN(cuenta) && cuenta > 2) {
            alert("Ingrese una opción correcta, para transferir a otra cuenta, añadala en la sección 'gestionar cuentas")
        }
    } else {
        alert("saldo insuficiente2")
    }

    actualizarSaldoEnPantalla();

}

// función de saldo en dolares
function cuentaDolares(){
	cuentaDolares = saldoCuenta / cotizacionDolar
	alert("Su cuenta tiene US $ " + cuentaDolares + " (Dólares americanos)")

}

//Funciones que actualizan el valor de las variables en el HTML
function cargarNombreEnPantalla() {
    document.getElementById("nombre").innerHTML = "Bienvenido/a " + nombreUsuario;
}

function actualizarSaldoEnPantalla() {
    document.getElementById("saldo-cuenta").innerHTML = "$" + saldoCuenta;
}

function actualizarLimiteEnPantalla() {
    document.getElementById("limite-extraccion").innerHTML = "Tu límite de extracción es: $" + limiteExtraccion;
}


//Funciones que actualizan el valor de las variables en el HTML
function cargarNombreEnPantalla() {
    document.getElementById("nombre").innerHTML = "Bienvenido/a " + nombreUsuario;
}

function actualizarSaldoEnPantalla() {
    document.getElementById("saldo-cuenta").innerHTML = "$" + saldoCuenta;
}

function actualizarLimiteEnPantalla() {
    document.getElementById("limite-extraccion").innerHTML = "Tu límite de extracción es: $" + limiteExtraccion;
}