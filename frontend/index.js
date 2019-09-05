ENDPOINT = "http://localhost:5000";

submit = function() {
  x = document.getElementById('x_input').value;  
  y = document.getElementById('y_input').value;
  month = document.getElementById('month_input').value;
  day = document.getElementById('day_input').value;
  ffmc = document.getElementById('ffmc_input').value;
  dmc = document.getElementById('dmc_input').value;
  dc = document.getElementById('dc_input').value;
  isi = document.getElementById('isi_input').value;
  temp = document.getElementById('temp_input').value;
  rh = document.getElementById('rh_input').value;
  wind = document.getElementById('wind_input').value;
  rain = document.getElementById('rain_input').value;

  
  var xhttp = new XMLHttpRequest();
  xhttp.addEventListener("readystatechange", function () {
    if (this.readyState === 4) {
      alert(this.responseText);
    }
  });


  xhttp.open("GET", ENDPOINT + "/predict/?x="+x
    +"&y="+y
    +"&month="+month
    +"&day="+day
    +"&ffmc="+ffmc
    +"&dmc="+dmc
    +"&dc="+dc
    +"&isi="+isi
    +"&temp="+temp
    +"&rh="+rh
    +"&wind="+wind
    +"&rain="+rain
    , true);
  xhttp.send();

};