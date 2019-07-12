function desenhaGrafico() {
  $("#grafico-linhas").highcharts({
     title: {
       text: "Dhrystone em milhões",
     },
     xAxis: {
       categories: ["windows", "ubunto", "virtual-mc"]
     },
     series: [{
       name: "Sistema 1",
       data: [8.5, 12.3, 8.4]
    },{

      name: "Sistema 2",
      data:[9.3, 12.5, 5.5]
    }]
  });
};
function desenhaGrafico2() {
  $("#grafico-linhas2").highcharts({
     title: {
       text: "Whetstone em milhões",
     },
     xAxis: {
       categories: ["windows", "ubunto", "virtual-mc"]
     },
     series: [{
       name: "Sistema 1",
       data: [2047, 3247, 4025]
    },{
      name: "Sistema 2",
      data:[3423, 4923, 2763]
    }]
  });
};

function desenhaGrafico3() {
  while (true) { // this loop runs forever

    var input = prompt("Por favor indique os Dhrystones em milhoes no windows: ");
    if (!input)
      break;        // leave the loop

    input = parseInt(input)

    if (isNaN(input)) {
        alert("Isso não é um numero!");

    } else if (input > 10000) {
        alert("O numero é muito alto.");

    }
    else{
      break;
    }
  }

    while (true) { // this loop runs forever

      var input2 = prompt("Por favor indique os Dhrystones em milhoes no ubunto: ");
      if (!input)
        break;        // leave the loop

      input2 = parseInt(input2)

      if (isNaN(input2)) {
          alert("Isso não é um numero");

      } else if (input2 > 10000) {
          alert("O numero é muito alto.");

      }
      else{
        break;
      }
    }

      while (true) { // this loop runs forever

        var input3 = prompt("Por favor indique os Dhrystones em milhoes na virtual machine: ");
        if (!input3)
          break;        // leave the loop

        input3 = parseInt(input3)

        if (isNaN(input3)) {
            alert("Isso não é um numero");

        } else if (input3 > 10000) {
            alert("O numero é muito alto.");

        }
        else{
          break;
        }

        }
  $("#grafico-linhas3").highcharts({
     title: {
       text: "Dhrystones em milhões",
     },
     xAxis: {
       categories: ["windows", "ubunto", "virtual-mc"]
     },
     series: [{
       name: "Sistema 1",
       data: [8.5, 12.3, 8.4]
    },{
      name: "O seu Sistema",
      data:[input, input2, input3]
    }]
  });

  $("#grafico-linhas4").highcharts({
     title: {
       text: "Dhrystones em milhões",
     },
     xAxis: {
       categories: ["windows", "ubunto", "virtual-mc"]
     },
     series: [{
       name: "Sistema 2",
       data: [9.3, 12.5, 5.5]
    },{
      name: "O seu Sistema",
      data:[input, input2, input3]
    }]
  });

  
};
