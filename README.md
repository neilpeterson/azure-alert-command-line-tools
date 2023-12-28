# Azure Alerts Command Line Tools

Fun project, attempting to create a command line tool to manage Azure Alerts which includes in terminal pltting and Open API integration.

## Details

So far, have used the `Pandas` library to create a dataframe of the Azure alerts. This can then be used to plot the data using native Pandas plotting capabilities, or using the awesome `plotext` library to plot in the terminal.

Pandas plotting example:

![Image showing a plot using the Pandas library.](images/pandas-plot.png)

Plotext plotting example:

```
    ┌────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
29.0┤                                                                                                                                                                           ▞│
    │                                                                                                                                                                           ▌│
24.2┤                                                                                                                                                                           ▌│
    │                                                                                                                                                                           ▌│
    │                                                                                                                                                                          ▗▘│
19.3┤                                                                                                                                                                          ▐ │
    │                                                                                                                                                                          ▐ │
14.5┤                                                                                                                                                                          ▐ │
    │                                                                                                                                                                          ▞ │
    │                                                                                                                                                                          ▌ │
 9.7┤                                                                                                          ▖              ▗                                                ▌ │
    │                                                                                                         ▐▌      ▗▚      ▌▀▌                                              ▌ │
 4.8┤                                                                                                         ▞▐      ▞ ▚    ▗▘ ▐   ▗                                        ▗▄▘ │
    │                                                                                                         ▌ ▌ ▞▄▖▗▘  ▚▖  ▐   ▚ ▗▘▚▖                                      ▌   │
    │ ▗    ▄▞▖    ▗     ▗▄▖                                                                                  ▐  ▐▞  ▝▀    ▝▀▖▌    ▚▞  ▝▀▖                                   ▐    │
 0.0┤▀▘▚▄▞▀  ▝▀▀▀▀▘▀▚▄▄▄▘ ▝▚▄▄▄▄▄▄▄▄▄▚▄▄▄▄▄▄▄▄▄▄▄▄▄▄▚▄▄▄▄▄▚▄▄▄▄▄▄▄▄▄▄▄▞▄▄▄▄▄▄▄▄▄▄▄▄▄▚▄▄▄▄▄▄▄▄▄▄▄▚▄▄▄▄▄▄▄▄▄▄▄▄▟   ▘          ▝▌     ▘    ▝▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▞▄▄▄▄▄▄▄▄▄▄▄▄▄▌    │
    └┬──────────────────────────────────────────┬──────────────────────────────────────────┬─────────────────────────────────────────┬──────────────────────────────────────────┬┘
  23/12/2023 22:00                      25/12/2023 02:15                           26/12/2023 06:30                          27/12/2023 10:45                    28/12/2023 15:00 
```