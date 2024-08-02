"""
Order_id, date_of_purchase, customer_id, paid_amount, category, product, city, state, payment_method

Txn.txt

1. Find Row count
2. Jan month order_id, customer_id, category, product, state
    A. Row count
3. July Month order_id, customer_id, category, product, state
    B. Row count
4. Each category [counts desc sort]
5. Category full details
6. Each pay method counts
7. jan-july month purchase count [includes]
8. Each category total amount
9. Each category maximum amount
10. Each category avg amount
11.total amount by cash and credit card
12. Indoor games, total amount
13. Each state count

"""

import numpy as np
import pandas as pd

df = pd.read_csv("C:/Users/jayas/OneDrive/Documents/txn.txt", header=None)
df.columns = ['order_id', 'date_of_purchase', 'customer_id', 'paid_amount', 'category', 'product', 'city', 'state',
              'payment_method']
print(df)

print("*" * 100)

print("Q1.")
print(df.shape[0])

print("*" * 100)

print("Q2.")
print(df.loc[(df['date_of_purchase'] <= "01-31-2011") & (df['date_of_purchase'] >= "01-01-2011")]
      [['order_id', 'customer_id', 'category', 'product', 'state']])

print("*" * 100)

print("Q2.A")
print(df.loc[(df['date_of_purchase'] <= "01-31-2011") & (df['date_of_purchase'] >= "01-01-2011")].shape[0])

print("*" * 100)

print("Q3.")
print(df.loc[(df['date_of_purchase'] <= "07-31-2011") & (df['date_of_purchase'] >= "07-01-2011")]
      [['order_id', 'customer_id', 'category', 'product', 'state']])

print("*" * 100)

print("Q3.A")
print(df.loc[(df['date_of_purchase'] <= "07-31-2011") & (df['date_of_purchase'] >= "07-01-2011")].shape[0])

print("*" * 100)

print("Q4.")
print(df.groupby('category')['category'].count().sort_values(ascending=False))

print("*" * 100)

print("Q5.")
print(df.loc[df['category'] == 'Outdoor Recreation'])

print("*" * 100)

print("Q6.")
print(df.groupby('payment_method')['payment_method'].count())

print("*" * 100)

print("Q7")
print(df.loc[(df['date_of_purchase'] <= "07-31-2011") & (df['date_of_purchase'] >= "01-01-2011")].shape[0])

print("*" * 100)

print("Q8.")
print(df.groupby('category')['paid_amount'].sum().sort_values(ascending=False))

print("*" * 100)

print("Q9.")
print(df.groupby('category')['paid_amount'].max().sort_values(ascending=False))

print("*" * 100)

print("Q10.")
print(df.groupby('category')['paid_amount'].mean().sort_values(ascending=False))

print("*" * 100)

print("Q11.")
print(df.groupby('payment_method')['paid_amount'].sum().sort_values(ascending=False))

print("*" * 100)

print("Q12.")
print(df.loc[df['category'] == 'Indoor Games'].groupby('category')['paid_amount'].result())

print("*" * 100)

print("Q13.")
print(df.groupby('state')['state'].count().sort_values(ascending=False))