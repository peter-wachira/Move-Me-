 //doughnut
 $(document).ready(function () {
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


  $('#usersData').DataTable();
  $('.dataTables_length').addClass('bs-select');
 

  const $tableID = $('#table');
  const $BTN = $('#export-btn');
  const $EXPORT = $('#export');

  const newTr = `
 <tr class="hide">
   <td class="pt-3-half" contenteditable="true">Example</td>
   <td class="pt-3-half" contenteditable="true">Example</td>
   <td class="pt-3-half" contenteditable="true">Example</td>
   <td class="pt-3-half" contenteditable="true">Example</td>
   <td class="pt-3-half" contenteditable="true">Example</td>
   <td class="pt-3-half">
     <span class="table-up"><a href="#!" class="indigo-text"><i class="fas fa-long-arrow-alt-up" aria-hidden="true"></i></a></span>
     <span class="table-down"><a href="#!" class="indigo-text"><i class="fas fa-long-arrow-alt-down" aria-hidden="true"></i></a></span>
   </td>
   <td>
     <span class="table-remove"><button type="button" class="btn btn-danger btn-rounded btn-sm my-0 waves-effect waves-light">Remove</button></span>
   </td>
 </tr>`;

  $('.table-add').on('click', 'i', () => {

    const $clone = $tableID.find('tbody tr').last().clone(true).removeClass('hide table-line');

    if ($tableID.find('tbody tr').length === 3) {

      $('tbody').append(newTr);
    }

    $tableID.find('table').append($clone);
  });

  $tableID.on('click', '.table-remove', function () {

    $(this).parents('tr').detach();
  });

  $tableID.on('click', '.table-up', function () {

    const $row = $(this).parents('tr');

    if ($row.index() === 1) {
      return;
    }

    $row.prev().before($row.get(0));
  });

  $tableID.on('click', '.table-down', function () {

    const $row = $(this).parents('tr');
    $row.next().after($row.get(0));
  });

  // A few jQuery helpers for exporting only
  jQuery.fn.pop = [].pop;
  jQuery.fn.shift = [].shift;

  $BTN.on('click', () => {

    const $rows = $tableID.find('tr:not(:hidden)');
    const headers = [];
    const data = [];

    // Get the headers (add special header logic here)
    $($rows.shift()).find('th:not(:empty)').each(function () {

      headers.push($(this).text().toLowerCase());
    });

    // Turn all existing rows into a loopable array
    $rows.each(function () {
      const $td = $(this).find('td');
      const h = {};

      // Use the headers from earlier to name our hash keys
      headers.forEach((header, i) => {

        h[header] = $td.eq(i).text();
      });

      data.push(h);
    });

    // Output the result
    $EXPORT.text(JSON.stringify(data));
  });


  var config={
    apiKey: "AIzaSyC0Z5dua996GPaJzlwX1aK_D6FcVSxUNSo",
    authDomain: "moveme-147d2.firebaseapp.com",
    databaseURL: "https://moveme-147d2.firebaseio.com",
    storageBucket: "moveme-147d2.appspot.com",
  }
   // Initialize Firebase
  firebase.initializeApp(config);
  
  function uploadimage(){
    var storage = firebase.storage();
  
    var file=document.getElementById('fileInput').files[0];
    var storageRef = storage.ref();
    var thisref=storageRef.child(file.name).put(file);
    thisref.on('state_changed',function(snapshot){
      console.log("file uploaded successfully")
    },
    function(error){
  
    },
    function() {
      // Upload completed successfully, now we can get the download URL
     var downloadURL=thisref.snapshot.getDownloadURL;
        console.log('Got url');
        alert('file uploaded successfully');
    }
    )
  }
  
});

