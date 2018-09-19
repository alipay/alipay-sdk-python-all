#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayInsDataAutoFraudSyncModel(object):

    def __init__(self):
        self._avoid_loss_amount = None
        self._avoid_loss_type = None
        self._case_end_amount = None
        self._fraud_query_request_no = None
        self._fraud_result = None
        self._report_no = None
        self._request_no = None
        self._syn_type = None

    @property
    def avoid_loss_amount(self):
        return self._avoid_loss_amount

    @avoid_loss_amount.setter
    def avoid_loss_amount(self, value):
        self._avoid_loss_amount = value
    @property
    def avoid_loss_type(self):
        return self._avoid_loss_type

    @avoid_loss_type.setter
    def avoid_loss_type(self, value):
        self._avoid_loss_type = value
    @property
    def case_end_amount(self):
        return self._case_end_amount

    @case_end_amount.setter
    def case_end_amount(self, value):
        self._case_end_amount = value
    @property
    def fraud_query_request_no(self):
        return self._fraud_query_request_no

    @fraud_query_request_no.setter
    def fraud_query_request_no(self, value):
        self._fraud_query_request_no = value
    @property
    def fraud_result(self):
        return self._fraud_result

    @fraud_result.setter
    def fraud_result(self, value):
        self._fraud_result = value
    @property
    def report_no(self):
        return self._report_no

    @report_no.setter
    def report_no(self, value):
        self._report_no = value
    @property
    def request_no(self):
        return self._request_no

    @request_no.setter
    def request_no(self, value):
        self._request_no = value
    @property
    def syn_type(self):
        return self._syn_type

    @syn_type.setter
    def syn_type(self, value):
        self._syn_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.avoid_loss_amount:
            if hasattr(self.avoid_loss_amount, 'to_alipay_dict'):
                params['avoid_loss_amount'] = self.avoid_loss_amount.to_alipay_dict()
            else:
                params['avoid_loss_amount'] = self.avoid_loss_amount
        if self.avoid_loss_type:
            if hasattr(self.avoid_loss_type, 'to_alipay_dict'):
                params['avoid_loss_type'] = self.avoid_loss_type.to_alipay_dict()
            else:
                params['avoid_loss_type'] = self.avoid_loss_type
        if self.case_end_amount:
            if hasattr(self.case_end_amount, 'to_alipay_dict'):
                params['case_end_amount'] = self.case_end_amount.to_alipay_dict()
            else:
                params['case_end_amount'] = self.case_end_amount
        if self.fraud_query_request_no:
            if hasattr(self.fraud_query_request_no, 'to_alipay_dict'):
                params['fraud_query_request_no'] = self.fraud_query_request_no.to_alipay_dict()
            else:
                params['fraud_query_request_no'] = self.fraud_query_request_no
        if self.fraud_result:
            if hasattr(self.fraud_result, 'to_alipay_dict'):
                params['fraud_result'] = self.fraud_result.to_alipay_dict()
            else:
                params['fraud_result'] = self.fraud_result
        if self.report_no:
            if hasattr(self.report_no, 'to_alipay_dict'):
                params['report_no'] = self.report_no.to_alipay_dict()
            else:
                params['report_no'] = self.report_no
        if self.request_no:
            if hasattr(self.request_no, 'to_alipay_dict'):
                params['request_no'] = self.request_no.to_alipay_dict()
            else:
                params['request_no'] = self.request_no
        if self.syn_type:
            if hasattr(self.syn_type, 'to_alipay_dict'):
                params['syn_type'] = self.syn_type.to_alipay_dict()
            else:
                params['syn_type'] = self.syn_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsDataAutoFraudSyncModel()
        if 'avoid_loss_amount' in d:
            o.avoid_loss_amount = d['avoid_loss_amount']
        if 'avoid_loss_type' in d:
            o.avoid_loss_type = d['avoid_loss_type']
        if 'case_end_amount' in d:
            o.case_end_amount = d['case_end_amount']
        if 'fraud_query_request_no' in d:
            o.fraud_query_request_no = d['fraud_query_request_no']
        if 'fraud_result' in d:
            o.fraud_result = d['fraud_result']
        if 'report_no' in d:
            o.report_no = d['report_no']
        if 'request_no' in d:
            o.request_no = d['request_no']
        if 'syn_type' in d:
            o.syn_type = d['syn_type']
        return o


