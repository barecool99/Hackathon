var graph1 = new Highcharts.chart({
    credits: {
        enabled: false
    },
    chart: {
        renderTo: 'graph1',
        type: 'column',
        backgroundColor: 'transparent'
    },
    tooltip:{
        enabled: false,
      },
    data: {
        enablePolling: true,
        csv: document.getElementById('csv').innerHTML
      
    },
    plotOptions: {
        column:{
            dataLabels:{
                formatter:function(){
                    return this.y + '%'
                },
                enabled: true
            },
            pointPlacement: 0.2
        },
        series: {
            
            pointWidth: 20,
            borderWidth: 0,
            borderRadius: 3,
            colorByPoint: true,
            colors: ['#EEC0CF', '#CAABCD', '#989BC8','#578EB7', '#007F96','#007F96'],
    }
},
    title: {
        text: 'Cases of Breast Cancer related to Age at Diagnosis'
    },
    yAxis: {
        lineColor: 'transparent',
        gridLineColor: '#878682',
        gridLineDashStyle: 'Dot',
        labels: false,
        title: {
            text: 'Units'
        }
    },
    xAxis: {
         lineColor: 'transparent',
         labels: {
            height: '70px'
         }
    },
    responsive: {
        rules: [{
        condition: {
            maxwidth: 500
        },
        chartOptions: {
           legend: { enabled: false},
           yAxis: {title: {text: ''}}
        }
    }]
    }
});
var graph2 = new Highcharts.chart({
    credits: {
        enabled: false
    },
    chart: {
        renderTo: 'graph2',
        type: 'bar',
        backgroundColor: 'transparent'
    },
    tooltip:{
        enabled: false,
      },
    data: {
        enablePolling: true,
        csv: document.getElementById('csv1').innerHTML
      
    },
    plotOptions: {
        bar:{
            dataLabels:{
               
                enabled: true
            },
            pointPlacement: -0.2
        },
        series: {
            
            pointWidth: 20,
            borderRadius: 3,
            colorByPoint: true,
            colors: ['#EEC0CF', '#CAABCD', '#989BC8','#578EB7', '#007F96','#007F96'],
    }
},
    title: {
        text: 'Cases of Breast Cancer incidence in the U.S by Race and Ethnicity per 100,000'
    },
    yAxis: {
        lineColor: 'transparent',
        gridLineColor: '#878682',
        gridLineDashStyle: 'Dot',
        labels: false,
        title: {
            text: 'Units'
        }
    },
    xAxis: {
         lineColor: 'transparent',
         labels: {
            height: '70px'
         }
    },
    responsive: {
        rules: [{
        condition: {
            maxwidth: 500
        },
        chartOptions: {
           legend: { enabled: false},
           yAxis: {title: {text: ''}}
        }
    }]
    }
});
var graph3 = new Highcharts.chart({
    credits: {
        enabled: false
    },
    chart: {
        renderTo: 'graph3',
        type: 'pie',
        marginBottom:30,
        marginTop: 0,
        
        backgroundColor: 'transparent'
    },
    data: {
        enablePolling: true,
       csv: document.getElementById('csv3').innerHTML
    },
    legend:{
        layout: 'vertical',
        itemMarginTop: 10,
        itemStyle:{'color':'black','fontSize':'15px'},
        align: 'center',
        verticalAlign: 'bottom',
        x: 0,
        y: 0
        
    },
    tooltip:{
      enabled: false,
    },
    plotOptions: {
        pie:{
            innerSize: '73%',
            size: '80%',
            showInLegend: true,
            
            dataLabels:{
                enabled: false,

               color: '#ffffff',
                distance: -24,
              style:{
                  fontSize: '13px',
                  fontWeight: 'bold',
                  textShadow: '1px 0 black, 1px 0 black, 0 -1px black'
              },
                formatter: function(){
                return this.y + '%';
                }
        },
        states:{
            inactive:{
                opacity: 1
            }
        }
     },
        series: {
            borderRadius: 3,
            point: {
                events: {
                    mouseOver: function (e) {
                        this.series.data.forEach(p => {
                            p.update({
                                datalabels: {
                                    enabled: false
                                },
                            }, false, false)

                        });
                        this.update({
                            dataLabels: {
                                enabled: true
                            },
                        });
                        
                    },
                    mouseOut: function(e){
                        this.series.data.forEach(p => {
                            p.update({
                                datalabels: {
                                    enabled: true
                                },
                            }, true, true)

                        });
                        this.update({
                            dataLabels: {
                                enabled: false
                            },
                        });
                        
                    }
                }
            },
            borderColor: '#000000',
            borderWidth: 3,
            colorByPoint: true,
    colors: ['#EEC0CF', '#CAABCD', '#989BC8','#578EB7', '#007F96','#007F96'],             
},
},
    title: {
        margin: 0,
        text: 'Chart showing the way in which Breast Cancer Paitinets got the Diagnosis '
    },
    xAxis: {
         labels: 'true'
    },
    responsive: {
        rules: [{
        condition: {
            maxwidth: 900 
        },
        chartOptions: {
           legend: { enabled: true},
        }
    }]
    }
});