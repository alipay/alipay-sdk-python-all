#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingCampaignDiscountBudgetCreateModel(object):

    def __init__(self):
        self._biz_from = None
        self._fund_type = None
        self._gmt_end = None
        self._name = None
        self._out_biz_no = None
        self._out_budget_no = None
        self._publisher_logon_id = None
        self._total_amount = None

    @property
    def biz_from(self):
        return self._biz_from

    @biz_from.setter
    def biz_from(self, value):
        self._biz_from = value
    @property
    def fund_type(self):
        return self._fund_type

    @fund_type.setter
    def fund_type(self, value):
        self._fund_type = value
    @property
    def gmt_end(self):
        return self._gmt_end

    @gmt_end.setter
    def gmt_end(self, value):
        self._gmt_end = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def out_budget_no(self):
        return self._out_budget_no

    @out_budget_no.setter
    def out_budget_no(self, value):
        self._out_budget_no = value
    @property
    def publisher_logon_id(self):
        return self._publisher_logon_id

    @publisher_logon_id.setter
    def publisher_logon_id(self, value):
        self._publisher_logon_id = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_from:
            if hasattr(self.biz_from, 'to_alipay_dict'):
                params['biz_from'] = self.biz_from.to_alipay_dict()
            else:
                params['biz_from'] = self.biz_from
        if self.fund_type:
            if hasattr(self.fund_type, 'to_alipay_dict'):
                params['fund_type'] = self.fund_type.to_alipay_dict()
            else:
                params['fund_type'] = self.fund_type
        if self.gmt_end:
            if hasattr(self.gmt_end, 'to_alipay_dict'):
                params['gmt_end'] = self.gmt_end.to_alipay_dict()
            else:
                params['gmt_end'] = self.gmt_end
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.out_budget_no:
            if hasattr(self.out_budget_no, 'to_alipay_dict'):
                params['out_budget_no'] = self.out_budget_no.to_alipay_dict()
            else:
                params['out_budget_no'] = self.out_budget_no
        if self.publisher_logon_id:
            if hasattr(self.publisher_logon_id, 'to_alipay_dict'):
                params['publisher_logon_id'] = self.publisher_logon_id.to_alipay_dict()
            else:
                params['publisher_logon_id'] = self.publisher_logon_id
        if self.total_amount:
            if hasattr(self.total_amount, 'to_alipay_dict'):
                params['total_amount'] = self.total_amount.to_alipay_dict()
            else:
                params['total_amount'] = self.total_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingCampaignDiscountBudgetCreateModel()
        if 'biz_from' in d:
            o.biz_from = d['biz_from']
        if 'fund_type' in d:
            o.fund_type = d['fund_type']
        if 'gmt_end' in d:
            o.gmt_end = d['gmt_end']
        if 'name' in d:
            o.name = d['name']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'out_budget_no' in d:
            o.out_budget_no = d['out_budget_no']
        if 'publisher_logon_id' in d:
            o.publisher_logon_id = d['publisher_logon_id']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        return o


