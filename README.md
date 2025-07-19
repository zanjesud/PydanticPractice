# Pydantic Practice Project

This repository is a collection of code examples and notes for learning and experimenting with the [Pydantic](https://docs.pydantic.dev/) library in Python. Pydantic is a powerful library for data validation and settings management using Python type annotations.

## Key Concepts Explored

This project covers a wide range of Pydantic features, from basic to advanced.

### Core Functionality

*   **Data Validation**: The primary use case of Pydantic, ensuring data conforms to a specified schema.
*   **Settings Management**: Creating robust, type-hinted application settings.
*   **Model Definition**: Defining data structures using classes that inherit from `BaseModel`.
*   **Type-Annotation Schema**: Leveraging Python's type hints to define data schemas.
*   **Data Exporting**: Easily exporting models to dictionaries (`.model_dump()`) and JSON strings (`.model_dump_json()`).

### Field Types and Constraints

*   **Basic & Complex Types**: Using standard Python types like `str`, `int`, `list`, `dict`, etc.
*   **Optional Fields**: Defining fields that are not required using `typing.Optional` or `| None`.
*   **Constrained Types**: Applying constraints to fields (e.g., `conint`, `constr` for value ranges and string patterns).
*   **Enum Types**: Using standard Python `Enum` for fields with a limited set of possible values.
*   **Literal Types**: Using `typing.Literal` to constrain a field to specific literal values.

### Validation

*   **Custom Validators**: Writing custom functions to perform complex validation logic using the `@validator` decorator (for Pydantic v1 style) or `@field_validator` (for Pydantic v2+).

### Advanced Model Features

*   **Nested Models**: Composing models by nesting one Pydantic model within another to represent complex data structures.
*   **`Field()` Function**:
    *   Setting default values, including dynamic defaults with `default_factory`.
    *   Creating aliases for fields to handle data from sources with different naming conventions (e.g., camelCase JSON to snake_case Python).
    *   Controlling field inclusion/exclusion during model export.
*   **Model Configuration**:
    *   Using `model_config` (`ConfigDict`) to control model behavior, such as allowing extra fields (`extra='allow'`), making models immutable (`frozen=True`), etc.

### JSON Schema Integration

*   **Generating JSON Schema**: Automatically creating a JSON Schema from a Pydantic model using `YourModel.model_json_schema()`.
*   **Generating Models from JSON Schema**: Using the `datamodel-code-generator` tool to auto-generate Pydantic model classes from existing JSON Schema definitions.

    We used the following commands for code generation:
    ```bash
    # To generate a model for modules
    datamodel-codegen --input ModuleSchema.json --output modulesmodel.py

    # To generate a model for students
    datamodel-codegen --input StudentSchema.json --output studentmodel.py
    ```
    > **Note**: This approach is excellent for bootstrapping models but does not automatically generate custom validator logic.

## Getting Started

To run the examples in this project, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd PydanticPractice
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # For Windows
    python -m venv venv
    .\venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install the dependencies:**
    The `requirements.txt` file contains all necessary packages.
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the example scripts:**
    Execute any of the Python files in this project to see the concepts in action.

## Useful Resources

Here are the resources that were referenced during the creation of this project.

### Blog Posts

*   Introduction to Pydantic
*   Pydantic Nested Models and JSON Schemas
*   Pydantic Field Function and Model Config

### Official Documentation

*   **Pydantic Models**: docs.pydantic.dev/usage/models/
*   **Pydantic Validators**: docs.pydantic.dev/latest/concepts/validators/
*   **Pydantic Schema**: docs.pydantic.dev/usage/schema/
*   **JSON Schema**: json-schema.org

### Datasets

*   **GitHub Dataset**: github.com/bugbytes-io/datasets