const {labels,datasets}=await getSourceData();
drawChart('doughnut',labels,datasets);
let myChart;
  $("#line").click(function() {
    drawChart('line',labels,datasets);
  });
  
  $("#bar").click(function() {
    drawChart('bar',labels,datasets);
  });
  $("#pie").click(function() {
    drawChart('pie',labels,datasets);
  });
  $("#doughnut").click(function() {
    drawChart('doughnut',labels,datasets);
  });
  $("getNewData").click(async()=>{
    const {labels,datasets}=await getSourceData();
    drawChart('doughnut',labels,datasets);
  })
  function drawChart(chartType,labels,datasets) {
    if (myChart) {
        myChart.destroy();
      }  
    const config = {
        type: chartType,
        data: {
      labels: labels,
      datasets: datasets
    },
        options: {
          responsive: true,
        }
      };
    const ctx = document.getElementById('myChart').getContext('2d');
    myChart = new Chart(ctx, config);
  };


async function getSourceData(){
  const destinationUrl=`${location.origin}/academic/get_results_between_date_range`;
  const res= await fetch(destinationUrl);
  const resJson=await res.json();
  const labels=Object.keys(resJson);
  const data=Object.values(resJson);
  const backgroundColor=[];
  const borderColor=[];
  for(let i=0;i<labels.length;i++){
    backgroundColor.push(getRandomColor());
    borderColor.push(getRandomColor());
  }
  const datasets= [{data: data,backgroundColor, fill: false,}]
  return {labels,datasets};
}
function getRandomColor() {
    let letters = '0123456789ABCDEF'.split('');
    let color = '#';
    for (var i = 0; i < 6; i++ ) {
        color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
}
