#constants
ONE_LITTER_CONTAINER_REFUND = .10
MORE_THAN_ONE_LITTER_CONTAINER_REFUND = .25

#input
print("Enter the number of plastic containers of one liter or less:")
oneLiterContainers: int = int(input())
print ("Enter the size of your plastic containers of more than one liter:")
moreThanOneLiterContaniers: int = int(input())

#calculations
refundForOneLiterContainers: float = oneLiterContainers * ONE_LITTER_CONTAINER_REFUND
refundForMoreThanOneLiterContainers:float = moreThanOneLiterContaniers * MORE_THAN_ONE_LITTER_CONTAINER_REFUND
totalRefund: float = refundForOneLiterContainers + refundForMoreThanOneLiterContainers

#output
print("Refund amount : $%.2f" %totalRefund)