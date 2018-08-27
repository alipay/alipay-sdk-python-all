#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AiOcrTableContext import AiOcrTableContext


class AiOcrTableRow(object):

    def __init__(self):
        self._row = None

    @property
    def row(self):
        return self._row

    @row.setter
    def row(self, value):
        if isinstance(value, list):
            self._row = list()
            for i in value:
                if isinstance(i, AiOcrTableContext):
                    self._row.append(i)
                else:
                    self._row.append(AiOcrTableContext.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.row:
            if isinstance(self.row, list):
                for i in range(0, len(self.row)):
                    element = self.row[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.row[i] = element.to_alipay_dict()
            if hasattr(self.row, 'to_alipay_dict'):
                params['row'] = self.row.to_alipay_dict()
            else:
                params['row'] = self.row
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AiOcrTableRow()
        if 'row' in d:
            o.row = d['row']
        return o


