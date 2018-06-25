import time
from qbittorrent import Client

if __name__ == '__main__':
	qb = Client('http://127.0.0.1:8080/')

	torrents = qb.torrents()
	count = 0

	for t in torrents:
		t_trackers = qb.get_torrent_trackers(t['hash'])

		for tt in t_trackers:
			if tt['status'] == 'Not working':
				if 'This torrent does not exist' in tt['msg']:
					print('AnimeBytes - ' + t['name'])
					count += 1
					break
				elif 'Unregistered torrent' in tt['msg']:
					print('Other      - ' + t['name'])
					count += 1
					break

		time.sleep(.001) # The script freezes if qBittorrent is queried too quickly

	if count > 0:
		print()

	print(str(count) + ' obsolete torrents found!')
