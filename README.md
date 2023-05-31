# dll2exe

dll2exe is a simple tool for converting DLLs to EXEs. It provides the option to select a specific exported function as the new entry point. This tool is particularly useful when you prefer not to debug a DLL file or when you want to treat it as a regular executable file with a custom entry point in an exported function.

# Install

You can quickly install dll2exe using pip:

`pip install dll2exe-cli`


# Usage:

dll2exe offers several options for conversion. Here are a few examples:

```
$ dll2exe -h
usage: Convert a DLL into a EXE choosing any exported function as your entrypoint

positional arguments:
  PE

options:
  -h, --help            show this help message and exit
  --output OUTPUT, -o OUTPUT
                        Output filename, default: filename.exe
  --entrypoint ENTRYPOINT, -e ENTRYPOINT
                        Exported function name to be used as new entrypoint, default: DllEntryPoint
  --list-exports        List exported functions
```

## Examples

### Get the list of exports

To obtain the list of exports from a DLL, use the following command:

`dll2exe randomfile.dll --list-exports`

### Convert to EXE using the original DLL entry point

To convert a DLL to an EXE using the original DLL entry point, execute the following command:

`dll2exe randomfile.dll -o newrandom.exe`

### Convert to EXE using a custom DLL exported function as entry point

If you want to convert a DLL to an EXE and specify a custom DLL exported function as the entry point, use the following command:

`dll2exe randomfile.dll --entrypoint SomeExportedFunction`

## Caveats

Please note that this tool does not handle the arguments of exported functions or the DLL entry point. Therefore, you may experience crashes if the code expects specific arguments.


Thanks 
