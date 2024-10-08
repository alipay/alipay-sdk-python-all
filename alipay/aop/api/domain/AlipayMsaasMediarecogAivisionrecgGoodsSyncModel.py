#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMsaasMediarecogAivisionrecgGoodsSyncModel(object):

    def __init__(self):
        self._goods_data_file_url = None
        self._isv_id = None
        self._isv_name = None
        self._merchant_id = None
        self._merchant_name = None

    @property
    def goods_data_file_url(self):
        return self._goods_data_file_url

    @goods_data_file_url.setter
    def goods_data_file_url(self, value):
        self._goods_data_file_url = value
    @property
    def isv_id(self):
        return self._isv_id

    @isv_id.setter
    def isv_id(self, value):
        self._isv_id = value
    @property
    def isv_name(self):
        return self._isv_name

    @isv_name.setter
    def isv_name(self, value):
        self._isv_name = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.goods_data_file_url:
            if hasattr(self.goods_data_file_url, 'to_alipay_dict'):
                params['goods_data_file_url'] = self.goods_data_file_url.to_alipay_dict()
            else:
                params['goods_data_file_url'] = self.goods_data_file_url
        if self.isv_id:
            if hasattr(self.isv_id, 'to_alipay_dict'):
                params['isv_id'] = self.isv_id.to_alipay_dict()
            else:
                params['isv_id'] = self.isv_id
        if self.isv_name:
            if hasattr(self.isv_name, 'to_alipay_dict'):
                params['isv_name'] = self.isv_name.to_alipay_dict()
            else:
                params['isv_name'] = self.isv_name
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMsaasMediarecogAivisionrecgGoodsSyncModel()
        if 'goods_data_file_url' in d:
            o.goods_data_file_url = d['goods_data_file_url']
        if 'isv_id' in d:
            o.isv_id = d['isv_id']
        if 'isv_name' in d:
            o.isv_name = d['isv_name']
        if 'merchant_id' in d:
            o.merchant_id = d['merchant_id']
        if 'merchant_name' in d:
            o.merchant_name = d['merchant_name']
        return o


