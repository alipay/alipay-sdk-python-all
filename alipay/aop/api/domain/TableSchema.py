#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ColumnDefinition import ColumnDefinition


class TableSchema(object):

    def __init__(self):
        self._columns = None
        self._description = None
        self._name = None

    @property
    def columns(self):
        return self._columns

    @columns.setter
    def columns(self, value):
        if isinstance(value, list):
            self._columns = list()
            for i in value:
                if isinstance(i, ColumnDefinition):
                    self._columns.append(i)
                else:
                    self._columns.append(ColumnDefinition.from_alipay_dict(i))
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


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
        if self.description:
            if hasattr(self.description, 'to_alipay_dict'):
                params['description'] = self.description.to_alipay_dict()
            else:
                params['description'] = self.description
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
        o = TableSchema()
        if 'columns' in d:
            o.columns = d['columns']
        if 'description' in d:
            o.description = d['description']
        if 'name' in d:
            o.name = d['name']
        return o


