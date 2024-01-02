# Azure Alerts Command Line Tools

Fun project, attempting to create a command line tool to manage Azure Alerts which includes in terminal pltting and Open API integration.

## Details

So far, have used the `Pandas` library to create a dataframe of the Azure alerts. This can then be used to plot the data using native Pandas plotting capabilities, or using the awesome `plotext` library to plot in the terminal.

## Command examples:

Get help:

```
>> python ./main.py --help  

Usage: main.py [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  load-alerts
  plot-console
  plot-pandas
```

Load alerts:

```
>> python ./main.py load-alerts --range 7d
```

## Notes

If you recieve a warning related to 'urllib3' when running the script on a Macintosh, see the following [Stack Overflow post](https://stackoverflow.com/questions/76187256/importerror-urllib3-v2-0-only-supports-openssl-1-1-1-currently-the-ssl-modug) for a solution.