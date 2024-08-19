#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ConsumerLoanBillAggInfo import ConsumerLoanBillAggInfo
from alipay.aop.api.domain.ConsumerLoanNotMatchData import ConsumerLoanNotMatchData


class ConsumerLoanBillSumQueryData(object):

    def __init__(self):
        self._bill_data = None
        self._not_match_data = None

    @property
    def bill_data(self):
        return self._bill_data

    @bill_data.setter
    def bill_data(self, value):
        if isinstance(value, ConsumerLoanBillAggInfo):
            self._bill_data = value
        else:
            self._bill_data = ConsumerLoanBillAggInfo.from_alipay_dict(value)
    @property
    def not_match_data(self):
        return self._not_match_data

    @not_match_data.setter
    def not_match_data(self, value):
        if isinstance(value, ConsumerLoanNotMatchData):
            self._not_match_data = value
        else:
            self._not_match_data = ConsumerLoanNotMatchData.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.bill_data:
            if hasattr(self.bill_data, 'to_alipay_dict'):
                params['bill_data'] = self.bill_data.to_alipay_dict()
            else:
                params['bill_data'] = self.bill_data
        if self.not_match_data:
            if hasattr(self.not_match_data, 'to_alipay_dict'):
                params['not_match_data'] = self.not_match_data.to_alipay_dict()
            else:
                params['not_match_data'] = self.not_match_data
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ConsumerLoanBillSumQueryData()
        if 'bill_data' in d:
            o.bill_data = d['bill_data']
        if 'not_match_data' in d:
            o.not_match_data = d['not_match_data']
        return o


