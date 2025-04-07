#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceHousingApartmentOfflineModel(object):

    def __init__(self):
        self._apartment_id = None
        self._reason = None

    @property
    def apartment_id(self):
        return self._apartment_id

    @apartment_id.setter
    def apartment_id(self, value):
        self._apartment_id = value
    @property
    def reason(self):
        return self._reason

    @reason.setter
    def reason(self, value):
        self._reason = value


    def to_alipay_dict(self):
        params = dict()
        if self.apartment_id:
            if hasattr(self.apartment_id, 'to_alipay_dict'):
                params['apartment_id'] = self.apartment_id.to_alipay_dict()
            else:
                params['apartment_id'] = self.apartment_id
        if self.reason:
            if hasattr(self.reason, 'to_alipay_dict'):
                params['reason'] = self.reason.to_alipay_dict()
            else:
                params['reason'] = self.reason
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceHousingApartmentOfflineModel()
        if 'apartment_id' in d:
            o.apartment_id = d['apartment_id']
        if 'reason' in d:
            o.reason = d['reason']
        return o


