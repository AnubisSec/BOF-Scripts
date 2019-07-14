# BOF-Scripts


Just some quick and dirty scripts I made. Originally developed while doing the VulnHub machine Brainpan.

Thought these might be useful for future use, so here they are. Pretty simplistic to use as well.

Also added `find_pwn.py` which is a wrapper around the `cyclic_find()` function for pwntools. It was annyoing adding the `0x` into the address from Immunity debugger and then spinning up python and typing everything out, so I just wrote this. It just asks for your address (without the `0x` and then it will find the offset
