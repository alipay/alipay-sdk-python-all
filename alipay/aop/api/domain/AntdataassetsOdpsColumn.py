#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntdataassetsOdpsColumn(object):

    def __init__(self):
        self._column_name = None
        self._column_type = None

    @property
    def column_name(self):
        return self._column_name

    @column_name.setter
    def column_name(self, value):
        self._column_name = value
    @property
    def column_type(self):
        return self._column_type

    @column_type.setter
    def column_type(self, value):
        self._column_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.column_name:
            if hasattr(self.column_name, 'to_alipay_dict'):
                params['column_name'] = self.column_name.to_alipay_dict()
            else:
                params['column_name'] = self.column_name
        if self.column_type:
            if hasattr(self.column_type, 'to_alipay_dict'):
                params['column_type'] = self.column_type.to_alipay_dict()
            else:
                params['column_type'] = self.column_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntdataassetsOdpsColumn()
        if 'column_name' in d:
            o.column_name = d['column_name']
        if 'column_type' in d:
            o.column_type = d['column_type']
        return o


