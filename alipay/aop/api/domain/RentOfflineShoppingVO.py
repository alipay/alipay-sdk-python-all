#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RentOfflineShoppingVO(object):

    def __init__(self):
        self._relate_rent_order_id = None
        self._relate_shopping_order_id = None

    @property
    def relate_rent_order_id(self):
        return self._relate_rent_order_id

    @relate_rent_order_id.setter
    def relate_rent_order_id(self, value):
        self._relate_rent_order_id = value
    @property
    def relate_shopping_order_id(self):
        return self._relate_shopping_order_id

    @relate_shopping_order_id.setter
    def relate_shopping_order_id(self, value):
        self._relate_shopping_order_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.relate_rent_order_id:
            if hasattr(self.relate_rent_order_id, 'to_alipay_dict'):
                params['relate_rent_order_id'] = self.relate_rent_order_id.to_alipay_dict()
            else:
                params['relate_rent_order_id'] = self.relate_rent_order_id
        if self.relate_shopping_order_id:
            if hasattr(self.relate_shopping_order_id, 'to_alipay_dict'):
                params['relate_shopping_order_id'] = self.relate_shopping_order_id.to_alipay_dict()
            else:
                params['relate_shopping_order_id'] = self.relate_shopping_order_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RentOfflineShoppingVO()
        if 'relate_rent_order_id' in d:
            o.relate_rent_order_id = d['relate_rent_order_id']
        if 'relate_shopping_order_id' in d:
            o.relate_shopping_order_id = d['relate_shopping_order_id']
        return o


