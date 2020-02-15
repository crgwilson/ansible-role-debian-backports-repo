# Ansible role: Debian Backports Repo

Install the Debian backports repo in one place rather than strewn about everywhere that needs it

* Add the debian backports repo into the apt sources list
* Thats it

## Variables

| Name | Default | Description |
| ---- | ------- | ----------- |
| `debian_backports_repo_url` | `http://deb.debian.org/debian` | The address of the mirror to install |
| `debian_backports_repo_components` | `['main']` | List of components to make available from this repo (ie: main, contrib, or non-free) |
| `debian_backports_repo_state` | `present` | Whether to add or remove the repo from apt |

## Testing

Testing for this project is setup using [Molecule](https://molecule.readthedocs.io/en/stable/) & [Docker](https://www.docker.com/).
Unit tests can be run using the below command:

```console
foo@bar:~$ molecule test --all
```
