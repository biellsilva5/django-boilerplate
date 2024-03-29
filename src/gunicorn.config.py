from utils.tracking import instrument_app

def post_fork(server, worker):
    server.log.info("Worker spawned (pid: %s)", worker.pid)

    instrument_app()