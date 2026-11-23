#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMsaasMediarecogAiguideItemsyncSyncModel(object):

    def __init__(self):
        self._file_url = None
        self._isv_name = None
        self._isv_pid = None
        self._merchant_id = None
        self._merchant_name = None
        self._n_device_id = None
        self._pos_id = None
        self._pos_name = None
        self._shop_id = None
        self._shop_name = None
        self._sn = None

    @property
    def file_url(self):
        return self._file_url

    @file_url.setter
    def file_url(self, value):
        self._file_url = value
    @property
    def isv_name(self):
        return self._isv_name

    @isv_name.setter
    def isv_name(self, value):
        self._isv_name = value
    @property
    def isv_pid(self):
        return self._isv_pid

    @isv_pid.setter
    def isv_pid(self, value):
        self._isv_pid = value
    @property
    def merchant_id(self):
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, value):
        self._merchant_id = value
    @property
    def merchant_name(self):
        return self._merchant_name

    @merchant_name.setter
    def merchant_name(self, value):
        self._merchant_name = value
    @property
    def n_device_id(self):
        return self._n_device_id

    @n_device_id.setter
    def n_device_id(self, value):
        self._n_device_id = value
    @property
    def pos_id(self):
        return self._pos_id

    @pos_id.setter
    def pos_id(self, value):
        self._pos_id = value
    @property
    def pos_name(self):
        return self._pos_name

    @pos_name.setter
    def pos_name(self, value):
        self._pos_name = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def shop_name(self):
        return self._shop_name

    @shop_name.setter
    def shop_name(self, value):
        self._shop_name = value
    @property
    def sn(self):
        return self._sn

    @sn.setter
    def sn(self, value):
        self._sn = value


    def to_alipay_dict(self):
        params = dict()
        if self.file_url:
            if hasattr(self.file_url, 'to_alipay_dict'):
                params['file_url'] = self.file_url.to_alipay_dict()
            else:
                params['file_url'] = self.file_url
        if self.isv_name:
            if hasattr(self.isv_name, 'to_alipay_dict'):
                params['isv_name'] = self.isv_name.to_alipay_dict()
            else:
                params['isv_name'] = self.isv_name
        if self.isv_pid:
            if hasattr(self.isv_pid, 'to_alipay_dict'):
                params['isv_pid'] = self.isv_pid.to_alipay_dict()
            else:
                params['isv_pid'] = self.isv_pid
        if self.merchant_id:
            if hasattr(self.merchant_id, 'to_alipay_dict'):
                params['merchant_id'] = self.merchant_id.to_alipay_dict()
            else:
                params['merchant_id'] = self.merchant_id
        if self.merchant_name:
            if hasattr(self.merchant_name, 'to_alipay_dict'):
                params['merchant_name'] = self.merchant_name.to_alipay_dict()
            else:
                params['merchant_name'] = self.merchant_name
        if self.n_device_id:
            if hasattr(self.n_device_id, 'to_alipay_dict'):
                params['n_device_id'] = self.n_device_id.to_alipay_dict()
            else:
                params['n_device_id'] = self.n_device_id
        if self.pos_id:
            if hasattr(self.pos_id, 'to_alipay_dict'):
                params['pos_id'] = self.pos_id.to_alipay_dict()
            else:
                params['pos_id'] = self.pos_id
        if self.pos_name:
            if hasattr(self.pos_name, 'to_alipay_dict'):
                params['pos_name'] = self.pos_name.to_alipay_dict()
            else:
                params['pos_name'] = self.pos_name
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.shop_name:
            if hasattr(self.shop_name, 'to_alipay_dict'):
                params['shop_name'] = self.shop_name.to_alipay_dict()
            else:
                params['shop_name'] = self.shop_name
        if self.sn:
            if hasattr(self.sn, 'to_alipay_dict'):
                params['sn'] = self.sn.to_alipay_dict()
            else:
                params['sn'] = self.sn
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMsaasMediarecogAiguideItemsyncSyncModel()
        if 'file_url' in d:
            o.file_url = d['file_url']
        if 'isv_name' in d:
            o.isv_name = d['isv_name']
        if 'isv_pid' in d:
            o.isv_pid = d['isv_pid']
        if 'merchant_id' in d:
            o.merchant_id = d['merchant_id']
        if 'merchant_name' in d:
            o.merchant_name = d['merchant_name']
        if 'n_device_id' in d:
            o.n_device_id = d['n_device_id']
        if 'pos_id' in d:
            o.pos_id = d['pos_id']
        if 'pos_name' in d:
            o.pos_name = d['pos_name']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'shop_name' in d:
            o.shop_name = d['shop_name']
        if 'sn' in d:
            o.sn = d['sn']
        return o


