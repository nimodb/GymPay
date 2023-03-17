enter = input("Enter Payment:\n(ex. r63-n351-a69)\n")
all_payment_list = enter.split()

reza_payment = list()
nima_payment = list()
amir_payment = list()

for name_pay in all_payment_list:
    if name_pay.startswith("r"):
        r_pay = int(name_pay.replace("r", ""))
        reza_payment.append(r_pay)
    elif name_pay.startswith("n"):
        n_pay = int(name_pay.replace("n", ""))
        nima_payment.append(n_pay)
    elif name_pay.startswith("a"):
        a_pay = int(name_pay.replace("a", ""))
        amir_payment.append(a_pay)
    else:
        print(f"OOoOOopsS. {name_pay} is Wrong. Try Again!!!")

totalPaymentReza = sum(reza_payment)
totalPaymentNima = sum(nima_payment)
totalPaymentAmir = sum(amir_payment)
payment_list = {
    "Nima": totalPaymentNima,
    "Reza": totalPaymentReza,
    "Amir": totalPaymentAmir,
}
totalPayment = sum(payment_list.values())
person_payment = totalPayment/3

for name, pay in payment_list.items():
    if name == "Nima":
        nima_sum = totalPaymentNima - person_payment
    elif name == "Reza":
        reza_sum = totalPaymentReza - person_payment
    elif name == "Amir":
        amir_sum = totalPaymentAmir - person_payment
    print(f"{name} Payment: {pay}")


print(amir_sum, nima_sum, reza_sum)
print(f"Total Payment: {totalPayment}")
print(f"Person Payment: {person_payment}")





