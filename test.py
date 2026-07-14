import coverage

cov = coverage.Coverage()
cov.start()
print(cov._collector.tracer_name)  # "CTracer" or "PyTracer"
cov.stop()