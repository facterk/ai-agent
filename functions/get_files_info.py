from pathlib import Path

def get_files_info(working_directory, directory=None):
    try:
        working_directory = Path(working_directory).resolve()
        directory = Path(directory).resolve() if directory else working_directory

        # Check if directory is within working_directory
        if not str(directory).startswith(str(working_directory)):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        # Check if the directory exists and is a directory
        if not directory.is_dir():
            return f'Error: "{directory}" is not a directory'

        # Build and return directory contents
        lines = []
        for entry in directory.iterdir():
            try:
                size = entry.stat().st_size
                is_dir = entry.is_dir()
                lines.append(f'- {entry.name}: file_size={size} bytes, is_dir={is_dir}')
            except Exception as e:
                lines.append(f'- {entry.name}: Error: {str(e)}')

        return '\n'.join(lines)

    except Exception as e:
        return f'Error: {str(e)}'
