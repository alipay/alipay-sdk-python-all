#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceHousingApartmentOnlineModel(object):

    def __init__(self):
        self._apartment_id = None

    @property
    def apartment_id(self):
        return self._apartment_id

    @apartment_id.setter
    def apartment_id(self, value):
        self._apartment_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.apartment_id:
            if hasattr(self.apartment_id, 'to_alipay_dict'):
                params['apartment_id'] = self.apartment_id.to_alipay_dict()
            else:
                params['apartment_id'] = self.apartment_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceHousingApartmentOnlineModel()
        if 'apartment_id' in d:
            o.apartment_id = d['apartment_id']
        return o


