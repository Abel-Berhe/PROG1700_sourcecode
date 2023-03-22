#Don't forget to rename this file after copying the template
#for a new program!
"""
Student Name:   Abel Berhe 
Program Title:  Online Store
Description:    This program will calculate how much tax will apply based on countries and provinces
"""
# pseudocode 
# 1.program start 
# 2.Create variables Country, total order, total order with tax, and total order 
# 3. Prompt user to enter country and the total order 
# 4. If the user is from canada then calculate the tax for the totalorder based on the province the user in since 
# the tax rate is different for some provinces 
# 5.Display the output using nested IF and ELIFs to the proper tax rate for the provinces 
# and do not apply tax if the user is not from canada, just display the total order.
# 6. program end

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!

    #prompting the user to enter country and the total order
    country = input("Enter your country ? :")
    totalOrder = float(input("Enter the your order total ? :"))

    #Creating variables for the tax rate
    ABTaxRate = 0.05
    ONNBNSTaxRate = 0.15
    remainingProvincesTaxRate = 0.11
     
    #Checking if the user is from canada 
    if country.lower()=="canada":
        #If the user is from canada then will prompt the user to enter the province user is from
        province = input("Enter your province ? :")

        #Checking the province, and calculating the tax based on the province, and then displaying the output
        if province.lower()=="alberta":
            totalOrderWithTax = totalOrder +(totalOrder * ABTaxRate) 
            print("your total is (including 5%  TAX) ${:.2f}".format(totalOrderWithTax))
        #Checking the provinces, and calculating the tax based on the provinces, and then displaying the output    
        elif province.lower()=="ontario" or province.lower()=="new brunswick" or province.lower()=="nova scotia":
            totalOrderWithTax = totalOrder +(totalOrder * ONNBNSTaxRate) 
            print("your total is (including 15%  TAX) ${:.2f}".format(totalOrderWithTax))
        #calculating the tax based on the remaining provinces, and then displaying the output    
        else:
            totalOrderWithTax = totalOrder +(totalOrder * remainingProvincesTaxRate) 
            print("your total is(including 11%  TAX) ${:.2f}".format(totalOrderWithTax))
    #Displaying the total order with out tax, if the user is not from canada                    
    else:
        print("your total is (no tax applied) ${:.2f}".format(totalOrder))


#made change to this file####################################################
    #Your code ends on the line above

#Do not change any of the code below!
if __name__ == "__main__":
    main()
