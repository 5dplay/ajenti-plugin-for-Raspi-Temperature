angular.module('raspi.raspi-temp').config(($routeProvider) => {
    $routeProvider.when('/view/raspi-temp', {
        templateUrl: '/raspi-temp:resources/partial/raspi-temp.html',
        controller: 'RaspiTempWidgetController',
    });
});
