#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DrugDTO(object):

    def __init__(self):
        self._count = None
        self._item_id = None

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        self._count = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.count:
            if hasattr(self.count, 'to_alipay_dict'):
                params['count'] = self.count.to_alipay_dict()
            else:
                params['count'] = self.count
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DrugDTO()
        if 'count' in d:
            o.count = d['count']
        if 'item_id' in d:
            o.item_id = d['item_id']
        return o


