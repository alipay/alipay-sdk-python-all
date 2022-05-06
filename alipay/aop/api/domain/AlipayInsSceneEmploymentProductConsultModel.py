#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InsCompany import InsCompany


class AlipayInsSceneEmploymentProductConsultModel(object):

    def __init__(self):
        self._channel = None
        self._merchant = None
        self._scene_code = None

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def merchant(self):
        return self._merchant

    @merchant.setter
    def merchant(self, value):
        if isinstance(value, InsCompany):
            self._merchant = value
        else:
            self._merchant = InsCompany.from_alipay_dict(value)
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.merchant:
            if hasattr(self.merchant, 'to_alipay_dict'):
                params['merchant'] = self.merchant.to_alipay_dict()
            else:
                params['merchant'] = self.merchant
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsSceneEmploymentProductConsultModel()
        if 'channel' in d:
            o.channel = d['channel']
        if 'merchant' in d:
            o.merchant = d['merchant']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        return o


