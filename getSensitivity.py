import json;
import urllib;
import urllib2;
import time;
import csv

url1 = 'https://api.particle.io/v1/devices/laser_aardvark/temperature?access_token=3b0183aac1a6233abc2cee57eb57d4299f6cf7d2';
url2 = 'https://api.particle.io/v1/devices/laser_aardvark/light?access_token=3b0183aac1a6233abc2cee57eb57d4299f6cf7d2';
url3 = 'https://api.particle.io/v1/devices/laser_aardvark/touch?access_token=3b0183aac1a6233abc2cee57eb57d4299f6cf7d2';
url4 = 'https://api.particle.io/v1/devices/laser_aardvark/sound?access_token=3b0183aac1a6233abc2cee57eb57d4299f6cf7d2';
url5 = 'https://api.particle.io/v1/devices/laser_aardvark/led?access_token=3b0183aac1a6233abc2cee57eb57d4299f6cf7d2';

url6 = 'https://api.particle.io/v1/devices/badger_vampire/temperature?access_token=3b0183aac1a6233abc2cee57eb57d4299f6cf7d2';
url7 = 'https://api.particle.io/v1/devices/badger_vampire/light?access_token=3b0183aac1a6233abc2cee57eb57d4299f6cf7d2';
url8 = 'https://api.particle.io/v1/devices/badger_vampire/touch?access_token=3b0183aac1a6233abc2cee57eb57d4299f6cf7d2';
url9 = 'https://api.particle.io/v1/devices/badger_vampire/sound?access_token=3b0183aac1a6233abc2cee57eb57d4299f6cf7d2';
url0 = 'https://api.particle.io/v1/devices/badger_vampire/led?access_token=3b0183aac1a6233abc2cee57eb57d4299f6cf7d2';

#urlpower = 'https://api.particle.io/v1/devices/laser_aardvark/powerleds?access_token=3b0183aac1a6233abc2cee57eb57d4299f6cf7d2';
#urlpower = 'https://api.particle.io/v1/devices/badger_vampire/powerleds?access_token=3b0183aac1a6233abc2cee57eb57d4299f6cf7d2';
#data = urllib.urlencode({'args':'on'})
#req = urllib2.Request(urlpower, data);
#response = urllib2.urlopen(req);
#print response.read();

led_module1_status = 1;
led_module2_status = 1;

while 1:
    
    print '******SENSOR 1*****'
    print "Temperature Sensor"
    response = urllib2.urlopen(url1);
    temperature_result = json.loads(response.read());
    print temperature_result
    
    print "Light sensor"
    response = urllib2.urlopen(url2);
    light_result = json.loads(response.read());
    print light_result;
    
    print "Touch sensor"
    response = urllib2.urlopen(url3);
    touch_result = json.loads(response.read());
    print touch_result;

    print "Sound sensor"
    response = urllib2.urlopen(url4);
    sound_result = json.loads(response.read());
    print sound_result;

    f = open('file.csv', 'a');
    value = str(sound_result['coreInfo']['deviceID']) + ',' \
        + str(sound_result['coreInfo']['last_heard']) + ',' \
        + str(temperature_result['result']) + ',' \
        + str(light_result['result']) + ',' \
        + str(touch_result['result']) + ',' + str(sound_result['result']) + '\n';
    f.write(value);
    f.close();

    print "LED stuff"
    if led_module1_status == 1:
        data = urllib.urlencode({'args':'on'})
        req = urllib2.Request(url5, data);
        response = urllib2.urlopen(req);
        print response.read();
        led_module1_status = 0;
    else:
        data = urllib.urlencode({'args':'off'})
        req = urllib2.Request(url5, data);
        response = urllib2.urlopen(req);
        print response.read();
        led_module1_status = 1;
    time.sleep(5);

    print '******SENSOR 2*********'
    print "Temperature Sensor"
    response = urllib2.urlopen(url6);
    temperature_result = json.loads(response.read());
    print temperature_result
    
    print "Light sensor"
    response = urllib2.urlopen(url7);
    light_result = json.loads(response.read());
    print light_result;
    
    print "Touch sensor"
    response = urllib2.urlopen(url8);
    touch_result = json.loads(response.read());
    print touch_result;

    print "Sound sensor"
    response = urllib2.urlopen(url9);
    sound_result = json.loads(response.read());
    print sound_result;

    f = open('file.csv', 'a');
    value = str(sound_result['coreInfo']['deviceID']) + ',' \
        + str(sound_result['coreInfo']['last_heard']) + ',' \
        + str(temperature_result['result']) + ',' \
        + str(light_result['result']) + ',' \
        + str(touch_result['result']) + ',' + str(sound_result['result']) + '\n';
    f.write(value);
    f.close();

    print "LED stuff"
    if led_module2_status == 1:
        data = urllib.urlencode({'args':'on'})
        req = urllib2.Request(url0, data);
        response = urllib2.urlopen(req);
        print response.read();
        led_module2_status = 0;
    else:
        data = urllib.urlencode({'args':'off'})
        req = urllib2.Request(url0, data);
        response = urllib2.urlopen(req);
        print response.read();
        led_module2_status = 1;
    time.sleep(5);
