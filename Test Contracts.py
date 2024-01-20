from Sign_Contract import signContract
from Recieve_Contract import recieveContract
data = signContract("0xb636A68F834B4D75aF9EDC5FB0138bB4758eD293", 0.00001, privateKey="FFFFFFFFFFFFFFF")
recieveContract(data)
