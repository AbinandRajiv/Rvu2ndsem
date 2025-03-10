#!/bin/bash

display_memory_usage() {
echo "Current Memory Usage:"
free -h
echo ""
}
# Function to display memory usage in real-time
monitor_memory_usage() {
echo "Monitoring memory usage in real-time. Press [CTRL+C] to stop."
# Use top command to show memory usage updates every 2 seconds
top -d 2 -o %MEM
}

log_memory_usage() {
  echo "Logging memory usage every 10 seconds to $LOG_FILE"
  while true; do
    TIMESTAMP=$(date "+%Y-%m-%d %H:%M:%S")
    MEMORY_USAGE=$(free -h)
    echo "$TIMESTAMP - $MEMORY_USAGE" >> $LOG_FILE
    echo "Logged memory usage at $TIMESTAMP"
    sleep 10
  done
}

check_memory_alert() {
  AVAILABLE_MEMORY=$(free -m | grep Mem | awk '{print $7}')
  if [ "$AVAILABLE_MEMORY" -lt "$ALERT_THRESHOLD_MB" ]; then
    echo "ALERT: Available memory is below $ALERT_THRESHOLD_MB MB! Current available memory: ${AVAILABLE_MEMORY}MB"
  fi
}
# Displaying options to the user
echo "Dynamic Memory Monitor"
echo "1. Display current memory usage"
echo "2. Monitor memory usage in real-time"
echo "3. Exit"
# Loop until the user chooses to exit
while true; do
read -p "Select an option (1-3): " option
case $option in
1) # Display current memory usage
display_memory_usage
;;
2) # Monitor memory usage in real-time
monitor_memory_usage
;;
3) # Exit the script
echo "Exiting the memory monitor. Goodbye!"
exit 0
;;
*) # Invalid option
echo "Invalid option. Please select 1-3."
;;
esac
echo "" # Print a newline for better readability
done
