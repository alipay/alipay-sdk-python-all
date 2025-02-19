#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.NDeliveryMerchantRule import NDeliveryMerchantRule


class NDeliveryTargetRule(object):

    def __init__(self):
        self._n_delivery_device_id = None
        self._n_delivery_merchant_rule = None

    @property
    def n_delivery_device_id(self):
        return self._n_delivery_device_id

    @n_delivery_device_id.setter
    def n_delivery_device_id(self, value):
        self._n_delivery_device_id = value
    @property
    def n_delivery_merchant_rule(self):
        return self._n_delivery_merchant_rule

    @n_delivery_merchant_rule.setter
    def n_delivery_merchant_rule(self, value):
        if isinstance(value, NDeliveryMerchantRule):
            self._n_delivery_merchant_rule = value
        else:
            self._n_delivery_merchant_rule = NDeliveryMerchantRule.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.n_delivery_device_id:
            if hasattr(self.n_delivery_device_id, 'to_alipay_dict'):
                params['n_delivery_device_id'] = self.n_delivery_device_id.to_alipay_dict()
            else:
                params['n_delivery_device_id'] = self.n_delivery_device_id
        if self.n_delivery_merchant_rule:
            if hasattr(self.n_delivery_merchant_rule, 'to_alipay_dict'):
                params['n_delivery_merchant_rule'] = self.n_delivery_merchant_rule.to_alipay_dict()
            else:
                params['n_delivery_merchant_rule'] = self.n_delivery_merchant_rule
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = NDeliveryTargetRule()
        if 'n_delivery_device_id' in d:
            o.n_delivery_device_id = d['n_delivery_device_id']
        if 'n_delivery_merchant_rule' in d:
            o.n_delivery_merchant_rule = d['n_delivery_merchant_rule']
        return o


