def update_order():
    chai_type = "Elaichi"
    def kitchen():
        nonlocal chai_type  # nonlocal inside to inside function 
        chai_type = "Kesar"
        print(f"After kitchen update: ",chai_type)
    kitchen()
    
update_order()        
        
        