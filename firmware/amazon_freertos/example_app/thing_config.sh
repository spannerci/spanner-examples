cd $AMAZON_FREERTOS_ROOT/tools/aws_config_quick_start

# Reference in https://github.com/aws/amazon-freertos/tree/master/tools/aws_config_quick_start

export afr_source_dir=$AMAZON_FREERTOS_ROOT
export thing_name=my_thing
export wifi_ssid=my_wifi_ssid
export wifi_password=my_wifi_pass
export wifi_security=eWiFiSecurityWPA2

# Set the config json file
echo "{
    \"afr_source_dir\": \"$afr_source_dir\",
    \"thing_name\":     \"$thing_name\",
    \"wifi_ssid\":      \"$wifi_ssid\",
    \"wifi_password\":  \"$wifi_password\",
    \"wifi_security\":  \"$wifi_security\"
}" > configure.json


# Run the example setup script
python SetupAWS.py setup






