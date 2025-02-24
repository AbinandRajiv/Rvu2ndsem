echo " Enter  filename: "
read filename
if [ -f "$filename" ]; then
  echo " file exists"
else
  echo " File does not exist "
fi
