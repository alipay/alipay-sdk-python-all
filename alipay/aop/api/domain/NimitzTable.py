#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.NimitzColumn import NimitzColumn


class NimitzTable(object):

    def __init__(self):
        self._columns = None

    @property
    def columns(self):
        return self._columns

    @columns.setter
    def columns(self, value):
        if isinstance(value, list):
            self._columns = list()
            for i in value:
                if isinstance(i, NimitzColumn):
                    self._columns.append(i)
                else:
                    self._columns.append(NimitzColumn.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.columns:
            if isinstance(self.columns, list):
                for i in range(0, len(self.columns)):
                    element = self.columns[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.columns[i] = element.to_alipay_dict()
            if hasattr(self.columns, 'to_alipay_dict'):
                params['columns'] = self.columns.to_alipay_dict()
            else:
                params['columns'] = self.columns
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = NimitzTable()
        if 'columns' in d:
            o.columns = d['columns']
        return o


