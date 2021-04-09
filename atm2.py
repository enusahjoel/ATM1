while True:
    u_name = input(" Enter ID:\n ")
    pin = input(" Enter pin:\n ")
    if u_name != "joel" or pin != '3733':
        print ("invalid ID or pin")
        continue
    else:
        while True:

            query1 = input(" 1. WITHDRAWAL \n 2. AIRTIME \n 3. TRANSFER \n ")
            if query1 == '1':
                while True: #withdraw code

                    w_draw = input (" 1. CURRENT \n 2. SAVINGS")
                    if w_draw == '1':
                        while True:
                            cash = input (' 1.$1000 \n 2.$5000 \n 3.$10,000 \n 4.$20,000 \n 5.$50,000 \n 6.$100,000 \n 7.$500,000 \n 8. OTHER \n 0. BACK ')
                            if cash == '1':
                                print (' HERE IS YOUR $1,000 ')
                                break
                            elif cash == '2':
                                print (' HERE IS YOUR $5,000')
                                break
                            elif cash == '3':
                                print (' HERE IS YOUR $10,000')
                                break
                            elif cash == '4':
                                print (' HERE IS YOUR $20,000')
                                break
                            elif cash == '5':
                                print (' HERE IS YOUR $50,000')
                                break
                            elif cash == '6':
                                print (' HERE IS YOUR $100,000')
                                break
                            elif cash == '7':
                                print (' HERE IS YOUR $500,000')
                                break
                            elif cash == '8':
                                x = input('HOW MUCH DO YOU WANT TO WITHDRAW? ')
                                print (' HERE IS YOUR', x)
                                break
                            else:
                                print('WRONG INPUT')
                                continue
                    if cash == '0':
                        continue

                        break
                    elif w_draw == '2':
                        while True:
                            cash = input (' 1.$1000 \n 2.$5000 \n 3.$10,000 \n 4.$20,000 \n 5.$50,000 \n 6.$100,000 \n 7.$500,000 \n 8. OTHER ')
                            if cash == '1':
                                print (' HERE IS YOUR $1,000 ')
                                break

                            elif cash == '2':
                                print (' HERE IS YOUR $5,000')
                                break

                            elif cash == '3':
                                print (' HERE IS YOUR $10,000')
                                break

                            elif cash == '4':
                                print (' HERE IS YOUR $20,000')
                                break

                            elif cash == '5':
                                print (' HERE IS YOUR $50,000')
                                break

                            elif cash == '6':
                                print (' HERE IS YOUR $100,000')
                                break

                            elif cash == '7':
                                print (' HERE IS YOUR $500,000')
                                break

                            elif cash == '8':
                                x = input('HOW MUCH DO YOU WANT TO WITHDRAW? ')
                                print (' HERE IS YOUR', x)
                                break
                            else:
                                print('WRONG INPUT')
                                continue
                        break
                    else:
                        print('INVALID INPUT')

                        continue #withdraw code end
            elif query1 == '2':
                while True: #Airtime code
                    y = input('ENTER DESTINATION NUMBER: \n')
                    if len(y) != 11:
                        print ('INVALID NUMBER(number should be 11 digits)')
                    else:
                        z = input('ENTER AMOUNT: \n')
                        print("YOU HAVE SUCCEFULLY SENT", z, 'TO', y)
                        break
                        #airtime code end
            elif query1 == '3':
                while True: #transfer vode
                    a = input("SELECT BANK \n 1. ACCESS BANK \n 2. GTB \n 3. FIRST BANK \n 4. ZENITH BANK \n 5. UBA \n 6. ECO BANK \n 7. ZENITH BANK \n 8. POLARIS BANK \n 9. KEYSTONE BANK \n")
                    b = input('ENTER ACCOUNT NUMBER(10 digits): \n ')
                    if len(b) < 10:
                        print('too short')
                        continue
                    elif len(b) > 10:
                        print('too long')
                        continue
                    else:
                        c = input('ENTER AMOUNT: \n')
                        d = input(' ENTER PIN \n' )
                        if d != pin:
                            print('INVALID PIN')
                            continue
                        else:
                            print('YOU HAVE SUCCESSFULLY TRANSFERED', c, 'TO THE ACCOUNT NUMBER', b)
                            break

                break

            break #major
    prompt= input('WILL YOU LIKE TO PERFORM ANOTHER TRANSACTION? (Y/N) \n ')
    if prompt == 'Y':
        continue
    else:
        print('PLEASE TAKE YOUR CARD. GOODBYE')
        break
