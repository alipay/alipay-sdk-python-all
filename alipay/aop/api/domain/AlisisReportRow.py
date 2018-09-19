#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AlisisReportColumn import AlisisReportColumn


class AlisisReportRow(object):

    def __init__(self):
        self._row_data = None

    @property
    def row_data(self):
        return self._row_data

    @row_data.setter
    def row_data(self, value):
        if isinstance(value, list):
            self._row_data = list()
            for i in value:
                if isinstance(i, AlisisReportColumn):
                    self._row_data.append(i)
                else:
                    self._row_data.append(AlisisReportColumn.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.row_data:
            if isinstance(self.row_data, list):
                for i in range(0, len(self.row_data)):
                    element = self.row_data[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.row_data[i] = element.to_alipay_dict()
            if hasattr(self.row_data, 'to_alipay_dict'):
                params['row_data'] = self.row_data.to_alipay_dict()
            else:
                params['row_data'] = self.row_data
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlisisReportRow()
        if 'row_data' in d:
            o.row_data = d['row_data']
        return o


