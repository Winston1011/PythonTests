import random
import urllib.request

def download_web_image(url):
    name = random.randrange(1, 1000)
    full_name = str(name) + ".jpg"
    urllib.request.urlretrieve(url, full_name)

download_web_image("https://scontent-nrt1-1.xx.fbcdn.net/v/t1.0-9/13000365_1177727875595005_1763057181045279384_n.jpg?_nc_cat=110&_nc_oc=AQmsOLSo9wz4v8SCSqbRogCDGSASYO-o_kkWeRYuudeI3cIzqSV-Iayj1XJxAcXULE0&_nc_ht=scontent-nrt1-1.xx&oh=07531dfba0c8ab32dd70dd72a5d7817f&oe=5DE182A1")
