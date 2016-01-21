# Nginx

Master: [![Build Status](https://travis-ci.org/ansible-city/nginx.svg?branch=master)](https://travis-ci.org/ansible-city/nginx)  
Develop: [![Build Status](https://travis-ci.org/ansible-city/nginx.svg?branch=develop)](https://travis-ci.org/ansible-city/nginx)

* [ansible.cfg](#ansible-cfg)
* [Installation and Dependencies](#installation-and-dependencies)
* [Tags](#tags)
* [Examples](#examples)

Installs nginx.




## ansible.cfg

This role is designed to work with merge "hash_behaviour". Make sure your
ansible.cfg contains these settings

```INI
[defaults]
hash_behaviour = merge
```




## Installation and Dependencies

This role has no dependencies.

To install run `ansible-galaxy install ansible-city.nginx` or add this to your
`roles.yml`

```YAML
- name: ansible-city.nginx
  version: v1.0
```

and run `ansible-galaxy install -p ./roles -r roles.yml`




## Tags

This role uses two tags: **build** and **configure**

* `build` - Installs Nginx.
* `configure` - (re-)Configures Nginx.




## Examples

To simply install Java:

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
    - name: ansible-city.nginx
```
