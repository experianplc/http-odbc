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
Please note tha the `HTTP_ODBC_PORT` is not the port in which your application is exposing itself. This will be the port in which the server itself listens. 

So for example, if you're running Experian Pandora or Experian Data Studio and its ODBC port listens at `7800`, you will *not* want to configure the `HTTP_ODBC_PORT` to also listen `7800`. Instead, you might want to make the port an available open port, for example `8000`. 

In addition, `HTTP-ODBC` must be running on the same machine that exposes the ODBC DSN name. So if you have a machine called `machine-1` that has the DSN name `PServer 64bit` listed under its ODBC Connections then `HTTP-ODBC` must be running on `machine-1` in order to access the DSN name `PServer 64bit` if that's the DSN you're trying to use. 

### Additions for Experian Pandora and Experian Data Studio
Be sure that the service Pandora and/or Data Studio is turned on before attempting to run `HTTP-ODBC`. If Pandora and/or Data Studio are not on and you run `HTTP-ODBC` it will attempt to connect to an ODBC connection that is not listening and fail with an error.

This is generally the same practice you would use for any application. 

## Usage
1. [Download](https://github.com/experianplc/http-odbc/releases/latest) the latest release - be sure to download `server-windows.zip`.
2. Make sure your User DSN is set (for Windows machines). See the Troubleshooting section below for details.
2. Set the envrionment variables as specified in `Configuration`.
3. Run the server.exe

> Alternatively, you can set the configuration in the included `server-pandora.bat` and `server-aperture.bat` files for Windows and execute the script as necessary for Pandora or Data Studio respectively. 

Once the server is running you will send a POST request to the URL in the following format

```http
{
  "sql": $QUERY
}
```

Where $QUERY is a properly escaped SQL query, e.g. `"SELECT * FROM \"PROFILES\""`. 

## Frequently asked questions
#### Does this work for Linux?

At the moment, our binary is only compiled for Windows. However, you can clone this project and set the environment variables as mentioned in the Configuration section and run `server.py` to use this on Linux machines that have Python installed. 

## Troubleshooting

#### The server will not start, what do I do?
If the server does not start you're most likely getting this particular error (on Windows).
![image](https://user-images.githubusercontent.com/5572859/66215825-54925280-e692-11e9-8313-cccec28c3607.png)

This means your `HTTP_ODBC_CONNECTION_STRING` has not been properly configured. To confirm that the configuration is correct, you can do the following:

1. Open up odbcad32.exe (Win + R -> odbcad32.exe) and make sure your User DSN includes the one you are using in `HTTP_ODBC_CONNECTION_STRING`. So as an example, based on these User Data Sources:

![image](https://user-images.githubusercontent.com/5572859/66216015-adfa8180-e692-11e9-828b-9ac370919b43.png)

You would set `HTTP_ODBC_CONNECTION_STRING` to `DSN=PServer 64bit;UID=administrator;PWD=administrator`. 

You can see that the PServer 64bit is reflected here. The UID and PWD will depend on the drivers configuration itself. If you're ensure please contact your system administrator. 

#### The server starts but I'm not getting a response.
If you're not getting a response it means the query itself you're attempting to use is invalid. 

![image](https://user-images.githubusercontent.com/5572859/66216219-13e70900-e693-11e9-8dd1-c4acee8e9d85.png)

With Pandora and Data Studio in particular, make sure that table you're querying exists. 
