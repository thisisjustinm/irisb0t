## irisb0t

>irisb0t is a simple image tweeting piece of code

## Why?
Just wanted to learn how to create a Twitter bot that does something.

## How it works
irisb0t generates a checkered image colored with a palette generated from blockchain hashes. It gets the latest blockchain [hash](https://blockchain.info/q/latesthash), and uses the hex values to generate a palette of colors, which are used to generate the image. The hash is split into a list 6-digit hex codes, which are used to generate the colors.

The b0t then tweets two images, one with palette created from the hash and one with palette created using the hash's reverse. The label in the middle of the image is a portion of the checksum of the file after its creation.

## Go check it out

<blockquote class="twitter-tweet"><p lang="ht" dir="ltr">Current Blockchain hash : 00000000000000000008f4e8c6292c499c5a14d6bb5dfbb0e11d3e8edc4b5982<br>Image : <a href="https://t.co/2uVPtcBsvz">pic.twitter.com/2uVPtcBsvz</a></p>&mdash; iris (@irisb0t) <a href="https://twitter.com/irisb0t/status/1394204591991009284?ref_src=twsrc%5Etfw">May 17, 2021</a></blockquote>
