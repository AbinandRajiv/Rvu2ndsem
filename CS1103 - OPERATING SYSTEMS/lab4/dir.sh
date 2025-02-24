echo " Enter a directory name "
read dirname
if [-d "$dirname" ]; then
 echo "Directory exits"
else
 echo "Directory does not exist" 
fi
