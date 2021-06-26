import requests,tweepy,random,hashlib
from textwrap import wrap
import matplotlib.pyplot as plt,os
from PIL import Image, ImageDraw

def generate_img(lh):
  ls = [i.zfill(6) for i in wrap(lh,6)]
  print(lh)
  size = 30
  img = Image.new("RGB", (size,size), "white")
  pixels = img.load()

  black_2 = []
  for i in range(img.size[0]):
      if i % 2 == 0:
          black_2.append(i)

  black_1 = [i-1 for i in black_2 if i > 0]
  if img.size[0] % 2 == 0:
      black_1.append(img.size[0]-1)


  for i in black_1:
      for j in range(0, size, 2):
          m = random.choice(ls[1:])
          color_tuple = tuple(int(m[i:i+2], 16) for i in (0, 2, 4))
          pixels[i,j] = color_tuple

  for k in black_2:
      for l in range(1, size+1, 2):
          m = random.choice(ls[3:])
          color_tuple = tuple(int(m[i:i+2], 16) for i in (0, 2, 4))
          pixels[k,l] = color_tuple

  ax = plt.gca()
  plt.axis('off')
  props = dict(boxstyle='round', facecolor='white', alpha=1)
  label_h = hashlib.md5(open('n.png','rb').read()).hexdigest()
  ax.text(0.5, 0.5,label_h[1:11] , transform=ax.transAxes, fontsize=14,verticalalignment='center',horizontalalignment = 'center', bbox=props)
  plt.imshow(img)
  plt.savefig('n.png') #,bbox_inches='tight',transparent=False, pad_inches=0.1
  plt.show()
  ls = ['#'+i for i in ls]
  return ls

def tweet_img(ls):
  twitter_auth_keys = {
      "consumer_key"        : "your_consumer_key",
      "consumer_secret"     : "your_consumer_secret",
      "access_token"        : "your_access_token",
      "access_token_secret" : "your_access_token_secret"
  }
  auth = tweepy.OAuthHandler(twitter_auth_keys['consumer_key'],twitter_auth_keys['consumer_secret'])
  auth.set_access_token(twitter_auth_keys['access_token'],twitter_auth_keys['access_token_secret'])
  api = tweepy.API(auth)
  media = api.media_upload("n.png")
  tweet = 'Current Blockchain hash : {}\nImage : '.format(requests.get('https://blockchain.info/q/latesthash').text)
  post_result = api.update_status(status=tweet, media_ids=[media.media_id])


def main():
  lh = requests.get('https://blockchain.info/q/latesthash').text
  color_ls = generate_img(lh)
  tweet_img(color_ls)
  color_ls = generate_img(lh[::-1])
  tweet_img(color_ls)

if __name__=='__main__':
  main()
