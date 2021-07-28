#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class HbMerchantInfo(object):

    def __init__(self):
        self._acquire_mode = None
        self._merchant_type = None
        self._origin_config_info = None

    @property
    def acquire_mode(self):
        return self._acquire_mode

    @acquire_mode.setter
    def acquire_mode(self, value):
        self._acquire_mode = value
    @property
    def merchant_type(self):
        return self._merchant_type

    @merchant_type.setter
    def merchant_type(self, value):
        self._merchant_type = value
    @property
    def origin_config_info(self):
        return self._origin_config_info

    @origin_config_info.setter
    def origin_config_info(self, value):
        self._origin_config_info = value


    def to_alipay_dict(self):
        params = dict()
        if self.acquire_mode:
            if hasattr(self.acquire_mode, 'to_alipay_dict'):
                params['acquire_mode'] = self.acquire_mode.to_alipay_dict()
            else:
                params['acquire_mode'] = self.acquire_mode
        if self.merchant_type:
            if hasattr(self.merchant_type, 'to_alipay_dict'):
                params['merchant_type'] = self.merchant_type.to_alipay_dict()
            else:
                params['merchant_type'] = self.merchant_type
        if self.origin_config_info:
            if hasattr(self.origin_config_info, 'to_alipay_dict'):
                params['origin_config_info'] = self.origin_config_info.to_alipay_dict()
            else:
                params['origin_config_info'] = self.origin_config_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = HbMerchantInfo()
        if 'acquire_mode' in d:
            o.acquire_mode = d['acquire_mode']
        if 'merchant_type' in d:
            o.merchant_type = d['merchant_type']
        if 'origin_config_info' in d:
            o.origin_config_info = d['origin_config_info']
        return o


