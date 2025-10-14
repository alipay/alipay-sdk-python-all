#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FsFundInfoForm import FsFundInfoForm


class AlipayMarketingBenefitaccountAccountRefundModel(object):

    def __init__(self):
        self._amount = None
        self._benefit_account_no = None
        self._biz_no = None
        self._budget_decrease_type = None
        self._fund_infos = None
        self._operator_id = None
        self._operator_name = None
        self._publisher_user_id = None
        self._refund_strategy = None
        self._verify_id = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def benefit_account_no(self):
        return self._benefit_account_no

    @benefit_account_no.setter
    def benefit_account_no(self, value):
        self._benefit_account_no = value
    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def budget_decrease_type(self):
        return self._budget_decrease_type

    @budget_decrease_type.setter
    def budget_decrease_type(self, value):
        self._budget_decrease_type = value
    @property
    def fund_infos(self):
        return self._fund_infos

    @fund_infos.setter
    def fund_infos(self, value):
        if isinstance(value, list):
            self._fund_infos = list()
            for i in value:
                if isinstance(i, FsFundInfoForm):
                    self._fund_infos.append(i)
                else:
                    self._fund_infos.append(FsFundInfoForm.from_alipay_dict(i))
    @property
    def operator_id(self):
        return self._operator_id

    @operator_id.setter
    def operator_id(self, value):
        self._operator_id = value
    @property
    def operator_name(self):
        return self._operator_name

    @operator_name.setter
    def operator_name(self, value):
        self._operator_name = value
    @property
    def publisher_user_id(self):
        return self._publisher_user_id

    @publisher_user_id.setter
    def publisher_user_id(self, value):
        self._publisher_user_id = value
    @property
    def refund_strategy(self):
        return self._refund_strategy

    @refund_strategy.setter
    def refund_strategy(self, value):
        self._refund_strategy = value
    @property
    def verify_id(self):
        return self._verify_id

    @verify_id.setter
    def verify_id(self, value):
        self._verify_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.benefit_account_no:
            if hasattr(self.benefit_account_no, 'to_alipay_dict'):
                params['benefit_account_no'] = self.benefit_account_no.to_alipay_dict()
            else:
                params['benefit_account_no'] = self.benefit_account_no
        if self.biz_no:
            if hasattr(self.biz_no, 'to_alipay_dict'):
                params['biz_no'] = self.biz_no.to_alipay_dict()
            else:
                params['biz_no'] = self.biz_no
        if self.budget_decrease_type:
            if hasattr(self.budget_decrease_type, 'to_alipay_dict'):
                params['budget_decrease_type'] = self.budget_decrease_type.to_alipay_dict()
            else:
                params['budget_decrease_type'] = self.budget_decrease_type
        if self.fund_infos:
            if isinstance(self.fund_infos, list):
                for i in range(0, len(self.fund_infos)):
                    element = self.fund_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.fund_infos[i] = element.to_alipay_dict()
            if hasattr(self.fund_infos, 'to_alipay_dict'):
                params['fund_infos'] = self.fund_infos.to_alipay_dict()
            else:
                params['fund_infos'] = self.fund_infos
        if self.operator_id:
            if hasattr(self.operator_id, 'to_alipay_dict'):
                params['operator_id'] = self.operator_id.to_alipay_dict()
            else:
                params['operator_id'] = self.operator_id
        if self.operator_name:
            if hasattr(self.operator_name, 'to_alipay_dict'):
                params['operator_name'] = self.operator_name.to_alipay_dict()
            else:
                params['operator_name'] = self.operator_name
        if self.publisher_user_id:
            if hasattr(self.publisher_user_id, 'to_alipay_dict'):
                params['publisher_user_id'] = self.publisher_user_id.to_alipay_dict()
            else:
                params['publisher_user_id'] = self.publisher_user_id
        if self.refund_strategy:
            if hasattr(self.refund_strategy, 'to_alipay_dict'):
                params['refund_strategy'] = self.refund_strategy.to_alipay_dict()
            else:
                params['refund_strategy'] = self.refund_strategy
        if self.verify_id:
            if hasattr(self.verify_id, 'to_alipay_dict'):
                params['verify_id'] = self.verify_id.to_alipay_dict()
            else:
                params['verify_id'] = self.verify_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingBenefitaccountAccountRefundModel()
        if 'amount' in d:
            o.amount = d['amount']
        if 'benefit_account_no' in d:
            o.benefit_account_no = d['benefit_account_no']
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'budget_decrease_type' in d:
            o.budget_decrease_type = d['budget_decrease_type']
        if 'fund_infos' in d:
            o.fund_infos = d['fund_infos']
        if 'operator_id' in d:
            o.operator_id = d['operator_id']
        if 'operator_name' in d:
            o.operator_name = d['operator_name']
        if 'publisher_user_id' in d:
            o.publisher_user_id = d['publisher_user_id']
        if 'refund_strategy' in d:
            o.refund_strategy = d['refund_strategy']
        if 'verify_id' in d:
            o.verify_id = d['verify_id']
        return o


