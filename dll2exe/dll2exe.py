import lief
import argparse
import sys

DLL_BIT = 0x2000

def print_exports(pe: lief.PE.Binary):
    print(f"Exports: ")
    for export in pe.exported_functions:
        print(f"\t- {export.name}")

def log_error(msg: str):
    print(f"[-] {msg} [-]")

def log(msg: str):
    print(f"[+] {msg} [+]") 

def main():
    parser = argparse.ArgumentParser("dll2exe", "Convert a DLL into a EXE choosing any exported function as your entrypoint")
    parser.add_argument("PE")
    parser.add_argument("--output", "-o", help="Output filename, default: filename.exe")
    parser.add_argument("--entrypoint", "-e", help="Exported function name to be used as new entrypoint, default: DllEntryPoint")
    parser.add_argument("--list-exports", help="List exported functions", action='store_true')

    args = parser.parse_args()

    target: str = args.PE
    log(f"Loading {target}...")

    pe: lief.PE.Binary = lief.parse(target)

    if not pe or pe.format != lief.EXE_FORMATS.PE:
        log_error(f"{target} is not a PE file!")
        sys.exit(1)

    if args.list_exports:
        print_exports(pe)
        sys.exit(0)

    if (pe.header.characteristics.value & DLL_BIT) == 0:
        log_error(f"{target} is not a DLL file!")
        sys.exit(1)

    output_name = args.output

    # Set the output name
    if not output_name:
        if target.endswith(".dll"):
            output_name = target[:-4] + ".exe"
        else:
            output_name = target + ".bin"

    # Remove the DLL bit
    pe.header.remove_characteristic(pe.header.characteristics.DLL)
    log("Converted to EXE!")

    # Replace the entrypoint, if needed
    if args.entrypoint:
        log(f"Replacing entrypoint to {args.entrypoint}")
        found = False

        for exported_function in pe.exported_functions:
            if exported_function.name == args.entrypoint:
                exported_rva = exported_function.address
                log(f"New entrypoint: {hex(exported_rva)}")
                pe.optional_header.addressof_entrypoint = exported_rva
                found = True
                break
        
        if not found:
            log_error(f"Export {args.entrypoint} does not exist!")
            sys.exit(1)

    log(f"Saving as {output_name}")
    pe.write(output_name)
    log(f"Saved!")
    
if __name__ == '__main__':
    main()