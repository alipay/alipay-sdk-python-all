#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOfflineProviderIndirectisvActivityEffectModel(object):

    def __init__(self):
        self._effective_time = None
        self._ext_info = None
        self._merchant_id = None

    @property
    def effective_time(self):
        return self._effective_time

    @effective_time.setter
    def effective_time(self, value):
        self._effective_time = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def merchant_id(self):
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, value):
        self._merchant_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.effective_time:
            if hasattr(self.effective_time, 'to_alipay_dict'):
                params['effective_time'] = self.effective_time.to_alipay_dict()
            else:
                params['effective_time'] = self.effective_time
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.merchant_id:
            if hasattr(self.merchant_id, 'to_alipay_dict'):
                params['merchant_id'] = self.merchant_id.to_alipay_dict()
            else:
                params['merchant_id'] = self.merchant_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOfflineProviderIndirectisvActivityEffectModel()
        if 'effective_time' in d:
            o.effective_time = d['effective_time']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'merchant_id' in d:
            o.merchant_id = d['merchant_id']
        return o


