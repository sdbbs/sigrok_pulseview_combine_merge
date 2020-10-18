
/*

Original from: [Analog Comparator Interrupt](https://forum.arduino.cc/index.php?topic=149840.msg1135919#msg1135919)

 Analog comparator example using interrupt and testing ACO flag

Compares voltage sensed at pins 6 (AIN0) and 7 (AIN1) which are the analog inputs into the comparator.  AIN0 is
the positve input and AIN1 is the negative input to the comparator. Once the voltage on AIN0(+) rises above the voltage
sensed at AIN1(-), the comparator output becomes high and triggers the interrupt to run.  The interrupt routine toggles
the LED connected to Pin 13.  The ACO flag is tested in the loop() and Pin 9 is set to match.

The circuit:
* audio output from PC is connected via: GND to GND of Arduino, channel to pin 6 (AIN0)
* pin 7 (AIN1) is connected to Arduino GND

* On board LED connected to Pin 13
* Pin 9 reflects the status of the comparator output.


created 27 Feb 2013
by Anthony Fremont
(modified: sdbbs, 2020)

*/

void setup() {
 // initialize serial communications at 9600 bps:
 //Serial.begin(9600);

 ACSR =
   (0 << ACD) |    // Analog Comparator: Enabled
   (0 << ACBG) |   // Analog Comparator Bandgap Select: AIN0 is applied to the positive input
   (0 << ACO) |    // Analog Comparator Output: Off
   (1 << ACI) |    // Analog Comparator Interrupt Flag: Clear Pending Interrupt
   (1 << ACIE) |   // Analog Comparator Interrupt: Enabled
   (0 << ACIC) |   // Analog Comparator Input Capture: Disabled
   (1 << ACIS1) | (1 << ACIS0);   // Analog Comparator Interrupt Mode: Comparator Interrupt on Rising Output Edge

 pinMode(13, OUTPUT);  // toggles when ISR runs

 pinMode(9, OUTPUT);   // indicates status of comparator output
}

void loop() {

 if(ACSR & (1 << ACO))         //  check status of comparator output flag
   digitalWrite(9, HIGH);    //   and mirror it to Pin 9
 else
   digitalWrite(9, LOW);

 delay(100);
}

ISR(ANALOG_COMP_vect ) {
 digitalWrite(13, !digitalRead(13));   // toggle state of Pin 13
}
