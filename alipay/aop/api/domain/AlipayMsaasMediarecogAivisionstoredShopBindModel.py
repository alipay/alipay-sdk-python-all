#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMsaasMediarecogAivisionstoredShopBindModel(object):

    def __init__(self):
        self._device_sn = None
        self._isv_pid = None
        self._shop_pid = None

    @property
    def device_sn(self):
        return self._device_sn

    @device_sn.setter
    def device_sn(self, value):
        self._device_sn = value
    @property
    def isv_pid(self):
        return self._isv_pid

    @isv_pid.setter
    def isv_pid(self, value):
        self._isv_pid = value
    @property
    def shop_pid(self):
        return self._shop_pid

    @shop_pid.setter
    def shop_pid(self, value):
        self._shop_pid = value


    def to_alipay_dict(self):
        params = dict()
        if self.device_sn:
            if hasattr(self.device_sn, 'to_alipay_dict'):
                params['device_sn'] = self.device_sn.to_alipay_dict()
            else:
                params['device_sn'] = self.device_sn
        if self.isv_pid:
            if hasattr(self.isv_pid, 'to_alipay_dict'):
                params['isv_pid'] = self.isv_pid.to_alipay_dict()
            else:
                params['isv_pid'] = self.isv_pid
        if self.shop_pid:
            if hasattr(self.shop_pid, 'to_alipay_dict'):
                params['shop_pid'] = self.shop_pid.to_alipay_dict()
            else:
                params['shop_pid'] = self.shop_pid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMsaasMediarecogAivisionstoredShopBindModel()
        if 'device_sn' in d:
            o.device_sn = d['device_sn']
        if 'isv_pid' in d:
            o.isv_pid = d['isv_pid']
        if 'shop_pid' in d:
            o.shop_pid = d['shop_pid']
        return o


