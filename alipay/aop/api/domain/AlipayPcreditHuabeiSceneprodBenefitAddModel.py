#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayPcreditHuabeiSceneprodBenefitAddModel(object):

    def __init__(self):
        self._benefit_id = None
        self._budget_amount = None
        self._out_biz_no = None
        self._partner_id = None
        self._request_from = None
        self._upper_benefit_id = None
        self._upper_seller_id = None

    @property
    def benefit_id(self):
        return self._benefit_id

    @benefit_id.setter
    def benefit_id(self, value):
        self._benefit_id = value
    @property
    def budget_amount(self):
        return self._budget_amount

    @budget_amount.setter
    def budget_amount(self, value):
        self._budget_amount = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def request_from(self):
        return self._request_from

    @request_from.setter
    def request_from(self, value):
        self._request_from = value
    @property
    def upper_benefit_id(self):
        return self._upper_benefit_id

    @upper_benefit_id.setter
    def upper_benefit_id(self, value):
        self._upper_benefit_id = value
    @property
    def upper_seller_id(self):
        return self._upper_seller_id

    @upper_seller_id.setter
    def upper_seller_id(self, value):
        self._upper_seller_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.benefit_id:
            if hasattr(self.benefit_id, 'to_alipay_dict'):
                params['benefit_id'] = self.benefit_id.to_alipay_dict()
            else:
                params['benefit_id'] = self.benefit_id
        if self.budget_amount:
            if hasattr(self.budget_amount, 'to_alipay_dict'):
                params['budget_amount'] = self.budget_amount.to_alipay_dict()
            else:
                params['budget_amount'] = self.budget_amount
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        if self.request_from:
            if hasattr(self.request_from, 'to_alipay_dict'):
                params['request_from'] = self.request_from.to_alipay_dict()
            else:
                params['request_from'] = self.request_from
        if self.upper_benefit_id:
            if hasattr(self.upper_benefit_id, 'to_alipay_dict'):
                params['upper_benefit_id'] = self.upper_benefit_id.to_alipay_dict()
            else:
                params['upper_benefit_id'] = self.upper_benefit_id
        if self.upper_seller_id:
            if hasattr(self.upper_seller_id, 'to_alipay_dict'):
                params['upper_seller_id'] = self.upper_seller_id.to_alipay_dict()
            else:
                params['upper_seller_id'] = self.upper_seller_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayPcreditHuabeiSceneprodBenefitAddModel()
        if 'benefit_id' in d:
            o.benefit_id = d['benefit_id']
        if 'budget_amount' in d:
            o.budget_amount = d['budget_amount']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'request_from' in d:
            o.request_from = d['request_from']
        if 'upper_benefit_id' in d:
            o.upper_benefit_id = d['upper_benefit_id']
        if 'upper_seller_id' in d:
            o.upper_seller_id = d['upper_seller_id']
        return o


