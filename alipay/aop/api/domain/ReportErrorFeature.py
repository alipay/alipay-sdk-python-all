#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ReportErrorFeature(object):

    def __init__(self):
        self._table_num = None

    @property
    def table_num(self):
        return self._table_num

    @table_num.setter
    def table_num(self, value):
        self._table_num = value


    def to_alipay_dict(self):
        params = dict()
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
        o = ReportErrorFeature()
        if 'table_num' in d:
            o.table_num = d['table_num']
        return o


