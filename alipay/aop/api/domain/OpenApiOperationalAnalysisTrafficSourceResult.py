#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OpenApiOperationAnalysisTrafficSourceAliasDTO import OpenApiOperationAnalysisTrafficSourceAliasDTO


class OpenApiOperationalAnalysisTrafficSourceResult(object):

    def __init__(self):
        self._items = None

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        if isinstance(value, list):
            self._items = list()
            for i in value:
                if isinstance(i, OpenApiOperationAnalysisTrafficSourceAliasDTO):
                    self._items.append(i)
                else:
                    self._items.append(OpenApiOperationAnalysisTrafficSourceAliasDTO.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.items:
            if isinstance(self.items, list):
                for i in range(0, len(self.items)):
                    element = self.items[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.items[i] = element.to_alipay_dict()
            if hasattr(self.items, 'to_alipay_dict'):
                params['items'] = self.items.to_alipay_dict()
            else:
                params['items'] = self.items
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenApiOperationalAnalysisTrafficSourceResult()
        if 'items' in d:
            o.items = d['items']
        return o


