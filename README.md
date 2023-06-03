# README

This repository contains a Python script that reads data from a file and extracts specific fields from a JSON object. The extracted fields are then written to separate text files.

## Installation

To use this script, you'll need Python installed on your machine. If you don't have Python installed, you can download and install it from the official Python website: [python.org](https://www.python.org/).

You'll also need to have a file named `data.txt` in the same directory as the script. The `data.txt` file should contain a valid JSON object.

## Usage

1. Clone this repository to your local machine or download the script directly.

2. Place the `data.txt` file in the same directory as the script.

3. Open a terminal or command prompt and navigate to the directory where the script is located.

4. Run the script by executing the following command:

   ```
   python script.py
   ```

5. The script will read the `data.txt` file, extract specific fields from the JSON object, and write them to separate text files.

   - The extracted `first_name` field will be written to `first_name.txt`.
   - The extracted `last_name` field will be written to `last_name.txt`.
   - The extracted `email` field will be written to `email.txt`.
   - The extracted `gender` field will be written to `gender.txt`.
   - The extracted `ip_address` field will be written to `ip_address.txt`.

## Example

Assuming the `data.txt` file contains the following JSON object:

```json
[
  {
    "first_name": "John",
    "last_name": "Doe",
    "email": "john.doe@example.com",
    "gender": "male",
    "ip_address": "192.168.0.1"
  },
  {
    "first_name": "Jane",
    "last_name": "Smith",
    "email": "jane.smith@example.com",
    "gender": "female",
    "ip_address": "192.168.0.2"
  }
]
```

Running the script will generate the following text files:

- `first_name.txt`:

  ```
  ['John', 'Jane']
  ```

- `last_name.txt`:

  ```
  ['Doe', 'Smith']
  ```

- `email.txt`:

  ```
  ['john.doe@example.com', 'jane.smith@example.com']
  ```

- `gender.txt`:

  ```
  ['male', 'female']
  ```

- `ip_address.txt`:

  ```
  ['192.168.0.1', '192.168.0.2']
  ```

## Contributing

Contributions to this project are welcome. If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use and modify the code as per the terms of the license.

## Acknowledgements

This script was created as a demonstration and can be used as a starting point for more complex data extraction tasks.