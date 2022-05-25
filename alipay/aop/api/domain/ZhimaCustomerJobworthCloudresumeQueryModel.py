#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCustomerJobworthCloudresumeQueryModel(object):

    def __init__(self):
        self._conn_key = None
        self._once_token = None

    @property
    def conn_key(self):
        return self._conn_key

    @conn_key.setter
    def conn_key(self, value):
        self._conn_key = value
    @property
    def once_token(self):
        return self._once_token

    @once_token.setter
    def once_token(self, value):
        self._once_token = value


    def to_alipay_dict(self):
        params = dict()
        if self.conn_key:
            if hasattr(self.conn_key, 'to_alipay_dict'):
                params['conn_key'] = self.conn_key.to_alipay_dict()
            else:
                params['conn_key'] = self.conn_key
        if self.once_token:
            if hasattr(self.once_token, 'to_alipay_dict'):
                params['once_token'] = self.once_token.to_alipay_dict()
            else:
                params['once_token'] = self.once_token
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCustomerJobworthCloudresumeQueryModel()
        if 'conn_key' in d:
            o.conn_key = d['conn_key']
        if 'once_token' in d:
            o.once_token = d['once_token']
        return o


