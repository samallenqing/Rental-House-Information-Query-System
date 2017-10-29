angular.module("app.controllers", [])
    .controller("myCtrl", function (FindAdService,$scope) {
            var mc = this;
            mc.ads = [];
            mc.findAdByZipCode = function (zip) {
                FindAdService.findAdByZipCode(zip).then(function (data) {
                    mc.ads = data;
                })
            }
            $scope.lessThan = function (item) {
                if ($scope.price == undefined || $scope.price == 0) {
                    return true;
                } else {
                    if ($scope.price > item.price) {
                        return true;
                    }
                }
                return false;
            }
        }
    )
