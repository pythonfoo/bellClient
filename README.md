# bellClient #

tiny door bell client for the Raspberry Pi  
It is mostly the same code as in the examples for the Pi.  

## What...? ##

I had an remote controlled door bell with far to less range.  
But it could reach the basement, where the main network infrastructure is located.  
So instead of making/buying any kind of radio transmitter, I used what i had (an really cheap remote door bell).  
I grabed one of the blinking LEDs and conected it with an Opto-isolator to the Pi.  
When the light fires up, I get the signal, using **wget** to "grab" an prepared webpage on the other Pi (with Apache)
on my destination and playing now how I think a door bell should sound like ;)

## The build ##

  1.) [Prototype] [1]  
  2.) [Prototype] [2] (blinking green light)  
  3.) [Opto-isolator (Optokoppler)] [3] with tiny board  
  4.) [tape it together] [4]  
  5.) [finished and installed] [5]  

  [1]: https://twitter.com/bison_42/status/328607913226682368        "p1"
  [2]: https://twitter.com/bison_42/status/328608426492039168        "p2"
  [3]: https://twitter.com/bison_42/status/328609083286487040        "p3"
  [4]: https://twitter.com/bison_42/status/328609371468746752        "p4"
  [5]: https://twitter.com/bison_42/status/328609700549648384        "p5"
