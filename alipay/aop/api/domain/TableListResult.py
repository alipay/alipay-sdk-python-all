#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TableListResult(object):

    def __init__(self):
        self._table_name = None
        self._table_num = None

    @property
    def table_name(self):
        return self._table_name

    @table_name.setter
    def table_name(self, value):
        self._table_name = value
    @property
    def table_num(self):
        return self._table_num

    @table_num.setter
    def table_num(self, value):
        self._table_num = value


    def to_alipay_dict(self):
        params = dict()
        if self.table_name:
            if hasattr(self.table_name, 'to_alipay_dict'):
                params['table_name'] = self.table_name.to_alipay_dict()
            else:
                params['table_name'] = self.table_name
        if self.table_num:
            if hasattr(self.table_num, 'to_alipay_dict'):
                params['table_num'] = self.table_num.to_alipay_dict()
            else:
                params['table_num'] = self.table_num
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TableListResult()
        if 'table_name' in d:
            o.table_name = d['table_name']
        if 'table_num' in d:
            o.table_num = d['table_num']
        return o


