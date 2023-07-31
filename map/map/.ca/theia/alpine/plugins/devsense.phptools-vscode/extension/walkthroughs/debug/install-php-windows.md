
# Install PHP on Windows

## With installer

To install PHP and Xdebug(required for debugging), download and run installer from [XAMPP](https://www.apachefriends.org) or [WAMPP](https://www.wampserver.com).

## With command line (Preview)

If you are on Windows 10 1809 (build 17763) or higher, run the following command:

```
winget install --id Microsoft.webpicmd
webpicmd.exe /Install /products:PHP81x64,XdebugForPHP81x64 /Feeds:https://api.devsense.com/webpi/latest/webproducts.xml /AcceptEULA
```