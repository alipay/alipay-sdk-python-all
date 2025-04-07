#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CodeExtBean(object):

    def __init__(self):
        self._ch_info = None
        self._code_token = None
        self._code_type = None
        self._table_name = None

    @property
    def ch_info(self):
        return self._ch_info

    @ch_info.setter
    def ch_info(self, value):
        self._ch_info = value
    @property
    def code_token(self):
        return self._code_token

    @code_token.setter
    def code_token(self, value):
        self._code_token = value
    @property
    def code_type(self):
        return self._code_type

    @code_type.setter
    def code_type(self, value):
        self._code_type = value
    @property
    def table_name(self):
        return self._table_name

    @table_name.setter
    def table_name(self, value):
        self._table_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.ch_info:
            if hasattr(self.ch_info, 'to_alipay_dict'):
                params['ch_info'] = self.ch_info.to_alipay_dict()
            else:
                params['ch_info'] = self.ch_info
        if self.code_token:
            if hasattr(self.code_token, 'to_alipay_dict'):
                params['code_token'] = self.code_token.to_alipay_dict()
            else:
                params['code_token'] = self.code_token
        if self.code_type:
            if hasattr(self.code_type, 'to_alipay_dict'):
                params['code_type'] = self.code_type.to_alipay_dict()
            else:
                params['code_type'] = self.code_type
        if self.table_name:
            if hasattr(self.table_name, 'to_alipay_dict'):
                params['table_name'] = self.table_name.to_alipay_dict()
            else:
                params['table_name'] = self.table_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CodeExtBean()
        if 'ch_info' in d:
            o.ch_info = d['ch_info']
        if 'code_token' in d:
            o.code_token = d['code_token']
        if 'code_type' in d:
            o.code_type = d['code_type']
        if 'table_name' in d:
            o.table_name = d['table_name']
        return o


