# Notes ID Mover

## Overview

This script helps you quickly move Notes ID files without the need to manually browse through folders. By searching for a specific name, it locates all matching files and allows you to copy the selected file to a specified directory.

## Features

- Search for files by name within a specified network folder.
- Display a list of matching files.
- Select a file from the list to copy to a desired location.
- Handles errors gracefully and provides user-friendly prompts.

## How to Use

1. **Setup**: Ensure the `folder_path` variable is set to the correct network path where the Notes ID files are stored. Replace the placeholder IP address (`\\XXX.XX.XX.XX\IDs`) with your actual network path.

2. **Running the Script**: Execute the script in a Python 3 environment. You will be prompted to enter the name of the file you are searching for.

3. **Search and Select**: The script will search for files containing the entered name and display a list of matches. You can then select a match to copy.

4. **Copying the File**: Enter the output directory where you want the selected file to be copied. The script will handle the rest, ensuring the file is copied to the specified location.

## Example

1. Run the script:
   ```sh
   python notes_id_mover.py
   ```

2. Enter the name to search for:
   ```
   Enter the name to search (or 'q' to quit): example_name
   ```

3. Select a match to copy:
   ```
   Found 3 matches for 'example_name':
   1. \\XXX.XX.XX.XX\IDs\example_name1.id
   2. \\XXX.XX.XX.XX\IDs\example_name2.id
   3. \\XXX.XX.XX.XX\IDs\example_name3.id
   Select a match to copy (1-3) or press Enter to search again: 1
   ```

4. Enter the output directory:
   ```
   Enter the output directory to copy the selected match to: 192.168.1.1
   ```

5. Confirm and copy the file:
   ```
   Selected file will be copied to: \\192.168.1.1\c$\Lotus\Notes\Data\example_name1.id
   Press Enter to continue or Ctrl+C to cancel.
   Successfully copied \\XXX.XX.XX.XX\IDs\example_name1.id to \\192.168.1.1\c$\Lotus\Notes\Data\example_name1.id.
   ```

## Important Notes

- **Customization**: You might need to change certain paths and IP addresses in the script to match your organization's network setup.
- **End of Maintenance**: This will be the last update to this script as I no longer work with Lotus Notes. Future modifications or updates will not be provided by me.

## Disclaimer

While this script is designed to be user-friendly and handle errors gracefully, please use it with caution, especially in a production environment. Always ensure you have the necessary permissions to access and copy files within your network.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to fork and modify this script to better suit your needs. If you encounter any issues or have suggestions for improvement, contributions are welcome!
