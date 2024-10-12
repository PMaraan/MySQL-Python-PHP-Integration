# execute_script.py
import subprocess

# List of scripts to execute
scripts = ['98_single_database_cleanup.py', '100_cleanup_files1.py']

for script in scripts:
    try:
        print(f"Executing {script}...")
        result = subprocess.run(['python', script], capture_output=True, text=True)

        # Print the output
        print("Output:")
        print(result.stdout)

        # Check for errors
        if result.stderr:
            print("Error:", result.stderr)

    except Exception as e:
        print(f"An error occurred while executing {script}: {e}")