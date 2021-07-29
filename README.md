<div align="center" >

[![Python](https://img.shields.io/badge/language-Python-4B8BBE.svg?style=plastic)](https://en.wikipedia.org/wiki/Python_(programming_language)) 
[![Discord](https://img.shields.io/badge/App-Discord-7289DA.svg?style=plastic)](https://discord.com/)
[![License](https://img.shields.io/github/license/R3nzTheCodeGOD/Discord-Token-Generator.svg?style=plastic)](LICENSE)
[![Issues](https://img.shields.io/github/issues/R3nzTheCodeGOD/Discord-Token-Generator.svg?style=plastic)](https://github.com/R3nzTheCodeGOD/R3nzCS/issues)

# Discord Token Generator

</div>

## How does it work

---

<img width=550 align="right" src="https://images-ext-1.discordapp.net/external/daqtkfm2MQZAiBpqC7jNZ6ZCKKpJ6e9MaSfCHcbDDFA/https/i.imgur.com/7WdehGn.png?width=992&height=488">

A discord token basically consists of 3 parts.
* UserID
* Token Creation Time
* Random

The first of these, the userid part, can be simply created and you will find the first head of a user's token, but finding the rest is pure luck.



### let's calculate
---

Let's do some math for this and find out in how many tries we will find the user token for sure.

* With this generator we always know the first side
* the middle part must be 5 characters and consist of 62 different characters = **62<sup>5</sup>**
* and we come to the last part, this one consists of 27 characters and 64 different characters = **64<sup>27</sup>**

```py
print((62 ** 5) + (64 ** 27))
>>> Output: 5846006549323611672814739330865132078624646304736
```
here is the result

`5,846,006,549,323,611,672,814,739,330,865,132,078,624,646,304,736`

**I hope you understand what I mean. Generators are not as cool as you think, on the contrary, they are unnecessary, but if you still want to try, read the usage section below.**

## Usage

First, clone the repository and then go into the `main.py` file and configure the `id` part and the `thread` part according to you, now it's ready to run, run it by typing `py main.py`

`Note:` Install libraries that are not installed using pip.




