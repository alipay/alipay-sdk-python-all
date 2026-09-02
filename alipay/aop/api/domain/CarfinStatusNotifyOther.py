#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CarfinGuaranteeInst import CarfinGuaranteeInst


class CarfinStatusNotifyOther(object):

    def __init__(self):
        self._accident_vehicle_flag = None
        self._approve_not_submit_code = None
        self._approve_not_submit_msg = None
        self._customer_credit_rating = None
        self._guarantee_org_list = None
        self._needs_gps_installation = None
        self._org_vehicle_valuation = None
        self._pay_method = None

    @property
    def accident_vehicle_flag(self):
        return self._accident_vehicle_flag

    @accident_vehicle_flag.setter
    def accident_vehicle_flag(self, value):
        self._accident_vehicle_flag = value
    @property
    def approve_not_submit_code(self):
        return self._approve_not_submit_code

    @approve_not_submit_code.setter
    def approve_not_submit_code(self, value):
        self._approve_not_submit_code = value
    @property
    def approve_not_submit_msg(self):
        return self._approve_not_submit_msg

    @approve_not_submit_msg.setter
    def approve_not_submit_msg(self, value):
        self._approve_not_submit_msg = value
    @property
    def customer_credit_rating(self):
        return self._customer_credit_rating

    @customer_credit_rating.setter
    def customer_credit_rating(self, value):
        self._customer_credit_rating = value
    @property
    def guarantee_org_list(self):
        return self._guarantee_org_list

    @guarantee_org_list.setter
    def guarantee_org_list(self, value):
        if isinstance(value, list):
            self._guarantee_org_list = list()
            for i in value:
                if isinstance(i, CarfinGuaranteeInst):
                    self._guarantee_org_list.append(i)
                else:
                    self._guarantee_org_list.append(CarfinGuaranteeInst.from_alipay_dict(i))
    @property
    def needs_gps_installation(self):
        return self._needs_gps_installation

    @needs_gps_installation.setter
    def needs_gps_installation(self, value):
        self._needs_gps_installation = value
    @property
    def org_vehicle_valuation(self):
        return self._org_vehicle_valuation

    @org_vehicle_valuation.setter
    def org_vehicle_valuation(self, value):
        self._org_vehicle_valuation = value
    @property
    def pay_method(self):
        return self._pay_method

    @pay_method.setter
    def pay_method(self, value):
        self._pay_method = value


    def to_alipay_dict(self):
        params = dict()
        if self.accident_vehicle_flag:
            if hasattr(self.accident_vehicle_flag, 'to_alipay_dict'):
                params['accident_vehicle_flag'] = self.accident_vehicle_flag.to_alipay_dict()
            else:
                params['accident_vehicle_flag'] = self.accident_vehicle_flag
        if self.approve_not_submit_code:
            if hasattr(self.approve_not_submit_code, 'to_alipay_dict'):
                params['approve_not_submit_code'] = self.approve_not_submit_code.to_alipay_dict()
            else:
                params['approve_not_submit_code'] = self.approve_not_submit_code
        if self.approve_not_submit_msg:
            if hasattr(self.approve_not_submit_msg, 'to_alipay_dict'):
                params['approve_not_submit_msg'] = self.approve_not_submit_msg.to_alipay_dict()
            else:
                params['approve_not_submit_msg'] = self.approve_not_submit_msg
        if self.customer_credit_rating:
            if hasattr(self.customer_credit_rating, 'to_alipay_dict'):
                params['customer_credit_rating'] = self.customer_credit_rating.to_alipay_dict()
            else:
                params['customer_credit_rating'] = self.customer_credit_rating
        if self.guarantee_org_list:
            if isinstance(self.guarantee_org_list, list):
                for i in range(0, len(self.guarantee_org_list)):
                    element = self.guarantee_org_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.guarantee_org_list[i] = element.to_alipay_dict()
            if hasattr(self.guarantee_org_list, 'to_alipay_dict'):
                params['guarantee_org_list'] = self.guarantee_org_list.to_alipay_dict()
            else:
                params['guarantee_org_list'] = self.guarantee_org_list
        if self.needs_gps_installation:
            if hasattr(self.needs_gps_installation, 'to_alipay_dict'):
                params['needs_gps_installation'] = self.needs_gps_installation.to_alipay_dict()
            else:
                params['needs_gps_installation'] = self.needs_gps_installation
        if self.org_vehicle_valuation:
            if hasattr(self.org_vehicle_valuation, 'to_alipay_dict'):
                params['org_vehicle_valuation'] = self.org_vehicle_valuation.to_alipay_dict()
            else:
                params['org_vehicle_valuation'] = self.org_vehicle_valuation
        if self.pay_method:
            if hasattr(self.pay_method, 'to_alipay_dict'):
                params['pay_method'] = self.pay_method.to_alipay_dict()
            else:
                params['pay_method'] = self.pay_method
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CarfinStatusNotifyOther()
        if 'accident_vehicle_flag' in d:
            o.accident_vehicle_flag = d['accident_vehicle_flag']
        if 'approve_not_submit_code' in d:
            o.approve_not_submit_code = d['approve_not_submit_code']
        if 'approve_not_submit_msg' in d:
            o.approve_not_submit_msg = d['approve_not_submit_msg']
        if 'customer_credit_rating' in d:
            o.customer_credit_rating = d['customer_credit_rating']
        if 'guarantee_org_list' in d:
            o.guarantee_org_list = d['guarantee_org_list']
        if 'needs_gps_installation' in d:
            o.needs_gps_installation = d['needs_gps_installation']
        if 'org_vehicle_valuation' in d:
            o.org_vehicle_valuation = d['org_vehicle_valuation']
        if 'pay_method' in d:
            o.pay_method = d['pay_method']
        return o


