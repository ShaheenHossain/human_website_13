eagle.define("website_sale.tour_info_backend", function (require) {
"use strict";

var tour = require("web_tour.tour");
var steps = require("website_sale.tour_info");
tour.register("info", steps);

});
