#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCreditEpCreditloanCouponNotifyModel(object):

    def __init__(self):
        self._financial_product_code = None
        self._merchant_request_id = None
        self._notify_content = None

    @property
    def financial_product_code(self):
        return self._financial_product_code

    @financial_product_code.setter
    def financial_product_code(self, value):
        self._financial_product_code = value
    @property
    def merchant_request_id(self):
        return self._merchant_request_id

    @merchant_request_id.setter
    def merchant_request_id(self, value):
        self._merchant_request_id = value
    @property
    def notify_content(self):
        return self._notify_content

    @notify_content.setter
    def notify_content(self, value):
        self._notify_content = value


    def to_alipay_dict(self):
        params = dict()
        if self.financial_product_code:
            if hasattr(self.financial_product_code, 'to_alipay_dict'):
                params['financial_product_code'] = self.financial_product_code.to_alipay_dict()
            else:
                params['financial_product_code'] = self.financial_product_code
        if self.merchant_request_id:
            if hasattr(self.merchant_request_id, 'to_alipay_dict'):
                params['merchant_request_id'] = self.merchant_request_id.to_alipay_dict()
            else:
                params['merchant_request_id'] = self.merchant_request_id
        if self.notify_content:
            if hasattr(self.notify_content, 'to_alipay_dict'):
                params['notify_content'] = self.notify_content.to_alipay_dict()
            else:
                params['notify_content'] = self.notify_content
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCreditEpCreditloanCouponNotifyModel()
        if 'financial_product_code' in d:
            o.financial_product_code = d['financial_product_code']
        if 'merchant_request_id' in d:
            o.merchant_request_id = d['merchant_request_id']
        if 'notify_content' in d:
            o.notify_content = d['notify_content']
        return o


