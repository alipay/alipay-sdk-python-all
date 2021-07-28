#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class QrCodeBusinessParam(object):

    def __init__(self):
        self._merchant_pid = None
        self._merchant_smid = None
        self._merhcant_name = None
        self._shop_address = None
        self._shop_id = None
        self._store_id = None
        self._store_name = None

    @property
    def merchant_pid(self):
        return self._merchant_pid

    @merchant_pid.setter
    def merchant_pid(self, value):
        self._merchant_pid = value
    @property
    def merchant_smid(self):
        return self._merchant_smid

    @merchant_smid.setter
    def merchant_smid(self, value):
        self._merchant_smid = value
    @property
    def merhcant_name(self):
        return self._merhcant_name

    @merhcant_name.setter
    def merhcant_name(self, value):
        self._merhcant_name = value
    @property
    def shop_address(self):
        return self._shop_address

    @shop_address.setter
    def shop_address(self, value):
        self._shop_address = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def store_id(self):
        return self._store_id

    @store_id.setter
    def store_id(self, value):
        self._store_id = value
    @property
    def store_name(self):
        return self._store_name

    @store_name.setter
    def store_name(self, value):
        self._store_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.merchant_pid:
            if hasattr(self.merchant_pid, 'to_alipay_dict'):
                params['merchant_pid'] = self.merchant_pid.to_alipay_dict()
            else:
                params['merchant_pid'] = self.merchant_pid
        if self.merchant_smid:
            if hasattr(self.merchant_smid, 'to_alipay_dict'):
                params['merchant_smid'] = self.merchant_smid.to_alipay_dict()
            else:
                params['merchant_smid'] = self.merchant_smid
        if self.merhcant_name:
            if hasattr(self.merhcant_name, 'to_alipay_dict'):
                params['merhcant_name'] = self.merhcant_name.to_alipay_dict()
            else:
                params['merhcant_name'] = self.merhcant_name
        if self.shop_address:
            if hasattr(self.shop_address, 'to_alipay_dict'):
                params['shop_address'] = self.shop_address.to_alipay_dict()
            else:
                params['shop_address'] = self.shop_address
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.store_id:
            if hasattr(self.store_id, 'to_alipay_dict'):
                params['store_id'] = self.store_id.to_alipay_dict()
            else:
                params['store_id'] = self.store_id
        if self.store_name:
            if hasattr(self.store_name, 'to_alipay_dict'):
                params['store_name'] = self.store_name.to_alipay_dict()
            else:
                params['store_name'] = self.store_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = QrCodeBusinessParam()
        if 'merchant_pid' in d:
            o.merchant_pid = d['merchant_pid']
        if 'merchant_smid' in d:
            o.merchant_smid = d['merchant_smid']
        if 'merhcant_name' in d:
            o.merhcant_name = d['merhcant_name']
        if 'shop_address' in d:
            o.shop_address = d['shop_address']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'store_id' in d:
            o.store_id = d['store_id']
        if 'store_name' in d:
            o.store_name = d['store_name']
        return o


