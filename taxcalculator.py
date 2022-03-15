"""
Program to compute tax based on the slabs
Example program by Prashant Joshi

Note: Tax computation is done keeping the slabs in mind

"""

# function to compute the tax
def computeTax(taxableincome):

    if (taxableincome <= firstslab):
        totaltax = 0
        print("\nDebug: No Tax")
    # tax only the amount in the slab
    if (taxableincome > firstslab and taxableincome <= secondslab):
        totaltax = (taxableincome-500000) * taxslab1
        if (debug == 1):
            print("\nDebug: Slab 1")

    if (taxableincome > secondslab):
        tax1 = (taxableincome - secondslab) * taxslab2
        tax2 = (firstslab) * taxslab1
        totaltax = tax1 + tax2
        if (debug == 1):
            print("\nDebug: Big slab")

    return totaltax

firstslab=500000
secondslab=1000000

more=1
debug=1
while (more==1):

    # initialise the rebates and slab rates
    rebaterate = 20/100
    taxslab1 = 20/100
    taxslab2 = 30/100

    # get the input from the user
    income         = int(input('Enter the income                    : '))
    incomeother    = int(input('Enter the income from other sources : '))
    incomeinterest = int(input('Enter the income from interest      : '))

    rebate = incomeinterest * rebaterate
    taxableincome = income + incomeother + rebate
    print("Taxable income:", taxableincome)

    computedtax = computeTax(taxableincome)

    # Print the tax on the console
    print("\n Total tax :" + str(computedtax))

    # continue if more to compute
    more=int(input('Got more data to compute? :'))

# End of program