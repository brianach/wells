# Install PHP on MacOS

To install latest version of PHP and Xdebug(required for debugging), start a new terminal (<kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>`</kbd>) and run the based on your Linux distribution.

1. Install [Homebrew](https://brew.sh/)

   In the terminal enter the following command:
   
   ```
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

2. Install PHP through [Homebrew](https://formulae.brew.sh/formula/php). 

    Following command will get you the most recent PHP version:
    ```
    brew install php
    ```

3. Install Xdebug with PECL

   Choose which command to run depending on your Mac architecture:
   - **Intel**

      ```
      pecl install xdebug
      ```

   - **Apple M1**
      
      ```
      arch -arm64 sudo pecl install xdebug
      ```

      or if PHP was compiled for x86_64 architecure, then run this command:
      ```
      arch -x86_64 sudo pecl install xdebug
      ```

4. Verify the installation

   ```
   php -v
   ```
   You should see output like this:
   ```
   PHP 8.0.17 (cli) (built: Mar 18 2022 09:45:09) (NTS)
   Copyright (c) The PHP Group
   Zend Engine v4.0.17, Copyright (c) Zend Technologies
       with Xdebug v3.1.3, Copyright (c) 2002-2022, by Derick Rethans
       with Zend OPcache v8.0.17, Copyright (c), by Zend Technologies
   ```