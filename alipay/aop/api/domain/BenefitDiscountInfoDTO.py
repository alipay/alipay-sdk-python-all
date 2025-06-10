#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BenefitDiscountInfoDTO(object):

    def __init__(self):
        self._benefit_id = None
        self._dilate = None
        self._merchant_discount = None
        self._platform_discount = None
        self._promo_rule_key = None
        self._promo_rule_value = None

    @property
    def benefit_id(self):
        return self._benefit_id

    @benefit_id.setter
    def benefit_id(self, value):
        self._benefit_id = value
    @property
    def dilate(self):
        return self._dilate

    @dilate.setter
    def dilate(self, value):
        self._dilate = value
    @property
    def merchant_discount(self):
        return self._merchant_discount

    @merchant_discount.setter
    def merchant_discount(self, value):
        self._merchant_discount = value
    @property
    def platform_discount(self):
        return self._platform_discount

    @platform_discount.setter
    def platform_discount(self, value):
        self._platform_discount = value
    @property
    def promo_rule_key(self):
        return self._promo_rule_key

    @promo_rule_key.setter
    def promo_rule_key(self, value):
        self._promo_rule_key = value
    @property
    def promo_rule_value(self):
        return self._promo_rule_value

    @promo_rule_value.setter
    def promo_rule_value(self, value):
        self._promo_rule_value = value


    def to_alipay_dict(self):
        params = dict()
        if self.benefit_id:
            if hasattr(self.benefit_id, 'to_alipay_dict'):
                params['benefit_id'] = self.benefit_id.to_alipay_dict()
            else:
                params['benefit_id'] = self.benefit_id
        if self.dilate:
            if hasattr(self.dilate, 'to_alipay_dict'):
                params['dilate'] = self.dilate.to_alipay_dict()
            else:
                params['dilate'] = self.dilate
        if self.merchant_discount:
            if hasattr(self.merchant_discount, 'to_alipay_dict'):
                params['merchant_discount'] = self.merchant_discount.to_alipay_dict()
            else:
                params['merchant_discount'] = self.merchant_discount
        if self.platform_discount:
            if hasattr(self.platform_discount, 'to_alipay_dict'):
                params['platform_discount'] = self.platform_discount.to_alipay_dict()
            else:
                params['platform_discount'] = self.platform_discount
        if self.promo_rule_key:
            if hasattr(self.promo_rule_key, 'to_alipay_dict'):
                params['promo_rule_key'] = self.promo_rule_key.to_alipay_dict()
            else:
                params['promo_rule_key'] = self.promo_rule_key
        if self.promo_rule_value:
            if hasattr(self.promo_rule_value, 'to_alipay_dict'):
                params['promo_rule_value'] = self.promo_rule_value.to_alipay_dict()
            else:
                params['promo_rule_value'] = self.promo_rule_value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BenefitDiscountInfoDTO()
        if 'benefit_id' in d:
            o.benefit_id = d['benefit_id']
        if 'dilate' in d:
            o.dilate = d['dilate']
        if 'merchant_discount' in d:
            o.merchant_discount = d['merchant_discount']
        if 'platform_discount' in d:
            o.platform_discount = d['platform_discount']
        if 'promo_rule_key' in d:
            o.promo_rule_key = d['promo_rule_key']
        if 'promo_rule_value' in d:
            o.promo_rule_value = d['promo_rule_value']
        return o


