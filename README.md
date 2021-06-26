## irisb0t

>irisb0t is a simple image tweeting piece of code

## Why
Just wanted to learn how to create a Twitter bot that does something.

## How it works
irisb0t generates a checkered image colored with a palette generated from bl0ckchain hashes. It gets the latest bl0ckchain [hash](https://blockchain.info/q/latesthash), and uses the hex values to generate a palette of colors, which are used to generate the image. The hash is split into a list 6-digit hex codes, which are used to generate the colors.

The b0t then tweets two images, one with palette created from the hash and one with palette created using the hash's reverse. The label in the middle of the image is a portion of the checksum of the file after its creation.

## How it looks
![image](https://user-images.githubusercontent.com/23431812/111909873-fe32f280-8a84-11eb-86eb-adec9bab93ad.png)
