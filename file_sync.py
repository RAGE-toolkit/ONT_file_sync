import subprocess
import time
from argparse import ArgumentParser

def rsync_transfer(source_path, dest_pth, dest_host_address, dest_user):

	command = [
		'rsync',
		'-vurht',
		'--progress',
		f'{source_path}',
		f'{destination_user}@{destination_host}:{destination_path}'
	]
	try:
		subprocess.run(command, check=True)
		print('File transfer successful!')
	except subprocess.CalledProcessError as e:
		print(f'Error during file transfer: {e}')

def job(args):
	while True:
		print('Running rsync_transfer...')
		rsync_transfer(args.source_path, args.destination_path, args.destination_host, args.destionat_user)
		time.sleep(args.time * 60) 

if __name__=="__main__":
	parser = ArgumentParser(description='cluster the integration sites')
	parser.add_argument('-s', '--source_path', help='source directory', required=True)
	parser.add_argument('-d', '--destination_path', help='destination path', required=True)
	parser.add_argument('-dh', '--destination_host', help='destination host address', required=True)
	parser.add_argument('-du', '--destination_user', help='destination user name', required=True)
	parser.add_argument('-t', '--time', help='time interval, performs sync for give time (in minutes)', default=30, type=int)
	args = parser.parse_args()
	job(args)
