#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CustomerTag(object):

    def __init__(self):
        self._col_name = None
        self._column_type = None
        self._id = None
        self._name = None

    @property
    def col_name(self):
        return self._col_name

    @col_name.setter
    def col_name(self, value):
        self._col_name = value
    @property
    def column_type(self):
        return self._column_type

    @column_type.setter
    def column_type(self, value):
        self._column_type = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


    def to_alipay_dict(self):
        params = dict()
        if self.col_name:
            if hasattr(self.col_name, 'to_alipay_dict'):
                params['col_name'] = self.col_name.to_alipay_dict()
            else:
                params['col_name'] = self.col_name
        if self.column_type:
            if hasattr(self.column_type, 'to_alipay_dict'):
                params['column_type'] = self.column_type.to_alipay_dict()
            else:
                params['column_type'] = self.column_type
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CustomerTag()
        if 'col_name' in d:
            o.col_name = d['col_name']
        if 'column_type' in d:
            o.column_type = d['column_type']
        if 'id' in d:
            o.id = d['id']
        if 'name' in d:
            o.name = d['name']
        return o


