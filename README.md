# GRPC Python Calculator Example

This repository contains a minimal gRPC example in Python that exposes a `Calculator` service with a `SquareRoot` RPC. The proto definition is in `protofiles/calc.proto` and the generated Python modules live in `protofiles/`.

## Prerequisites

- Python 3.8+ (this repo was tested with Python 3.10)
- pip
- Optional: virtualenv or `venv` for an isolated environment

## Recommended setup (one-time)

1. Create and activate a virtual environment (optional but recommended):

```bash
cd /Users/code2aum/Desktop/grpc/GRPC
python3 -m venv .venv
source .venv/bin/activate
```

2. Install required packages:

```bash
python3 -m pip install --upgrade pip
python3 -m pip install grpcio grpcio-tools
```

Or install from the included `requirements.txt` (if present):

```bash
python3 -m pip install -r requirements.txt
```

## Generate the protobuf Python files

If you change `protofiles/calc.proto` or need to (re)generate the Python modules, run the following from the `GRPC` directory:

```bash
cd /Users/code2aum/Desktop/grpc/GRPC
python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. protofiles/calc.proto
```

This will produce `protofiles/calc_pb2.py` and `protofiles/calc_pb2_grpc.py`.

Notes:
- The command uses `-I.` so imports inside the `.proto` resolve relative to the `GRPC` directory.
- By default this writes generated files into the `protofiles/` directory. If you prefer a different package, change the `--python_out` and `--grpc_python_out` directories and update imports in `server.py` and `client.py` accordingly.

## Run the server and client

1. Start the server (uses port `50051` so no root privileges required):

```bash
cd /Users/code2aum/Desktop/grpc/GRPC
python3 server.py
```

2. In another terminal, run the client:

```bash
cd /Users/code2aum/Desktop/grpc/GRPC
python3 client.py
```

Expected output from the client (for input value 16):

```
4.0
```

## Files changed / important notes

- `protofiles/calc.proto` – gRPC service definition.
- `protofiles/calc_pb2.py`, `protofiles/calc_pb2_grpc.py` – generated files (may be regenerated with the command above).
- `server.py`/`client.py` were updated to import the generated modules from the `protofiles` package and to use port `50051`.

If you prefer to commit generated code, remove the `protofiles/*_pb2.py` and `protofiles/*_pb2_grpc.py` entries from `.gitignore`.

## Optional: generate into a separate package

If you prefer generated modules to live under a separate package (for example `grpc_generated_files`), create that folder and an `__init__.py`, then run:

```bash
mkdir -p grpc_generated_files
touch grpc_generated_files/__init__.py
python3 -m grpc_tools.protoc -I. --python_out=grpc_generated_files --grpc_python_out=grpc_generated_files protofiles/calc.proto
```

Then update imports in `server.py` and `client.py` to import from `grpc_generated_files`.

## Troubleshooting

- `ImportError: No module named 'calc_pb2'`: make sure you generated the protobuf files and that the directory containing them has an `__init__.py` if you import as a package (this repo uses `protofiles/__init__.py`).
- `PermissionError` on port 80: the server originally used port 80; the code has been updated to use `50051` to avoid needing root.
- If your editor/linter shows unresolved imports before generating code, that's expected — generate the files then reload the editor.

## Development notes

- To run quickly without installing packages globally, use the venv shown above.
- To re-run tests or manual checks: start `server.py` and run `client.py` in another terminal.

-- End of README
