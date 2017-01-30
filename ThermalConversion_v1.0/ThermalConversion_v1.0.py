while True:
        format_selection = input("Would you like your temperature converted to Fahrenheit or Celsius?(F or C) ").lower()
        
        if format_selection and format_selection == "f" or format_selection == "fahrenheit":
                import CtoF
                CtoF
                again = input("Would you like another temperature converted?" ).lower() 
                if again and again == "y" or again == "yes":
                        continue
                elif again and again == "n" or again == "no":
                        print("Thanks for using ThermalConversion v1.0!!")
                        break
                else:
                        print("I will assume you meant yes! :) ")
                        continue
        elif format_selection and format_selection == "c" or format_selection == "celsius":
                import FtoC
                FtoC
                again1 = input("Would you like another temperature converted?" ).lower()
                if again1 and again1 == "y" or again1 == "yes":
                        continue
                elif again1 and again1 == "n" or again1 == "no":
                        print("Thanks for using ThermalConversion v1.0!!")
                        break
                else:
                        print("I will assume you meant yes! :) ")
                        continue
        else:
                print("I did not understand your input. Please type F, Fahrenheit, C, or Celsius!(Not Case Sensitive)")
                continue	
