#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CreditPerformancePlanDetailOpen import CreditPerformancePlanDetailOpen


class ZhimaCreditBusinessPlanModifyModel(object):

    def __init__(self):
        self._biz_no = None
        self._operate_type = None
        self._out_request_no = None
        self._plan_details = None
        self._product_code = None

    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def operate_type(self):
        return self._operate_type

    @operate_type.setter
    def operate_type(self, value):
        self._operate_type = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def plan_details(self):
        return self._plan_details

    @plan_details.setter
    def plan_details(self, value):
        if isinstance(value, list):
            self._plan_details = list()
            for i in value:
                if isinstance(i, CreditPerformancePlanDetailOpen):
                    self._plan_details.append(i)
                else:
                    self._plan_details.append(CreditPerformancePlanDetailOpen.from_alipay_dict(i))
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_no:
            if hasattr(self.biz_no, 'to_alipay_dict'):
                params['biz_no'] = self.biz_no.to_alipay_dict()
            else:
                params['biz_no'] = self.biz_no
        if self.operate_type:
            if hasattr(self.operate_type, 'to_alipay_dict'):
                params['operate_type'] = self.operate_type.to_alipay_dict()
            else:
                params['operate_type'] = self.operate_type
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        if self.plan_details:
            if isinstance(self.plan_details, list):
                for i in range(0, len(self.plan_details)):
                    element = self.plan_details[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.plan_details[i] = element.to_alipay_dict()
            if hasattr(self.plan_details, 'to_alipay_dict'):
                params['plan_details'] = self.plan_details.to_alipay_dict()
            else:
                params['plan_details'] = self.plan_details
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCreditBusinessPlanModifyModel()
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'operate_type' in d:
            o.operate_type = d['operate_type']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'plan_details' in d:
            o.plan_details = d['plan_details']
        if 'product_code' in d:
            o.product_code = d['product_code']
        return o


