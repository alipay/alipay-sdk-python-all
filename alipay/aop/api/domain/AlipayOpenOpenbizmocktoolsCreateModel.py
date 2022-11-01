#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenOpenbizmocktoolsCreateModel(object):

    def __init__(self):
        self._action_type = None
        self._allow_sign_types = None
        self._app_name = None
        self._app_number = None
        self._application_type = None
        self._charset_type = None
        self._encrypt_type = None
        self._env = None
        self._gateway_url = None
        self._group_id = None
        self._header = None
        self._interface_name = None
        self._isv_app_id = None
        self._load_test = None
        self._mock_config = None
        self._notify_fields = None
        self._notify_triggers = None
        self._oid = None
        self._open_id = None
        self._operation_type = None
        self._outputs = None
        self._package_code = None
        self._pid = None
        self._protocol = None
        self._public_key = None
        self._query = None
        self._return_url_address = None
        self._scope = None
        self._secret_key = None
        self._signature_type = None
        self._status = None
        self._sub_tag = None
        self._subscribe_type = None
        self._test_url = None
        self._timeout = None
        self._uid = None
        self._use_encrypt = None
        self._user_id = None
        self._version_no = None

    @property
    def action_type(self):
        return self._action_type

    @action_type.setter
    def action_type(self, value):
        self._action_type = value
    @property
    def allow_sign_types(self):
        return self._allow_sign_types

    @allow_sign_types.setter
    def allow_sign_types(self, value):
        self._allow_sign_types = value
    @property
    def app_name(self):
        return self._app_name

    @app_name.setter
    def app_name(self, value):
        self._app_name = value
    @property
    def app_number(self):
        return self._app_number

    @app_number.setter
    def app_number(self, value):
        self._app_number = value
    @property
    def application_type(self):
        return self._application_type

    @application_type.setter
    def application_type(self, value):
        self._application_type = value
    @property
    def charset_type(self):
        return self._charset_type

    @charset_type.setter
    def charset_type(self, value):
        self._charset_type = value
    @property
    def encrypt_type(self):
        return self._encrypt_type

    @encrypt_type.setter
    def encrypt_type(self, value):
        self._encrypt_type = value
    @property
    def env(self):
        return self._env

    @env.setter
    def env(self, value):
        self._env = value
    @property
    def gateway_url(self):
        return self._gateway_url

    @gateway_url.setter
    def gateway_url(self, value):
        self._gateway_url = value
    @property
    def group_id(self):
        return self._group_id

    @group_id.setter
    def group_id(self, value):
        self._group_id = value
    @property
    def header(self):
        return self._header

    @header.setter
    def header(self, value):
        self._header = value
    @property
    def interface_name(self):
        return self._interface_name

    @interface_name.setter
    def interface_name(self, value):
        self._interface_name = value
    @property
    def isv_app_id(self):
        return self._isv_app_id

    @isv_app_id.setter
    def isv_app_id(self, value):
        self._isv_app_id = value
    @property
    def load_test(self):
        return self._load_test

    @load_test.setter
    def load_test(self, value):
        self._load_test = value
    @property
    def mock_config(self):
        return self._mock_config

    @mock_config.setter
    def mock_config(self, value):
        self._mock_config = value
    @property
    def notify_fields(self):
        return self._notify_fields

    @notify_fields.setter
    def notify_fields(self, value):
        self._notify_fields = value
    @property
    def notify_triggers(self):
        return self._notify_triggers

    @notify_triggers.setter
    def notify_triggers(self, value):
        self._notify_triggers = value
    @property
    def oid(self):
        return self._oid

    @oid.setter
    def oid(self, value):
        self._oid = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def operation_type(self):
        return self._operation_type

    @operation_type.setter
    def operation_type(self, value):
        self._operation_type = value
    @property
    def outputs(self):
        return self._outputs

    @outputs.setter
    def outputs(self, value):
        self._outputs = value
    @property
    def package_code(self):
        return self._package_code

    @package_code.setter
    def package_code(self, value):
        self._package_code = value
    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, value):
        self._pid = value
    @property
    def protocol(self):
        return self._protocol

    @protocol.setter
    def protocol(self, value):
        self._protocol = value
    @property
    def public_key(self):
        return self._public_key

    @public_key.setter
    def public_key(self, value):
        self._public_key = value
    @property
    def query(self):
        return self._query

    @query.setter
    def query(self, value):
        self._query = value
    @property
    def return_url_address(self):
        return self._return_url_address

    @return_url_address.setter
    def return_url_address(self, value):
        self._return_url_address = value
    @property
    def scope(self):
        return self._scope

    @scope.setter
    def scope(self, value):
        self._scope = value
    @property
    def secret_key(self):
        return self._secret_key

    @secret_key.setter
    def secret_key(self, value):
        self._secret_key = value
    @property
    def signature_type(self):
        return self._signature_type

    @signature_type.setter
    def signature_type(self, value):
        self._signature_type = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def sub_tag(self):
        return self._sub_tag

    @sub_tag.setter
    def sub_tag(self, value):
        self._sub_tag = value
    @property
    def subscribe_type(self):
        return self._subscribe_type

    @subscribe_type.setter
    def subscribe_type(self, value):
        self._subscribe_type = value
    @property
    def test_url(self):
        return self._test_url

    @test_url.setter
    def test_url(self, value):
        self._test_url = value
    @property
    def timeout(self):
        return self._timeout

    @timeout.setter
    def timeout(self, value):
        self._timeout = value
    @property
    def uid(self):
        return self._uid

    @uid.setter
    def uid(self, value):
        self._uid = value
    @property
    def use_encrypt(self):
        return self._use_encrypt

    @use_encrypt.setter
    def use_encrypt(self, value):
        self._use_encrypt = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def version_no(self):
        return self._version_no

    @version_no.setter
    def version_no(self, value):
        self._version_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.action_type:
            if hasattr(self.action_type, 'to_alipay_dict'):
                params['action_type'] = self.action_type.to_alipay_dict()
            else:
                params['action_type'] = self.action_type
        if self.allow_sign_types:
            if hasattr(self.allow_sign_types, 'to_alipay_dict'):
                params['allow_sign_types'] = self.allow_sign_types.to_alipay_dict()
            else:
                params['allow_sign_types'] = self.allow_sign_types
        if self.app_name:
            if hasattr(self.app_name, 'to_alipay_dict'):
                params['app_name'] = self.app_name.to_alipay_dict()
            else:
                params['app_name'] = self.app_name
        if self.app_number:
            if hasattr(self.app_number, 'to_alipay_dict'):
                params['app_number'] = self.app_number.to_alipay_dict()
            else:
                params['app_number'] = self.app_number
        if self.application_type:
            if hasattr(self.application_type, 'to_alipay_dict'):
                params['application_type'] = self.application_type.to_alipay_dict()
            else:
                params['application_type'] = self.application_type
        if self.charset_type:
            if hasattr(self.charset_type, 'to_alipay_dict'):
                params['charset_type'] = self.charset_type.to_alipay_dict()
            else:
                params['charset_type'] = self.charset_type
        if self.encrypt_type:
            if hasattr(self.encrypt_type, 'to_alipay_dict'):
                params['encrypt_type'] = self.encrypt_type.to_alipay_dict()
            else:
                params['encrypt_type'] = self.encrypt_type
        if self.env:
            if hasattr(self.env, 'to_alipay_dict'):
                params['env'] = self.env.to_alipay_dict()
            else:
                params['env'] = self.env
        if self.gateway_url:
            if hasattr(self.gateway_url, 'to_alipay_dict'):
                params['gateway_url'] = self.gateway_url.to_alipay_dict()
            else:
                params['gateway_url'] = self.gateway_url
        if self.group_id:
            if hasattr(self.group_id, 'to_alipay_dict'):
                params['group_id'] = self.group_id.to_alipay_dict()
            else:
                params['group_id'] = self.group_id
        if self.header:
            if hasattr(self.header, 'to_alipay_dict'):
                params['header'] = self.header.to_alipay_dict()
            else:
                params['header'] = self.header
        if self.interface_name:
            if hasattr(self.interface_name, 'to_alipay_dict'):
                params['interface_name'] = self.interface_name.to_alipay_dict()
            else:
                params['interface_name'] = self.interface_name
        if self.isv_app_id:
            if hasattr(self.isv_app_id, 'to_alipay_dict'):
                params['isv_app_id'] = self.isv_app_id.to_alipay_dict()
            else:
                params['isv_app_id'] = self.isv_app_id
        if self.load_test:
            if hasattr(self.load_test, 'to_alipay_dict'):
                params['load_test'] = self.load_test.to_alipay_dict()
            else:
                params['load_test'] = self.load_test
        if self.mock_config:
            if hasattr(self.mock_config, 'to_alipay_dict'):
                params['mock_config'] = self.mock_config.to_alipay_dict()
            else:
                params['mock_config'] = self.mock_config
        if self.notify_fields:
            if hasattr(self.notify_fields, 'to_alipay_dict'):
                params['notify_fields'] = self.notify_fields.to_alipay_dict()
            else:
                params['notify_fields'] = self.notify_fields
        if self.notify_triggers:
            if hasattr(self.notify_triggers, 'to_alipay_dict'):
                params['notify_triggers'] = self.notify_triggers.to_alipay_dict()
            else:
                params['notify_triggers'] = self.notify_triggers
        if self.oid:
            if hasattr(self.oid, 'to_alipay_dict'):
                params['oid'] = self.oid.to_alipay_dict()
            else:
                params['oid'] = self.oid
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.operation_type:
            if hasattr(self.operation_type, 'to_alipay_dict'):
                params['operation_type'] = self.operation_type.to_alipay_dict()
            else:
                params['operation_type'] = self.operation_type
        if self.outputs:
            if hasattr(self.outputs, 'to_alipay_dict'):
                params['outputs'] = self.outputs.to_alipay_dict()
            else:
                params['outputs'] = self.outputs
        if self.package_code:
            if hasattr(self.package_code, 'to_alipay_dict'):
                params['package_code'] = self.package_code.to_alipay_dict()
            else:
                params['package_code'] = self.package_code
        if self.pid:
            if hasattr(self.pid, 'to_alipay_dict'):
                params['pid'] = self.pid.to_alipay_dict()
            else:
                params['pid'] = self.pid
        if self.protocol:
            if hasattr(self.protocol, 'to_alipay_dict'):
                params['protocol'] = self.protocol.to_alipay_dict()
            else:
                params['protocol'] = self.protocol
        if self.public_key:
            if hasattr(self.public_key, 'to_alipay_dict'):
                params['public_key'] = self.public_key.to_alipay_dict()
            else:
                params['public_key'] = self.public_key
        if self.query:
            if hasattr(self.query, 'to_alipay_dict'):
                params['query'] = self.query.to_alipay_dict()
            else:
                params['query'] = self.query
        if self.return_url_address:
            if hasattr(self.return_url_address, 'to_alipay_dict'):
                params['return_url_address'] = self.return_url_address.to_alipay_dict()
            else:
                params['return_url_address'] = self.return_url_address
        if self.scope:
            if hasattr(self.scope, 'to_alipay_dict'):
                params['scope'] = self.scope.to_alipay_dict()
            else:
                params['scope'] = self.scope
        if self.secret_key:
            if hasattr(self.secret_key, 'to_alipay_dict'):
                params['secret_key'] = self.secret_key.to_alipay_dict()
            else:
                params['secret_key'] = self.secret_key
        if self.signature_type:
            if hasattr(self.signature_type, 'to_alipay_dict'):
                params['signature_type'] = self.signature_type.to_alipay_dict()
            else:
                params['signature_type'] = self.signature_type
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.sub_tag:
            if hasattr(self.sub_tag, 'to_alipay_dict'):
                params['sub_tag'] = self.sub_tag.to_alipay_dict()
            else:
                params['sub_tag'] = self.sub_tag
        if self.subscribe_type:
            if hasattr(self.subscribe_type, 'to_alipay_dict'):
                params['subscribe_type'] = self.subscribe_type.to_alipay_dict()
            else:
                params['subscribe_type'] = self.subscribe_type
        if self.test_url:
            if hasattr(self.test_url, 'to_alipay_dict'):
                params['test_url'] = self.test_url.to_alipay_dict()
            else:
                params['test_url'] = self.test_url
        if self.timeout:
            if hasattr(self.timeout, 'to_alipay_dict'):
                params['timeout'] = self.timeout.to_alipay_dict()
            else:
                params['timeout'] = self.timeout
        if self.uid:
            if hasattr(self.uid, 'to_alipay_dict'):
                params['uid'] = self.uid.to_alipay_dict()
            else:
                params['uid'] = self.uid
        if self.use_encrypt:
            if hasattr(self.use_encrypt, 'to_alipay_dict'):
                params['use_encrypt'] = self.use_encrypt.to_alipay_dict()
            else:
                params['use_encrypt'] = self.use_encrypt
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.version_no:
            if hasattr(self.version_no, 'to_alipay_dict'):
                params['version_no'] = self.version_no.to_alipay_dict()
            else:
                params['version_no'] = self.version_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenOpenbizmocktoolsCreateModel()
        if 'action_type' in d:
            o.action_type = d['action_type']
        if 'allow_sign_types' in d:
            o.allow_sign_types = d['allow_sign_types']
        if 'app_name' in d:
            o.app_name = d['app_name']
        if 'app_number' in d:
            o.app_number = d['app_number']
        if 'application_type' in d:
            o.application_type = d['application_type']
        if 'charset_type' in d:
            o.charset_type = d['charset_type']
        if 'encrypt_type' in d:
            o.encrypt_type = d['encrypt_type']
        if 'env' in d:
            o.env = d['env']
        if 'gateway_url' in d:
            o.gateway_url = d['gateway_url']
        if 'group_id' in d:
            o.group_id = d['group_id']
        if 'header' in d:
            o.header = d['header']
        if 'interface_name' in d:
            o.interface_name = d['interface_name']
        if 'isv_app_id' in d:
            o.isv_app_id = d['isv_app_id']
        if 'load_test' in d:
            o.load_test = d['load_test']
        if 'mock_config' in d:
            o.mock_config = d['mock_config']
        if 'notify_fields' in d:
            o.notify_fields = d['notify_fields']
        if 'notify_triggers' in d:
            o.notify_triggers = d['notify_triggers']
        if 'oid' in d:
            o.oid = d['oid']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'operation_type' in d:
            o.operation_type = d['operation_type']
        if 'outputs' in d:
            o.outputs = d['outputs']
        if 'package_code' in d:
            o.package_code = d['package_code']
        if 'pid' in d:
            o.pid = d['pid']
        if 'protocol' in d:
            o.protocol = d['protocol']
        if 'public_key' in d:
            o.public_key = d['public_key']
        if 'query' in d:
            o.query = d['query']
        if 'return_url_address' in d:
            o.return_url_address = d['return_url_address']
        if 'scope' in d:
            o.scope = d['scope']
        if 'secret_key' in d:
            o.secret_key = d['secret_key']
        if 'signature_type' in d:
            o.signature_type = d['signature_type']
        if 'status' in d:
            o.status = d['status']
        if 'sub_tag' in d:
            o.sub_tag = d['sub_tag']
        if 'subscribe_type' in d:
            o.subscribe_type = d['subscribe_type']
        if 'test_url' in d:
            o.test_url = d['test_url']
        if 'timeout' in d:
            o.timeout = d['timeout']
        if 'uid' in d:
            o.uid = d['uid']
        if 'use_encrypt' in d:
            o.use_encrypt = d['use_encrypt']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'version_no' in d:
            o.version_no = d['version_no']
        return o


