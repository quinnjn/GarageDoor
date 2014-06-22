GarageDoor
==========

Raspberry Pi setup for my Garage door. 

### Purpose

I'm currently renting a basement suite which luckily comes with my own garage. The problem though is it only has one garage door opener which sucks when: I want to go biking, motorcycling, enter the garage myself.

If only there was a way to open my garage door through my cell phone! Now there is!

### Parts Required

1. [Raspberry Pi](http://www.raspberrypi.org/products/)
2. [Relay Module](http://www.amazon.com/SainSmart-2-CH-2-Channel-Relay-Module/dp/B0057OC6D8/ref=pd_sim_e_5?ie=UTF8&refRID=1M70ZSQT04YCGDHK01KH)

### Pre-Setup

I won't be going through any pre-setup information here. There are way better blogs on setting up the raspberry pi than what I can explain. Although there should be some requirements funfilled before continuing on to the actual garage door operating stuff

1. Raspberry Pi should be connected to the internet
2. Python should be installed along with the Flask and Rpi.GPIO modules

### Connecting the Pi to the Relay

I found this wonderful video on [how to connect the relay to the pi](https://www.youtube.com/watch?v=Z2B67hybdAA). Definately check it out!

Using the video, here are the connections I came up with:

Raspberry Pi  | Relay
------------- | -------------
              | Jumper [JD-VCC, VCC]
5V OUT        | VCC
GRD           | GRD
GPIO18        | IN1
