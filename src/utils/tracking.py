
from opentelemetry.instrumentation.django import DjangoInstrumentor
from opentelemetry.instrumentation.psycopg2 import Psycopg2Instrumentor
from opentelemetry.instrumentation.logging import LoggingInstrumentor

from opentelemetry import trace
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor, SimpleSpanProcessor, ConsoleSpanExporter

from setup.settings import DEBUG
import logging

def instrument_app():
    
    logger = logging.getLogger(__name__)
    resource = Resource({
        "service.name": "app-service"
    })
    provider = TracerProvider(resource=resource)
    trace.set_tracer_provider(provider)
    
    #trace.get_tracer_provider().add_span_processor(SimpleSpanProcessor(ConsoleSpanExporter()))
    trace.get_tracer_provider().add_span_processor(BatchSpanProcessor(JaegerExporter(agent_host_name='jaeger-all',
    agent_port=6831,)))
    
    LoggingInstrumentor().instrument(trace_provider=provider, set_logging_format=True)
    DjangoInstrumentor().instrument(trace_provider=provider, is_sql_commentor_enabled=True)
    Psycopg2Instrumentor().instrument(trace_provider=provider, skip_dep_check=True, enable_commenter=True)
    logger.info('App is instrumented')
    