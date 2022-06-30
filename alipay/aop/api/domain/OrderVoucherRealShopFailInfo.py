#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OrderVoucherRealShopFailInfo(object):

    def __init__(self):
        self._fail_message = None
        self._fail_reasons = None
        self._real_shop_id = None

    @property
    def fail_message(self):
        return self._fail_message

    @fail_message.setter
    def fail_message(self, value):
        self._fail_message = value
    @property
    def fail_reasons(self):
        return self._fail_reasons

    @fail_reasons.setter
    def fail_reasons(self, value):
        if isinstance(value, list):
            self._fail_reasons = list()
            for i in value:
                self._fail_reasons.append(i)
    @property
    def real_shop_id(self):
        return self._real_shop_id

    @real_shop_id.setter
    def real_shop_id(self, value):
        self._real_shop_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.fail_message:
            if hasattr(self.fail_message, 'to_alipay_dict'):
                params['fail_message'] = self.fail_message.to_alipay_dict()
            else:
                params['fail_message'] = self.fail_message
        if self.fail_reasons:
            if isinstance(self.fail_reasons, list):
                for i in range(0, len(self.fail_reasons)):
                    element = self.fail_reasons[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.fail_reasons[i] = element.to_alipay_dict()
            if hasattr(self.fail_reasons, 'to_alipay_dict'):
                params['fail_reasons'] = self.fail_reasons.to_alipay_dict()
            else:
                params['fail_reasons'] = self.fail_reasons
        if self.real_shop_id:
            if hasattr(self.real_shop_id, 'to_alipay_dict'):
                params['real_shop_id'] = self.real_shop_id.to_alipay_dict()
            else:
                params['real_shop_id'] = self.real_shop_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OrderVoucherRealShopFailInfo()
        if 'fail_message' in d:
            o.fail_message = d['fail_message']
        if 'fail_reasons' in d:
            o.fail_reasons = d['fail_reasons']
        if 'real_shop_id' in d:
            o.real_shop_id = d['real_shop_id']
        return o


