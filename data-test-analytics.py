import pandas as pd

data = pd.read_csv('/home/silvia/Documentos/Case_PetLove/data-test-analytics_5.csv', nrows=None)

date_columns = ['created_at', 'updated_at', 'deleted_at', 'birth_date', 'last_date_purchase']
for col in date_columns:
    data[col] = pd.to_datetime(data[col], dayfirst=True, errors='coerce')

data.drop_duplicates(inplace=True)

active_subscribers = data[data['status'] == 'active'].shape[0]
paused_subscribers = data[data['status'] == 'paused'].shape[0]
cancelled_subscribers = data[data['status'] == 'canceled'].shape[0]

total_subscribers = active_subscribers + paused_subscribers + cancelled_subscribers

churn_rate = (cancelled_subscribers / total_subscribers) * 100

churn_by_state = data[data['status'] == 'canceled']['state'].value_counts()
total_subscribers_by_state = data['state'].value_counts()

churn_percent_by_state = (churn_by_state / total_subscribers_by_state) * 100

cancelled_subscribers_by_state = churn_by_state
churn_percent_by_state = churn_percent_by_state.round(2)

churn_data_by_state = pd.DataFrame({
    'Churn Percent': churn_percent_by_state,
    'Cancelled Subscribers': cancelled_subscribers_by_state
})

churn_data_by_state = churn_data_by_state.sort_values(by='Cancelled Subscribers', ascending=False)

average_ticket = data['average_ticket'].mean()

total_revenue = data['all_revenue'].sum()
total_orders = data['all_orders'].sum()

average_items = data['items_quantity'].mean()

city_distribution = data['city'].value_counts()
state_distribution = data['state'].value_counts()

marketing_channel = data['marketing_source'].value_counts()

data['birth_date'] = pd.to_datetime(data['birth_date'], format='%Y-%m-%d')

data = data[data['birth_date'] <= pd.to_datetime('today')]

current_date = pd.to_datetime('today')
data['age'] = ((current_date - data['birth_date']).dt.days / 365)

mean_age = data['age'].mean()

mean_recency = data['recency'].mean()

cancelled_data = data[data['status'] == 'canceled']
cancelled_data['time_to_cancel'] = (cancelled_data['deleted_at'] - cancelled_data['created_at']).dt.days

mean_time_to_cancel = cancelled_data['time_to_cancel'].mean()

print("Taxa de Churn: {:.2f}%".format(churn_rate))
print("Média de Gastos por Pedido: {:.2f}".format(average_ticket))
print("Total de Receita: {:.2f}".format(total_revenue))
print("Total de Pedidos Realizados:", total_orders)
print("Média de Itens na Assinatura: {:.2f}".format(average_items))
print("\nDistribuição Geográfica (Estados):", state_distribution)
print("\nChurn por Estado:", churn_data_by_state)
print("\nCanal de Marketing:", marketing_channel)
print("Média de Idade dos Clientes: {:.1f}".format(mean_age))
print("Média de Recência da Última Compra: {:.1f}".format(mean_recency))
print("Média de Tempo até o Cancelamento: {:.1f} dias".format(mean_time_to_cancel))

