"""Module to backup Tiny House Home Assistant configuration files to Github."""

from subprocess import call
import os
import sys


def run_acp_config_files(branch_name):
    """Function responsible for updating Github configuration files."""
    
    original_dir = os.environ.get('ORIGINAL_DIR', 'Not Set')
    path_to_project_dir = os.environ.get('PROJECT_DIR_PATH', 'Not Set')
    path_to_original_config_dir = os.environ.get('ORIGINAL_DIR_PATH', 'Not Set')
    
    call(['sudo', 'rm', '-rf', path_to_project_dir + '/homeassistant_config_backup'])
    call(['sudo', 'cp', '-r', path_to_original_config_dir, path_to_project_dir])
    call(['sudo', 'mv', path_to_project_dir + original_dir, path_to_project_dir + '/homeassistant_config_backup'])
    call(['sudo', 'git', 'add', '.'])
    commit_message = input('Please enter a Github commit message: ')
    call(['sudo', 'git', 'commit', '-m', commit_message])
    call(['sudo', 'git', 'push', 'origin', branch_name])


if __name__ == '__main__':
    run_acp_config_files(sys.argv[1])

