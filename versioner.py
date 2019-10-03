#!usr/bin/python3
#
# Project Versioner
#   Makes snapshots of files on the src/ folder with named tags.

try:
    def main(projectRoot, args):

        # Create an error for this application
        class VersionerError(Exception): ...

        # Debug Information
        #print('Project root: {}'.format(projectRoot))
        #print('Args: {}'.format(args))

        # Main Program
        if len(args) != 2:
            raise VersionerError('Invalid amount of arguments')
        
        else:
            # Import some applications
            from shutil import copytree
            from pathlib import Path
            from os.path import isfile, exists

            # Check if the version/ folder exists
            exportPath = Path(projectRoot) / 'version'
            if isfile(exportPath):
                # Raise an error if it is a file
                raise VersionerError('Folder version/ on the project root is a file, not a directory.')
            elif not exists('version'):
                # Create the folder if it doesn't exist
                exportPath.mkdir()

            # Check if the version folder exists
            versionPath = Path(projectRoot) / 'version/{}'.format(args[1])
            if exists(versionPath):
                raise VersionerError('\'version/{}\' already exists. Consider renaming or removing it.'.format(args[1]))
            else:
                projectSource = Path(projectRoot) / 'src/'
                copytree(projectSource, versionPath)

    if __name__ == '__main__':
        
        from sys import argv
        from pathlib import Path
        from os import getcwd
        
        cwd = Path(getcwd()).resolve()
        main(cwd, argv)
    
except Exception as ex:
    print('Program interrupted by exception:')
    print('  {}: {}'.format(type(ex).__name__, ex))
