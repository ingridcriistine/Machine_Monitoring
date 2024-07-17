import {service} from "./datebaseConfig.js"

const endPoint = "/Ingrid"

// Definindo estrutura do corpo do meu objeto do banco.
var body = {
    
}

// Carregando dados do meu banco
const loadData = () => {
    service.load(endPoint).then( data => {
        body = data;
        console.log(body);

        setRPM()
        // setTempValues()
    })
}

// Definindo os dados no meu banco.
// service.set(endPoint, body)

// ==================  Colocando os dados no HTML   ==================

const setRPM = (idLocal = 'dashboard') => {
    const RpmElement = document.getElementById(idLocal + "Rpm")

    let rpm_value = 0;

    rpm_value = body.Sensor_RPM;
    
    RpmElement.innerHTML = "RPM:" + rpm_value
}

// ================== Funções de Interação com HTML ==================

// const toggleStatus = (idRoom = 'dashboard') => {
//     const element = document.getElementById(idRoom + "Status")
//     let isOn = false;

//     body.Status = !body.Status;
//     isOn = body.Status;
//     service.set(endPoint, body);

//     if(isOn) {
//         element.innerHTML = "ON"
//     } else {
//         element.innerHTML = "OFF"
//     }
// }

// console.log('script loaded');

// // Adicionando as funções no HTML 

// window.toggleLamp = toggleLamp
// window.toggleTv = toggleTv
window.setRPM = setRPM

setInterval(() => {
    loadData();
}, 2000);
