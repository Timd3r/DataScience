import os
from pathlib import Path


def generate_sql():
    script_dir = Path(__file__).parent
    data_path = (script_dir / "../subject/customer").resolve()
    output_file = script_dir / "tables.sql"

    if not data_path.exists():
        print(f"{data_path} Folder not found!")
        return

    with open(output_file, "w") as sql_file:
        for file in data_path.glob("*.csv"):
            table_name = file.stem
            print(f"Found: {table_name}")
            sql_file.write(f"CREATE TABLE IF NOT EXISTS {table_name} (\n")
            sql_file.write("    event_time TIMESTAMP,\n")
            sql_file.write("    event_type TEXT,\n")
            sql_file.write("    product_id INTEGER,\n")
            sql_file.write("    price FLOAT,\n")
            sql_file.write("    user_id BIGINT,\n")
            sql_file.write("    user_session UUID\n")
            sql_file.write(");\n\n")
            sql_file.write(
                f"COPY {table_name} FROM '{file.resolve()}' WITH (FORMAT csv, HEADER true);\n\n")
    print(f"✅ SQL script generated: {output_file}")


def main():
    generate_sql()


if __name__ == "__main__":
    main()
