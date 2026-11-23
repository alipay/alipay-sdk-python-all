#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMsaasMediarecogAivisionstoredShopUpgradeModel(object):

    def __init__(self):
        self._isv_pid = None
        self._shop_name = None
        self._shop_pid = None

    @property
    def isv_pid(self):
        return self._isv_pid

    @isv_pid.setter
    def isv_pid(self, value):
        self._isv_pid = value
    @property
    def shop_name(self):
        return self._shop_name

    @shop_name.setter
    def shop_name(self, value):
        self._shop_name = value
    @property
    def shop_pid(self):
        return self._shop_pid

    @shop_pid.setter
    def shop_pid(self, value):
        self._shop_pid = value


    def to_alipay_dict(self):
        params = dict()
        if self.isv_pid:
            if hasattr(self.isv_pid, 'to_alipay_dict'):
                params['isv_pid'] = self.isv_pid.to_alipay_dict()
            else:
                params['isv_pid'] = self.isv_pid
        if self.shop_name:
            if hasattr(self.shop_name, 'to_alipay_dict'):
                params['shop_name'] = self.shop_name.to_alipay_dict()
            else:
                params['shop_name'] = self.shop_name
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
        o = AlipayMsaasMediarecogAivisionstoredShopUpgradeModel()
        if 'isv_pid' in d:
            o.isv_pid = d['isv_pid']
        if 'shop_name' in d:
            o.shop_name = d['shop_name']
        if 'shop_pid' in d:
            o.shop_pid = d['shop_pid']
        return o


