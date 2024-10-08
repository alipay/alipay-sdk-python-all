#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DatabaseTable(object):

    def __init__(self):
        self._database_name = None
        self._table_name_list = None

    @property
    def database_name(self):
        return self._database_name

    @database_name.setter
    def database_name(self, value):
        self._database_name = value
    @property
    def table_name_list(self):
        return self._table_name_list

    @table_name_list.setter
    def table_name_list(self, value):
        if isinstance(value, list):
            self._table_name_list = list()
            for i in value:
                self._table_name_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.database_name:
            if hasattr(self.database_name, 'to_alipay_dict'):
                params['database_name'] = self.database_name.to_alipay_dict()
            else:
                params['database_name'] = self.database_name
        if self.table_name_list:
            if isinstance(self.table_name_list, list):
                for i in range(0, len(self.table_name_list)):
                    element = self.table_name_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.table_name_list[i] = element.to_alipay_dict()
            if hasattr(self.table_name_list, 'to_alipay_dict'):
                params['table_name_list'] = self.table_name_list.to_alipay_dict()
            else:
                params['table_name_list'] = self.table_name_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DatabaseTable()
        if 'database_name' in d:
            o.database_name = d['database_name']
        if 'table_name_list' in d:
            o.table_name_list = d['table_name_list']
        return o


