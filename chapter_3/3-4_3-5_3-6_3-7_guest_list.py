invite_list = ["Anna","John","Chris","Andrew","Alex"]

print(f"Hey {invite_list[0]}! I'm inviting you to have dinner with me.")
print(f"Hey {invite_list[1]}! I'm inviting you to have dinner with me.")
print(f"Hey {invite_list[2]}! I'm inviting you to have dinner with me.")
print(f"Hey {invite_list[3]}! I'm inviting you to have dinner with me.")
print(f"Hey {invite_list[4]}! I'm inviting you to have dinner with me.")

# ---------------------

invite_list[3] = "Boob"

print(f"Hey {invite_list[0]}! I'm inviting you to have dinner with me.")
print(f"Hey {invite_list[1]}! I'm inviting you to have dinner with me.")
print(f"Hey {invite_list[2]}! I'm inviting you to have dinner with me.")
print(f"Hey {invite_list[3]}! I'm inviting you to have dinner with me.")
print(f"Hey {invite_list[4]}! I'm inviting you to have dinner with me.")

# ---------------------

invite_list.insert(0,"Alison")
invite_list.insert(3,"Marry")
invite_list.append("Leo")

print(f"Hey {invite_list[0]}! I'm inviting you to have dinner with me.")
print(f"Hey {invite_list[1]}! I'm inviting you to have dinner with me.")
print(f"Hey {invite_list[2]}! I'm inviting you to have dinner with me.")
print(f"Hey {invite_list[3]}! I'm inviting you to have dinner with me.")
print(f"Hey {invite_list[4]}! I'm inviting you to have dinner with me.")
print(f"Hey {invite_list[5]}! I'm inviting you to have dinner with me.")
print(f"Hey {invite_list[6]}! I'm inviting you to have dinner with me.")
print(f"Hey {invite_list[7]}! I'm inviting you to have dinner with me.")

# ---------------------

person = invite_list.pop()
print(f"{person} sorry for that!")

person = invite_list.pop()
print(f"{person} sorry for that!")

person = invite_list.pop()
print(f"{person} sorry for that!")

person = invite_list.pop()
print(f"{person} sorry for that!")

person = invite_list.pop()
print(f"{person} sorry for that!")

person = invite_list.pop()
print(f"{person} sorry for that!")


print(f"Hey {invite_list[0]}! You are still on a list.")
print(f"Hey {invite_list[1]}! You are still on a list.")

del invite_list[1]
del invite_list[0]

print(invite_list)