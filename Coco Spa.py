# Title: Coco Spa
# Author: Wang Zining
# Date: May 12, 2024
# Description: Automate Coco spa's sales process, customer management and order management.

# Runtime Environment:
# - Python Version: 3.12
# - Operating System: Windows 11

# mainMenu
def mainMenu():
    print("@ @ @ @ Coco Spa @ @ @ @\n"
          "1. Product management\n"
          "2. Sales management\n"
          "0. Exit")


customerName1 = ''  # Declare a global variable
mainMenu()
choice_main_menu = input("Enter option:")

# Product management
goback_sub_menu = True
while goback_sub_menu:
    if choice_main_menu == '1':
        print()
        print("a. View/Update services\n"
              "b. Add new services\n"
              "c. View / Update Packages\n"
              "d. Add new Package\n"
              "e. View/Update Products\n"
              "f. Add new Product\n"
              "g. Back to main menu")
        print()
        choice_product_management = input("Enter your choice:")
        print()

        # View/Update services
        if choice_product_management.lower() == 'a':
            # Display services
            with open("Services.txt", "r") as services_files:
                content = services_files.read()
                print(content)
                print()

                choice_a = input('To update a service, enter the item code. '
                                 'Or enter 0 to go back to previous menu.\n')

                if choice_a == '0':
                    continue
                else:
                    with open("Services.txt", "r") as services_file1:
                        services = services_file1.readlines()
                    for line in services:
                        code, serviceA, priceA = line.strip().split(',')
                        if code == choice_a.upper():
                            print(line.strip())
                            newPrice = input("Enter the new price to update,"
                                             "or press Enter to delete.\n")
                            # Update
                            if newPrice:
                                services[services.index(line)] = f"{code},{serviceA},{newPrice}\n"
                            # Delete
                            else:
                                services.remove(line)
                            with open("Services.txt", "w") as services_files2:
                                services_files2.writelines(services)
                            print('The service has updated successfully.')
                            break
                    # Return error
                    else:
                        print('Error: No service found with this item code.')

        # Add new services
        elif choice_product_management.lower() == 'b':
            service = input('Enter the new service name:')
            item_code = input('Enter the new item code')
            price = input('Enter the new price')
            with open('Services.txt', 'a') as services_file1:
                services_file1.write(f'\n{item_code},{service},{price}')
            print('The new service has been added.')

        # View / Update Packages
        elif choice_product_management.lower() == 'c':
            with open("Packages.txt", "r") as packages_file:
                # services_dataA = []
                packages0 = packages_file.read()
                print(packages0)

                choice_c = input('To update a service, enter the item code. '
                                 'Or enter 0 to go back to previous menu.\n')
                if choice_c == '0':
                    continue

                else:
                    with open("Packages.txt", "r") as packages_file1:
                        packages = packages_file1.readlines()
                    for line in packages:
                        code, name, qty, priceB, serviceB = line.strip().split(',')
                        if code == choice_c.upper():
                            print(line.strip())
                            newPriceB = input("Enter the new price to update,"
                                              "or press Enter to delete.")
                            # Update
                            if newPriceB:
                                packages[packages.index(line)] = f"{code},{name},{qty},{newPriceB},{serviceB}\n"
                            # Delete
                            else:
                                packages.remove(line)
                            with open("Packages.txt", "w") as packages_file2:
                                packages_file2.writelines(packages)
                            print('The package has updated successfully.')
                            break
                    else:
                        print("Error: No service found with that item code.")

        # Add new Package
        elif choice_product_management.lower() == 'd':
            newNameB = input('Enter the new item name:')
            item_codeB = input('Enter the new item code')
            addPriceB = float(input('Enter the new price'))
            newServiceB = input('Enter the new service code')
            qty = int(input('Enter the new quantity'))

            service_found = False
            with open('Services.txt', "r") as services_file3:
                for line in services_file3:
                    code, _, priceA = line.strip().split(',')
                    if code == newServiceB:
                        oldPrice = int(priceA) * qty
                        service_found = True
                        break
            if not service_found:
                print("Error: Service code not found.")

            # Make sure the price is reasonable.
            if addPriceB >= oldPrice:
                print("Error: The price of the package exceeds or equals the price of the service.")
            else:
                with open('Packages.txt', 'a') as packages_file1:
                    packages_file1.write(f'\n{item_codeB},{newNameB},{qty},{addPriceB},{newServiceB}')
                print('The new package has been added.')

        # View/Update Products
        elif choice_product_management.lower() == 'e':
            with open("Products.txt", "r") as products_file:
                content = products_file.read()
                print(content)
                print()

                choice_e = input('To update a Product, enter the item code. '
                                 'Or enter 0 to go back to previous menu.\n')
                if choice_e == '0':
                    continue

                else:
                    with open("Products.txt", "r") as products_file1:
                        products = products_file1.readlines()
                        for line in products:
                            codeC, nameC, priceC, status = line.strip().split(',')
                            if codeC == choice_e.upper():
                                print(line.strip())
                                newPriceC = input("Enter the new price to update,"
                                                  "or press Enter to delete.")
                                if newPriceC:
                                    newStatus = input('Enter the new status: (Available/Unavailable)')  # Status
                                    if newStatus.lower() == 'available' or 'unavailable':
                                        products[products.index(line)] = (f'{codeC},{nameC},{newPriceC},'
                                                                          f'{newStatus.capitalize()}\n')
                                    else:
                                        print('The status is invalid.')
                                else:
                                    products.remove(line)
                                with open("Products.txt", "w") as products_file2:
                                    products_file2.writelines(products)
                                print('The product has updated successfully.')
                                break
                        else:
                            print("Error: No service found with that item code.")

        # Add new Product
        elif choice_product_management.lower() == 'f':
            nameC = input('Enter the new item name:')
            item_codeC = input('Enter the new item code:')
            priceC = input('Enter the new price:')
            statusC = input('Enter the new status:')
            if statusC.lower() == 'available':
                with open('Products.txt', 'a') as products_file1:
                    products_file1.write(f'\n{item_codeC},{nameC},{priceC},{statusC.capitalize()}')
                print('The new product has been added.')

        elif choice_product_management == 'g':
            mainMenu()
            choice_main_menu = input("Enter option:")
            continue
        else:
            print('Error: Invalid input. Please enter valid option.')

    # Sales management
    elif choice_main_menu == '2':
        print()
        print("a. Create order\n"
              "b. View order\n"
              "c. Create customer\n"
              "d. View customer\n"
              "e. Back to main menu")
        choice_sub2_menu = input("Enter your choice:")
        print()

        # Choice customer
        if choice_sub2_menu.lower() == 'a':
            customer_search = True
            while customer_search:
                customerName = input('Enter customer name (0 for main menu)\n')
                if customerName == '0':
                    mainMenu()
                    choice_main_menu = input("Enter option:")
                    break
                else:
                    with open('customer.txt', 'r') as customers_file:
                        for line in customers_file:
                            num, name = line.strip().split(',')
                            if customerName in name:
                                print(line.strip())

                    customerName1 = input('Enter number or 0 to search again')
                    if customerName1 == '0':
                        continue

                    # Create order
                    else:
                        continue_order = True
                        price_list = []
                        while continue_order:
                            print()
                            print("1.Use Service\n"
                                  "2.Buy Package\n"
                                  "3.Buy product\n"
                                  "4.Back to main menu")
                            choice_order = input("Enter option:")

                            # Back to main menu
                            if choice_order == '4':
                                break
                            else:

                                # Use Service
                                if choice_order == '1':
                                    print()
                                    with open('Services.txt', 'r') as services_files3:
                                        for line in services_files3:
                                            print(line.strip())
                                        print()
                                        choice_2a1 = input('Select the services')
                                        print()
                                        with open('oldCustomer.txt', 'r') as services_files4:
                                            services1 = services_files4.readlines()
                                        service_found1 = False
                                        for line in services1:
                                            index, name, packages1, item, num, services0 = line.split(',')

                                            # To be resolved: non-duplicable types of services owned by customers.
                                            # name == customerName1 and services0 == choice_2a1 can't be used.
                                            if customerName1 in line and choice_2a1.upper() in line:

                                                num1 = int(num)
                                                if num1 < 1:
                                                    print('You don\'t have enough services')
                                                else:
                                                    print(f'Customer has a Face Cleansing package: {num} left\n'
                                                          'Qty will be deducted automatically when order is complete')

                                                    # Deduct Qty
                                                    with open('ordersList.txt', 'a') as order1:
                                                        order1.write(f'\nServices:\t{item}\t{services0}\t$0(package)')

                                                    num1 -= 1
                                                    services1[services1.index(line)] = (f'{index},{name},{packages1},'
                                                                                        f'{item},{num1},{services0}')
                                                    with open('oldCustomer.txt', 'w') as oldCustomer_file:
                                                        oldCustomer_file.writelines(services1)
                                                    service_found1 = True

                                        if not service_found1:
                                            print('You don\'t have this services')

                                    # Ask customers if they want to continue ordering
                                    print()
                                    choice_2a12 = input('Do you want to continue ordering(Y), or complete order(N)')
                                    if choice_2a12.upper() == 'Y':
                                        continue

                                # Buy package
                                if choice_order == '2':
                                    print()
                                    print('Buy package')
                                    print()
                                    with open('Packages.txt', 'r') as packages_files3:
                                        for line in packages_files3:
                                            print(line.strip())

                                    choice_2a2 = input('Select the packages')
                                    with open('Packages.txt', 'r') as packages_files4:
                                        packages2 = packages_files4.readlines()
                                    for line in packages2:
                                        index, name, num, price, code = line.strip().split(',')
                                        if index == choice_2a2.upper():
                                            with open('ordersList.txt', 'a') as order2:
                                                order2.write(f'\nPackages:\t{name}\t{index}\t${price}')
                                            price1 = int(price)
                                            price_list.append(price1)

                                    choice_2a21 = input('Do you want to continue ordering(Y), or complete order(N)')
                                    if choice_2a21.upper() == 'Y':
                                        continue

                                # Buy product
                                if choice_order == '3':
                                    print('Buy product')
                                    print()
                                    with open('Products.txt', 'r') as products_file3:
                                        products3 = products_file3.readlines()

                                        # Put products listed in ascending
                                        price_sort = []
                                        for line in products3:
                                            index, name, price, status = line.strip().split(',')
                                            price1 = int(price)
                                            product = {'index': index, 'name': name, 'price': price1, 'status': status}
                                            price_sort.append(product)
                                    products_sort = sorted(price_sort, key=lambda product0: product0['price'])
                                    for product in products_sort:
                                        print(f'{product['index']}, {product['name']},'
                                              f'{product['price']}, {product['status']}')

                                    choice_2a3 = input('Select the packages')
                                    with open('Products.txt', 'r') as products_file3:
                                        products3 = products_file3.readlines()
                                    product_found = False
                                    for line in products3:
                                        index, name, price, status = line.strip().split(',')
                                        if choice_2a3.upper() in line:
                                            if status == 'Available':
                                                with open('ordersList.txt', 'a') as order3:
                                                    order3.write(f'\nProduct:\t{name}\t{index}\t${price}')
                                                price2 = int(price)
                                                price_list.append(price2)
                                            else:
                                                print('This product is invalid.')
                                            product_found = True
                                    if not product_found:
                                        print('Error: No product found with that item code.')

                                    choice_2a31 = input('Do you want to continue ordering(Y), or complete order(N)')
                                    if choice_2a31.upper() == 'Y':
                                        continue

                                # BONUS: Loyalty points
                                total_price = sum(price_list)
                                with open('customer_information.txt', 'r') as information:
                                    infor = information.readlines()
                                    for line in infor:
                                        num, name, gender, birthday, contact, point = line.strip().split(',')
                                        if num == customerName1:
                                            use_point = int(input(f'You have {point} points(1 points = $1).\n'
                                                                  f'How many do you want to use?'))
                                            points = int(point)
                                            if use_point <= points:
                                                total_price -= use_point
                                                points -= use_point
                                                infor[infor.index(line)] = (f'{num},{name},{gender},{birthday},'
                                                                            f'{contact},{points}\n')
                                                with open('customer_information.txt', 'w') as information1:
                                                    information1.writelines(infor)
                                            else:
                                                print('You don\'t have enough points.')

                                # Order Summary
                                print('---------\tOrder Summary\t---------')
                                with open('ordersList.txt', 'r') as orderList:
                                    for line in orderList:
                                        print(line.strip())
                                print()
                                with open('customer.txt', 'r') as customers_file:
                                    customer = customers_file.readlines()
                                    for line in customer:
                                        num, name = line.strip().split(',')
                                        if num == customerName1:
                                            customerName2 = name
                                print(f'Total\t\t\t\t\t${total_price}(Discount{use_point})'
                                      f'\nCustomer\'s name:{customerName2}'
                                      '\n-------------------------')
                                confirm = input('Enter 1 to confirm, 0 to cancel:')

                                # Restore the status before order creation
                                if confirm == '0':
                                    with open('ordersList.txt', 'w') as orderList:
                                        orderList.write('')
                                    with open('customer_information.txt', 'r') as customerInfo:
                                        infor = customerInfo.readlines()
                                        for line in infor:
                                            num, name, gender, birthday, contact, point = line.strip().split(',')
                                            if name == customerName2:
                                                points2 = int(point) + use_point
                                                infor[infor.index(line)] = (f'{num},{name},{gender},{birthday},'
                                                                            f'{contact},{points2}\n')
                                    with open('customer_information.txt', 'w') as customerInfo:
                                        customerInfo.writelines(infor)
                                    with open('oldCustomer.txt', 'r') as oldCustomer_file:
                                        old_customer = oldCustomer_file.readlines()
                                        for line in old_customer:
                                            index, name, packages1, item, num, services0 = line.split(',')
                                            if name == customerName2:
                                                number = int(num)
                                                number += 1
                                                old_customer[old_customer.index(line)] = (f'{index},{name},{packages1}'
                                                                                          f'{item},{number},{services0}\n')
                                    with open('oldCustomer.txt', 'w') as oldCustomer_file:
                                        oldCustomer_file.writelines(old_customer)

                                # Get points
                                if confirm == '1':
                                    points = total_price // 10
                                    with open('customer_information.txt', 'r') as information:
                                        infor = information.readlines()
                                        for line in infor:
                                            num, name, gender, birthday, contact, point = line.strip().split(',')
                                            points1 = int(point)
                                            points1 += points
                                            if customerName2 in name:
                                                infor[infor.index(line)] = (f'{num},{name},{gender},{birthday},'
                                                                            f'{contact},{points1}\n')
                                                with open('customer_information.txt', 'w') as information1:
                                                    information1.writelines(infor)
                                                with open('ordersList.txt', 'a') as orderList:
                                                    orderList.write(f'Total\t\t\t\t\t'f'${total_price}(Discount{use_point})'
                                                                    f'\nCustomer\'s name:{customerName2}'
                                                                    f'\n-------------------------')
                            break
                break

        # View order
        if choice_sub2_menu.lower() == 'b':
            print('---------\tOrder Summary\t---------')
            with open('ordersList.txt', 'r') as orderList:
                for line in orderList:
                    print(line.strip())
            print()

        # Creat customer
        if choice_sub2_menu.lower() == 'c':
            num2 = input('Enter customer number:')
            Customer_name = input("Enter customer name:")
            Gender = input("Enter customer gender:")
            Birthday = input("Enter customer birthday:")
            Contact = input("Enter customer contact:")
            if num2 and Customer_name and Gender and Birthday and Contact:  # Ensure the fields are not blank.
                with open('customer_information.txt', 'a') as customerInfo:
                    customerInfo.write(f'{num2},{Customer_name},{Gender},{Birthday},{Contact},0\n')
                with open('customer.txt', 'a') as customers_file1:
                    customers_file1.write(f'\n{num2},{Customer_name}')
                print('Create a new customer successfully!')
            else:
                print('Error: There are blank in the input.')

        # View customer
        if choice_sub2_menu.lower() == 'd':
            with open('customer.txt', 'r') as customers_file2:
                for line in customers_file2:
                    print(line.strip())

            choice_2d = input('Enter number to view customer, or 0 to return to main menu')
            if choice_2d == '0':
                continue

            with open('customer_information.txt', 'r') as information:
                infor = information.readlines()
                for line in infor:
                    num, name, gender, birthday, contact, point = line.strip().split(',')
                    if num == choice_2d:
                        print()
                        print(f'Name:{name}'
                              f'\nGender:{gender}'
                              f'\nBirthday:{birthday}'
                              f'\nContact:{contact}'
                              f'\nPackages:')

            # Add new customer in oldCustomer.txt
            with open('oldCustomer.txt', 'r') as oldPackages:
                old = oldPackages.readlines()
                for line in old:
                    index, _, _, name, num, _ = line.strip().split(',')
                    if index == choice_2d:
                        print(f'\n{name}:{num}')

            # Edit customer details
            print()
            new_name = input('Edit customer name.')
            new_gender = input('Edit customer gender.')
            new_birthday = input('Edit customer birthday.')
            new_contact = input('Edit customer contact.')
            with open('customer_information.txt', 'r') as customerInfo:
                infor = customerInfo.readlines()
                for line in infor:
                    num, name, gender, birthday, contact, point = line.strip().split(',')
                    if num == choice_2d:
                        infor[infor.index(line)] = f'{num},{new_name},{new_gender},{new_birthday},{new_contact},{point}\n'
            with open('customer_information.txt', 'w') as information:
                information.writelines(infor)
            with open('oldCustomer.txt', 'r') as customers_file:
                customer = customers_file.readlines()
                for line in customer:
                    num, name = line.strip().split(',')
                    if num == choice_2d:
                        customer[customer.index(line)] = f'{num},{new_name}\n'
            with open('oldCustomer.txt', 'w') as customers_file:
                customers_file.writelines(customer)

        # Back to main menu
        if choice_sub2_menu.lower() == 'e':
            mainMenu()
            choice_main_menu = input("Enter option:")
            continue

    # Exit the program
    elif choice_main_menu == '0':
        break

    # Return error
    else:
        print('Error: Invalid input. Please enter 1, 2 or 0.')

    print()
    mainMenu()
    choice_main_menu = input("Enter option:")
    continue
