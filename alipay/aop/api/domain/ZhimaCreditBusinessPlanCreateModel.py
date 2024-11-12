#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CreditPerformancePlanInfoOpen import CreditPerformancePlanInfoOpen


class ZhimaCreditBusinessPlanCreateModel(object):

    def __init__(self):
        self._out_order_no = None
        self._plan_info = None
        self._plan_mode = None
        self._plan_sub_mode = None
        self._plan_type = None
        self._product_code = None
        self._zm_service_id = None

    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def plan_info(self):
        return self._plan_info

    @plan_info.setter
    def plan_info(self, value):
        if isinstance(value, CreditPerformancePlanInfoOpen):
            self._plan_info = value
        else:
            self._plan_info = CreditPerformancePlanInfoOpen.from_alipay_dict(value)
    @property
    def plan_mode(self):
        return self._plan_mode

    @plan_mode.setter
    def plan_mode(self, value):
        self._plan_mode = value
    @property
    def plan_sub_mode(self):
        return self._plan_sub_mode

    @plan_sub_mode.setter
    def plan_sub_mode(self, value):
        self._plan_sub_mode = value
    @property
    def plan_type(self):
        return self._plan_type

    @plan_type.setter
    def plan_type(self, value):
        self._plan_type = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def zm_service_id(self):
        return self._zm_service_id

    @zm_service_id.setter
    def zm_service_id(self, value):
        self._zm_service_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
        if self.plan_info:
            if hasattr(self.plan_info, 'to_alipay_dict'):
                params['plan_info'] = self.plan_info.to_alipay_dict()
            else:
                params['plan_info'] = self.plan_info
        if self.plan_mode:
            if hasattr(self.plan_mode, 'to_alipay_dict'):
                params['plan_mode'] = self.plan_mode.to_alipay_dict()
            else:
                params['plan_mode'] = self.plan_mode
        if self.plan_sub_mode:
            if hasattr(self.plan_sub_mode, 'to_alipay_dict'):
                params['plan_sub_mode'] = self.plan_sub_mode.to_alipay_dict()
            else:
                params['plan_sub_mode'] = self.plan_sub_mode
        if self.plan_type:
            if hasattr(self.plan_type, 'to_alipay_dict'):
                params['plan_type'] = self.plan_type.to_alipay_dict()
            else:
                params['plan_type'] = self.plan_type
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.zm_service_id:
            if hasattr(self.zm_service_id, 'to_alipay_dict'):
                params['zm_service_id'] = self.zm_service_id.to_alipay_dict()
            else:
                params['zm_service_id'] = self.zm_service_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCreditBusinessPlanCreateModel()
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'plan_info' in d:
            o.plan_info = d['plan_info']
        if 'plan_mode' in d:
            o.plan_mode = d['plan_mode']
        if 'plan_sub_mode' in d:
            o.plan_sub_mode = d['plan_sub_mode']
        if 'plan_type' in d:
            o.plan_type = d['plan_type']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'zm_service_id' in d:
            o.zm_service_id = d['zm_service_id']
        return o


