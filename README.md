# HTTP-ODBC

HTTP-ODBC is a small server that serves as an HTTP access point to an ODBC endpoint. 
In particular, Experian Pandora uses a propertiary JDBC driver, and so the most
effective way to connect to Experian Pandora is through a DSN. However, some clients
do not support accessing ODBC via DSN. This tool is ideal for those circumstances.

**If you are capable of connecting to the underlying driver directly using JDBC that will
be more effective, and performant.**


## Configuration

Before using HTTP-ODBC be sure to set the necessary environment variables:

| Environment Variable | Description | Default |
| -------------------- | ----------- | ------- |
| HTTP_ODBC_CONNECTION_STRING | Connection string to be used to connect via ODBC | None |
| HTTP_ODBC_PORT | Port to be used when server starts | 8005 |

Find more information about the connection string to use  [here](https://github.com/mkleehammer/pyodbc/wiki/Connecting-to-databases).

## Usage
1. [Download](https://github.com/experianplc/http-odbc/releases/latest) the latest release.
2. Set the envrionment variables as specified in `Configuration`.
3. Run the server.exe

> Alternatively, you can set the configuration in the included `server-pandora.bat` and `server-aperture.bat` files for Windows and execute the script as necessary for Pandora or Data Studio respectively. 

## Frequently asked questions
> Does this work for Linux?

At the moment, our binary is only compiled for Windows. However, you can clone this project and set the environment variables as mentioned in the Configuration section and run `server.py` to use this on Linux machines that have Python installed. 

## Troubleshooting
> The server will not start, what do I do?
If the server does not start you're most likely getting this particular error (on Windows).
![image](https://user-images.githubusercontent.com/5572859/66215825-54925280-e692-11e9-8313-cccec28c3607.png)

This means your `HTTP_ODBC_CONNECTION_STRING` has not been properly configured. To confirm that the configuration is correct, you can do the following:

1. Open up odbcad32.exe (Win + R -> odbcad32.exe) and make sure your User DSN includes the one you are using in `HTTP_ODBC_CONNECTION_STRING`. So as an example, based on these User Data Sources:

![image](https://user-images.githubusercontent.com/5572859/66216015-adfa8180-e692-11e9-828b-9ac370919b43.png)

HTTP_ODBC_CONNECTION_STRING=DSN=**PServer 64bit**;UID=administrator;PWD=administrator

You can see that the PServer 64bit is reflected here. The UID and PWD will depend on the drivers configuration itself. If you're ensure please contact your system administrator. 

> The server starts but I'm not getting a response.
If you're not getting a response it means the query itself you're attempting to use is invalid. 

![image](https://user-images.githubusercontent.com/5572859/66216219-13e70900-e693-11e9-8dd1-c4acee8e9d85.png)

With Pandora and Data Studio in particular, make sure that table you're querying exists. 
