from solcx import compile_standard, install_solc
import json

with open("./Donations.sol", "r") as file:
  donations_file = file.read()

install_solc("0.6.0")
compiled_sol = compile_standard(
  {
    "language": "Solidity",
    "sources": {"Donations.sol": {"content": donations_file}},
    "settings": {
      "outputSelection": {
        "*": {
          "*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]
        }
      }
    }
  },
  solc_version="0.6.0"
)

with open("compile_code.json", "w") as file:
  json.dump(compiled_sol, file)
