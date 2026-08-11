test = {
	'https://10.0.0.40:443/': {
		
		'path': {
			'../config/nginx/site-confs/test', 
			'../config/nginx/site-confs/docs-test'
		}, 
		'url': [
			{
				'dns': 'test-is27.duckdns.org'
			}
		], 
		'scope': [], 
		'subfolder': [
			'.well-known', 
			'.well-known/carddav', 
			'nextcloud/'
		]
	}, 
	'https://10.0.0.23:8084/': {
		'path': {
			'../config/nginx/site-confs/default.conf'
		}, 
		'url': [
			{
				'dns': 'is27.duckdns.org'
			}, 
			{
				'host': '10.0.0.23', 
				'port3': '8084'
			}
		], 
		'scope': [
			{
				'confPath': '/config/nginx/proxy-confs/*.subfolder.conf', 
				'type': 'folder'
			}
		], 
		'subfolder': [
			'\\.ht', 
			'standalone-signaling/', 
			'standalone-signaling/spreed'
		]
	}, 
	'http://nextcloud-talk-hpb:8084/': {
		'path': {
			'../config/nginx/site-confs/default.conf'
		}, 
		'url': [
			{
				'dns': 'is27.duckdns.org'
			}, 
			{
				'host': '10.0.0.23', 
				'port3': '8084'
			}
		], 
		'scope': [
			{
				'confPath': '/config/nginx/proxy-confs/*.subfolder.conf', 
				'type': 'folder'
			}
		], 
		'subfolder': [
			'\\.ht', 
			'standalone-signaling/', 
			'standalone-signaling/spreed'
		]
	}, 
	'https://127.0.0.1:9980/': {
		'path': {
			'../config/nginx/site-confs/docs-is27'
		}, 
		'url': [], 
		'scope': [], 
		'subfolder': [
			'browser', 
			'hosting/discovery', 
			'cool/adminws', 
			'hosting/capabilities'
		]
	}, 
	'https://10.0.0.40:27443/': {
		'path': {
			'../config/nginx/site-confs/test'
		}, 
		'url': [
			{
				'dns': 'test-is27.duckdns.org'
			}
		], 
		'scope': [], 
		'subfolder': [
			'.well-known', 
			'.well-known/carddav', 
			'nextcloud/'
		]
	}, 
	'https://minecraft1:25565/': {
		'path': {
			'../config/nginx/nginx.conf'
		}, 
		'url': [
			{
				'host': 'minecraft1', 
				'port3': '25565'
			}, 
			{
				'host': 'minecraft2', 
				'port3': '25565'
			}
		], 
		'scope': [], 
		'subfolder': []
	}, 
	'https://minecraft2:25565/': {
		'path': {
			'../config/nginx/nginx.conf'
		}, 
		'url': [
			{
				'host': 'minecraft1', 
				'port3': '25565'
			}, 
			{
				'host': 'minecraft2', 
				'port3': '25565'
			}
		], 
		'scope': [], 
		'subfolder': []
	}, 
	'http://$upstream_authelia:9091/': {
		'path': {
			'../config/nginx/authelia-server.conf'
		}, 
		'url': [], 
		'scope': [], 
		'subfolder': []
	}, 
	'http://$upstream_authentik:9000/': {
		'path': {
			'../config/nginx/authentik-server.conf'
		}, 
		'url': [], 
		'scope': [], 
		'subfolder': []
	}, 
	'http://zigbee2mqtt:8080/': {'path': set()}, 
	'http://freshrss:80/': {'path': set()}, 
	'http://ghost:2368/': {'path': set()}, 
	'http://speedtest-tracker:80/': {'path': set()}, 
	'http://komga:25600/': {'path': set()}, 
	'http://jfa-go:8056/': {'path': set()}, 
	'http://skyhook:8080/': {'path': set()}, 
	'http://gaps:8484/': {'path': set()}, 
	'http://privatebin:8080/': {'path': set()}, 
	'http://netdata:19999/': {'path': set()}, 
	'http://mattermost:8065/': {'path': set()}, 
	'http://shlink:8080/': {'path': set()}, 
	'http://lychee:80/': {'path': set()}, 
	'http://planka:1337/': {'path': set()}, 
	'http://crowdsec:8080/': {'path': set()}, 
	'http://semaphore:3000/': {'path': set()}, 
	'http://crowdsec-dashboard:3000/': {'path': set()}, 
	'http://babybuddy:8001/': {
		'path': {
			'../config/nginx/proxy-confs/babybuddy.subdomain.conf'
		}, 
		'url': [
			{
				'dns': 'babybuddy.*'
			}
		], 
		'scope': [], 
		'subfolder': []
	}, 
	'http://beszel:8090/': {'path': set()}, 
	'http://nocodb:8080/': {'path': set()}, 
	'http://10.255.255.20:8082/': {
		'path': {
			'../config/nginx/proxy-confs/qbittorrent.subfolder.conf.dl'
		}, 
		'url': [], 
		'scope': [], 
		'subfolder': [
			'qbittorrent', 
			'qbittorrent/', 
			'qbittorrent/api', 
			'qbittorrent/command', 
			'qbittorrent/query', 
			'qbittorrent/login', 
			'qbittorrent/sync', 
			'qbittorrent/scripts'
		]
	}, 
	'http://quassel-web:64080/': {'path': set()}, 
	'http://openhab:8080/': {'path': set()}, 
	'http://bookstack:80/': {'path': set()}, 
	'http://librespeed:80/': {'path': set()}, 
	'http://adminer:8080/': {'path': set()}, 
	'http://resilio-sync:8888/': {'path': set()}, 
	'http://taisun:3000/': {'path': set()}, 
	'http://cryptgeon:8000/': {'path': set()}, 
	'http://grafana:3000/': {'path': set()}, 
	'http://dozzle:8080/': {'path': set()}, 
	'http://readarr:8787/': {'path': set()}, 
	'http://thelounge:9000/': {'path': set()}, 
	'http://glances:61208/': {'path': set()}, 
	'http://mastodon:80/': {'path': set()}, 
	'https://10.255.255.30;\n      proxy_set_header Host $host/': {
		'path': {
			'../config/nginx/proxy-confs/wazuh.subdomain.conf'
		}, 
		'url': [
			{
				'dns': 'wazuh.*'
			}
		], 
		'scope': [], 
		'subfolder': []
	}, 
	'http://nzbhydra2:5076/': {'path': set()}, 
	'http://10.255.255.20:9696/': {
		'path': {
			'../config/nginx/proxy-confs/prowlarr.subfolder.conf.dl'
		}, 
		'url': [], 
		'scope': [], 
		'subfolder': [
			'prowlarr', 
			'prowlarr(/[0-9]+)?/api', 
			'prowlarr(/[0-9]+)?/download']
	}, 
	'http://prowlarr:9696/': {
		'path': {
			'../config/nginx/proxy-confs/prowlarr.subfolder.conf.dl'
		}, 
		'url': [], 
		'scope': [], 
		'subfolder': [
			'prowlarr', 
			'prowlarr(/[0-9]+)?/api', 
			'prowlarr(/[0-9]+)?/download']
	}, 
	'http://phpmyadmin:80/': {'path': set()}, 
	'https://kanzi:8000/': {'path': set()}, 
	'http://ombi:3579/': {
		'path': {
			'../config/nginx/proxy-confs/ombi.subfolder.conf'
		}, 
		'url': [], 
		'scope': [], 
		'subfolder': [
			'requests', 
			'requests/'
		]
	}, 
	'http://your-spotify-server:8080/': {'path': set()}, 
	'http://monitorr:80/': {'path': set()}, 
	'https://nextcloud:443/': {
		'path': {
			'../config/nginx/proxy-confs/nextcloud.subfolder.conf'
		}, 
		'url': [], 
		'scope': [], 
		'subfolder': [
			'.well-known', 
			'.well-known/carddav', 
			'.well-known/caldav', 
			'nextcloud/'
		]
	}, 
	'http://qbittorrent:8080/': {'path': set()}, 
	'http://monica:80/': {'path': set()}, 
	'http://miniflux:8080/': {'path': set()}, 
	'http://ntfy:80/': {'path': set()}, 
	'http://yourls:80/': {'path': set()}, 
	'http://jackett:9117/': {'path': set()}, 
	'http://10.255.255.20:8083/': {
		'path': {
			'../config/nginx/proxy-confs/calibre-web.subfolder.conf'
		}, 
		'url': [], 
		'scope': [], 
		'subfolder': [
			'calibre-web', 
			'calibre-web/'
		]
	}, 
	'http://dillinger:8080/': {'path': set()}, 
	'https://frigate:8971/': {'path': set()}, 
	'http://10.255.255.20:8990/': {
		'path': {
			'../config/nginx/proxy-confs/sonarrjoe.subfolder.conf.dl'
		}, 
		'url': [], 
		'scope': [], 
		'subfolder': [
			'sonarrjoe', 
			'sonarrjoe/api'
		]
	}, 
	'http://stirling-pdf:8080/': {'path': set()}, 
	'http://shinobi:8080/': {'path': set()}, 
	'https://192.168.1.11:9443/': {
		'path': {
			'../config/nginx/proxy-confs/portainer.subdomain.conf'
		}, 
		'url': [
			{
				'dns': 'portainer.*'
			}
		], 
		'scope': [], 
		'subfolder': [
			'api/websocket/'
		]
	}, 
	'https://pydio:443/': {'path': set()}, 
	'http://flood:3000/': {'path': set()}, 
	'http://boinc:8080/': {'path': set()}, 
	'http://atuin:8888/': {'path': set()}, 
	'http://tautulli:8181/': {
		'path': {
			'../config/nginx/proxy-confs/tautulli.subfolder.conf'
		}, 
		'url': [], 
		'scope': [], 
		'subfolder': [
			'tautulli', 
			'tautulli/api', 
			'tautulli/newsletter', 
			'tautulli/image'
		]
	}, 
	'http://pinry:80/': {'path': set()}, 
	'http://rclone:5800/': {'path': set()}, 
	'http://graylog:9000/': {'path': set()}, 
	'http://storm:8221/': {'path': set()}, 
	'http://hass-configurator:3218/': {'path': set()}, 
	'http://get_iplayer:1935/': {'path': set()}, 
	'http://immich:2283/': {'path': set()}, 
	'http://10.0.0.23:3001/': {
		'path': {
			'../config/nginx/proxy-confs/firefox.subdomain.conf'
		}, 
		'url': [
			{
				'dns': 'jqplay.*'
			}
		], 
		'scope': [], 
		'subfolder': []
	}, 
	'http://watchstate:8080/': {'path': set()}, 
	'http://podgrab:8080/': {'path': set()}, 
	'http://10.255.255.20:7879/': {
		'path': {
			'../config/nginx/proxy-confs/radarrjoe.subfolder.conf.dl'
		}, 
		'url': [], 
		'scope': [], 
		'subfolder': [
			'radarrjoe', 
			'radarrjoe/api'
		]
	}, 
	'http://10.255.255.20:8787/': {
		'path': {
			'../config/nginx/proxy-confs/readarrb.subfolder.conf.dl'
		}, 
		'url': [], 
		'scope': [], 
		'subfolder': [
			'readarrb', 
			'readarrb/api'
		]
	}, 
	'http://ubooquity:2202/': {'path': set()}, 
	'http://ubooquity:2203/': {'path': set()}, 
	'http://paperless:8000/': {'path': set()}, 
	'http://lidarr:8686/': {'path': set()}, 
	'http://sickchill:8081/': {'path': set()}, 
	'http://hoarder:3000/': {'path': set()}, 
	'http://headphones:8181/': {'path': set()}, 
	'http://statup:8080/': {'path': set()}, 
	'https://unifi-network-application:8443/': {'path': set()}, 
	'http://10.255.255.20:6767/': {
		'path': {
			'../config/nginx/proxy-confs/bazarr.subfolder.conf.dl'
		}, 
		'url': [], 
		'scope': [], 
		'subfolder': [
			'bazarr', 
			'bazarr/', 
			'bazarr/api'
		]
	}, 
	'http://calibre:8080/': {'path': set()}, 
	'http://calibre:8081/': {'path': set()}, 
	'http://couchpotato:5050/': {'path': set()}, 
	'http://smokeping:80/': {'path': set()}, 
	'https://10.0.0.26:443/': {
		'path': {
			'../config/nginx/proxy-confs/swag.subdomain.conf'
		}, 
		'url': [
			{
				'dns': 'test.is27.duckdns.org'
			}
		], 
		'scope': [], 
		'subfolder': []
	}, 
	'http://calibre-web:8083/': {'path': set()}, 
	'http://maintainerr:6246/': {'path': set()}, 
	'http://metube:8081/': {'path': set()}, 
	'http://linkwarden:3000/': {'path': set()}, 
	'http://mylar:8090/': {'path': set()}, 
	'http://prometheus:9090/': {'path': set()}, 
	'http://chronograf:8888/': {'path': set()}, 
	'http://gatus:8080/': {'path': set()}, 
	'http://ddns-updater:8000/': {'path': set()}, 
	'http://healthchecks:8000/': {'path': set()}, 
	'http://scrutiny:8080/': {'path': set()}, 
	'http://gotify:80/': {'path': set()}, 
	'http://forgejo:3000/': {'path': set()}, 
	'http://drone:80/': {'path': set()}, 
	'http://airsonic:4040/': {'path': set()}, 
	'http://radarr:7878/': {'path': set()}, 
	'http://portainer:9000/': {'path': set()}, 
	'http://leantime:80/': {'path': set()}, 
	'http://wrapperr:8282/': {'path': set()}, 
	'http://10.0.0.23:8083/': {
		'path': {
			'../config/nginx/proxy-confs/openproject.subdomain.conf'
		}, 
		'url': [
			{
				'dns': 'openproject.is27.duckdns.org'
			}, 
			{
				'dns': 'openproject.is27.duckdns.org'
			}
		], 
		'scope': [], 
		'subfolder': []
	}, 
	'http://plex:33400/': {'path': set()}, 
	'http://duplicacy:3875/': {'path': set()}, 
	'https://heimdall:443/': {'path': set()}, 
	'http://gitea:3000/': {'path': set()}, 
	'https://warpgate:8888/': {'path': set()}, 
	'http://raneto:3000/': {'path': set()}, 
	'http://vaultwarden:80/': {'path': set()}, 
	'http://slskd:5000/': {'path': set()}, 
	'http://wordpress:80/': {'path': set()}, 
	'http://synapse:8008/': {'path': set()}, 
	'https://pydio-cells:8080/': {'path': set()}, 
	'http://jellyseerr:5055/': {'path': set()}, 
	'http://kavita:5000/': {'path': set()}, 
	'http://10.255.255.20:8084/': {
		'path': {
			'../config/nginx/proxy-confs/podgrab.subdomain.conf'
		}, 
		'url': [
			{
				'dns': 'podgrab.*'
			}
		], 
		'scope': [], 
		'subfolder': []
	}, 
	'http://syncthing:8384/': {'path': set()}, 
	'http://front:80/': {'path': set()}, 
	'http://booksonic:4040/': {'path': set()}, 
	'http://wallabag:80/': {'path': set()}, 
	'http://filebot:5800/': {'path': set()}, 
	'http://hedgedoc:3000/': {'path': set()}, 
	'http://huginn:3000/': {'path': set()}, 
	'http://flaresolverr:8191/': {'path': set()}, 
	'http://matomo:80/': {'path': set()}, 
	'http://dokuwiki:80/': {'path': set()}, 
	'http://guacamole:8080/': {'path': set()}, 
	'http://domoticz:8080/': {'path': set()}, 
	'http://mstream:3000/': {'path': set()}, 
	'http://homepage:3000/': {'path': set()}, 
	'http://sonarrtorss:18989/': {'path': set()}, 
	'http://organizr:80/': {'path': set()}, 
	'http://bazarr:6767/': {'path': set()}, 
	'http://theme-park:80/': {'path': set()}, 
	'http://yacht:8000/': {'path': set()}, 
	'http://aria2-with-webui:80/': {'path': set()}, 
	'http://aria2-with-webui:6800/': {'path': set()}, 
	'http://sabnzbd:8080/': {'path': set()}, 
	'http://webtop:3000/': {'path': set()}, 
	'http://codimd:3000/': {'path': set()}, 
	'http://deluge:8112/': {'path': set()}, 
	'http://sonarr:8989/': {'path': set()}, 
	'http://oogway:8080/': {'path': set()}, 
	'http://lazylibrarian:5299/': {'path': set()}, 
	'http://znc:6501/': {'path': set()}, 
	'http://petio:7777/': {'path': set()}, 
	'http://10.255.255.20:8789/': {
		'path': {
			'../config/nginx/proxy-confs/readarrajoe.subfolder.conf.dl'
		}, 
		'url': [], 
		'scope': [], 
		'subfolder': [
			'readarrajoe', 
			'readarrajoe/api'
		]
	}, 
	'http://babybuddy:8000/': {'path': set()}, 
	'http://10.255.255.20:7878/': {
		'path': {
			'../config/nginx/proxy-confs/radarr.subfolder.conf.dl'
		}, 
		'url': [], 
		'scope': [], 
		'subfolder': [
			'radarr', 
			'radarr/api'
		]
	}, 
	'http://dockge:5001/': {'path': set()}, 
	'https://budge:443/': {'path': set()}, 
	'http://cloudbeaver:8978/': {'path': set()}, 
	'http://whisparr:6969/': {'path': set()}, 
	'https://10.0.0.23:9980/': {
		'path': {
			'../config/nginx/proxy-confs/collabora.subdomain.conf'
		}, 
		'url': [
			{
				'dns': 'docs.*'
			}
		], 
		'scope': [], 
		'subfolder': []
	}, 
	'http://emby:8096/': {'path': set()}, 
	'http://filebrowser:8080/': {'path': set()}, 
	'http://code-server:8443/': {
		'path': {
			'../config/nginx/proxy-confs/code-server.subdomain.conf'
		}, 
		'url': [], 
		'scope': [], 
		'subfolder': []
	}, 
	'http://archisteamfarm:1242/': {'path': set()}, 
	'http://rutorrent:80/': {'path': set()}, 
	'http://flexget:5050/': {'path': set()}, 
	'http://homebox:7745/': {'path': set()}, 
	'http://192.168.1.11:8096/': {
		'path': {
			'../config/nginx/proxy-confs/jellyfin.subdomain.conf'
		}, 
		'url': [
			{
				'dns': 'jellyfin.*'
			}
		], 
		'scope': [], 
		'subfolder': []
	}, 
	'http://recipes:8080/': {'path': set()}, 
	'http://pixelfed:80/': {'path': set()}, 
	'http://beets:8337/': {'path': set()}, 
	'http://synclounge:8088/': {'path': set()}, 
	'http://medusa:8081/': {'path': set()}, 
	'http://castopod-app:8000/': {'path': set()}, 
	'http://plex:32400/': {'path': set()}, 
	'http://pyload:8000/': {'path': set()}, 
	'http://audiobookshelf:80/': {'path': set()}, 
	'https://collabora:9980/': {'path': set()}, 
	'http://transmission:9091/': {'path': set()}, 
	'http://pterodactylnode:443/': {'path': set()}, 
	'http://jellyfin:8096/': {'path': set()}, 
	'http://phoneinfoga:5000/': {'path': set()}, 
	'http://pihole:80/': {'path': set()}, 
	'http://metabase:3000/': {'path': set()}, 
	'http://duplicati:8200/': {'path': set()}, 
	'http://sickrage:8081/': {'path': set()}, 
	'http://pgadmin:80/': {'path': set()}, 
	'http://your-spotify-web:3000/': {'path': set()}, 
	'http://open-webui:8080/': {'path': set()}, 
	'http://nzbget:6789/': {'path': set()}, 
	'http://grocy:80/': {
		'path': {
			'../config/nginx/proxy-confs/grocy.subdomain.conf'
		}, 
		'url': [
			{
				'dns': 'grocy.*'
			}
		], 
		'scope': [], 
		'subfolder': []
	}, 
	'http://uptime-kuma:3001/': {'path': set()}, 
	'http://kimai:80/': {'path': set()}, 
	'http://10.255.255.20:8989/': {
		'path': {
			'../config/nginx/proxy-confs/sonarr.subfolder.conf.dl'
		}, 
		'url': [], 
		'scope': [], 
		'subfolder': [
			'sonarr', 
			'sonarr/api'
		]
	}, 
	'http://mealie:9000/': {'path': set()}, 
	'http://homeassistant:8123/': {'path': set()}, 
	'http://10.255.255.20:8090/': {
		'path': {
			'../config/nginx/proxy-confs/mylar.subfolder.conf.dl'
		}, 
		'url': [], 
		'scope': [], 
		'subfolder': [
			'mylar'
		]
	}, 
	'http://changedetection:5000/': {'path': set()}, 
	'http://n8n:5678/': {'path': set()}, 
	'http://onetimesecret:3000/': {'path': set()}, 
	'http://adguard:80/': {'path': set()}, 
	'http://scope:4040/': {'path': set()}, 
	'http://authentik-server:9000/': {'path': set()}, 
	'http://requestrr:4545/': {'path': set()}, 
	'http://watcharr:3080/': {'path': set()}, 
	'http://romm:8080/': {'path': set()}, 
	'http://10.255.255.20:8081/': {
		'path': {
			'../config/nginx/proxy-confs/calibre.subfolder.conf'
		}, 
		'url': [], 
		'scope': [], 
		'subfolder': [
			'Reader', 
			'Reader/', 
			'content-server', 
			'content-server/'
		]
	}, 
	'http://10.255.255.20:6901/': {
		'path': {
			'../config/nginx/proxy-confs/calibre.subfolder.conf'
		}, 
		'url': [], 
		'scope': [], 
		'subfolder': [
			'Reader', 
			'Reader/', 
			'content-server', 
			'content-server/'
		]
	}, 
	'https://kasm:8443/': {'path': set()}, 
	'https://kasm:3000/': {'path': set()}, 
	'http://fenrus:3000/': {'path': set()}, 
	'http://boinc:6901/': {'path': set()}, 
	'http://192.168.1.11:8265/': {
		'path': {
			'../config/nginx/proxy-confs/tdarr.subdomain.conf.dl'
		}, 
		'url': [
			{
				'dns': 'tdarr.*'
			}
		], 
		'scope': [], 
		'subfolder': []
	}, 
	'http://esphome:6052/': {'path': set()}, 
	'http://notifiarr:5454/': {'path': set()}, 
	'http://langtool:8081/': {
		'path': {
			'../config/nginx/proxy-confs/languagetool.subdomain.conf'
		}, 
		'url': [
			{
				'dns': 'languagetool.*'
			}
		], 
		'scope': [], 
		'subfolder': [
			'v2'
		]
	}, 
	'http://emulatorjs:80/': {
		'path': {
			'../config/nginx/proxy-confs/emulatorjs.subdomain.conf'
		}, 
		'url': [
			{
				'dns': 'emulatorjs.*'
			}
		], 
		'scope': [], 
		'subfolder': [
			'backend', 
			'backend/'
		]
	}, 
	'http://emulatorjs:3000/': {
		'path': {
			'../config/nginx/proxy-confs/emulatorjs.subdomain.conf'
		}, 
		'url': [
			{
				'dns': 'emulatorjs.*'
			}
		], 
		'scope': [], 
		'subfolder': [
			'backend', 
			'backend/'
		]
	}, 
	'http://pwndrop:8080/': {'path': set()}, 
	'http://netboot:3000/': {'path': set()}, 
	'http://calibre:6901/': {'path': set()}, 
	'http://jdownloader:5800/': {'path': set()}, 
	'http://youtube-dl-server:8080/': {'path': set()}, 
	'https://linkstack:443/': {'path': set()}, 
	'http://yt-dlp-web:3000/': {'path': set()}, 
	'http://10.255.255.20:6789/': {
		'path': {
			'../config/nginx/proxy-confs/nzbget.subfolder.conf.dl'
		}, 
		'url': [], 
		'scope': [], 
		'subfolder': [
			'nzbget', 
			'nzbget(/[^\\/:]*:[^\\/]*)?/jsonrpc', 'nzbget(/[^\\/:]*:[^\\/]*)?/jsonprpc', 'nzbget(/[^\\/:]*:[^\\/]*)?/xmlrpc']
	}, 
	'http://piwigo:80/': {'path': set()}, 
	'http://zwavejs2mqtt:8091/': {'path': set()}, 
	'http://10.255.255.20:7880/': {
		'path': {
			'../config/nginx/proxy-confs/radarrjoelocal.subfolder.conf.dl'
		}, 
		'url': [], 
		'scope': [], 
		'subfolder': [
			'radarrjoelocal', 
			'radarrjoelocal/api'
		]
	}, 
	'http://chevereto:80/': {'path': set()}, 
	'http://netbox:8000/': {'path': set()}, 
	'http://homer:8080/': {'path': set()}, 
	'http://crontabui:8000/': {'path': set()}, 
	'http://foundryvtt:30000/': {'path': set()}, 
	'http://embystat:6555/': {'path': set()}, 
	'http://cadvisor:8080/': {'path': set()}, 
	'http://partdb:80/': {'path': set()}, 
	'grpc://dnsdist:443/': {'path': set()}, 
	'http://nexusoss:8081/': {'path': set()}, 
	'http://nexusoss:8082/': {'path': set()}, 
	'http://homarr:7575/': {'path': set()}, 
	'http://lubelogger:8080/': {'path': set()}, 
	'http://pterodactyl:80/': {'path': set()}, 
	'http://10.255.255.20:8688/': {
		'path': {
			'../config/nginx/proxy-confs/lidarrjoelocal.subfolder.conf.dl'
		}, 
		'url': [], 
		'scope': [], 
		'subfolder': [
			'lidarrjoelocal', 
			'lidarrjoelocal/api'
		]
	}, 
	'https://unifi-controller:8443/': {'path': set()}, 
	'http://10.255.255.20:8790/': {
		'path': {
			'../config/nginx/proxy-confs/readarrbjoe.subfolder.conf.dl'
		}, 
		'url': [], 
		'scope': [], 
		'subfolder': [
			'readarrbjoe', 
			'readarrbjoe/api'
		]
	}, 
	'http://wikijs:3000/': {'path': set()}, 
	'http://rallly:3000/': {'path': set()}, 
	'http://grampsweb:5000/': {'path': set()}, 
	'https://monica:443/': {'path': set()}, 
	'http://linkace:80/': {'path': set()}, 
	'http://10.255.255.20:8686/': {
		'path': {
			'../config/nginx/proxy-confs/lidarr.subfolder.conf.dl'
		}, 
		'url': [], 
		'scope': [], 
		'subfolder': [
			'lidarr', 
			'lidarr/api'
		]
	}, 
	'http://foldingathome:7396/': {'path': set()}, 
	'http://openvscode-server:3000/': {'path': set()}, 
	'http://viewtube:8066/': {'path': set()}, 
	'http://jenkins:8080/': {'path': set()}, 
	'http://overseerr:5055/': {'path': set()}, 
	'http://libreddit:8080/': {'path': set()}, 
	'http://10.255.255.20:8687/': {
		'path': {
			'../config/nginx/proxy-confs/lidarrjoe.subfolder.conf.dl'
		}, 
		'url': [], 
		'scope': [], 
		'subfolder': [
			'lidarrjoe', 
			'lidarrjoe/api'
		]
	}, 
	'http://10.255.255.20:5299/': {
		'path': {
			'../config/nginx/proxy-confs/lazylibrarian.subfolder.conf'
		}, 
		'url': [], 
		'scope': [], 
		'subfolder': [
			'BookRequests'
		]
	}, 
	'http://it-tools:80/': {'path': set()}, 
	'http://apprise-api:8000/': {'path': set()}, 
	'http://wordpress:27080/': {
		'path': {
			'../config/nginx/proxy-confs/wordpress.subdomain.conf'
		}, 
		'url': [
			{
				'dns': 'portal.*'
			}
		], 
		'scope': [], 
		'subfolder': []
	}, 
	'http://immich_server:2283/': {'path': set()}, 
	'http://adminmongo:1234/': {'path': set()}, 
	'http://wizarr:5690/': {'path': set()}, 
	'https://openvpn-as:943/': {'path': set()}, 
	'http://photoprism:2342/': {'path': set()}, 
	'http://10.255.255.20:8991/': {
		'path': {
			'../config/nginx/proxy-confs/sonarrjoelocal.subfolder.conf.dl'
		}, 
		'url': [], 
		'scope': [], 
		'subfolder': [
			'sonarrjoelocal', 
			'sonarrjoelocal/api'
		]
	}, 
	'http://firefly:8080/': {'path': set()}, 
	'http://authelia:9091/': {
		'path': {
			'../config/nginx/proxy-confs/authelia.subdomain.conf.dl'
		}, 
		'url': [
			{
				'dns': 'auth.dl.is27.duckdns.org'
			}
		], 
		'scope': [], 
		'subfolder': []
	}, 
	'http://navidrome:4533/': {'path': set()}, 
	'http://grav:80/': {'path': set()}, 
	'http://firefox:3000/': {'path': set()}, 
	'http://tdarr:8265/': {'path': set()}, 
	'http://documentserver:80/': {'path': set()}, 
	'http://influxdb:8086/': {'path': set()}, 
	'http://commento:8080/': {'path': set()}, 
	'http://dashy:8080/': {'path': set()}, 
	'http://picard:5800/': {'path': set()}, 
	'http://papermerge:8000/': {'path': set()}, 
	'http://192.168.1.11:32400/': {
		'path': {
			'../config/nginx/proxy-confs/plex.subdomain.conf'
		}, 
		'url': [
			{
				'dns': 'plex.*'
			}
		], 
		'scope': [], 
		'subfolder': []
	}, 
	'http://octoprint:80/': {'path': set()}, 
	'http://mytinytodo:80/': {'path': set()}, 
	'http://actual-server:5006/': {'path': set()}, 
	'http://10.0.0.23:8082/': {
		'path': {
			'../config/nginx/proxy-confs/budge.subdomain.conf'
		}, 
		'url': [
			{
				'dns': 'budge.*'
			}
		], 
		'scope': [], 
		'subfolder': []
	}, 
	'http://bitwarden:8080/': {'path': set()}, 
	'http://joplin:22300/': {'path': set()}, 
	'https://192.168.1.11:8006/': {'path': set()}, 
	'http://zwave-js-ui:8091/': {'path': set()}, 
	'http://lldap:17170/': {'path': set()}, 
	'http://osticket:80/': {'path': set()}, 
	'http://tasmobackup:80/': {'path': set()}, 
	'http://homebridge:8581/': {'path': set()}, 
	'http://bar_assistant-webserver-1:3000/': {'path': set()}, 
	'http://10.255.255.20:6768/': {
		'path': {
			'../config/nginx/proxy-confs/bazarrjoe.subfolder.conf.dl'
		}, 
		'url': [], 
		'scope': [], 
		'subfolder': [
			'bazarrjoe', 
			'bazarrjoe/', 
			'bazarrjoe/api'
		]
	}, 
	'http://10.255.255.20:8788/': {
		'path': {
			'../config/nginx/proxy-confs/readarra.subfolder.conf.dl'
		}, 
		'url': [], 
		'scope': [], 
		'subfolder': [
			'readarra', 
			'readarra/api'
		]
	}, 
	'http://tvheadend:9981/': {'path': set()}, 
	'http://dsmr:80/': {'path': set()}}