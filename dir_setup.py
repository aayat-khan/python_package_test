import os

def create_directory_structure():
    # Create src directory
    src_dir = "src"
    os.makedirs(src_dir, exist_ok=True)

    # Create __init__.py file in src
    with open(os.path.join(src_dir, "__init__.py"), "w") as init_file:
        init_file.write("")

    # Create main.py file
    with open("main.py", "w") as main_file:
        main_file.write("# Your main script goes here")

    # Create setup.py file
    with open("setup.py", "w") as setup_file:
        setup_file.write("# Your setup config goes here")

    # Create additional directories inside src
    directories = ["api", "models", "services", "utils", "configs", "data_processing", "recommendatin_drivers"]
    for directory in directories:
        dir_path = os.path.join(src_dir, directory)
        os.makedirs(dir_path, exist_ok=True)

        # Create __init__.py file in each directory
        with open(os.path.join(dir_path, "__init__.py"), "w") as init_file:
            init_file.write("")

    print("Directory structure created successfully!")

if __name__ == "__main__":
    create_directory_structure()