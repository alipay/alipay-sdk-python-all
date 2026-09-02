#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ReceiptIdentityInfo(object):

    def __init__(self):
        self._identity_name = None
        self._pid = None
        self._shop_id = None

    @property
    def identity_name(self):
        return self._identity_name

    @identity_name.setter
    def identity_name(self, value):
        self._identity_name = value
    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, value):
        self._pid = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.identity_name:
            if hasattr(self.identity_name, 'to_alipay_dict'):
                params['identity_name'] = self.identity_name.to_alipay_dict()
            else:
                params['identity_name'] = self.identity_name
        if self.pid:
            if hasattr(self.pid, 'to_alipay_dict'):
                params['pid'] = self.pid.to_alipay_dict()
            else:
                params['pid'] = self.pid
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ReceiptIdentityInfo()
        if 'identity_name' in d:
            o.identity_name = d['identity_name']
        if 'pid' in d:
            o.pid = d['pid']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        return o


