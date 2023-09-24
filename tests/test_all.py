import subprocess

def check_script():

    processes = ['src/main.py',
                 'tests/test_adaptive_step_selection.py',
                 'tests/test_runge_kutta_modification.py',
                 'tests/test_error_estimation.py',
                 ]

    for process_name in processes:
        process = subprocess.run(['python3', process_name], check=False)
        return_code = process.returncode
        if return_code == 0:
            print(f"{process_name} ran successfully.")
        else:
            print(f"{process_name} encountered an error with return code: {return_code}")

if __name__ == "__main__":
    check_script()
