#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TableListResult import TableListResult


class TableInfoResult(object):

    def __init__(self):
        self._table_info_list = None

    @property
    def table_info_list(self):
        return self._table_info_list

    @table_info_list.setter
    def table_info_list(self, value):
        if isinstance(value, list):
            self._table_info_list = list()
            for i in value:
                if isinstance(i, TableListResult):
                    self._table_info_list.append(i)
                else:
                    self._table_info_list.append(TableListResult.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.table_info_list:
            if isinstance(self.table_info_list, list):
                for i in range(0, len(self.table_info_list)):
                    element = self.table_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.table_info_list[i] = element.to_alipay_dict()
            if hasattr(self.table_info_list, 'to_alipay_dict'):
                params['table_info_list'] = self.table_info_list.to_alipay_dict()
            else:
                params['table_info_list'] = self.table_info_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TableInfoResult()
        if 'table_info_list' in d:
            o.table_info_list = d['table_info_list']
        return o


