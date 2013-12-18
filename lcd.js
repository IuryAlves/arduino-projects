var arduino = require('duino');
var board = new arduino.Board({
	device: '/dev/ttyACM0'
});

var lcd = new arduino.LCD({
	board: board,
  pins: {rs:7, rw:8, e:9, data:[10, 11, 12]}
});

lcd.begin(16, 2);
lcd.print("Hello Internet.");

