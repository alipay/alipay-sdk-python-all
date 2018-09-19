#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BudgetInfo import BudgetInfo
from alipay.aop.api.domain.GetRuleInfo import GetRuleInfo
from alipay.aop.api.domain.VoucherInfo import VoucherInfo


class AlipayOfflineMarketingVoucherCreateModel(object):

    def __init__(self):
        self._budget_info = None
        self._code_inventory_id = None
        self._ext_info = None
        self._get_rule = None
        self._out_biz_no = None
        self._voucher_info = None

    @property
    def budget_info(self):
        return self._budget_info

    @budget_info.setter
    def budget_info(self, value):
        if isinstance(value, BudgetInfo):
            self._budget_info = value
        else:
            self._budget_info = BudgetInfo.from_alipay_dict(value)
    @property
    def code_inventory_id(self):
        return self._code_inventory_id

    @code_inventory_id.setter
    def code_inventory_id(self, value):
        self._code_inventory_id = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def get_rule(self):
        return self._get_rule

    @get_rule.setter
    def get_rule(self, value):
        if isinstance(value, GetRuleInfo):
            self._get_rule = value
        else:
            self._get_rule = GetRuleInfo.from_alipay_dict(value)
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def voucher_info(self):
        return self._voucher_info

    @voucher_info.setter
    def voucher_info(self, value):
        if isinstance(value, VoucherInfo):
            self._voucher_info = value
        else:
            self._voucher_info = VoucherInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.budget_info:
            if hasattr(self.budget_info, 'to_alipay_dict'):
                params['budget_info'] = self.budget_info.to_alipay_dict()
            else:
                params['budget_info'] = self.budget_info
        if self.code_inventory_id:
            if hasattr(self.code_inventory_id, 'to_alipay_dict'):
                params['code_inventory_id'] = self.code_inventory_id.to_alipay_dict()
            else:
                params['code_inventory_id'] = self.code_inventory_id
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.get_rule:
            if hasattr(self.get_rule, 'to_alipay_dict'):
                params['get_rule'] = self.get_rule.to_alipay_dict()
            else:
                params['get_rule'] = self.get_rule
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.voucher_info:
            if hasattr(self.voucher_info, 'to_alipay_dict'):
                params['voucher_info'] = self.voucher_info.to_alipay_dict()
            else:
                params['voucher_info'] = self.voucher_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOfflineMarketingVoucherCreateModel()
        if 'budget_info' in d:
            o.budget_info = d['budget_info']
        if 'code_inventory_id' in d:
            o.code_inventory_id = d['code_inventory_id']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'get_rule' in d:
            o.get_rule = d['get_rule']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'voucher_info' in d:
            o.voucher_info = d['voucher_info']
        return o


