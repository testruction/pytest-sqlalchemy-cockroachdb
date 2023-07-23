# -*- coding: utf-8 -*-
import os
import argparse

from sqlalchemy.engine import URL

from fakenamesservice.utils.logging import init_logger
from fakenamesservice.utils.telemetry import init_tracer

# CLI arguments composition
parser = argparse.ArgumentParser()
parser.add_argument('--debug',
                    help='Enable debug logging',
                    action='store_true')
parser.add_argument('--disable-tracing',
                    help="Disable OpenTelemetry tracing",
                    action="store_true")
parser.add_argument('--disable-logging',
                    help="Disable logging",
                    action="store_true")
parser.add_argument('--host',
                    type=str,
                    help='Hostname, fully qualified name or IP address',
                    default=os.environ.get('COCKROACH_HOST',
                                           default='localhost'))
parser.add_argument('--port',
                    type=int,
                    help='Listening port',
                    default=os.environ.get('COCKROACH_PORT',
                                           default=26257))
parser.add_argument('--username',
                    type=str,
                    help='Database user login name',
                    default=os.environ.get('COCKROACH_USER',
                                           default=None))
parser.add_argument('--password',
                    type=str,
                    help='Database user login password',
                    default=os.environ.get('COCKROACH_PASSWORD',
                                           default=None))
parser.add_argument('--database',
                    type=str,
                    help='Name of the database',
                    default=os.environ.get('COCKROACH_DB',
                                           default='postgres'))
args, unknown = parser.parse_known_args()

# Initialize logging and telemetry
if args.disable_logging:
    init_logger(args)

if args.disable_tracing:
    init_tracer(args)


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_NABLED = True
    SITE_NAME = 'app'
    SECRET_KEY = os.urandom(32)
    SQLALCHEMY_DATABASE_URI = URL.create(drivername='cockroachdb',
                                         username=args.username,
                                         password=args.password,
                                         host=args.host,
                                         port=args.port,
                                         database=args.database)
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
