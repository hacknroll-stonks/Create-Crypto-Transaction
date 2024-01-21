from Sign_Contract import signContract
from Recieve_Contract import recieveContract
data = signContract("0xb636A68F834B4D75aF9EDC5FB0138bB4758eD293", 0.0001, privateKey="c60eff0de750d9a304e3dc1f2bc82d18c59111795696c7ba170d7abb90b15930")
recieveContract(data)
