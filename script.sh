sudo mount.cifs //192.168.1.254/posserver /mnt/posserver -o user=linux,vers=2.1
rsync -acvzh /mnt/posserver/sales /home/server/posserver --log-file=/tmp/rsync-status.txt  
rsync -acvzh /mnt/posserver/ics /home/server/posserver --log-file=/tmp/rsync-status.txt  
