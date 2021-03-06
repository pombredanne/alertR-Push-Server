#!/usr/bin/python3

# written by sqall
# twitter: https://twitter.com/sqall01
# blog: http://blog.h4des.org
# github: https://github.com/sqall01
#
# Licensed under the GNU Public License, version 2.

import os


class ErrorCodes:
    NO_ERROR = 0
    DATABASE_ERROR = 1
    AUTH_ERROR = 2
    ILLEGAL_MSG_ERROR = 3
    GOOGLE_MSG_TOO_LARGE = 4
    GOOGLE_CONNECTION = 5
    GOOGLE_UNKNOWN = 6
    GOOGLE_AUTH = 7
    VERSION_MISSMATCH = 8
    NO_NOTIFICATION_PERMISSION = 9


class AclCodes:
    NOTIFICATION_CHANNEL = 0


# This class is a global configuration class that holds
# values that are needed all over the server.
class GlobalData:

    def __init__(self):

        # Version of the used server (and protocol).
        self.version = 0.100

        # Revision of the used server.
        self.rev = 0

        # Path to the configuration file of the client.
        self.config_file = os.path.dirname(os.path.abspath(__file__)) + "/../config/config.xml"

        # Location of the certificate file.
        self.server_cert_file = None

        # Location of the key file
        self.server_key_file = None

        # Information concerning logging instances.
        self.logger = None
        self.logdir = None
        self.loglevel = None

        # Needed mysql parameters.
        self.mysql_host = None
        self.mysql_port = None
        self.mysql_database = None
        self.mysql_username = None
        self.mysql_password = None

        # How often the push server should try to connect to the
        # MySQL server when the connection establishment fails.
        self.mysql_connection_retries = 5

        # Time the server is waiting on receives until a time out occurs.
        self.server_receive_timeout = 20.0

        # Settings for bruteforce protection.
        self.bf_fail_attempts_count = None
        self.bf_fail_attempts_timer = 120
        self.bf_block_time = None

        # Settings for google firebase service.
        self.google_auth_key = None
        self.google_cert_file = None

        # Amount of days the statistics are kept in the database.
        self.statistics_life_span = None

        # Time the db cleaner thread should sleep before starting a new clean up run.
        self.db_cleaner_sleep_timer = 600

        # Channel that is used to receive all devices that uses the service.
        self.notification_channel = "alertR_notification"