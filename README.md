# Nginx

Master: [![Build Status](https://travis-ci.org/sansible/nginx.svg?branch=master)](https://travis-ci.org/sansible/nginx)
Develop: [![Build Status](https://travis-ci.org/sansible/nginx.svg?branch=develop)](https://travis-ci.org/sansible/nginx)

* [Installation and Dependencies](#installation-and-dependencies)
* [Tags](#tags)
* [Examples](#examples)

Installs and configures nginx.




## Installation and Dependencies

This role has no dependencies.

To install run `ansible-galaxy install sansible.nginx` or add this to your
`roles.yml`

```YAML
- name: sansible.nginx
  version: v2.1
```

and run `ansible-galaxy install -p ./roles -r roles.yml`




## Tags

This role uses two tags: **build** and **configure**

* `build` - Installs Nginx.
* `configure` - (re-)Configures Nginx.




## Examples

To simply install Nginx:

```YAML
- name: Install Nginx
  hosts: sandbox

  pre_tasks:
    - name: Update apt
      become: yes
      apt:
        cache_valid_time: 1800
        update_cache: yes
      tags:
        - build

  roles:
    - role: sansible.nginx
```

The default access log format is in JSON, to use the standard txt format:


```YAML
- name: Install Nginx
  hosts: sandbox

  pre_tasks:
    - name: Update apt
      become: yes
      apt:
        cache_valid_time: 1800
        update_cache: yes
      tags:
        - build

  roles:
    - role: sansible.nginx
      sansible_nginx_access_log_format: standard
```
