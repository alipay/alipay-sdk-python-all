#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceHousingHouseSaleQueryModel(object):

    def __init__(self):
        self._external_id = None
        self._housing_id = None

    @property
    def external_id(self):
        return self._external_id

    @external_id.setter
    def external_id(self, value):
        self._external_id = value
    @property
    def housing_id(self):
        return self._housing_id

    @housing_id.setter
    def housing_id(self, value):
        self._housing_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.external_id:
            if hasattr(self.external_id, 'to_alipay_dict'):
                params['external_id'] = self.external_id.to_alipay_dict()
            else:
                params['external_id'] = self.external_id
        if self.housing_id:
            if hasattr(self.housing_id, 'to_alipay_dict'):
                params['housing_id'] = self.housing_id.to_alipay_dict()
            else:
                params['housing_id'] = self.housing_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceHousingHouseSaleQueryModel()
        if 'external_id' in d:
            o.external_id = d['external_id']
        if 'housing_id' in d:
            o.housing_id = d['housing_id']
        return o


