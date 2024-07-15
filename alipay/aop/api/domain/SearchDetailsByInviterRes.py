#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SearchDetailsByInviterResItem import SearchDetailsByInviterResItem


class SearchDetailsByInviterRes(object):

    def __init__(self):
        self._res_items = None

    @property
    def res_items(self):
        return self._res_items

    @res_items.setter
    def res_items(self, value):
        if isinstance(value, list):
            self._res_items = list()
            for i in value:
                if isinstance(i, SearchDetailsByInviterResItem):
                    self._res_items.append(i)
                else:
                    self._res_items.append(SearchDetailsByInviterResItem.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.res_items:
            if isinstance(self.res_items, list):
                for i in range(0, len(self.res_items)):
                    element = self.res_items[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.res_items[i] = element.to_alipay_dict()
            if hasattr(self.res_items, 'to_alipay_dict'):
                params['res_items'] = self.res_items.to_alipay_dict()
            else:
                params['res_items'] = self.res_items
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SearchDetailsByInviterRes()
        if 'res_items' in d:
            o.res_items = d['res_items']
        return o


