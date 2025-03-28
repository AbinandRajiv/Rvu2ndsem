sudo mkdir /tmp/Backups
cp *.c /tmp/Backups
cp *.py /tmp/Backups
cd /tmp
tar -czvf Backup-2025-03-28.tar.gz
udisksctl mount -b /dev/sda1
mv /tmp/Backup-2025-03-28.tar.gz /media/RVU/Pendrive/
udisksctl unmount -b /dev/sda1
rm -r /tmp/Backups
