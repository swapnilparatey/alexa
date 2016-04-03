// -----------------------------------------
// Function and Variable with Photoresistors
// -----------------------------------------
// In this example, we're going to register a Spark.variable() with the cloud so that we can read brightness levels from the photoresistor.
// We'll also register a Spark.function so that we can turn the LED on and off remotely.

// We're going to start by declaring which pins everything is plugged into.
#include <math.h>

int led = D7; // This is where your LED is plugged in. The other side goes to a resistor connected to GND.

int photoresistor = A0; // This is where your photoresistor is plugged in. The other side goes to the "power" pin (below).
int light = A1;
int touch = A2;
int sound = A3;
int dzero = D0;
int done = D1;
int dtwo = D2;

int power = A5; // This is the other end of your photoresistor. The other side is plugged into the "photoresistor" pin (above).
// The reason we have plugged one side into an analog pin instead of to "power" is because we want a very steady voltage to be sent to the photoresistor.
// That way, when we read the value from the other side of the photoresistor, we can accurately calculate a voltage drop.
const int B=4275;                 // B value of the thermistor
const int R0 = 100000;            // R0 = 100k
float analogvalue; // Here we are declaring the integer variable analogvalue, which we will use later to store the value of the photoresistor.
int temperature;
float R;
char value[5];
int lightvalue;
int touchvalue;
int soundvalue;
double temperature_d, sound_d, light_d;

// Next we go into the setup function.

void setup() {

    // First, declare all of our pins. This lets our device know which ones will be used for outputting voltage, and which ones will read incoming voltage.
    pinMode(led,OUTPUT); // Our LED pin is output (lighting up the LED)
    pinMode(photoresistor,INPUT);  // Our photoresistor pin is input (reading the photoresistor)
    pinMode(light, INPUT);
    pinMode(touch, INPUT);
    pinMode(sound, INPUT);
    pinMode(power,OUTPUT); // The pin powering the photoresistor is output (sending out consistent power)
    pinMode(dzero, OUTPUT);pinMode(done, OUTPUT);pinMode(dtwo, OUTPUT);

    // Next, write the power of the photoresistor to be the maximum possible, so that we can use this for power.
    digitalWrite(power,HIGH);
    digitalWrite(led, LOW);
    digitalWrite(dzero, LOW);digitalWrite(done, LOW);digitalWrite(dtwo, LOW);

    // We are going to declare a Spark.variable() here so that we can access the value of the photoresistor from the cloud.
    Particle.variable("temperature", value, STRING);
    Particle.variable("light", &lightvalue, INT);
    Particle.variable("touch", &touchvalue, INT);
    Particle.variable("sound", &soundvalue, INT);
    Particle.variable("tempd", &temperature_d, DOUBLE);
    Particle.variable("soundd", &sound_d, DOUBLE);
    Particle.variable("lightd", &light_d, DOUBLE);
    Spark.function("led",ledToggle);
    Spark.function("powerleds", powerledsfunc);
    // This is saying that when we ask the cloud for "analogvalue", this will reference the variable analogvalue in this app, which is an integer variable.

    // We are also going to declare a Spark.function so that we can turn the LED on and off from the cloud.
    
}


// Next is the loop function...

void loop() {

    // Probe temperature sensor and get data ready
    temperature = analogRead(photoresistor);
    R = 4095.0/((float)temperature)-1.0;
    R = R0*R;
    analogvalue = 1.0/(log(R/100000.0)/B+1/298.15)-273.15; //convert to temperature via datasheet ;
    sprintf(value,"%.2f",analogvalue);
    
    lightvalue = analogRead(light);
    
    touchvalue = analogRead(touch);
    
    soundvalue = analogRead(sound);
    
    temperature_d = (double)analogvalue;
    sound_d = (double)soundvalue;
    light_d = (double)touchvalue;

}


// Finally, we will write out our ledToggle function, which is referenced by the Spark.function() called "led"
int ledToggle(String command) {

    if (command=="on") {
        digitalWrite(led,HIGH);
        return 1;
    }
    else if (command=="off") {
        digitalWrite(led,LOW);
        return 0;
    }
    else {
        return -1;
    }

}

int powerledsfunc(String command) {

    if (command=="on") {
        digitalWrite(dzero,HIGH);
        digitalWrite(done,HIGH);
        digitalWrite(dtwo,HIGH);
        return 1;
    }
    else if (command=="off") {
        digitalWrite(dzero,LOW);
        digitalWrite(done,LOW);
        digitalWrite(dtwo,LOW);
        return 0;
    }
    else {
        return -1;
    }
}