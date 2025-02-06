#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenSpCommissionDetailQueryModel(object):

    def __init__(self):
        self._commission_scene = None
        self._merchant_id = None
        self._merchant_logon_id = None

    @property
    def commission_scene(self):
        return self._commission_scene

    @commission_scene.setter
    def commission_scene(self, value):
        self._commission_scene = value
    @property
    def merchant_id(self):
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, value):
        self._merchant_id = value
    @property
    def merchant_logon_id(self):
        return self._merchant_logon_id

    @merchant_logon_id.setter
    def merchant_logon_id(self, value):
        self._merchant_logon_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.commission_scene:
            if hasattr(self.commission_scene, 'to_alipay_dict'):
                params['commission_scene'] = self.commission_scene.to_alipay_dict()
            else:
                params['commission_scene'] = self.commission_scene
        if self.merchant_id:
            if hasattr(self.merchant_id, 'to_alipay_dict'):
                params['merchant_id'] = self.merchant_id.to_alipay_dict()
            else:
                params['merchant_id'] = self.merchant_id
        if self.merchant_logon_id:
            if hasattr(self.merchant_logon_id, 'to_alipay_dict'):
                params['merchant_logon_id'] = self.merchant_logon_id.to_alipay_dict()
            else:
                params['merchant_logon_id'] = self.merchant_logon_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenSpCommissionDetailQueryModel()
        if 'commission_scene' in d:
            o.commission_scene = d['commission_scene']
        if 'merchant_id' in d:
            o.merchant_id = d['merchant_id']
        if 'merchant_logon_id' in d:
            o.merchant_logon_id = d['merchant_logon_id']
        return o


