<p align="center">
  <img width="300" src="https://github.com/sentriz/betanin/blob/master/betanin/client/src/assets/logo.png?raw=true">
</p>
<h4 align="center">beets based man-in-the-middle of your torrent client and music player</h4>

<hr>

### installation

    pip install --user requirements.txt
    pip install git+https://github.com/edavis/transmission-fluid
    
<hr>

### docker
###### image
`docker pull sentriz/betanin`  
###### volumes
`/root/.local/share/betanin/` for a persistent database  
`/root/.config/beets/` for a persistent beets home (point this to your current beets home if you have one)  
`/music/` so beets can access your music  
`/downloads/` so beets can access your downloads  
###### port
5000
###### compose (example with [traefik](https://traefik.io/))
```yml
betanin:
  container_name: betanin
  image: sentriz/betanin
  labels:
    traefik.docker.network: <your external network>
    traefik.frontend.auth.basic: ${HTPASSWD}
    traefik.frontend.rule: Host:betanin.${DOMAIN}
  networks:
  - proxy
  restart: unless-stopped
  volumes:
  - ${DATA}/betanin/data:/root/.local/share/betanin/
  - ${DATA}/betanin/beets:/root/.config/beets/
  - ${MEDIA}/music:/music/
  - ${MEDIA}/downloads:/downloads/
```

<hr>

### transmission
###### settings.json (example excerpt)
```json
"script-torrent-done-enabled": true,
"script-torrent-done-filename": "/scripts/done",
```
###### done script
```bash
#!/bin/sh

curl \
    --request POST \
    -d "id=$TR_TORRENT_HASH" \
    -d "path=/downloads/complete/beets" \
    -d "name=$TR_TORRENT_NAME" \
    --user 'user:password' \
    'http://betanin:5000/api/torrents'
```
###### docker compose (excerpt)
```yaml
volumes:
- ${DATA}/transmission/config:/config
- ${DATA}/transmission/scripts:/scripts
- ${MEDIA}/download:/downloads
```
