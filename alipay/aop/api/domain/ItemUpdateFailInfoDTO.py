#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ItemUpdateFailInfoDTO(object):

    def __init__(self):
        self._desc = None
        self._item_code = None

    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def item_code(self):
        return self._item_code

    @item_code.setter
    def item_code(self, value):
        self._item_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
        if self.item_code:
            if hasattr(self.item_code, 'to_alipay_dict'):
                params['item_code'] = self.item_code.to_alipay_dict()
            else:
                params['item_code'] = self.item_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ItemUpdateFailInfoDTO()
        if 'desc' in d:
            o.desc = d['desc']
        if 'item_code' in d:
            o.item_code = d['item_code']
        return o


