webiopi().ready(function() {
    var updateLightValues = function(macro, args, response) {
                var rgbValues = response.split(";");
                $("#redPct").val(rgbValues[0]);         //jQuery functions
                $("#greenPct").val(rgbValues[1]);
                $("#bluePct").val(rgbValues[2]);
    }

    // Immediately call getLightValues macro to update the UI
    // updateLightValues is the callback function, defined above    
    webiopi().callMacro("getLightValue", [], updateLightValues);  //[] empty array

    // Create a button to call setLightValue macro
    var updateButton = webiopi().createButton("updateButton", "Update", function() {
        var values = [$("#redPct").val(), $("#greenPct").val(), $("#bluePct").val()];
        webiopi().callMacro("setLightValue", values, updateLightValues);
    });
    $("#controls").append(updateButton); // Append the button to the controls box using a jQuery function

    var rainbowButton = webiopi().createButton("rainbowButton", "Rainbow", function() {
        webiopi().callMacro("rainbowCycle", [], updateLightValues);
    });
    $("#controls").append(rainbowButton); // Append the button to the controls box using a jQuery function

    // pass true to refresh repeatedly
    webiopi().refreshGPIO(true);

});