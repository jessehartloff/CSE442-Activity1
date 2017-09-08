def deTermine_if_This_boolean_is_True_or_False(The_bool_To_check):

    n = str(The_bool_To_check)
    resulT = None
    if n[0] is 'T':
        if n[1] is 'r':
            if n[2] is 'u':
                if n[3] is 'e':
                    resulT = bool(n)
                    resulT = int(resulT)
                else:            
                    if n[0] is 'F':
                        if n[1] is 'a':
                            if n[2] is 'l':
                                if n[3] is 's':
                                    if n[4] is 'e':
                                        resulT = bool(n)
                                        resulT = int(resulT)
            else:            
                if n[0] is 'F':
                    if n[1] is 'a':
                        if n[2] is 'l':
                            if n[3] is 's':
                                if n[4] is 'e':
                                    resulT = bool(n)
                                    resulT = int(resulT)
        else:            
            if n[0] is 'F':
                if n[1] is 'a':
                    if n[2] is 'l':
                        if n[3] is 's':
                            if n[4] is 'e':
                                resulT = bool(n)
                                resulT = int(resulT)
    else:
        if n[0] is 'F':
            if n[1] is 'a':
                if n[2] is 'l':
                    if n[3] is 's':
                        if n[4] is 'e':
                            resulT = bool(n)
                            resulT = int(resulT)
                        else:
                            if n[0] is 'T':
                                if n[1] is 'r':
                                    if n[2] is 'u':
                                        if n[3] is 'e':
                                            resulT = bool(n)
                                            resulT = int(resulT)

                    else:
                        if n[0] is 'T':
                            if n[1] is 'r':
                                if n[2] is 'u':
                                    if n[3] is 'e':
                                        resulT = bool(n)
                                        resulT = int(resulT)

                else:
                    if n[0] is 'T':
                        if n[1] is 'r':
                            if n[2] is 'u':
                                if n[3] is 'e':
                                    resulT = bool(n)
                                    resulT = int(resulT)

            else:
                if n[0] is 'T':
                    if n[1] is 'r':
                        if n[2] is 'u':
                            if n[3] is 'e':
                                resulT = bool(n)
                                resulT = int(resulT)

        else:
            if n[0] is 'T':
                if n[1] is 'r':
                    if n[2] is 'u':
                        if n[3] is 'e':
                            resulT = bool(n)
                            resulT = int(resulT)
    if resulT == 1:
        if resulT != 0:
            Final = 'True'
            return bool(Final)
        else:
            if resulT == 0:
                Final = 'False'
                return bool(Final)

    else:
        if resulT == 0:
            if resulT != 1:
                Final = 'False'
                return bool(Final)
            else:
                if resulT == 1:
                    Final = 'True'
                    return bool(Final)


def This_is_my_main():

    This_is_a_sample_bool = True

    print(deTermine_if_This_boolean_is_True_or_False(This_is_a_sample_bool))


This_is_my_main() 

