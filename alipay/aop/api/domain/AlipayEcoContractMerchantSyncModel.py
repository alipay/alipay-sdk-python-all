#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MerchantConfigRequest import MerchantConfigRequest


class AlipayEcoContractMerchantSyncModel(object):

    def __init__(self):
        self._batch_no = None
        self._merchant_configs = None
        self._sign_platform_code = None

    @property
    def batch_no(self):
        return self._batch_no

    @batch_no.setter
    def batch_no(self, value):
        self._batch_no = value
    @property
    def merchant_configs(self):
        return self._merchant_configs

    @merchant_configs.setter
    def merchant_configs(self, value):
        if isinstance(value, list):
            self._merchant_configs = list()
            for i in value:
                if isinstance(i, MerchantConfigRequest):
                    self._merchant_configs.append(i)
                else:
                    self._merchant_configs.append(MerchantConfigRequest.from_alipay_dict(i))
    @property
    def sign_platform_code(self):
        return self._sign_platform_code

    @sign_platform_code.setter
    def sign_platform_code(self, value):
        self._sign_platform_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.batch_no:
            if hasattr(self.batch_no, 'to_alipay_dict'):
                params['batch_no'] = self.batch_no.to_alipay_dict()
            else:
                params['batch_no'] = self.batch_no
        if self.merchant_configs:
            if isinstance(self.merchant_configs, list):
                for i in range(0, len(self.merchant_configs)):
                    element = self.merchant_configs[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.merchant_configs[i] = element.to_alipay_dict()
            if hasattr(self.merchant_configs, 'to_alipay_dict'):
                params['merchant_configs'] = self.merchant_configs.to_alipay_dict()
            else:
                params['merchant_configs'] = self.merchant_configs
        if self.sign_platform_code:
            if hasattr(self.sign_platform_code, 'to_alipay_dict'):
                params['sign_platform_code'] = self.sign_platform_code.to_alipay_dict()
            else:
                params['sign_platform_code'] = self.sign_platform_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoContractMerchantSyncModel()
        if 'batch_no' in d:
            o.batch_no = d['batch_no']
        if 'merchant_configs' in d:
            o.merchant_configs = d['merchant_configs']
        if 'sign_platform_code' in d:
            o.sign_platform_code = d['sign_platform_code']
        return o


