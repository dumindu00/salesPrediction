from sqlalchemy import text

def get_quarterly_profit(db):
    query = text("""
        SELECT 
            YEAR(sale_date) AS year,
            QUARTER(sale_date) AS quarter,
            SUM(total_sales) AS revenue
        FROM sales
        GROUP BY year, quarter
    """)
    return db.execute(query).fetchall()