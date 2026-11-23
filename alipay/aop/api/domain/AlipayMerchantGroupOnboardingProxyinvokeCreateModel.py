#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMerchantGroupOnboardingProxyinvokeCreateModel(object):

    def __init__(self):
        self._isv_app_id = None
        self._isv_pid = None
        self._leads_id = None
        self._march_type = None
        self._merchant_pid = None
        self._unique_biz_id = None

    @property
    def isv_app_id(self):
        return self._isv_app_id

    @isv_app_id.setter
    def isv_app_id(self, value):
        self._isv_app_id = value
    @property
    def isv_pid(self):
        return self._isv_pid

    @isv_pid.setter
    def isv_pid(self, value):
        self._isv_pid = value
    @property
    def leads_id(self):
        return self._leads_id

    @leads_id.setter
    def leads_id(self, value):
        self._leads_id = value
    @property
    def march_type(self):
        return self._march_type

    @march_type.setter
    def march_type(self, value):
        self._march_type = value
    @property
    def merchant_pid(self):
        return self._merchant_pid

    @merchant_pid.setter
    def merchant_pid(self, value):
        self._merchant_pid = value
    @property
    def unique_biz_id(self):
        return self._unique_biz_id

    @unique_biz_id.setter
    def unique_biz_id(self, value):
        self._unique_biz_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.isv_app_id:
            if hasattr(self.isv_app_id, 'to_alipay_dict'):
                params['isv_app_id'] = self.isv_app_id.to_alipay_dict()
            else:
                params['isv_app_id'] = self.isv_app_id
        if self.isv_pid:
            if hasattr(self.isv_pid, 'to_alipay_dict'):
                params['isv_pid'] = self.isv_pid.to_alipay_dict()
            else:
                params['isv_pid'] = self.isv_pid
        if self.leads_id:
            if hasattr(self.leads_id, 'to_alipay_dict'):
                params['leads_id'] = self.leads_id.to_alipay_dict()
            else:
                params['leads_id'] = self.leads_id
        if self.march_type:
            if hasattr(self.march_type, 'to_alipay_dict'):
                params['march_type'] = self.march_type.to_alipay_dict()
            else:
                params['march_type'] = self.march_type
        if self.merchant_pid:
            if hasattr(self.merchant_pid, 'to_alipay_dict'):
                params['merchant_pid'] = self.merchant_pid.to_alipay_dict()
            else:
                params['merchant_pid'] = self.merchant_pid
        if self.unique_biz_id:
            if hasattr(self.unique_biz_id, 'to_alipay_dict'):
                params['unique_biz_id'] = self.unique_biz_id.to_alipay_dict()
            else:
                params['unique_biz_id'] = self.unique_biz_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMerchantGroupOnboardingProxyinvokeCreateModel()
        if 'isv_app_id' in d:
            o.isv_app_id = d['isv_app_id']
        if 'isv_pid' in d:
            o.isv_pid = d['isv_pid']
        if 'leads_id' in d:
            o.leads_id = d['leads_id']
        if 'march_type' in d:
            o.march_type = d['march_type']
        if 'merchant_pid' in d:
            o.merchant_pid = d['merchant_pid']
        if 'unique_biz_id' in d:
            o.unique_biz_id = d['unique_biz_id']
        return o


