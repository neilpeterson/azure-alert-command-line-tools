from azure.identity import DefaultAzureCredential
from azure.mgmt.alertsmanagement import AlertsManagementClient
import matplotlib.pyplot as plt
import pandas as pd
import plotext as pltconsole

subscription = ""
credential = DefaultAzureCredential()
plot_terminal = True
plot_window = False

def plot_terminal(alerts):

    dates = pd.to_datetime(daily_alerts.index).strftime("%d/%m/%Y %H:%M")
    dates = dates.drop_duplicates().tolist()

    pltconsole.date_form("d/m/Y H:M")
    pltconsole.plot(dates, alerts)
    pltconsole.title('Number of alerts per day')
    pltconsole.theme("pro")
    pltconsole.show()

def plot_pandas(alerts):

    alerts.plot(kind='line')
    plt.title('Number of alerts per day')
    plt.xlabel('Date')
    plt.ylabel('Number of alerts')
    plt.show()

client = AlertsManagementClient(
    credential,
    subscription
)

alert_list = []
for alert in client.alerts.get_all(time_range="30d"):
    alert_list.append(alert.properties.essentials.as_dict())

df = pd.DataFrame(alert_list)

# Convert the 'startDateTime' column to datetime format, set it as the index, and sort
df['start_date_time'] = pd.to_datetime(df['start_date_time'])
df.set_index('start_date_time', inplace=True)
df.sort_index(inplace=True)

# Resample the DataFrame by day and count the number of alerts each day
daily_alerts = df.resample('H').size()

if plot_window:
    plot_pandas(daily_alerts)

if plot_terminal:
    plot_terminal(daily_alerts)

