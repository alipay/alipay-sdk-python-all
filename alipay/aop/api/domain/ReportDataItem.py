#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ReportDataItem(object):

    def __init__(self):
        self._row_data = None

    @property
    def row_data(self):
        return self._row_data

    @row_data.setter
    def row_data(self, value):
        self._row_data = value


    def to_alipay_dict(self):
        params = dict()
        if self.row_data:
            if hasattr(self.row_data, 'to_alipay_dict'):
                params['row_data'] = self.row_data.to_alipay_dict()
            else:
                params['row_data'] = self.row_data
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ReportDataItem()
        if 'row_data' in d:
            o.row_data = d['row_data']
        return o


