#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SupplementCategoryInfo(object):

    def __init__(self):
        self._supplement_category = None
        self._supplement_details_list = None
        self._supplement_payment_amt = None
        self._supplement_reason_for_customer_service = None

    @property
    def supplement_category(self):
        return self._supplement_category

    @supplement_category.setter
    def supplement_category(self, value):
        self._supplement_category = value
    @property
    def supplement_details_list(self):
        return self._supplement_details_list

    @supplement_details_list.setter
    def supplement_details_list(self, value):
        if isinstance(value, list):
            self._supplement_details_list = list()
            for i in value:
                self._supplement_details_list.append(i)
    @property
    def supplement_payment_amt(self):
        return self._supplement_payment_amt

    @supplement_payment_amt.setter
    def supplement_payment_amt(self, value):
        self._supplement_payment_amt = value
    @property
    def supplement_reason_for_customer_service(self):
        return self._supplement_reason_for_customer_service

    @supplement_reason_for_customer_service.setter
    def supplement_reason_for_customer_service(self, value):
        self._supplement_reason_for_customer_service = value


    def to_alipay_dict(self):
        params = dict()
        if self.supplement_category:
            if hasattr(self.supplement_category, 'to_alipay_dict'):
                params['supplement_category'] = self.supplement_category.to_alipay_dict()
            else:
                params['supplement_category'] = self.supplement_category
        if self.supplement_details_list:
            if isinstance(self.supplement_details_list, list):
                for i in range(0, len(self.supplement_details_list)):
                    element = self.supplement_details_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.supplement_details_list[i] = element.to_alipay_dict()
            if hasattr(self.supplement_details_list, 'to_alipay_dict'):
                params['supplement_details_list'] = self.supplement_details_list.to_alipay_dict()
            else:
                params['supplement_details_list'] = self.supplement_details_list
        if self.supplement_payment_amt:
            if hasattr(self.supplement_payment_amt, 'to_alipay_dict'):
                params['supplement_payment_amt'] = self.supplement_payment_amt.to_alipay_dict()
            else:
                params['supplement_payment_amt'] = self.supplement_payment_amt
        if self.supplement_reason_for_customer_service:
            if hasattr(self.supplement_reason_for_customer_service, 'to_alipay_dict'):
                params['supplement_reason_for_customer_service'] = self.supplement_reason_for_customer_service.to_alipay_dict()
            else:
                params['supplement_reason_for_customer_service'] = self.supplement_reason_for_customer_service
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SupplementCategoryInfo()
        if 'supplement_category' in d:
            o.supplement_category = d['supplement_category']
        if 'supplement_details_list' in d:
            o.supplement_details_list = d['supplement_details_list']
        if 'supplement_payment_amt' in d:
            o.supplement_payment_amt = d['supplement_payment_amt']
        if 'supplement_reason_for_customer_service' in d:
            o.supplement_reason_for_customer_service = d['supplement_reason_for_customer_service']
        return o


