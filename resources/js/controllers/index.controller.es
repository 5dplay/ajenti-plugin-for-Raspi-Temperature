angular.module('raspi.raspi-temp').controller('RaspiTempWidgetController', $scope => {
    $scope.$on('widget-update', ($event, id, data) => {
        if (id !== $scope.widget.id) {
            return;
        }
        $scope.raspi_temp = data;
    })
});
