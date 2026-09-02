#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOfflineProviderExpoCheckplaceDeleteModel(object):

    def __init__(self):
        self._activity_code = None
        self._place_id = None

    @property
    def activity_code(self):
        return self._activity_code

    @activity_code.setter
    def activity_code(self, value):
        self._activity_code = value
    @property
    def place_id(self):
        return self._place_id

    @place_id.setter
    def place_id(self, value):
        self._place_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_code:
            if hasattr(self.activity_code, 'to_alipay_dict'):
                params['activity_code'] = self.activity_code.to_alipay_dict()
            else:
                params['activity_code'] = self.activity_code
        if self.place_id:
            if hasattr(self.place_id, 'to_alipay_dict'):
                params['place_id'] = self.place_id.to_alipay_dict()
            else:
                params['place_id'] = self.place_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOfflineProviderExpoCheckplaceDeleteModel()
        if 'activity_code' in d:
            o.activity_code = d['activity_code']
        if 'place_id' in d:
            o.place_id = d['place_id']
        return o


