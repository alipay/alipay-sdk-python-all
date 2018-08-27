#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserAntpaasTestaccountCreateModel(object):

    def __init__(self):
        self._account_level = None
        self._cert_name = None
        self._cert_no = None
        self._cert_type = None
        self._logon_id = None
        self._logon_type = None
        self._memo = None
        self._operation_type = None
        self._operator_id = None
        self._remote_ip = None
        self._user_id = None
        self._user_status = None
        self._user_type = None

    @property
    def account_level(self):
        return self._account_level

    @account_level.setter
    def account_level(self, value):
        self._account_level = value
    @property
    def cert_name(self):
        return self._cert_name

    @cert_name.setter
    def cert_name(self, value):
        self._cert_name = value
    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def cert_type(self):
        return self._cert_type

    @cert_type.setter
    def cert_type(self, value):
        self._cert_type = value
    @property
    def logon_id(self):
        return self._logon_id

    @logon_id.setter
    def logon_id(self, value):
        self._logon_id = value
    @property
    def logon_type(self):
        return self._logon_type

    @logon_type.setter
    def logon_type(self, value):
        self._logon_type = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def operation_type(self):
        return self._operation_type

    @operation_type.setter
    def operation_type(self, value):
        self._operation_type = value
    @property
    def operator_id(self):
        return self._operator_id

    @operator_id.setter
    def operator_id(self, value):
        self._operator_id = value
    @property
    def remote_ip(self):
        return self._remote_ip

    @remote_ip.setter
    def remote_ip(self, value):
        self._remote_ip = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def user_status(self):
        return self._user_status

    @user_status.setter
    def user_status(self, value):
        self._user_status = value
    @property
    def user_type(self):
        return self._user_type

    @user_type.setter
    def user_type(self, value):
        self._user_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_level:
            if hasattr(self.account_level, 'to_alipay_dict'):
                params['account_level'] = self.account_level.to_alipay_dict()
            else:
                params['account_level'] = self.account_level
        if self.cert_name:
            if hasattr(self.cert_name, 'to_alipay_dict'):
                params['cert_name'] = self.cert_name.to_alipay_dict()
            else:
                params['cert_name'] = self.cert_name
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.cert_type:
            if hasattr(self.cert_type, 'to_alipay_dict'):
                params['cert_type'] = self.cert_type.to_alipay_dict()
            else:
                params['cert_type'] = self.cert_type
        if self.logon_id:
            if hasattr(self.logon_id, 'to_alipay_dict'):
                params['logon_id'] = self.logon_id.to_alipay_dict()
            else:
                params['logon_id'] = self.logon_id
        if self.logon_type:
            if hasattr(self.logon_type, 'to_alipay_dict'):
                params['logon_type'] = self.logon_type.to_alipay_dict()
            else:
                params['logon_type'] = self.logon_type
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.operation_type:
            if hasattr(self.operation_type, 'to_alipay_dict'):
                params['operation_type'] = self.operation_type.to_alipay_dict()
            else:
                params['operation_type'] = self.operation_type
        if self.operator_id:
            if hasattr(self.operator_id, 'to_alipay_dict'):
                params['operator_id'] = self.operator_id.to_alipay_dict()
            else:
                params['operator_id'] = self.operator_id
        if self.remote_ip:
            if hasattr(self.remote_ip, 'to_alipay_dict'):
                params['remote_ip'] = self.remote_ip.to_alipay_dict()
            else:
                params['remote_ip'] = self.remote_ip
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.user_status:
            if hasattr(self.user_status, 'to_alipay_dict'):
                params['user_status'] = self.user_status.to_alipay_dict()
            else:
                params['user_status'] = self.user_status
        if self.user_type:
            if hasattr(self.user_type, 'to_alipay_dict'):
                params['user_type'] = self.user_type.to_alipay_dict()
            else:
                params['user_type'] = self.user_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserAntpaasTestaccountCreateModel()
        if 'account_level' in d:
            o.account_level = d['account_level']
        if 'cert_name' in d:
            o.cert_name = d['cert_name']
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'logon_id' in d:
            o.logon_id = d['logon_id']
        if 'logon_type' in d:
            o.logon_type = d['logon_type']
        if 'memo' in d:
            o.memo = d['memo']
        if 'operation_type' in d:
            o.operation_type = d['operation_type']
        if 'operator_id' in d:
            o.operator_id = d['operator_id']
        if 'remote_ip' in d:
            o.remote_ip = d['remote_ip']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'user_status' in d:
            o.user_status = d['user_status']
        if 'user_type' in d:
            o.user_type = d['user_type']
        return o


