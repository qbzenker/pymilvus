#  Tencent is pleased to support the open source community by making GNES available.
#
#  Copyright (C) 2019 THL A29 Limited, a Tencent company. All rights reserved.
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.


import argparse
from . import api


def set_base_parser():
    # create the top-level parser
    parser = argparse.ArgumentParser(
        description='Milvus, An open source similarity search engine for massive feature vectors.\n'
                    'Visit %s for tutorials and documentations.' % (('https://github.com/milvus-io/milvus')),
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    return parser


def _set_grpc_parser(parser=None):
    if not parser:
        parser = set_base_parser()
    parser.add_argument('--host', type=str, default='127.0.0.1', help='host address of the grpc service')
    parser.add_argument('--port', type=int, default=19530, help='host port of the grpc service')
    return parser

################################################################################
# milvus table [sub-command]

def set_table_create_parser(parser=None):
    if not parser:
        parser = set_base_parser()
    _set_grpc_parser(parser)
    parser.add_argument('--table_name', type=str, help='table name')
    parser.add_argument('--dim', type=int, default=128, help='vector dimension')
    parser.add_argument('--metric_type', type=str, default='L2', help='L2 or IP')

    return parser

def set_table_exist_parser(parser=None):
    if not parser:
        parser = set_base_parser()
    _set_grpc_parser(parser)
    parser.add_argument('--table_name', type=str, help='table name')
    return parser

def set_table_drop_parser(parser=None):
    if not parser:
        parser = set_base_parser()
    _set_grpc_parser(parser)
    parser.add_argument('--table_name', type=str, help='table name')
    return parser

def set_table_describe_parser(parser=None):
    if not parser:
        parser = set_base_parser()
    _set_grpc_parser(parser)
    parser.add_argument('--table_name', type=str, help='table name')
    return parser

def set_table_list_parser(parser=None):
    if not parser:
        parser = set_base_parser()
    _set_grpc_parser(parser)
    return parser

def set_table_count_parser(parser=None):
    if not parser:
        parser = set_base_parser()
    _set_grpc_parser(parser)
    parser.add_argument('--table_name', type=str, help='table name')
    return parser

def set_table_load_parser(parser=None):
    if not parser:
        parser = set_base_parser()
    _set_grpc_parser(parser)
    parser.add_argument('--table_name', type=str, help='table name')
    return parser

################################################################################
# milvus index [sub-command]

def set_index_create_parser(parser=None):
    if not parser:
        parser = set_base_parser()
    _set_grpc_parser(parser)
    parser.add_argument('--table_name', type=str, help='table name')
    parser.add_argument('--index_type', type=str, default='FLAT', help='[FLAT, IVF_FLAT, IVF_SQ8, MIX_NSG, IVF_SQ8H]')
    return parser

def set_index_describe_parser(parser=None):
    if not parser:
        parser = set_base_parser()
    _set_grpc_parser(parser)
    parser.add_argument('--table_name', type=str, help='table name')
    return parser

def set_index_drop_parser(parser=None):
    if not parser:
        parser = set_base_parser()
    _set_grpc_parser(parser)
    parser.add_argument('--table_name', type=str, help='table name')
    return parser

################################################################################
# milvus vector [sub-command]

def set_vector_add_parser(parser=None):
    if not parser:
        parser = set_base_parser()
    _set_grpc_parser(parser)
    parser.add_argument('--table_name', type=str, help='table name')
    parser.add_argument('--file_records', type=str, help='file name with vectors')
    parser.add_argument('--file_ids', type=str, help='file name with ids')
    return parser

def set_vector_search_parser(parser=None):
    if not parser:
        parser = set_base_parser()
    _set_grpc_parser(parser)
    parser.add_argument('--table_name', type=str, help='table name')
    parser.add_argument('--topk', type=int, help='top k')
    parser.add_argument('--nprobe', type=int, help='bucket num to search')
    parser.add_argument('--file_records', type=str, help='file name with vectors')
    parser.add_argument('--query_range', type=str, help='time range')
    return parser

################################################################################
# milvus server [sub-command]

def set_server_version_parser(parser=None):
    if not parser:
        parser = set_base_parser()
    _set_grpc_parser(parser)

    return parser

def set_server_status_parser(parser=None):
    if not parser:
        parser = set_base_parser()
    _set_grpc_parser(parser)

    return parser

################################################################################
# milvus client [sub-command]

def set_client_version_parser(parser=None):
    if not parser:
        parser = set_base_parser()
    _set_grpc_parser(parser)

    return parser

################################################################################
def get_main_parser():
    # create the top-level parser
    parser = set_base_parser()
    adf = argparse.ArgumentDefaultsHelpFormatter
    sp = parser.add_subparsers(dest='cli', title='MILVUS sub-commands',
                               description='use "milvus [sub-command] --help" '
                                           'to get detailed information about each sub-command')

    # table operations
    pp = sp.add_parser('table', help='table related operations')
    spp = pp.add_subparsers(dest='table', title='milvus table sub-commands',
                            description='use "milvus table [sub-command] --help" '
                                        'to get detailed information about each table sub-command')
    spp.required = True
    set_table_create_parser(spp.add_parser('create', help='create table', formatter_class=adf))
    set_table_exist_parser(spp.add_parser('exist', help='check table existence', formatter_class=adf))
    set_table_drop_parser(spp.add_parser('drop', help='drop table', formatter_class=adf))
    set_table_describe_parser(spp.add_parser('describe', help='describe table', formatter_class=adf))
    set_table_list_parser(spp.add_parser('list', help='list all tables', formatter_class=adf))
    set_table_count_parser(spp.add_parser('count', help='count table rows', formatter_class=adf))
    set_table_load_parser(spp.add_parser('load', help='load table', formatter_class=adf))

    # index operations
    pp = sp.add_parser('index', help='index related operations')
    spp = pp.add_subparsers(dest='index', title='milvus index sub-commands',
                            description='use "milvus index [sub-command] --help" '
                                        'to get detailed information about each index sub-command')
    spp.required = True
    set_index_create_parser(spp.add_parser('create', help='create index', formatter_class=adf))
    set_index_describe_parser(spp.add_parser('describe', help='describe index', formatter_class=adf))
    set_index_drop_parser(spp.add_parser('drop', help='drop index', formatter_class=adf))

    # vector operations
    pp = sp.add_parser('vector', help='vector related operations')
    spp = pp.add_subparsers(dest='vector', title='milvus vector sub-commands',
                            description='use "milvus vector [sub-command] --help" '
                                        'to get detailed information about each vector sub-command')
    spp.required = True
    set_vector_add_parser(spp.add_parser('add', help='add vectors', formatter_class=adf))
    set_vector_search_parser(spp.add_parser('search', help='search vectors', formatter_class=adf))

    # server operations
    pp = sp.add_parser('server', help='server related operations')
    spp = pp.add_subparsers(dest='server', title='milvus server sub-commands',
                            description='use "milvus server [sub-command] --help" '
                                        'to get detailed information about each server sub-command')
    spp.required = True
    set_server_version_parser(spp.add_parser('version', help='show server version', formatter_class=adf))
    set_server_status_parser(spp.add_parser('status', help='show server status', formatter_class=adf))

    # client operations
    pp = sp.add_parser('client', help='client related operations')
    spp = pp.add_subparsers(dest='client', title='milvus client sub-commands',
                            description='use "milvus client [sub-command] --help" '
                                        'to get detailed information about each client sub-command')
    spp.required = True
    set_client_version_parser(spp.add_parser('version', help='show client version', formatter_class=adf))

    return parser

