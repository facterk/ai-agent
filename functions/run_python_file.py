import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    try:
        abs_working_dir = os.path.abspath(working_directory)
        abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

        if not abs_file_path.startswith(abs_working_dir):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not os.path.exists(abs_file_path):
            return f'Error: File "{file_path}" not found.'
        
        if not abs_file_path.endswith(".py") :
            return f'Error: "{file_path}" is not a Python file.'
        
        cmd = ["python", abs_file_path]
        if args:
            cmd.extend(args)
        
        completed_process = subprocess.run(
            cmd,
            cwd=abs_working_dir,
            capture_output=True,
            text=True,
            timeout=30
        )
        stdout = completed_process.stdout.strip()
        stderr = completed_process.stderr.strip()
        output_parts = []

        if stdout:
            output_parts.append(f"STDOUT:\n{stdout}")

        if stderr:
            output_parts.append(f"STDERR:\n{stderr}")

        if completed_process.returncode != 0:
            output_parts.append(f"Process exited with code {completed_process.returncode}")

        if not output_parts:
            return "No output produced."

        return "\n".join(output_parts)

    except Exception as e:
        return f"Error: executing Python file: {e}"


        