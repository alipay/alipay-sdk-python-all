#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CouponUseProduct(object):

    def __init__(self):
        self._commodity_code = None
        self._spec_code = None

    @property
    def commodity_code(self):
        return self._commodity_code

    @commodity_code.setter
    def commodity_code(self, value):
        self._commodity_code = value
    @property
    def spec_code(self):
        return self._spec_code

    @spec_code.setter
    def spec_code(self, value):
        self._spec_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.commodity_code:
            if hasattr(self.commodity_code, 'to_alipay_dict'):
                params['commodity_code'] = self.commodity_code.to_alipay_dict()
            else:
                params['commodity_code'] = self.commodity_code
        if self.spec_code:
            if hasattr(self.spec_code, 'to_alipay_dict'):
                params['spec_code'] = self.spec_code.to_alipay_dict()
            else:
                params['spec_code'] = self.spec_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CouponUseProduct()
        if 'commodity_code' in d:
            o.commodity_code = d['commodity_code']
        if 'spec_code' in d:
            o.spec_code = d['spec_code']
        return o


