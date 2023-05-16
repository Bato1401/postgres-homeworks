"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv


def read_csv(path):
    """Возвращает список словарей"""
    with open(path, 'r', encoding='utf-8') as file:
        file_reader = csv.reader(file, delimiter=",")
        data = []
        for line in file_reader:
            data.append(line)

    return data


def main():

    conn = psycopg2.connect(host="localhost", database="north", user="postgres", password="bavi1406")
    try:
        with conn:
            with conn.cursor() as cur:
                read_cus = read_csv('north_data/customers_data.csv')
                for row in read_cus[1:]:
                    cur.execute(
                        'INSERT INTO customers VALUES (%s, %s, %s)', (row[0], row[1], row[2])
                    )
                read_emp = read_csv('north_data/employees_data.csv')
                for row in read_emp[1:]:
                    cur.execute(
                        'INSERT INTO employees (first_name, last_name, title, birth_date, notes) '
                        'VALUES (%s, %s, %s, %s, %s)',
                        (row[0], row[1], row[2], row[3], row[4])
                    )
                read_ord = read_csv('north_data/orders_data.csv')
                for row in read_ord[1:]:
                    cur.execute(
                        'INSERT INTO orders (order_id, customer_id, employee_id, order_date, ship_city) '
                        'VALUES (%s, %s, %s, %s, %s)',
                        (row[0], row[1], row[2], row[3], row[4])
                    )
    finally:
        conn.close()


if __name__ == '__main__':
    main()

