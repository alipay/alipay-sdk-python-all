#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ToBDiscountCustomerServiceInfo(object):

    def __init__(self):
        self._customer_service_link = None
        self._customer_service_mobile = None

    @property
    def customer_service_link(self):
        return self._customer_service_link

    @customer_service_link.setter
    def customer_service_link(self, value):
        self._customer_service_link = value
    @property
    def customer_service_mobile(self):
        return self._customer_service_mobile

    @customer_service_mobile.setter
    def customer_service_mobile(self, value):
        self._customer_service_mobile = value


    def to_alipay_dict(self):
        params = dict()
        if self.customer_service_link:
            if hasattr(self.customer_service_link, 'to_alipay_dict'):
                params['customer_service_link'] = self.customer_service_link.to_alipay_dict()
            else:
                params['customer_service_link'] = self.customer_service_link
        if self.customer_service_mobile:
            if hasattr(self.customer_service_mobile, 'to_alipay_dict'):
                params['customer_service_mobile'] = self.customer_service_mobile.to_alipay_dict()
            else:
                params['customer_service_mobile'] = self.customer_service_mobile
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ToBDiscountCustomerServiceInfo()
        if 'customer_service_link' in d:
            o.customer_service_link = d['customer_service_link']
        if 'customer_service_mobile' in d:
            o.customer_service_mobile = d['customer_service_mobile']
        return o


