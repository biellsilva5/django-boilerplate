def initialize_debugger():
    from setup.settings import DEBUG
    if not DEBUG:
        return False
    
    import debugpy
    import os
    import sys

    # RUN_MAIN envvar is set by the reloader to indicate that this is the 
    # actual thread running Django. This code is in the parent process and
    # initializes the debugger
    if not os.getenv("RUN_MAIN"):
        debugpy.listen(("0.0.0.0", 5678))
        sys.stdout.write("Start the VS Code debugger now\n")