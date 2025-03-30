import mysql.connector
import pandas as pd

def update_records(dataset, db_config, student, key_column):

    conn = mysql.connector.connect(
        host=db_config["localhost"],
        user=db_config["root"],
        password=db_config["Yuki_8686009"],
        database=db_config["sekai"]
    )
    cursor = conn.cursor()

    df = pd.read_csv("dataset.csv")
  
    for _, row in df.iterrows():
        set_clause = ", ".join([f"{col} = %s" for col in df.columns if col != key_column])
        sql = f"""
            UPDATE {student}
            SET {set_clause}
            WHERE {key_column} = %s
        """
        values = tuple(row[col] for col in df.columns if col != key_column) + (row[key_column],)
        cursor.execute(sql, values)
    
   
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    db_config = {
        "host": "localhost",
        "user": "root",
        "password": "Yuki_8686009",
        "database": "sekai"
    }
update_records("data.csv", db_config, "student", "student_id")
