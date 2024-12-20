#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RentCarTableInfo import RentCarTableInfo


class RentCarGuaranteeSubDetailDescription(object):

    def __init__(self):
        self._desc = None
        self._table = None
        self._title = None

    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def table(self):
        return self._table

    @table.setter
    def table(self, value):
        if isinstance(value, list):
            self._table = list()
            for i in value:
                if isinstance(i, RentCarTableInfo):
                    self._table.append(i)
                else:
                    self._table.append(RentCarTableInfo.from_alipay_dict(i))
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
        if self.table:
            if isinstance(self.table, list):
                for i in range(0, len(self.table)):
                    element = self.table[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.table[i] = element.to_alipay_dict()
            if hasattr(self.table, 'to_alipay_dict'):
                params['table'] = self.table.to_alipay_dict()
            else:
                params['table'] = self.table
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RentCarGuaranteeSubDetailDescription()
        if 'desc' in d:
            o.desc = d['desc']
        if 'table' in d:
            o.table = d['table']
        if 'title' in d:
            o.title = d['title']
        return o


