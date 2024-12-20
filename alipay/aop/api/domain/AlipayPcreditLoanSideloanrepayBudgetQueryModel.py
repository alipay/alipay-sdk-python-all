#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayPcreditLoanSideloanrepayBudgetQueryModel(object):

    def __init__(self):
        self._alipay_user_id = None
        self._apply_repay_amount = None
        self._extension = None
        self._loan_apply_no_list = None
        self._open_id = None
        self._product_code = None
        self._repayment_scene = None

    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def apply_repay_amount(self):
        return self._apply_repay_amount

    @apply_repay_amount.setter
    def apply_repay_amount(self, value):
        self._apply_repay_amount = value
    @property
    def extension(self):
        return self._extension

    @extension.setter
    def extension(self, value):
        self._extension = value
    @property
    def loan_apply_no_list(self):
        return self._loan_apply_no_list

    @loan_apply_no_list.setter
    def loan_apply_no_list(self, value):
        if isinstance(value, list):
            self._loan_apply_no_list = list()
            for i in value:
                self._loan_apply_no_list.append(i)
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def repayment_scene(self):
        return self._repayment_scene

    @repayment_scene.setter
    def repayment_scene(self, value):
        self._repayment_scene = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.apply_repay_amount:
            if hasattr(self.apply_repay_amount, 'to_alipay_dict'):
                params['apply_repay_amount'] = self.apply_repay_amount.to_alipay_dict()
            else:
                params['apply_repay_amount'] = self.apply_repay_amount
        if self.extension:
            if hasattr(self.extension, 'to_alipay_dict'):
                params['extension'] = self.extension.to_alipay_dict()
            else:
                params['extension'] = self.extension
        if self.loan_apply_no_list:
            if isinstance(self.loan_apply_no_list, list):
                for i in range(0, len(self.loan_apply_no_list)):
                    element = self.loan_apply_no_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.loan_apply_no_list[i] = element.to_alipay_dict()
            if hasattr(self.loan_apply_no_list, 'to_alipay_dict'):
                params['loan_apply_no_list'] = self.loan_apply_no_list.to_alipay_dict()
            else:
                params['loan_apply_no_list'] = self.loan_apply_no_list
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.repayment_scene:
            if hasattr(self.repayment_scene, 'to_alipay_dict'):
                params['repayment_scene'] = self.repayment_scene.to_alipay_dict()
            else:
                params['repayment_scene'] = self.repayment_scene
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayPcreditLoanSideloanrepayBudgetQueryModel()
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'apply_repay_amount' in d:
            o.apply_repay_amount = d['apply_repay_amount']
        if 'extension' in d:
            o.extension = d['extension']
        if 'loan_apply_no_list' in d:
            o.loan_apply_no_list = d['loan_apply_no_list']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'repayment_scene' in d:
            o.repayment_scene = d['repayment_scene']
        return o


