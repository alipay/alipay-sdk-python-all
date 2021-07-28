#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ShopMerchantInfo(object):

    def __init__(self):
        self._isv_mid = None
        self._name = None
        self._pid = None
        self._sign_mode = None
        self._smid = None

    @property
    def isv_mid(self):
        return self._isv_mid

    @isv_mid.setter
    def isv_mid(self, value):
        self._isv_mid = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, value):
        self._pid = value
    @property
    def sign_mode(self):
        return self._sign_mode

    @sign_mode.setter
    def sign_mode(self, value):
        self._sign_mode = value
    @property
    def smid(self):
        return self._smid

    @smid.setter
    def smid(self, value):
        self._smid = value


    def to_alipay_dict(self):
        params = dict()
        if self.isv_mid:
            if hasattr(self.isv_mid, 'to_alipay_dict'):
                params['isv_mid'] = self.isv_mid.to_alipay_dict()
            else:
                params['isv_mid'] = self.isv_mid
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.pid:
            if hasattr(self.pid, 'to_alipay_dict'):
                params['pid'] = self.pid.to_alipay_dict()
            else:
                params['pid'] = self.pid
        if self.sign_mode:
            if hasattr(self.sign_mode, 'to_alipay_dict'):
                params['sign_mode'] = self.sign_mode.to_alipay_dict()
            else:
                params['sign_mode'] = self.sign_mode
        if self.smid:
            if hasattr(self.smid, 'to_alipay_dict'):
                params['smid'] = self.smid.to_alipay_dict()
            else:
                params['smid'] = self.smid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ShopMerchantInfo()
        if 'isv_mid' in d:
            o.isv_mid = d['isv_mid']
        if 'name' in d:
            o.name = d['name']
        if 'pid' in d:
            o.pid = d['pid']
        if 'sign_mode' in d:
            o.sign_mode = d['sign_mode']
        if 'smid' in d:
            o.smid = d['smid']
        return o


