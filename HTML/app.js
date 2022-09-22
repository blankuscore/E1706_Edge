// **10.14 completion date**
// mobile vs tablet vs laptop
// add boilerplate
// update threephase.gif (shorter moving x axis)
// test on mobile device
// add buy me now! link
// test web page on raspberry pi
// test rs485 on raspberry pi

function hidewarningbanner(data) { // function to determine if banner is necessary
  var carrier_qty = data.general.carrier;
  // Check the power system and carrier quantity
  if(data.general.power_system == 2){ //120240SP
    var module_qty = carrier_qty * 5;
  } else if(data.general.power_system == 4 || data.general.power_system == 8){ //240D | 480D
    var module_qty = carrier_qty * 6;
  } else { //208Y | 480 Y | 400TTS | 400TT | 240HD
    var module_qty = carrier_qty * 7;
  }

  let count = 0;
  let DTX_text = ""
  for(k in data.modules){
    count = count + 1;
    if(count > module_qty){
      break
    }
    if(data.modules[k] != 1){
      DTX_text = DTX_text.concat(count);
      DTX_text = DTX_text.concat(", ");
    }
  }
  
  var x = document.getElementById("warningbanner");
  
  if(DTX_text == ""){  
    if (x.style.display === "none") {
      x.style.display = "block";
    } else {
      x.style.display = "none";
    }
  } else {
    var DTXtext = "Warning! Module(s) ";
    DTXtext = DTXtext.concat(DTX_text);
    DTXtext = DTXtext.concat(" have disconnected!");
    x.textContent= DTXtext;
  }

}

function module_check(data){ // function to check modules and apply proper DTX image
  var carrier_qty = data.general.carrier;
  // Check the power system and carrier quantity
  if(data.general.power_system == 2){ //120240SP
    var module_qty = carrier_qty * 5;
  } else if(data.general.power_system == 4 || data.general.power_system == 8){ //240D | 480D
    var module_qty = carrier_qty * 6;
  } else { //208Y | 480 Y | 400TTS | 400TT | 240HD
    var module_qty = carrier_qty * 7;
  }
  let DTX_text = "DTX"
  let count = 0;
  for(k in data.modules){
    count = count + 1;
    if(count > module_qty){
      break
    }
    if(data.modules[k] != 1){
      DTX_text = DTX_text.concat("_");
      DTX_text = DTX_text.concat(count);
    }
  }
  DTX_text = DTX_text.concat(".png");
  var img_path = "C:/Users/e1176752/Documents/VSCode/Projects/E1706_Edge/E1706_Edge/HTML/Images/";
  img_path = img_path.concat(DTX_text);

  var mainContainer = document.getElementById("demo");
  var img = document.createElement("img");

  var win = window,
    doc = document,
    docElem = doc.documentElement,
    body = doc.getElementsByTagName('body')[0],
    x = win.innerWidth || docElem.clientWidth || body.clientWidth,
    y = win.innerHeight|| docElem.clientHeight|| body.clientHeight;
  console.log(x)
  console.log(y)

  img.width = x*0.175;
  img.src = img_path

  mainContainer.appendChild(img);
}

function line_check(data){ // function to check the incoming line presence (also adds surge/tov plots)

  var win = window,
    doc = document,
    docElem = doc.documentElement,
    body = doc.getElementsByTagName('body')[0],
    x = win.innerWidth || docElem.clientWidth || body.clientWidth;

  if(data.general.power_system != 4 || data.general.power_system != 8){
    var table = document.getElementById("table");
    var row = table.insertRow(-1);
    var cell = row.insertCell(0);

    var img = document.createElement("img");
    img.width = x*0.25;
    img.src = "C:/Users/e1176752/Documents/VSCode/Projects/E1706_Edge/E1706_Edge/HTML/Images/Surge-TOV Plot.png"
    cell.appendChild(img);
    
    var cell = row.insertCell(1);
    var img = document.createElement("img");
    img.width = x*0.25;
    img.src = "C:/Users/e1176752/Documents/VSCode/Projects/E1706_Edge/E1706_Edge/HTML/Images/threephase.gif"
    cell.appendChild(img);
  }
}

function addCounts(data){ // function to add raw data from surge & tov count
  var x = document.getElementById("toptext");
  var text = "Surge Count: ";
  text = text.concat(data.general.surge);
  text = text.concat(" | TOV: ");
  text = text.concat(data.general.tov);
  console.log(text)
  x.textContent= text;
}

//https://raw.githubusercontent.com/blankuscore/E1706_Edge/main/HTML/data.json

fetch('https://raw.githubusercontent.com/blankuscore/E1706_Edge/main/HTML/data.json')
  .then(function(response){
      return response.json();
  })
  .then(data => {
      hidewarningbanner(data)
      line_check(data)
      module_check(data)
      addCounts(data)
  })

function conlog(variable){
  console.log(variable)
}