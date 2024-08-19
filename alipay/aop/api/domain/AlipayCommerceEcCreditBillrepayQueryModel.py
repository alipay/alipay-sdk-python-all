#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEcCreditBillrepayQueryModel(object):

    def __init__(self):
        self._end_date = None
        self._enterprise_id = None
        self._loan_out_biz_no = None
        self._start_date = None

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
    @property
    def enterprise_id(self):
        return self._enterprise_id

    @enterprise_id.setter
    def enterprise_id(self, value):
        self._enterprise_id = value
    @property
    def loan_out_biz_no(self):
        return self._loan_out_biz_no

    @loan_out_biz_no.setter
    def loan_out_biz_no(self, value):
        self._loan_out_biz_no = value
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.end_date:
            if hasattr(self.end_date, 'to_alipay_dict'):
                params['end_date'] = self.end_date.to_alipay_dict()
            else:
                params['end_date'] = self.end_date
        if self.enterprise_id:
            if hasattr(self.enterprise_id, 'to_alipay_dict'):
                params['enterprise_id'] = self.enterprise_id.to_alipay_dict()
            else:
                params['enterprise_id'] = self.enterprise_id
        if self.loan_out_biz_no:
            if hasattr(self.loan_out_biz_no, 'to_alipay_dict'):
                params['loan_out_biz_no'] = self.loan_out_biz_no.to_alipay_dict()
            else:
                params['loan_out_biz_no'] = self.loan_out_biz_no
        if self.start_date:
            if hasattr(self.start_date, 'to_alipay_dict'):
                params['start_date'] = self.start_date.to_alipay_dict()
            else:
                params['start_date'] = self.start_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEcCreditBillrepayQueryModel()
        if 'end_date' in d:
            o.end_date = d['end_date']
        if 'enterprise_id' in d:
            o.enterprise_id = d['enterprise_id']
        if 'loan_out_biz_no' in d:
            o.loan_out_biz_no = d['loan_out_biz_no']
        if 'start_date' in d:
            o.start_date = d['start_date']
        return o


