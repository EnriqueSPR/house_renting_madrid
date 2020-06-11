
function getBathValue() {
    var uibathrooms = document.getElementsByName("uibathrooms");
    for (var i in uibathrooms) {
        if (uibathrooms[i].checked) {
            return parseInt(i) + 1;
        }
    }
    return -1; // Invalid Value
}

function getRoomsValue() {
    var uibedrooms = document.getElementsByName("uibedrooms");
    for (var i in uibedrooms) {
        if (uibedrooms[i].checked) {
            return parseInt(i) + 1;
        }
    }
    return -1; // Invalid Value
}


function onClickedEstimatePrice() {

    console.log("Estimate price button clicked");
    var url2 = "http://127.0.0.1:5000/predict_home_rent"; // Use this if you are NOT using nginx which is first 7 tutorials
    //var url = "/api/predict_home_price"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
    var mt_sq = document.getElementByName("sq_mt");
    var bedrooms = getRoomsValue();
    var bathrooms = getBathroomsValue();
    var loc = document.getElementById("uiarea");
    var estRent = document.getElementById("uiEstimatedRent");

    $.post(url2, {
        sq_mt: parseFloat(mt_sq.value),
        bedrooms: bedrooms,
        bathrooms: bathrooms,
        area: loc.value
    }, function (data, status) {
            console.log(data.estimated_rent);
            estRent.innerHTML = "<h2>" + data.estimated_rent.toString() + " Euros per month </h2>";
            console.log(status);
    });
}

function onPageLoad() {
    console.log("document loaded");
    var url1 = "http://127.0.0.1:5000/get_area_names"; // Use this if you are NOT using nginx which is first 7 tutorials
    // var url = "/api/get_location_names"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
    $.get(url1, function (data, status) {
        console.log("got response for get_location_names request");
        if (data) {
            var areas = data.Areas;
            // var uiLocations = document.getElementById("uiLocations");
            $('#uiarea').empty();
            for (var i in areas) {
                var opt = new Option(areas[i]);
                $('#uiarea').append(opt);
            }
        }
    });
}

window.onload = onPageLoad;