#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RepaymemtPlanPreview import RepaymemtPlanPreview


class RepaymentPlanListPreview(object):

    def __init__(self):
        self._repay_plan_detail_list = None
        self._total_amt = None
        self._total_deduct_int_amt = None
        self._total_initial_int_amt = None
        self._total_int_amt = None
        self._total_prin_amt = None
        self._total_serv_amt = None

    @property
    def repay_plan_detail_list(self):
        return self._repay_plan_detail_list

    @repay_plan_detail_list.setter
    def repay_plan_detail_list(self, value):
        if isinstance(value, list):
            self._repay_plan_detail_list = list()
            for i in value:
                if isinstance(i, RepaymemtPlanPreview):
                    self._repay_plan_detail_list.append(i)
                else:
                    self._repay_plan_detail_list.append(RepaymemtPlanPreview.from_alipay_dict(i))
    @property
    def total_amt(self):
        return self._total_amt

    @total_amt.setter
    def total_amt(self, value):
        self._total_amt = value
    @property
    def total_deduct_int_amt(self):
        return self._total_deduct_int_amt

    @total_deduct_int_amt.setter
    def total_deduct_int_amt(self, value):
        self._total_deduct_int_amt = value
    @property
    def total_initial_int_amt(self):
        return self._total_initial_int_amt

    @total_initial_int_amt.setter
    def total_initial_int_amt(self, value):
        self._total_initial_int_amt = value
    @property
    def total_int_amt(self):
        return self._total_int_amt

    @total_int_amt.setter
    def total_int_amt(self, value):
        self._total_int_amt = value
    @property
    def total_prin_amt(self):
        return self._total_prin_amt

    @total_prin_amt.setter
    def total_prin_amt(self, value):
        self._total_prin_amt = value
    @property
    def total_serv_amt(self):
        return self._total_serv_amt

    @total_serv_amt.setter
    def total_serv_amt(self, value):
        self._total_serv_amt = value


    def to_alipay_dict(self):
        params = dict()
        if self.repay_plan_detail_list:
            if isinstance(self.repay_plan_detail_list, list):
                for i in range(0, len(self.repay_plan_detail_list)):
                    element = self.repay_plan_detail_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.repay_plan_detail_list[i] = element.to_alipay_dict()
            if hasattr(self.repay_plan_detail_list, 'to_alipay_dict'):
                params['repay_plan_detail_list'] = self.repay_plan_detail_list.to_alipay_dict()
            else:
                params['repay_plan_detail_list'] = self.repay_plan_detail_list
        if self.total_amt:
            if hasattr(self.total_amt, 'to_alipay_dict'):
                params['total_amt'] = self.total_amt.to_alipay_dict()
            else:
                params['total_amt'] = self.total_amt
        if self.total_deduct_int_amt:
            if hasattr(self.total_deduct_int_amt, 'to_alipay_dict'):
                params['total_deduct_int_amt'] = self.total_deduct_int_amt.to_alipay_dict()
            else:
                params['total_deduct_int_amt'] = self.total_deduct_int_amt
        if self.total_initial_int_amt:
            if hasattr(self.total_initial_int_amt, 'to_alipay_dict'):
                params['total_initial_int_amt'] = self.total_initial_int_amt.to_alipay_dict()
            else:
                params['total_initial_int_amt'] = self.total_initial_int_amt
        if self.total_int_amt:
            if hasattr(self.total_int_amt, 'to_alipay_dict'):
                params['total_int_amt'] = self.total_int_amt.to_alipay_dict()
            else:
                params['total_int_amt'] = self.total_int_amt
        if self.total_prin_amt:
            if hasattr(self.total_prin_amt, 'to_alipay_dict'):
                params['total_prin_amt'] = self.total_prin_amt.to_alipay_dict()
            else:
                params['total_prin_amt'] = self.total_prin_amt
        if self.total_serv_amt:
            if hasattr(self.total_serv_amt, 'to_alipay_dict'):
                params['total_serv_amt'] = self.total_serv_amt.to_alipay_dict()
            else:
                params['total_serv_amt'] = self.total_serv_amt
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RepaymentPlanListPreview()
        if 'repay_plan_detail_list' in d:
            o.repay_plan_detail_list = d['repay_plan_detail_list']
        if 'total_amt' in d:
            o.total_amt = d['total_amt']
        if 'total_deduct_int_amt' in d:
            o.total_deduct_int_amt = d['total_deduct_int_amt']
        if 'total_initial_int_amt' in d:
            o.total_initial_int_amt = d['total_initial_int_amt']
        if 'total_int_amt' in d:
            o.total_int_amt = d['total_int_amt']
        if 'total_prin_amt' in d:
            o.total_prin_amt = d['total_prin_amt']
        if 'total_serv_amt' in d:
            o.total_serv_amt = d['total_serv_amt']
        return o


