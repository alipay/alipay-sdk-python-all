#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceHousingHouseOfflineModel(object):

    def __init__(self):
        self._house_source = None
        self._housing_id = None
        self._reason = None

    @property
    def house_source(self):
        return self._house_source

    @house_source.setter
    def house_source(self, value):
        self._house_source = value
    @property
    def housing_id(self):
        return self._housing_id

    @housing_id.setter
    def housing_id(self, value):
        self._housing_id = value
    @property
    def reason(self):
        return self._reason

    @reason.setter
    def reason(self, value):
        self._reason = value


    def to_alipay_dict(self):
        params = dict()
        if self.house_source:
            if hasattr(self.house_source, 'to_alipay_dict'):
                params['house_source'] = self.house_source.to_alipay_dict()
            else:
                params['house_source'] = self.house_source
        if self.housing_id:
            if hasattr(self.housing_id, 'to_alipay_dict'):
                params['housing_id'] = self.housing_id.to_alipay_dict()
            else:
                params['housing_id'] = self.housing_id
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
        o = AlipayCommerceHousingHouseOfflineModel()
        if 'house_source' in d:
            o.house_source = d['house_source']
        if 'housing_id' in d:
            o.housing_id = d['housing_id']
        if 'reason' in d:
            o.reason = d['reason']
        return o


