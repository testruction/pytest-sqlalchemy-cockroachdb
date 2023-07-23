from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.resources import Resource

from opentelemetry.sdk.trace.export import ConsoleSpanExporter, SimpleSpanProcessor, BatchSpanProcessor

from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter

from opentelemetry.instrumentation.psycopg2 import Psycopg2Instrumentor
from opentelemetry.instrumentation.sqlalchemy import SQLAlchemyInstrumentor

def init_tracer(args):
    """
    Tracing configuration using OpenTelemetry
    """
    resource = Resource.create(attributes={"service.namespace": "io.testruction",
                                           "service.name": "fakenamesservice"})

    provider = TracerProvider()

    otlp_exporter = OTLPSpanExporter()
    otlp_processor = BatchSpanProcessor(otlp_exporter)
    provider.add_span_processor(otlp_processor)

    trace.set_tracer_provider(provider)

    Psycopg2Instrumentor().instrument(enable_commenter=True, skip_dep_check=True)
