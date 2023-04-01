#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OperatorQuery(object):

    def __init__(self):
        self._id = None
        self._id_type = None
        self._logon_id_type = None
        self._main_ip_role_id = None
        self._main_ip_role_type = None
        self._open_id = None

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def id_type(self):
        return self._id_type

    @id_type.setter
    def id_type(self, value):
        self._id_type = value
    @property
    def logon_id_type(self):
        return self._logon_id_type

    @logon_id_type.setter
    def logon_id_type(self, value):
        self._logon_id_type = value
    @property
    def main_ip_role_id(self):
        return self._main_ip_role_id

    @main_ip_role_id.setter
    def main_ip_role_id(self, value):
        self._main_ip_role_id = value
    @property
    def main_ip_role_type(self):
        return self._main_ip_role_type

    @main_ip_role_type.setter
    def main_ip_role_type(self, value):
        self._main_ip_role_type = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.id_type:
            if hasattr(self.id_type, 'to_alipay_dict'):
                params['id_type'] = self.id_type.to_alipay_dict()
            else:
                params['id_type'] = self.id_type
        if self.logon_id_type:
            if hasattr(self.logon_id_type, 'to_alipay_dict'):
                params['logon_id_type'] = self.logon_id_type.to_alipay_dict()
            else:
                params['logon_id_type'] = self.logon_id_type
        if self.main_ip_role_id:
            if hasattr(self.main_ip_role_id, 'to_alipay_dict'):
                params['main_ip_role_id'] = self.main_ip_role_id.to_alipay_dict()
            else:
                params['main_ip_role_id'] = self.main_ip_role_id
        if self.main_ip_role_type:
            if hasattr(self.main_ip_role_type, 'to_alipay_dict'):
                params['main_ip_role_type'] = self.main_ip_role_type.to_alipay_dict()
            else:
                params['main_ip_role_type'] = self.main_ip_role_type
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OperatorQuery()
        if 'id' in d:
            o.id = d['id']
        if 'id_type' in d:
            o.id_type = d['id_type']
        if 'logon_id_type' in d:
            o.logon_id_type = d['logon_id_type']
        if 'main_ip_role_id' in d:
            o.main_ip_role_id = d['main_ip_role_id']
        if 'main_ip_role_type' in d:
            o.main_ip_role_type = d['main_ip_role_type']
        if 'open_id' in d:
            o.open_id = d['open_id']
        return o


