import os
from pathlib import Path

def generate_sql():
    script_dir = Path(__file__).parent
    data_path = (script_dir / "../subject/customer").resolve()
    
    # This MUST match the path inside your container (from docker-compose.yml)
    docker_data_path = "/tmp/customer"
    output_file = script_dir / "tables.sql"

    if not data_path.exists():
        print(f"{data_path} Folder not found!")
        return

    with open(output_file, "w") as sql_file:
        table_names = []
        for file in data_path.glob("*.csv"):
            table_name = file.stem
            table_names.append(table_name)
            
            sql_file.write(f"CREATE TABLE IF NOT EXISTS {table_name} (\n")
            sql_file.write("    event_time TIMESTAMP,\n")
            sql_file.write("    event_type TEXT,\n")
            sql_file.write("    product_id INTEGER,\n")
            sql_file.write("    price FLOAT,\n")
            sql_file.write("    user_id BIGINT,\n")
            sql_file.write("    user_session UUID\n")
            sql_file.write(");\n\n")
            
            # USE THE DOCKER PATH HERE
            sql_file.write(f"COPY {table_name} FROM '{docker_data_path}/{file.name}' WITH (FORMAT csv, HEADER true);\n\n")
        
        # Corrected '1 big table' logic
        sql_file.write("CREATE TABLE IF NOT EXISTS customers AS\n")
        for i, table in enumerate(table_names):
            sql_file.write(f"    SELECT * FROM {table}")
            if i < len(table_names) - 1:
                sql_file.write("\n    UNION ALL\n")
            else:
                sql_file.write(";\n")
                
    print(f"✅ SQL script generated with internal container paths: {output_file}")

if __name__ == "__main__":
    generate_sql()