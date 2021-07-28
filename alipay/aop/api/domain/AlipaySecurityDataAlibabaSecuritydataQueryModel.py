#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySecurityDataAlibabaSecuritydataQueryModel(object):

    def __init__(self):
        self._biz_id = None
        self._service_name = None
        self._system_name = None
        self._table_name = None
        self._umid = None
        self._user_id = None

    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def service_name(self):
        return self._service_name

    @service_name.setter
    def service_name(self, value):
        self._service_name = value
    @property
    def system_name(self):
        return self._system_name

    @system_name.setter
    def system_name(self, value):
        self._system_name = value
    @property
    def table_name(self):
        return self._table_name

    @table_name.setter
    def table_name(self, value):
        self._table_name = value
    @property
    def umid(self):
        return self._umid

    @umid.setter
    def umid(self, value):
        self._umid = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.service_name:
            if hasattr(self.service_name, 'to_alipay_dict'):
                params['service_name'] = self.service_name.to_alipay_dict()
            else:
                params['service_name'] = self.service_name
        if self.system_name:
            if hasattr(self.system_name, 'to_alipay_dict'):
                params['system_name'] = self.system_name.to_alipay_dict()
            else:
                params['system_name'] = self.system_name
        if self.table_name:
            if hasattr(self.table_name, 'to_alipay_dict'):
                params['table_name'] = self.table_name.to_alipay_dict()
            else:
                params['table_name'] = self.table_name
        if self.umid:
            if hasattr(self.umid, 'to_alipay_dict'):
                params['umid'] = self.umid.to_alipay_dict()
            else:
                params['umid'] = self.umid
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityDataAlibabaSecuritydataQueryModel()
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'service_name' in d:
            o.service_name = d['service_name']
        if 'system_name' in d:
            o.system_name = d['system_name']
        if 'table_name' in d:
            o.table_name = d['table_name']
        if 'umid' in d:
            o.umid = d['umid']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


