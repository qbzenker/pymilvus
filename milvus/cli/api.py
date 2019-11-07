import numpy as np
from .. import Milvus, IndexType, MetricType


################################################################################
# milvus table [sub-command]

def _table_create(client, _args):
    _metric_type = MetricType.L2;
    if (_args.metric_type != 'L2'):
        _metric_type = MetricType.IP

    param = {
        'table_name': _args.table_name,
        'dimension': _args.dim,
        'index_file_size': 1024,
        'metric_type': _metric_type
    }

    status = client.create_table(param)
    print(status)

def _table_exist(client, _args):
    status, exist = client.has_table(_args.table_name)
    print(exist)
    print(status)

def _table_drop(client, _args):
    status = client.drop_table(_args.table_name)
    print(status)

def _table_describe(client, _args):
    status, table_schema = client.describe_table(_args.table_name)
    print(table_schema)
    print(status)

def _table_list(client, _args):
    status, tables = client.show_tables()
    print(tables)
    print(status)

def _table_count(client, _args):
    status, rows = client.get_table_row_count(_args.table_name)
    print(rows)
    print(status)

def _table_load(client, _args):
    status = client.preload_table(_args.table_name)
    print(status)

def table(_args):
    client = Milvus()
    status = client.connect(host=_args.host, port=_args.port)
    if not status.OK():
        print(status.message)
        exit(1)

    if (_args.table == 'create'):
        _table_create(client, _args)
    elif (_args.table == 'exist'):
        _table_exist(client, _args)
    elif (_args.table == 'drop'):
        _table_drop(client, _args)
    elif (_args.table == 'describe'):
        _table_describe(client, _args)
    elif (_args.table == 'list'):
        _table_list(client, _args)
    elif (_args.table == 'count'):
        _table_count(client, _args)
    elif (_args.table == 'load'):
        _table_load(client, _args)

    client.disconnect()

################################################################################
# milvus index [sub-command]

def _index_create(client, _args):
    status = client.create_index(_args.table_name, _args.index_type)
    print(status)

def _index_describe(client, _args):
    status, index_schema = client.describe_index(_args.table_name)
    print(index_schema)
    print(status)

def _index_drop(client, _args):
    status = client.drop_index(_args.table_name)
    print(status)

def index(_args):
    client = Milvus()
    status = client.connect(host=_args.host, port=_args.port)
    if not status.OK():
        print(status.message)
        exit(1)

    if (_args.index == 'create'):
        _index_create(client, _args)
    elif (_args.index == 'describe'):
        _index_describe(client, _args)
    elif (_args.index == 'drop'):
        _index_drop(client, _args)

    client.disconnect()

################################################################################
# milvus vector [sub-command]

def _vector_add(client, _args):
    data_records = np.load(_args.file_records)
    records = data_records[:].tolist()
    data_ids = np.load(_args.file_ids)
    ids = data_ids[].tolist()
    status, r_ids = client.add_vectors(_args.table_name, records, ids)
    print(status)

def _vector_search(client, _args):
    data_records = np.load(_args.file_records)
    records = data_records[:].tolist()
    status, results = client.search_vectors(_args.table_name, _args.topk, _args.nprobs,
                                            records, _args.query_ranges)
    print(results)
    print(status)

def vector(_args):
    client = Milvus()
    status = client.connect(host=_args.host, port=_args.port)
    if not status.OK():
        print(status.message)
        exit(1)

    if (_args.vector == 'add'):
        _vector_add(client, _args)
    elif (_args.vector == 'search'):
        _vector_search(client, _args)

    client.disconnect()

################################################################################
# milvus server [sub-command]

def _server_version(client, _args):
    status, version = client.server_version()
    print(version)
    print(status)

def _server_status(client, _args):
    status, str = client.server_status()
    print(str)
    print(status)

def server(_args):
    client = Milvus()
    status = client.connect(host=_args.host, port=_args.port)
    if not status.OK():
        print(status.message)
        exit(1)

    if (_args.server == 'version'):
        _server_version(client, _args)
    elif (_args.server == 'status'):
        _server_status(client, _args)

    client.disconnect()

################################################################################
# milvus client [sub-command]

def _client_version(client, _args):
    version = client.client_version()
    print(version)

def client(_args):
    client = Milvus()
    status = client.connect(host=_args.host, port=_args.port)
    if not status.OK():
        print(status.message)
        exit(1)

    if (_args.client == 'version'):
        _client_version(client, _args)

    client.disconnect()