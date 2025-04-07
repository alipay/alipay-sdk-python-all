#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RentGoodsInfoDTO(object):

    def __init__(self):
        self._item_value = None
        self._rent_model = None
        self._supervised = None

    @property
    def item_value(self):
        return self._item_value

    @item_value.setter
    def item_value(self, value):
        self._item_value = value
    @property
    def rent_model(self):
        return self._rent_model

    @rent_model.setter
    def rent_model(self, value):
        self._rent_model = value
    @property
    def supervised(self):
        return self._supervised

    @supervised.setter
    def supervised(self, value):
        self._supervised = value


    def to_alipay_dict(self):
        params = dict()
        if self.item_value:
            if hasattr(self.item_value, 'to_alipay_dict'):
                params['item_value'] = self.item_value.to_alipay_dict()
            else:
                params['item_value'] = self.item_value
        if self.rent_model:
            if hasattr(self.rent_model, 'to_alipay_dict'):
                params['rent_model'] = self.rent_model.to_alipay_dict()
            else:
                params['rent_model'] = self.rent_model
        if self.supervised:
            if hasattr(self.supervised, 'to_alipay_dict'):
                params['supervised'] = self.supervised.to_alipay_dict()
            else:
                params['supervised'] = self.supervised
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RentGoodsInfoDTO()
        if 'item_value' in d:
            o.item_value = d['item_value']
        if 'rent_model' in d:
            o.rent_model = d['rent_model']
        if 'supervised' in d:
            o.supervised = d['supervised']
        return o


