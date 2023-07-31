# Install PHP on Linux

To install latest version of PHP and Xdebug(required for debugging), start a new terminal (<kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>`</kbd>) and run the following commands the based on your Linux distribution.

## [Debian-based Linux distributions](https://www.debian.org/)

Run the following commands:

```
sudo apt-get update
sudo apt-get install php
sudo apt-get install php-xdebug
```


## [Fedora-based Linux distributions](https://getfedora.org/)

Run the following commands:

```
sudo dnf -y update
sudo dnf -y install php
sudo dnf -y install php-xdebug
```

## Verify the installation

Verify the installation by running the following command:

```
php -v
```

The output should indicate both PHP and Xdebug is installed:

```
PHP 8.1.7 (cli) (built: Jun  7 2022 18:21:38) (NTS gcc x86_64)
Copyright (c) The PHP Group
Zend Engine v4.1.7, Copyright (c) Zend Technologies
    with Zend OPcache v8.1.7, Copyright (c), by Zend Technologies
    with Xdebug v3.1.5, Copyright (c) 2002-2022, by Derick Rethans
```