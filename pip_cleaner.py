import subprocess

# Get a list of installed packages
completed_process = subprocess.run(['pip', 'list'], capture_output=True, text=True)
output_lines = completed_process.stdout.strip().split('\n')
package_lines = output_lines[2:]  # Skip the header and separator lines

# Extract package names from the output, excluding base packages
packages = []
for line in package_lines:
    package_name = line.split()[0]
    if package_name.lower() not in ('pip', 'setuptools'):
        packages.append(package_name)

# Display the list of installed packages
print("Installed Packages:")
for package in packages:
    print(package)

# Confirm deletion of packages
confirmation = input("Do you want to delete these packages? (y/n): ")

if confirmation.lower() in ('y'):
    # Delete the packages
    for package in packages:
        subprocess.run(['pip', 'uninstall', '-y', package])
        print(f"Deleted package: {package}")
else:
    print("Package deletion canceled.")
