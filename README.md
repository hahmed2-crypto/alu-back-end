# alu-back-end

Python scripts in the `api` directory that use the JSONPlaceholder REST API
(https://jsonplaceholder.typicode.com) to gather employee TODO list data.

| File | Description |
|------|-------------|
| `0-gather_data_from_an_API.py` | Prints an employee's TODO progress (takes an employee ID) |
| `1-export_to_CSV.py` | Exports an employee's tasks to `USER_ID.csv` |
| `2-export_to_JSON.py` | Exports an employee's tasks to `USER_ID.json` |
| `3-dictionary_of_list_of_dictionaries.py` | Exports all employees' tasks to `todo_all_employees.json` |

## Usage

    python3 0-gather_data_from_an_API.py 2
