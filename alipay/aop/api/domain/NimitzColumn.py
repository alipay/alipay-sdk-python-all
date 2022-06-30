#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.NimitzCell import NimitzCell


class NimitzColumn(object):

    def __init__(self):
        self._cells = None
        self._kind = None
        self._name = None

    @property
    def cells(self):
        return self._cells

    @cells.setter
    def cells(self, value):
        if isinstance(value, list):
            self._cells = list()
            for i in value:
                if isinstance(i, NimitzCell):
                    self._cells.append(i)
                else:
                    self._cells.append(NimitzCell.from_alipay_dict(i))
    @property
    def kind(self):
        return self._kind

    @kind.setter
    def kind(self, value):
        self._kind = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


    def to_alipay_dict(self):
        params = dict()
        if self.cells:
            if isinstance(self.cells, list):
                for i in range(0, len(self.cells)):
                    element = self.cells[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.cells[i] = element.to_alipay_dict()
            if hasattr(self.cells, 'to_alipay_dict'):
                params['cells'] = self.cells.to_alipay_dict()
            else:
                params['cells'] = self.cells
        if self.kind:
            if hasattr(self.kind, 'to_alipay_dict'):
                params['kind'] = self.kind.to_alipay_dict()
            else:
                params['kind'] = self.kind
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
        o = NimitzColumn()
        if 'cells' in d:
            o.cells = d['cells']
        if 'kind' in d:
            o.kind = d['kind']
        if 'name' in d:
            o.name = d['name']
        return o


