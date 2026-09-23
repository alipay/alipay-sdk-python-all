#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ShopProductPriceModifyResult(object):

    def __init__(self):
        self._error_code = None
        self._error_reason = None
        self._external_shop_id = None
        self._shop_id = None

    @property
    def error_code(self):
        return self._error_code

    @error_code.setter
    def error_code(self, value):
        self._error_code = value
    @property
    def error_reason(self):
        return self._error_reason

    @error_reason.setter
    def error_reason(self, value):
        self._error_reason = value
    @property
    def external_shop_id(self):
        return self._external_shop_id

    @external_shop_id.setter
    def external_shop_id(self, value):
        self._external_shop_id = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.error_code:
            if hasattr(self.error_code, 'to_alipay_dict'):
                params['error_code'] = self.error_code.to_alipay_dict()
            else:
                params['error_code'] = self.error_code
        if self.error_reason:
            if hasattr(self.error_reason, 'to_alipay_dict'):
                params['error_reason'] = self.error_reason.to_alipay_dict()
            else:
                params['error_reason'] = self.error_reason
        if self.external_shop_id:
            if hasattr(self.external_shop_id, 'to_alipay_dict'):
                params['external_shop_id'] = self.external_shop_id.to_alipay_dict()
            else:
                params['external_shop_id'] = self.external_shop_id
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ShopProductPriceModifyResult()
        if 'error_code' in d:
            o.error_code = d['error_code']
        if 'error_reason' in d:
            o.error_reason = d['error_reason']
        if 'external_shop_id' in d:
            o.external_shop_id = d['external_shop_id']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        return o


