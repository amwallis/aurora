webiopi().ready(function() {
                        webiopi().setFunction(26,"out");
                        webiopi().setFunction(19,"out");
        		webiopi().setFunction(13,"out");
        		
        		var content, buttonR, buttonG, buttonB;
        		content = $("#content");
        		
        		buttonR = webiopi().createGPIOButton(26,"red");
                        buttonG = webiopi().createGPIOButton(19,"green");
                        buttonB = webiopi().createGPIOButton(13,"blue");

                        content.append(buttonR);
                        content.append(buttonG);
                        content.append(buttonB);
                        
        });