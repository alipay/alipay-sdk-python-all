#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ItemConsultInfo(object):

    def __init__(self):
        self._item_id = None
        self._promo_amount = None
        self._promo_count = None

    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def promo_amount(self):
        return self._promo_amount

    @promo_amount.setter
    def promo_amount(self, value):
        self._promo_amount = value
    @property
    def promo_count(self):
        return self._promo_count

    @promo_count.setter
    def promo_count(self, value):
        self._promo_count = value


    def to_alipay_dict(self):
        params = dict()
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.promo_amount:
            if hasattr(self.promo_amount, 'to_alipay_dict'):
                params['promo_amount'] = self.promo_amount.to_alipay_dict()
            else:
                params['promo_amount'] = self.promo_amount
        if self.promo_count:
            if hasattr(self.promo_count, 'to_alipay_dict'):
                params['promo_count'] = self.promo_count.to_alipay_dict()
            else:
                params['promo_count'] = self.promo_count
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ItemConsultInfo()
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'promo_amount' in d:
            o.promo_amount = d['promo_amount']
        if 'promo_count' in d:
            o.promo_count = d['promo_count']
        return o


