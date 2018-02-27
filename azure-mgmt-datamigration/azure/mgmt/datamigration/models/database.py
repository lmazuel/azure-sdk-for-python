# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class Database(Model):
    """Information about a single database.

    :param id: Unique identifier for the database
    :type id: str
    :param name: Name of the database
    :type name: str
    :param compatibility_level: SQL Server compatibility level of database.
     Possible values include: 'CompatLevel80', 'CompatLevel90',
     'CompatLevel100', 'CompatLevel110', 'CompatLevel120', 'CompatLevel130',
     'CompatLevel140'
    :type compatibility_level: str or
     ~azure.mgmt.datamigration.models.DatabaseCompatLevel
    :param collation: Collation name of the database
    :type collation: str
    :param server_name: Name of the server
    :type server_name: str
    :param fqdn: Fully qualified name
    :type fqdn: str
    :param install_id: Install id of the database
    :type install_id: str
    :param server_version: Version of the server
    :type server_version: str
    :param server_edition: Edition of the server
    :type server_edition: str
    :param server_level: Product level of the server (RTM, SP, CTP).
    :type server_level: str
    :param server_default_data_path: Default path of the data files
    :type server_default_data_path: str
    :param server_default_log_path: Default path of the log files
    :type server_default_log_path: str
    :param server_default_backup_path: Default path of the backup folder
    :type server_default_backup_path: str
    :param server_core_count: Number of cores on the server
    :type server_core_count: int
    :param server_visible_online_core_count: Number of cores on the server
     that have VISIBLE ONLINE status
    :type server_visible_online_core_count: int
    :param database_state: State of the database. Possible values include:
     'Online', 'Restoring', 'Recovering', 'RecoveryPending', 'Suspect',
     'Emergency', 'Offline', 'Copying', 'OfflineSecondary'
    :type database_state: str or
     ~azure.mgmt.datamigration.models.DatabaseState
    :param server_id: The unique Server Id
    :type server_id: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'compatibility_level': {'key': 'compatibilityLevel', 'type': 'DatabaseCompatLevel'},
        'collation': {'key': 'collation', 'type': 'str'},
        'server_name': {'key': 'serverName', 'type': 'str'},
        'fqdn': {'key': 'fqdn', 'type': 'str'},
        'install_id': {'key': 'installId', 'type': 'str'},
        'server_version': {'key': 'serverVersion', 'type': 'str'},
        'server_edition': {'key': 'serverEdition', 'type': 'str'},
        'server_level': {'key': 'serverLevel', 'type': 'str'},
        'server_default_data_path': {'key': 'serverDefaultDataPath', 'type': 'str'},
        'server_default_log_path': {'key': 'serverDefaultLogPath', 'type': 'str'},
        'server_default_backup_path': {'key': 'serverDefaultBackupPath', 'type': 'str'},
        'server_core_count': {'key': 'serverCoreCount', 'type': 'int'},
        'server_visible_online_core_count': {'key': 'serverVisibleOnlineCoreCount', 'type': 'int'},
        'database_state': {'key': 'databaseState', 'type': 'DatabaseState'},
        'server_id': {'key': 'serverId', 'type': 'str'},
    }

    def __init__(self, id=None, name=None, compatibility_level=None, collation=None, server_name=None, fqdn=None, install_id=None, server_version=None, server_edition=None, server_level=None, server_default_data_path=None, server_default_log_path=None, server_default_backup_path=None, server_core_count=None, server_visible_online_core_count=None, database_state=None, server_id=None):
        super(Database, self).__init__()
        self.id = id
        self.name = name
        self.compatibility_level = compatibility_level
        self.collation = collation
        self.server_name = server_name
        self.fqdn = fqdn
        self.install_id = install_id
        self.server_version = server_version
        self.server_edition = server_edition
        self.server_level = server_level
        self.server_default_data_path = server_default_data_path
        self.server_default_log_path = server_default_log_path
        self.server_default_backup_path = server_default_backup_path
        self.server_core_count = server_core_count
        self.server_visible_online_core_count = server_visible_online_core_count
        self.database_state = database_state
        self.server_id = server_id
