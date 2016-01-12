
function colorCoord(event) {
    event = event || window.event;
    
    var canvas = document.getElementById('colorPicker'),
        x = event.pageX - canvas.offsetLeft,
        y = event.pageY - canvas.offsetTop;
    
    alert(x + ' ' + y);
}