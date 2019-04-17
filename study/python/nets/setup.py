from cx_Freeze import setup, Executable

setup(
    name = "nets",
    version = "0.1",
    description = "Creates ip routes for pochta Ka Gilat migration for vrf russianpost_Telemat",
    executables = [Executable("nets.py")]
)