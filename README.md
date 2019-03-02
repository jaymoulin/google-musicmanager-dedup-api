![logo](logo.png)

Google MusicManager Deduplication API - Docker Image
====================================================

[![Docker Pulls](https://img.shields.io/docker/pulls/jaymoulin/google-musicmanager-dedup-api.svg)](https://hub.docker.com/r/jaymoulin/google-musicmanager-dedup-api/)
[![Docker stars](https://img.shields.io/docker/stars/jaymoulin/google-musicmanager-dedup-api.svg)](https://hub.docker.com/r/jaymoulin/google-musicmanager-dedup-api/)
[![Bitcoin donation](https://github.com/jaymoulin/jaymoulin.github.io/raw/master/btc.png "Bitcoin donation")](https://m.freewallet.org/id/374ad82e/btc)
[![Litecoin donation](https://github.com/jaymoulin/jaymoulin.github.io/raw/master/ltc.png "Litecoin donation")](https://m.freewallet.org/id/374ad82e/ltc)
[![PayPal donation](https://github.com/jaymoulin/jaymoulin.github.io/raw/master/ppl.png "PayPal donation")](https://www.paypal.me/jaymoulin)
[![Buy me a coffee](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png "Buy me a coffee")](https://www.buymeacoffee.com/3Yu8ajd7W)

This image allows you utilize deduplication feature for [Google MusicManager](https://github.com/jaymoulin/google-music-manager)

Installation
---

```
docker run -d --restart=always -v /path/to/your/db:/app/db --name googlemusic-dedup jaymoulin/google-musicmanager-dedup-api
```

You can mount a volume to `/app/db/` to keep the database outside the container

Appendixes
---

### Install Docker

If you don't have Docker installed yet, you can do it easily in one line using this command
 
```
curl -sSL "https://gist.githubusercontent.com/jaymoulin/e749a189511cd965f45919f2f99e45f3/raw/0e650b38fde684c4ac534b254099d6d5543375f1/ARM%2520(Raspberry%2520PI)%2520Docker%2520Install" | sudo sh && sudo usermod -aG docker $USER
```
