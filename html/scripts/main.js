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
    var sendButton = webiopi().createButton("sendButton", "Send", function() {
        var values = [$("#redPct").val(), $("#greenPct").val(), $("#bluePct").val()];
        webiopi().callMacro("setLightValue", values, updateLightValues);
    });
    $("#controls").append(sendButton); // Append the button to the controls box using a jQuery function

    // pass true to refresh repeatedly
    webiopi().refreshGPIO(true);

});



// webiopi().ready(function() {
//     webiopi().setFunction(26,"out");
//     webiopi().setFunction(19,"out");
//     webiopi().setFunction(13,"out");
    
//     // var content, buttonR, buttonG, buttonB;
//     // content = $("#content");
    
//     // buttonR = webiopi().createGPIOButton(26,"red");
//     // buttonG = webiopi().createGPIOButton(19,"green");
//     // buttonB = webiopi().createGPIOButton(13,"blue");

//     // content.append(buttonR);
//     // content.append(buttonG);
//     // content.append(buttonB);                
// });