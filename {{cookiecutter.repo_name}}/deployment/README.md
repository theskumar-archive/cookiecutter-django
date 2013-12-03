To develop, we will need to set up our VM to share a code directory with the host computer, so we can easily see the changes we make without needing to commit or do anything else. Add a shared directory (read/write, because that’s sometimes necessary for migrations) to the VM, and give it the project’s name, as we will need it later on in the scripts.

These scripts create a user called `{{cookiecutter.project_name}}` and a directory called `/var/projects/{{cookiecutter.project_name}}`, and install everything in that directory as that user.

## hosts

`local` is the VM used for development (that’s what the vm=1 means), and it tracks the develop git branch. `staging` is the staging server, it’s not a VM (vm=0) and it also tracks `develop`, and `production` tracks `master`.
