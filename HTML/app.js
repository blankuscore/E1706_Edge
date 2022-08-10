function hidewarningbanner(data) {
  var x = document.getElementById("warningbanner");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}

function module_check(data){
  var carrier_qty = data.general.carrier;
  // Check the power system and carrier quantity
  if(data.general.power_system == 2){ //120240SP
    var module_qty = carrier_qty * 5;
  } else if(data.general.power_system == 4 || data.general.power_system == 8){ //240D | 480D
    var module_qty = carrier_qty * 6;
  } else { //208Y | 480 Y | 400TTS | 400TT | 240HD
    var module_qty = carrier_qty * 7;
  }
  let DTX_text = ""
  let count = 0
  for(k in data.modules){
    count = count + 1
    if(count > module_qty){
      break
    }
    if(data.modules[k] != 1){
      DTX_text = DTX_text.concat("_")
      DTX_text = DTX_text.concat(count)
    }
  }
  console.log(DTX_text)
}

//https://raw.githubusercontent.com/blankuscore/E1706_Edge/main/HTML/data.json

fetch('https://raw.githubusercontent.com/blankuscore/E1706_Edge/main/HTML/data.json')
  .then(function(response){
      return response.json();
  })
  .then(data => {
      //conlog(data.carrier)
      module_check(data)
  })

function conlog(variable){
  console.log(variable)
}

function appendData(data) {
  var mainContainer = document.getElementById("myData");
  for (var i = 0; i < data.length; i++) {
      var div = document.createElement("div");
      div.innerHTML = "Surge Count: " + data[i].surge;
      mainContainer.appendChild(div);
      var div = document.createElement("div");
      div.innerHTML = "TOV Count: " + data[i].tov;
      mainContainer.appendChild(div)
      if(data[i].module_status_1 == 1){
          var div = document.createElement("div");
          div.innerHTML = "Module Status 1: OK";
          mainContainer.appendChild(div)
      }
      if(data[i].module_status_2 == 1){
          var div = document.createElement("div");
          div.innerHTML = "Module Status 2: OK";
          mainContainer.appendChild(div)
      }
      if(data[i].module_status_3 == 1){
          var div = document.createElement("div");
          div.innerHTML = "Module Status 3: OK";
          mainContainer.appendChild(div)
      }
      if(data[i].module_status_4 == 1){
          var div = document.createElement("div");
          div.innerHTML = "Module Status 4: OK";
          mainContainer.appendChild(div)
      }
      if(data[i].module_status_5 == 1){
          var div = document.createElement("div");
          div.innerHTML = "Module Status 5: OK";
          mainContainer.appendChild(div)
      }
      if(data[i].module_status_6 == 1){
          var div = document.createElement("div");
          div.innerHTML = "Module Status 6: OK";
          mainContainer.appendChild(div)
      }
      if(data[i].module_status_7 == 1){
          var div = document.createElement("div");
          div.innerHTML = "Module Status 7: OK";
          mainContainer.appendChild(div)
      }
  }
}