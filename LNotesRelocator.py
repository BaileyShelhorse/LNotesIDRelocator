print("Made by Bailey Shelhorse")
print("""
       (づ  ◕‿◕ )づ  Let me do this for you!
      """)

print("Move notes ID quickly without browsing through the folder.")
print("  ")

import os
import shutil

# Replace with IP
folder_path = r"\\XXX.XX.XX.XX\IDs"

while True:
    search_name = input("Enter the name to search (or 'q' to quit): ")
    if search_name == 'q':
        break

    matches = []

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if search_name in file:
                matches.append(os.path.join(root, file))

    if matches:
        print(f"Found {len(matches)} matches for '{search_name}':")
        for i, match in enumerate(matches):
            print(f"{i + 1}. {match}")

        while True:
            selection = input(f"Select a match to copy (1-{len(matches)}) or press Enter to search again: ")
            if not selection:
                break

            try:
                selection_index = int(selection) - 1
                if 0 <= selection_index < len(matches):
                    selected_match = matches[selection_index]

                    output_folder = input("Enter the output directory to copy the selected match to: ")
                    output_folder_path = '\\\\' + output_folder + '\\c$\\Lotus\\Notes\\Data'

                    print(f"Selected file will be copied to: {os.path.join(output_folder_path, os.path.basename(selected_match))}")
                    input("Press Enter to continue or Ctrl+C to cancel.")

                    try:
                        shutil.copy(selected_match, os.path.join(output_folder_path, os.path.basename(selected_match)))
                        print(f"Successfully copied {selected_match} to {os.path.join(output_folder_path, os.path.basename(selected_match))}.")
                    except (shutil.Error, FileNotFoundError) as e:
                        print(f"Error: {e}")
                else:
                    print("Invalid selection.")
            except ValueError:
                print("Invalid selection.")
    else:
        print(f"No matches found for '{search_name}'.")

input("Press Enter to exit.")
