
(function ($) {
    "use strict";

    /*----------------------------------*/
    const production_curr_year = JSON.parse(document.getElementById('data-years').textContent);

    var data = {
        labels: ['Январь','Февраль',
                'Март','Апрель','Май',
                'Июнь','Июль','Август',
                'Сентябрь','Октябрь','Ноябрь','Декабрь'],
        series: production_curr_year
    };

    var options = {
        seriesBarDistance: 10
    };

    var responsiveOptions = [
  ['screen and (max-width: 640px)', {
            seriesBarDistance: 5,
            axisX: {
                labelInterpolationFnc: function (value) {
                    return value[0];
                }
            }
  }]
];

    new Chartist.Bar('.ct-bar-chart', data, options, responsiveOptions);


})(jQuery);








