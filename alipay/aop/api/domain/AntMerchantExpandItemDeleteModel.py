#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntMerchantExpandItemDeleteModel(object):

    def __init__(self):
        self._external_item_id = None
        self._item_id = None

    @property
    def external_item_id(self):
        return self._external_item_id

    @external_item_id.setter
    def external_item_id(self, value):
        self._external_item_id = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.external_item_id:
            if hasattr(self.external_item_id, 'to_alipay_dict'):
                params['external_item_id'] = self.external_item_id.to_alipay_dict()
            else:
                params['external_item_id'] = self.external_item_id
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
        o = AntMerchantExpandItemDeleteModel()
        if 'external_item_id' in d:
            o.external_item_id = d['external_item_id']
        if 'item_id' in d:
            o.item_id = d['item_id']
        return o


