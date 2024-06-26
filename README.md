> [!CAUTION]
> As-of 2021, this product does not have a free support team anymore. If you want this product to be maintained, please support my work.
 
> [!NOTE]
> (This product is available under a free and permissive license, but needs financial support to sustain its continued improvements. In addition to maintenance and stability there are many  desirable features yet to be added.)

![logo](logo.png)

Google MusicManager Deduplication API - Docker Image
====================================================

[![Docker Pulls](https://img.shields.io/docker/pulls/jaymoulin/google-musicmanager-dedup-api.svg)](https://hub.docker.com/r/jaymoulin/google-musicmanager-dedup-api/)
[![Docker stars](https://img.shields.io/docker/stars/jaymoulin/google-musicmanager-dedup-api.svg)](https://hub.docker.com/r/jaymoulin/google-musicmanager-dedup-api/)
[![PayPal donation](https://github.com/jaymoulin/jaymoulin.github.io/raw/master/ppl.png "PayPal donation")](https://www.paypal.me/jaymoulin)
[![Buy me a coffee](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png "Buy me a coffee")](https://www.buymeacoffee.com/jaymoulin)
[![Buy me a coffee](https://ko-fi.com/img/githubbutton_sm.svg "Buy me a coffee")](https://www.ko-fi.com/jaymoulin)

This image allows you utilize deduplication feature for [Youtube Music Uploader](https://github.com/jaymoulin/youtube-music-uploader)

Installation
---
Please note that this package is also hosted on Github Container Registry, just add `ghcr.io/` before the image name (`docker pull ghcr.io/jaymoulin/google-musicmanager-dedup-api` instead of `jaymoulin/google-musicmanager-dedup-api`)

```
docker run -d --restart=always -p 80:80 -v /path/to/your/db:/app/db --name googlemusic-dedup jaymoulin/google-musicmanager-dedup-api
```

You can mount a volume to `/app/db/` to keep the database outside the container

