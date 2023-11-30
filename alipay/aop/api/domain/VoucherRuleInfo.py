#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class VoucherRuleInfo(object):

    def __init__(self):
        self._customer_service_tel = None
        self._customer_service_url = None
        self._usage_rule_text = None
        self._usage_rule_url = None

    @property
    def customer_service_tel(self):
        return self._customer_service_tel

    @customer_service_tel.setter
    def customer_service_tel(self, value):
        self._customer_service_tel = value
    @property
    def customer_service_url(self):
        return self._customer_service_url

    @customer_service_url.setter
    def customer_service_url(self, value):
        self._customer_service_url = value
    @property
    def usage_rule_text(self):
        return self._usage_rule_text

    @usage_rule_text.setter
    def usage_rule_text(self, value):
        self._usage_rule_text = value
    @property
    def usage_rule_url(self):
        return self._usage_rule_url

    @usage_rule_url.setter
    def usage_rule_url(self, value):
        self._usage_rule_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.customer_service_tel:
            if hasattr(self.customer_service_tel, 'to_alipay_dict'):
                params['customer_service_tel'] = self.customer_service_tel.to_alipay_dict()
            else:
                params['customer_service_tel'] = self.customer_service_tel
        if self.customer_service_url:
            if hasattr(self.customer_service_url, 'to_alipay_dict'):
                params['customer_service_url'] = self.customer_service_url.to_alipay_dict()
            else:
                params['customer_service_url'] = self.customer_service_url
        if self.usage_rule_text:
            if hasattr(self.usage_rule_text, 'to_alipay_dict'):
                params['usage_rule_text'] = self.usage_rule_text.to_alipay_dict()
            else:
                params['usage_rule_text'] = self.usage_rule_text
        if self.usage_rule_url:
            if hasattr(self.usage_rule_url, 'to_alipay_dict'):
                params['usage_rule_url'] = self.usage_rule_url.to_alipay_dict()
            else:
                params['usage_rule_url'] = self.usage_rule_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VoucherRuleInfo()
        if 'customer_service_tel' in d:
            o.customer_service_tel = d['customer_service_tel']
        if 'customer_service_url' in d:
            o.customer_service_url = d['customer_service_url']
        if 'usage_rule_text' in d:
            o.usage_rule_text = d['usage_rule_text']
        if 'usage_rule_url' in d:
            o.usage_rule_url = d['usage_rule_url']
        return o


