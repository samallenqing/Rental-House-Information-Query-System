angular.module('app.services', [])
    .service("FindAdService", function ($http) {
        this.findAdByZipCode = function findAdByZipCode(zip) {
            var query = 'api/ads/' + zip;
            return $http.get(query).then(function success(response) {
                    return response.data;
                },
                function fail(response) {
                    return response;
                })
        }
    });
