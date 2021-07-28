#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SignRestrictInfo(object):

    def __init__(self):
        self._restrict_product = None
        self._restrict_reason = None
        self._restrict_reason_code = None
        self._restrict_version = None

    @property
    def restrict_product(self):
        return self._restrict_product

    @restrict_product.setter
    def restrict_product(self, value):
        self._restrict_product = value
    @property
    def restrict_reason(self):
        return self._restrict_reason

    @restrict_reason.setter
    def restrict_reason(self, value):
        self._restrict_reason = value
    @property
    def restrict_reason_code(self):
        return self._restrict_reason_code

    @restrict_reason_code.setter
    def restrict_reason_code(self, value):
        self._restrict_reason_code = value
    @property
    def restrict_version(self):
        return self._restrict_version

    @restrict_version.setter
    def restrict_version(self, value):
        self._restrict_version = value


    def to_alipay_dict(self):
        params = dict()
        if self.restrict_product:
            if hasattr(self.restrict_product, 'to_alipay_dict'):
                params['restrict_product'] = self.restrict_product.to_alipay_dict()
            else:
                params['restrict_product'] = self.restrict_product
        if self.restrict_reason:
            if hasattr(self.restrict_reason, 'to_alipay_dict'):
                params['restrict_reason'] = self.restrict_reason.to_alipay_dict()
            else:
                params['restrict_reason'] = self.restrict_reason
        if self.restrict_reason_code:
            if hasattr(self.restrict_reason_code, 'to_alipay_dict'):
                params['restrict_reason_code'] = self.restrict_reason_code.to_alipay_dict()
            else:
                params['restrict_reason_code'] = self.restrict_reason_code
        if self.restrict_version:
            if hasattr(self.restrict_version, 'to_alipay_dict'):
                params['restrict_version'] = self.restrict_version.to_alipay_dict()
            else:
                params['restrict_version'] = self.restrict_version
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SignRestrictInfo()
        if 'restrict_product' in d:
            o.restrict_product = d['restrict_product']
        if 'restrict_reason' in d:
            o.restrict_reason = d['restrict_reason']
        if 'restrict_reason_code' in d:
            o.restrict_reason_code = d['restrict_reason_code']
        if 'restrict_version' in d:
            o.restrict_version = d['restrict_version']
        return o


