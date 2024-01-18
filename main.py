from azure.identity import DefaultAzureCredential
from azure.mgmt.alertsmanagement import AlertsManagementClient
import matplotlib.pyplot as plt
import pandas as pd
import plotext as pltconsole
from pandasai import SmartDataframe
from pandasai.llm import OpenAI
import click
import csv
import os

subscription = "65ae371b-6c46-4e36-8a7b-93efb1f2c2bd"
llm = OpenAI(api_token='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')
alerts_csv = "alerts.csv"
plot_terminal = True
plot_window = True

@click.group()
def cli():
    pass

def plot_window(alerts):

    alerts.plot(kind='line')
    plt.title('Number of alerts per day')
    plt.xlabel('Date')
    plt.ylabel('Number of alerts')
    plt.show()

def plot_terminal(alerts):

    dates = pd.to_datetime(alerts.index).strftime("%d/%m/%Y %H:%M")
    dates = dates.drop_duplicates().tolist()

    pltconsole.date_form("d/m/Y H:M")
    pltconsole.plot(dates, alerts)
    pltconsole.title('Number of alerts per day')
    pltconsole.theme("pro")
    pltconsole.show()

def return_df():

    var_local_alerts_csv = alerts_csv
    df = pd.read_csv(var_local_alerts_csv)

    # Convert the 'start_date_time' column to datetime64
    df['start_date_time'] = pd.to_datetime(df['start_date_time'])

    # Set the index to the 'start_date_time' column
    df.set_index('start_date_time', inplace=True)

    # Sort the DataFrame by the index
    df.sort_index(inplace=True)

    return df

@click.command()
@click.option('--range', default='7d', type=click.Choice(['1h', '1d', '7d', '30d']))
def load_alerts(range):

    # Azure auth under CLI context
    credential = DefaultAzureCredential()
    client = AlertsManagementClient(
        credential,
        subscription
    )

    var_local_alerts_csv = alerts_csv

    alert_list = []
    for alert in client.alerts.get_all(time_range=range):
        alert_list.append(alert.properties.essentials.as_dict())

    df = pd.DataFrame(alert_list)

    if os.path.exists(var_local_alerts_csv):
        os.remove(var_local_alerts_csv)

    df.to_csv(var_local_alerts_csv, index=False)

@click.command()
def plot_pandas():

    # Get datafram and resample day and count the number of alerts each day.
    daily_alerts = return_df()
    daily_alerts_resample = daily_alerts.resample('H').size()
    plot_window(daily_alerts_resample)

@click.command()
def plot_console():

    # Get datafram and resample day and count the number of alerts each day.
    daily_alerts = return_df()
    daily_alerts_resample = daily_alerts.resample('H').size()
    plot_terminal(daily_alerts_resample)

@click.command()
def pandas_ai():

    print('Alerts loaded, please enter a query or type \'quit()\' to exit')

    user_input = ""
    while user_input != "quit()":

        daily_alerts = return_df()
        df = SmartDataframe(daily_alerts, config={"llm": llm})

        user_input = input()
        openai_response = df.chat(user_input)

        if isinstance(openai_response, SmartDataframe):

            print('Enter a new query or type \'quit()\' to exit')
            print()

            # Resample the DataFrame by day and count the number of alerts each day
            daily_alerts = openai_response.resample('H').size()
            print(openai_response)
        else:
            if user_input != "quit()":
                print(openai_response)
                print()
                print('Enter a new query or type \'quit()\' to exit')

cli.add_command(load_alerts)
cli.add_command(plot_pandas)
cli.add_command(plot_console)
cli.add_command(pandas_ai)

if __name__ == '__main__':
    cli()