# ONT_file_sync
performs rsync on minion raw data directory for the continous file transfer.

## Setup 
When dealing with such continuous file transfer its better to have the public key from your local machine to be saved on the destination system (remote system). You can set up the password free rsync using the following steps.
Generating ssh key
```
ssh-keygen -t rsa -b 4096
```
Continue with passphrase (you can leave blank or add passphrase), you can view ssh public key from id_rsa.pub file
```
less ~/.ssh/id_rsa.pub
```
Save the public key to a file named authorized_keys. Also don't forget to add your local system user_name and host address. Example user123@server_name.organization_name.ac.uk
```
cat ~/.ssh/id_rsa.pub | ssh username@hostname 'cat >> ~/.ssh/authorized_keys'
```
Use SCP to transfer the autherized_keys to your remote host
```
scp ~/.ssh/authorized_keys user_name@server_name.organization.ac.uk:~/.ssh
```
You can use the python script to transfer the files once the above step is complete
```
python file_sync.py -d <source_path> -d <destination_path> -dh <destination_host> -du <destination_user> -t <time>
```
Example command
```
python file_sync.py -d /path/to/your/directory/ -d /your/destination/directory -dh server1.organization.ac.uk -du abc123 -t 30
```
In the above command -t 30 indicates the time in minutes. 

#command for live basecalling (script undergoing development)
```
python live_basecalling.py -g /export/home4/sk312p/projects/tools/dorado-0.5.0-linux-x64/bin/dorado -b DORADO -i /export/home4/sk312p/projects/tm/ -o /export/home4/sk312p/projects/test.fastq -d hac -t 1 -x cpu
```
