#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EmployeeDataItem import EmployeeDataItem


class AlipayDigitalmgmtEmbenefitMasterdataEmployeeSyncModel(object):

    def __init__(self):
        self._alipay_open_id = None
        self._api_key = None
        self._auto_authenticate = None
        self._data_list = None
        self._identity_type = None
        self._login_id = None

    @property
    def alipay_open_id(self):
        return self._alipay_open_id

    @alipay_open_id.setter
    def alipay_open_id(self, value):
        self._alipay_open_id = value
    @property
    def api_key(self):
        return self._api_key

    @api_key.setter
    def api_key(self, value):
        self._api_key = value
    @property
    def auto_authenticate(self):
        return self._auto_authenticate

    @auto_authenticate.setter
    def auto_authenticate(self, value):
        self._auto_authenticate = value
    @property
    def data_list(self):
        return self._data_list

    @data_list.setter
    def data_list(self, value):
        if isinstance(value, list):
            self._data_list = list()
            for i in value:
                if isinstance(i, EmployeeDataItem):
                    self._data_list.append(i)
                else:
                    self._data_list.append(EmployeeDataItem.from_alipay_dict(i))
    @property
    def identity_type(self):
        return self._identity_type

    @identity_type.setter
    def identity_type(self, value):
        self._identity_type = value
    @property
    def login_id(self):
        return self._login_id

    @login_id.setter
    def login_id(self, value):
        self._login_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_open_id:
            if hasattr(self.alipay_open_id, 'to_alipay_dict'):
                params['alipay_open_id'] = self.alipay_open_id.to_alipay_dict()
            else:
                params['alipay_open_id'] = self.alipay_open_id
        if self.api_key:
            if hasattr(self.api_key, 'to_alipay_dict'):
                params['api_key'] = self.api_key.to_alipay_dict()
            else:
                params['api_key'] = self.api_key
        if self.auto_authenticate:
            if hasattr(self.auto_authenticate, 'to_alipay_dict'):
                params['auto_authenticate'] = self.auto_authenticate.to_alipay_dict()
            else:
                params['auto_authenticate'] = self.auto_authenticate
        if self.data_list:
            if isinstance(self.data_list, list):
                for i in range(0, len(self.data_list)):
                    element = self.data_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.data_list[i] = element.to_alipay_dict()
            if hasattr(self.data_list, 'to_alipay_dict'):
                params['data_list'] = self.data_list.to_alipay_dict()
            else:
                params['data_list'] = self.data_list
        if self.identity_type:
            if hasattr(self.identity_type, 'to_alipay_dict'):
                params['identity_type'] = self.identity_type.to_alipay_dict()
            else:
                params['identity_type'] = self.identity_type
        if self.login_id:
            if hasattr(self.login_id, 'to_alipay_dict'):
                params['login_id'] = self.login_id.to_alipay_dict()
            else:
                params['login_id'] = self.login_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDigitalmgmtEmbenefitMasterdataEmployeeSyncModel()
        if 'alipay_open_id' in d:
            o.alipay_open_id = d['alipay_open_id']
        if 'api_key' in d:
            o.api_key = d['api_key']
        if 'auto_authenticate' in d:
            o.auto_authenticate = d['auto_authenticate']
        if 'data_list' in d:
            o.data_list = d['data_list']
        if 'identity_type' in d:
            o.identity_type = d['identity_type']
        if 'login_id' in d:
            o.login_id = d['login_id']
        return o


