#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AxfMerchantConfig import AxfMerchantConfig


class AlipayCommerceMerchantcardConfigModifyModel(object):

    def __init__(self):
        self._axf_merchant_config = None

    @property
    def axf_merchant_config(self):
        return self._axf_merchant_config

    @axf_merchant_config.setter
    def axf_merchant_config(self, value):
        if isinstance(value, AxfMerchantConfig):
            self._axf_merchant_config = value
        else:
            self._axf_merchant_config = AxfMerchantConfig.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.axf_merchant_config:
            if hasattr(self.axf_merchant_config, 'to_alipay_dict'):
                params['axf_merchant_config'] = self.axf_merchant_config.to_alipay_dict()
            else:
                params['axf_merchant_config'] = self.axf_merchant_config
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMerchantcardConfigModifyModel()
        if 'axf_merchant_config' in d:
            o.axf_merchant_config = d['axf_merchant_config']
        return o


