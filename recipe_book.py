# Recipe Book Project

def add_recipe(recipe_book):
    name = input("Enter the name of the recipe: ")
    ingredients = input("Enter the ingredients separated by commas: ").split(',')
    instructions = input("Enter the instructions: ")
    
    recipe_book[name] = {
        "ingredients": ingredients,
        "instructions": instructions
    }
    print(f"Recipe '{name}' added successfully!")

def search_recipe(recipe_book):
    ingredient = input("Enter the ingredient to search for: ")
    found = False
    for name, details in recipe_book.items():
        if ingredient in details['ingredients']:
            print(f"Recipe found: {name}")
            print(f"Ingredients: {details['ingredients']}")
            print(f"Instructions: {details['instructions']}\n")
            found = True
    if not found:
        print("No recipes found with that ingredient.")

def remove_recipe(recipe_book):
    name = input("Enter the name of the recipe to remove: ")
    if name in recipe_book:
        del recipe_book[name]
        print(f"Recipe '{name}' removed successfully!")
    else:
        print(f"Recipe '{name}' not found.")

def main():
    recipe_book = {}
    
    while True:
        print("\nRecipe Book")
        print("1. Add a recipe")
        print("2. Search for a recipe by ingredient")
        print("3. Remove a recipe")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_recipe(recipe_book)
        elif choice == '2':
            search_recipe(recipe_book)
        elif choice == '3':
            remove_recipe(recipe_book)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
