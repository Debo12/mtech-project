armFolder="infrastructure/templates"
[[ "$1" == "-RESOURCE_GROUP_NAME" ]] && RESOURCE_GROUP_NAME="$2"
[[ "$3" == "-LOCATION" ]] && LOCATION="$4"
# Define the list
template_list=("container-registry.json")
parameter_file="container-parameters.json"

# Function to deploy ARM templates
deploy_template() {
    # Length of the list
    list_length=${#template_list[@]}
    script_dir=$(dirname "$0")
    parent_dir=$(dirname "$script_dir")

    # # Loop through the list
    for (( i=0; i<list_length; i++ ))
    do
        template_file="$parent_dir/templates/${template_list[i]}"
        parameters_file="$parent_dir/templates/$parameter_file"

        # Deploy ARM template
        az deployment group create \
            --template-file $template_file \
            --parameters $parameters_file \
            -g $RESOURCE_GROUP_NAME
    done
}

# Deploy ARM templates
deploy_template
