import {service} from "./js/datebaseConfig.js"

const endPoint = "/Ingrid"

var body = 
{
    
}

var cont = 0;

const getData = () => {

    service.load(endPoint).then( data => 
    {
        body = data;
    })

    console.log(body);
    cont += 1;

    setRPM();
    getTempValues();
    getRpmValues();
    getNivelValues();
    getGasValues();
    getOtherValues();

    if(body.Status)
        addChart("rpmChart", body.Sensor_RPM);
    addChart("temperatureChart", body.Sensor_Temp);

    const toggleSwitch = document.getElementById('toggleStatus');

    if(body.Status)
    {
        toggleSwitch.checked = true
    } else 
    {
        toggleSwitch.checked = false
    }
}

// ==================  GRÁFICOS   ==================

const chartIt = (id) => {

    var name
    if(id == "rpmChart")
        name = 'Motor RPM'
    else
        name = "Temperatura"

        const ctx = document.getElementById(id);
        new Chart(ctx, 
        {
        type: 'line',
        data: 
        {   
            labels: [],
            datasets: [
            {
            label: name,
            data: [],
            borderWidth: 1
            }]
        },
        });

}

const addChart = (id, newData) => {

    var chart = Chart.getChart(id);
    chart.data.labels.push(cont);
    chart.data.datasets.forEach((dataset) =>
    {
    dataset.data.push(newData); 
    });
    chart.update();
}

chartIt('rpmChart');
chartIt('temperatureChart');

setInterval(() =>
    {
        getData();
    }, 2000); 
    
// ================== ATUALIZA O 'RPM' ==================
    
const setRPM = () => {

    const RpmElement = document.getElementById("dashboardRpm")
    let rpm_value 
    rpm_value = body.Status ? body.Sensor_RPM : 0;
    
    RpmElement.innerHTML = rpm_value
}


// ================== HORÁRIO ==================

const getCurrentTime = () => {

    const now = new Date();
    const hours = now.getHours().toString().padStart(2, '0');
    const minutes = now.getMinutes().toString().padStart(2, '0');
    const seconds = now.getSeconds().toString().padStart(2, '0');
    return `${hours}:${minutes}:${seconds}`;
}

const updateTime = () => {

    const timeElement = document.getElementById('time');
    if (timeElement) 
    {
        timeElement.textContent = `Hora: ${getCurrentTime()}`;
    }
}

updateTime();
setInterval(updateTime, 1000);

// ================== INVERTE O STATUS DA MAQUINA ==================

const toggleStatus = (elementId) => {

    const statusElement = document.getElementById('status');
    const toggleSwitch = document.getElementById('toggleStatus');

    if (toggleSwitch.checked)
    {
        statusElement.innerHTML = 'Status: Trabalhando';
        body.Status = 1;
        service.set(endPoint, body)
    } else 
    {
        statusElement.innerHTML = 'Status: Desligado';
        body.Status = 0;
        service.set(endPoint, body)
    }
};

const toggleSwitch = document.getElementById('toggleStatus');

toggleSwitch.addEventListener('change', () => 
{
    toggleStatus('dashboard');
});


// ================== ALERTAS ==================

const getTempValues = (elementId)  => {

    let sensorTemp = body.Sensor_Temp;
    let iconTemp = document.getElementById('icon-temp');

    if (sensorTemp > 80) {
        iconTemp.classList.add("warning");
    } 
    else {
        iconTemp.classList.remove("warning");
    }
};

const getRpmValues = (elementId)  => {

    let sensorRpm = body.Sensor_RPM;
    let iconRpm = document.getElementById('icon-rpm');

    if (sensorRpm > 600) {
        iconRpm.classList.add("warning");
    }
    else {
        iconRpm.classList.remove("warning");
    }
};

const getNivelValues = (elementId)  => {

    let sensorNivel = body.Sensor_Nivel;
    let iconNivel = document.getElementById('icon-nivel');

    if (sensorNivel == 0) {
        iconNivel.classList.add("warning");
    } 
    else {
        iconNivel.classList.remove("warning");
    }
};

const getGasValues = (elementId)  => {

    let sensorGas = body.Sensor_Gas;
    let iconGas = document.getElementById('icon-gas');

    if (sensorGas > 600) {
        iconGas.classList.add("warning");
    } 
    else {
        iconGas.classList.remove("warning");
    }
};

const getOtherValues = (elementId)  => {

    let sensorGiro = body.Sensor_Giro;
    let iconGiro = document.getElementById('icon-outros');

    if (sensorGiro == 0) {
        iconGiro.classList.add("warning");
    } 
    else {
        iconGiro.classList.remove("warning");
    }
};