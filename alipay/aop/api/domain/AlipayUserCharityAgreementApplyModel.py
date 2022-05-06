#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserCharityAgreementApplyModel(object):

    def __init__(self):
        self._biz_id = None
        self._product_code = None
        self._withhold_pid = None

    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def withhold_pid(self):
        return self._withhold_pid

    @withhold_pid.setter
    def withhold_pid(self, value):
        self._withhold_pid = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.withhold_pid:
            if hasattr(self.withhold_pid, 'to_alipay_dict'):
                params['withhold_pid'] = self.withhold_pid.to_alipay_dict()
            else:
                params['withhold_pid'] = self.withhold_pid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserCharityAgreementApplyModel()
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'withhold_pid' in d:
            o.withhold_pid = d['withhold_pid']
        return o


