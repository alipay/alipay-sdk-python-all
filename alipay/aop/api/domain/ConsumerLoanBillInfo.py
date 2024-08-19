#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ConsumerLoanBillInfoItem import ConsumerLoanBillInfoItem
from alipay.aop.api.domain.ConsumerLoanLoanInfo import ConsumerLoanLoanInfo
from alipay.aop.api.domain.ConsumerLoanBillRepayPlanInfo import ConsumerLoanBillRepayPlanInfo


class ConsumerLoanBillInfo(object):

    def __init__(self):
        self._bill_list = None
        self._loan_info = None
        self._period_count = None
        self._repay_amount = None
        self._repay_plan = None

    @property
    def bill_list(self):
        return self._bill_list

    @bill_list.setter
    def bill_list(self, value):
        if isinstance(value, list):
            self._bill_list = list()
            for i in value:
                if isinstance(i, ConsumerLoanBillInfoItem):
                    self._bill_list.append(i)
                else:
                    self._bill_list.append(ConsumerLoanBillInfoItem.from_alipay_dict(i))
    @property
    def loan_info(self):
        return self._loan_info

    @loan_info.setter
    def loan_info(self, value):
        if isinstance(value, ConsumerLoanLoanInfo):
            self._loan_info = value
        else:
            self._loan_info = ConsumerLoanLoanInfo.from_alipay_dict(value)
    @property
    def period_count(self):
        return self._period_count

    @period_count.setter
    def period_count(self, value):
        self._period_count = value
    @property
    def repay_amount(self):
        return self._repay_amount

    @repay_amount.setter
    def repay_amount(self, value):
        self._repay_amount = value
    @property
    def repay_plan(self):
        return self._repay_plan

    @repay_plan.setter
    def repay_plan(self, value):
        if isinstance(value, ConsumerLoanBillRepayPlanInfo):
            self._repay_plan = value
        else:
            self._repay_plan = ConsumerLoanBillRepayPlanInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.bill_list:
            if isinstance(self.bill_list, list):
                for i in range(0, len(self.bill_list)):
                    element = self.bill_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.bill_list[i] = element.to_alipay_dict()
            if hasattr(self.bill_list, 'to_alipay_dict'):
                params['bill_list'] = self.bill_list.to_alipay_dict()
            else:
                params['bill_list'] = self.bill_list
        if self.loan_info:
            if hasattr(self.loan_info, 'to_alipay_dict'):
                params['loan_info'] = self.loan_info.to_alipay_dict()
            else:
                params['loan_info'] = self.loan_info
        if self.period_count:
            if hasattr(self.period_count, 'to_alipay_dict'):
                params['period_count'] = self.period_count.to_alipay_dict()
            else:
                params['period_count'] = self.period_count
        if self.repay_amount:
            if hasattr(self.repay_amount, 'to_alipay_dict'):
                params['repay_amount'] = self.repay_amount.to_alipay_dict()
            else:
                params['repay_amount'] = self.repay_amount
        if self.repay_plan:
            if hasattr(self.repay_plan, 'to_alipay_dict'):
                params['repay_plan'] = self.repay_plan.to_alipay_dict()
            else:
                params['repay_plan'] = self.repay_plan
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ConsumerLoanBillInfo()
        if 'bill_list' in d:
            o.bill_list = d['bill_list']
        if 'loan_info' in d:
            o.loan_info = d['loan_info']
        if 'period_count' in d:
            o.period_count = d['period_count']
        if 'repay_amount' in d:
            o.repay_amount = d['repay_amount']
        if 'repay_plan' in d:
            o.repay_plan = d['repay_plan']
        return o


