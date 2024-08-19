#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ConsumerLoanBillRepayPlanInfoItem import ConsumerLoanBillRepayPlanInfoItem


class ConsumerLoanBillRepayPlanInfo(object):

    def __init__(self):
        self._last_period_count = None
        self._repay_plan_record = None

    @property
    def last_period_count(self):
        return self._last_period_count

    @last_period_count.setter
    def last_period_count(self, value):
        self._last_period_count = value
    @property
    def repay_plan_record(self):
        return self._repay_plan_record

    @repay_plan_record.setter
    def repay_plan_record(self, value):
        if isinstance(value, list):
            self._repay_plan_record = list()
            for i in value:
                if isinstance(i, ConsumerLoanBillRepayPlanInfoItem):
                    self._repay_plan_record.append(i)
                else:
                    self._repay_plan_record.append(ConsumerLoanBillRepayPlanInfoItem.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.last_period_count:
            if hasattr(self.last_period_count, 'to_alipay_dict'):
                params['last_period_count'] = self.last_period_count.to_alipay_dict()
            else:
                params['last_period_count'] = self.last_period_count
        if self.repay_plan_record:
            if isinstance(self.repay_plan_record, list):
                for i in range(0, len(self.repay_plan_record)):
                    element = self.repay_plan_record[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.repay_plan_record[i] = element.to_alipay_dict()
            if hasattr(self.repay_plan_record, 'to_alipay_dict'):
                params['repay_plan_record'] = self.repay_plan_record.to_alipay_dict()
            else:
                params['repay_plan_record'] = self.repay_plan_record
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ConsumerLoanBillRepayPlanInfo()
        if 'last_period_count' in d:
            o.last_period_count = d['last_period_count']
        if 'repay_plan_record' in d:
            o.repay_plan_record = d['repay_plan_record']
        return o


