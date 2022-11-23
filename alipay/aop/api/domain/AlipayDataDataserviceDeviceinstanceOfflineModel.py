#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataDataserviceDeviceinstanceOfflineModel(object):

    def __init__(self):
        self._biz_token = None
        self._device_instance_id = None

    @property
    def biz_token(self):
        return self._biz_token

    @biz_token.setter
    def biz_token(self, value):
        self._biz_token = value
    @property
    def device_instance_id(self):
        return self._device_instance_id

    @device_instance_id.setter
    def device_instance_id(self, value):
        self._device_instance_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_token:
            if hasattr(self.biz_token, 'to_alipay_dict'):
                params['biz_token'] = self.biz_token.to_alipay_dict()
            else:
                params['biz_token'] = self.biz_token
        if self.device_instance_id:
            if hasattr(self.device_instance_id, 'to_alipay_dict'):
                params['device_instance_id'] = self.device_instance_id.to_alipay_dict()
            else:
                params['device_instance_id'] = self.device_instance_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataserviceDeviceinstanceOfflineModel()
        if 'biz_token' in d:
            o.biz_token = d['biz_token']
        if 'device_instance_id' in d:
            o.device_instance_id = d['device_instance_id']
        return o


