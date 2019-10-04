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
