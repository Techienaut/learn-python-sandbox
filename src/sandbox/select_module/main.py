import pkgutil
import importlib

def list_subpackages(package):
    subpackages = []
    for importer, modname, ispkg in pkgutil.iter_modules(package.__path__):
        if ispkg:
            subpackages.append(modname)
    return subpackages

def main():
    import sandbox
    subpackages = list_subpackages(sandbox)
    
    print("Select a game to play:")
    for i, pkg in enumerate(subpackages):
        print(f"{i + 1}. {pkg.capitalize()}")

    choice = input("Enter the number of your choice: ")
    
    try:
        choice = int(choice) - 1
        if 0 <= choice < len(subpackages):
            selected_pkg = subpackages[choice]
            module = importlib.import_module(f"sandbox.{selected_pkg}")
            if hasattr(module, f"play_{selected_pkg}"):
                getattr(module, f"play_{selected_pkg}")()
            else:
                print(f"No play function found in {selected_pkg}.")
        else:
            print("Invalid choice. Please enter a valid number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
