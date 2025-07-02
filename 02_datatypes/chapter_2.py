spice_mix = set()

print(f"Intial spice mix id : {id(spice_mix)}")
spice_mix.add("cumin")
spice_mix.add("coriander")
print(f"Updated spice mix id : {id(spice_mix)}")

# both id are same, so we can say that sets are mutable (Sets are mutable)
