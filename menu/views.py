from django.shortcuts import render, redirect
from .models import Menu
from .forms import MenuItemForm, DeleteItemForm

def menuView(request):
    main_dishs = Menu.objects.filter(type = 'main')
    drink = Menu.objects.filter(type = 'drink')
    dessert = Menu.objects.filter(type = 'dessert')
    item_count = Menu.objects.count()
    form = MenuItemForm()
    delete_form = DeleteItemForm()  # Initialize delete form

    if request.method == "POST":
        if "delete_item" in request.POST:
            delete_form = DeleteItemForm(request.POST)
            if delete_form.is_valid():
                dish_name = delete_form.cleaned_data["delete_dish_name"]
                deleted_count, _ = Menu.objects.filter(dish_name=dish_name).delete()  
                
                if deleted_count == 0:
                    print(f"Error: No dish found with name '{dish_name}'")
                
                return redirect('menu')

        else:  # Handle Add Item Form
            form = MenuItemForm(request.POST)
            if form.is_valid():
                print("Cleaned data:", form.cleaned_data) 
                form.save()  
                return redirect('menu')
            else:
                print("Form errors:", form.errors)
    
    menu_items = {
        'main_dishes': main_dishs,
        'drink':drink,
        'dessert':dessert,
    }

    return render(request, 'menu.html', {
        'menu_items': menu_items,
        'item_count': item_count,
        'form': form,
        'delete_form': delete_form,  # Pass delete form to template
    })
