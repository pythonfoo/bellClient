# bellClient #

tiny door bell client for the Raspberry Pi  
It is mostly the same code as in the examples for the Pi.  

## What...? ##

I had an remote controlled door bell with far to less range.  
But it could reach the basement, where the main network infrastructure is located.  
So instead of making/buying any kind of radio transmitter, I used what I had (an really cheap remote door bell).  
I grabed one of the blinking LEDs and conected it with an Opto-isolator to the Pi.  
When the light fires up, I get the signal, using **wget** to "grab" an prepared webpage on another Pi (with Apache)
on my destination and playing sounds which I think a door bell should play ;)  

The server-side is an ugly PHP-script, so I would publish it on my [GitHub] [6] account, instead (soon [tm] ;)


## The build ##

  1.) [Prototype] [1]  
  2.) [Prototype] [2] (blinking green light)  
  3.) [Opto-isolator (Optokoppler) CNY 17-4] [3] with tiny board  
  4.) [tape it together] [4]  
  5.) [finished and installed] [5]  


## Credits ##

Thanks to [derf] [7] for the help selecting the right Opto-isolator.

  [1]: https://twitter.com/bison_42/status/328607913226682368        "Prototype"
  [2]: https://twitter.com/bison_42/status/328608426492039168        "Prototype"
  [3]: https://twitter.com/bison_42/status/328609083286487040        "Opto-isolator"
  [4]: https://twitter.com/bison_42/status/328609371468746752        "tape it together"
  [5]: https://twitter.com/bison_42/status/328609700549648384        "finished and installed"
  [6]: https://github.com/bison--                                    "myGitHub"
  [7]: https://github.com/derf                                       "credits derf"
