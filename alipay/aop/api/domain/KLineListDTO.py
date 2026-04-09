#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.KLineDTO import KLineDTO


class KLineListDTO(object):

    def __init__(self):
        self._items = None

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        if isinstance(value, KLineDTO):
            self._items = value
        else:
            self._items = KLineDTO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.items:
            if hasattr(self.items, 'to_alipay_dict'):
                params['items'] = self.items.to_alipay_dict()
            else:
                params['items'] = self.items
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KLineListDTO()
        if 'items' in d:
            o.items = d['items']
        return o


