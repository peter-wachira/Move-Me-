 //doughnut
 var ctxD = document.getElementById("doughnutChart1").getContext('2d');
 var myLineChart = new Chart(ctxD, {
   type: 'doughnut',
   data: {
     labels: ["Red", "Green", "Yellow", "Grey", "Dark Grey"],
     datasets: [{
       data: [300, 50, 100, 40, 120],
       backgroundColor: ["#ff4500", "#8fbc8f", "#FDB45C", "#949FB1", "#4D5360"],
       hoverBackgroundColor: ["#FF5A5E", "#90ee90", "#FFC870", "#A8B3C5", "#616774"],
       borderColor:["#393e46","#393e46","#393e46","#393e46","#393e46"]
     }]
   },
   options: {
     responsive: true
   }
 });

 var ctxD = document.getElementById("doughnutChart2").getContext('2d');
 var myLineChart = new Chart(ctxD, {
   type: 'doughnut',
   data: {
     labels: ["Red", "Green", "Yellow", "Grey", "Dark Grey"],
     datasets: [{
       data: [300, 50, 100, 40, 120],
       backgroundColor: ["#ff4500", "#8fbc8f", "#FDB45C", "#949FB1", "#4D5360"],
       hoverBackgroundColor: ["#FF5A5E", "#90ee90", "#FFC870", "#A8B3C5", "#616774"],
       borderColor:["#393e46","#393e46","#393e46","#393e46","#393e46"]
     }]
   },
   options: {
     responsive: true
   }
 });

 