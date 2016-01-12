
function colorCoord(event) {
    event = event || window.event;
    var x;
    var y;
    var canvas = document.getElementById('colorPicker'),
        x = event.pageX - canvas.offsetLeft,
        y = event.pageY - canvas.offsetTop;
    var args = "fwd"
    var pos = [ x, y ];
    webiopi().callMacro("get_color", pos);
    alert(x + ' ' + y);
}