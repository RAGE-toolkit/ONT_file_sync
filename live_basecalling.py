import subprocess
import time
from argparse import ArgumentParser

def rsync_transfer(basecaller_path, basecaller, input_dir, output_dir, data_model, gpu):
	if basecaller == "GUPPY":
		if gpu:
			command = [
				f'{basecaller_path}',
				'--recursive',
				'-c',
				f'{data_model}',
				'-i',
				f'{input_dir}',
				'-s',
				f'{output_dir}',
				f'{gpu}'
			]
		else:
			command = [
				f'{basecaller_path}',
				'--recursive',
				'-c',
				f'{data_model}',
				'-i',
				f'{input_dir}',
				'-s',
				f'{output_dir}'
		 ]
	else:
		command = [
			f'{basecaller_path}',
			'basecaller',
			f'{data_model}',
			f'{input_dir}',
			'--emit-fastq',
			'--barcode-both-ends',
			'-r',
			'--kit-name EXP-NBD196', 
			'-x',
			f'{gpu}',
			'>',
			f'{output_dir}'
		]
		cmd = [
			f'{basecaller_path}',
			'basecaller',
			f'{data_model}',
			f'{input_dir}',
			'--emit-fastq',
			'--barcode-both-ends',
			'-r',
			'--kit-name SQK-LSK109',
			'-x',
			f'{gpu}',
			'>',
			f'{output_dir}'
		]

	try:
		if basecaller == "GUPPY":
			subprocess.run(command, check=True)
		else:
			subprocess.run(' '.join(command), check=True, shell=True)
			subprocess.run(' '.join(cmd), check=True, shell=True)
		print('Basecaller sucessfull!')
	except subprocess.CalledProcessError as e:
		print(f'Error during file transfer: {e}')

def job(args):
	while True:
		print('Running live basecalling...')
		rsync_transfer(args.basecaller_path, args.basecaller, args.input_dir, args.output_dir, args.guppy_config, args.cuda_cores)
		time.sleep(args.time_in_sec * 60)

if __name__=="__main__":
	parser = ArgumentParser(description='cluster the integration sites')
	parser.add_argument('-g', '--basecaller_path', help='guppy basecaller directory', required=True)
	parser.add_argument('-b', '--basecaller', help='basecalling tool name GUPPY or Dorado', required=True)
	parser.add_argument('-i', '--input_dir', help='fast5 input directory', required=True)
	parser.add_argument('-o', '--output_dir', help='output directory to store basecaller data', required=True)
	parser.add_argument('-d', '--guppy_config', help='guppy config to be used', required=True)
	parser.add_argument('-x', '--cuda_cores', help='cuda device to use', required=False)
	parser.add_argument('-t', '--time_in_sec', help='time interval (in minutes)', default=30, type=int, required=True)
	args = parser.parse_args()
	job(args)
