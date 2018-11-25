from vm_monitoring import VM
opt = raw_input("1.show monitoring details\n2.insert new vm details\n3.quit")
if opt=="1":
	pass
elif opt=="2":
	user_name=raw_input("Enter username:")
    pwd=raw_input("Enter password:")
    ip=raw_input("enter an ip:")
    vm = VM(user_name,password,ip)
    vm.insert()