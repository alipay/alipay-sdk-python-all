#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TradeFundBill import TradeFundBill


class PaytoolRefundResultDetail(object):

    def __init__(self):
        self._gmt_refund = None
        self._paytool_bill_no = None
        self._paytool_request_no = None
        self._refund_amount = None
        self._refund_fund_bill_list = None
        self._status = None
        self._tool_code = None

    @property
    def gmt_refund(self):
        return self._gmt_refund

    @gmt_refund.setter
    def gmt_refund(self, value):
        self._gmt_refund = value
    @property
    def paytool_bill_no(self):
        return self._paytool_bill_no

    @paytool_bill_no.setter
    def paytool_bill_no(self, value):
        self._paytool_bill_no = value
    @property
    def paytool_request_no(self):
        return self._paytool_request_no

    @paytool_request_no.setter
    def paytool_request_no(self, value):
        self._paytool_request_no = value
    @property
    def refund_amount(self):
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        self._refund_amount = value
    @property
    def refund_fund_bill_list(self):
        return self._refund_fund_bill_list

    @refund_fund_bill_list.setter
    def refund_fund_bill_list(self, value):
        if isinstance(value, list):
            self._refund_fund_bill_list = list()
            for i in value:
                if isinstance(i, TradeFundBill):
                    self._refund_fund_bill_list.append(i)
                else:
                    self._refund_fund_bill_list.append(TradeFundBill.from_alipay_dict(i))
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def tool_code(self):
        return self._tool_code

    @tool_code.setter
    def tool_code(self, value):
        self._tool_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.gmt_refund:
            if hasattr(self.gmt_refund, 'to_alipay_dict'):
                params['gmt_refund'] = self.gmt_refund.to_alipay_dict()
            else:
                params['gmt_refund'] = self.gmt_refund
        if self.paytool_bill_no:
            if hasattr(self.paytool_bill_no, 'to_alipay_dict'):
                params['paytool_bill_no'] = self.paytool_bill_no.to_alipay_dict()
            else:
                params['paytool_bill_no'] = self.paytool_bill_no
        if self.paytool_request_no:
            if hasattr(self.paytool_request_no, 'to_alipay_dict'):
                params['paytool_request_no'] = self.paytool_request_no.to_alipay_dict()
            else:
                params['paytool_request_no'] = self.paytool_request_no
        if self.refund_amount:
            if hasattr(self.refund_amount, 'to_alipay_dict'):
                params['refund_amount'] = self.refund_amount.to_alipay_dict()
            else:
                params['refund_amount'] = self.refund_amount
        if self.refund_fund_bill_list:
            if isinstance(self.refund_fund_bill_list, list):
                for i in range(0, len(self.refund_fund_bill_list)):
                    element = self.refund_fund_bill_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.refund_fund_bill_list[i] = element.to_alipay_dict()
            if hasattr(self.refund_fund_bill_list, 'to_alipay_dict'):
                params['refund_fund_bill_list'] = self.refund_fund_bill_list.to_alipay_dict()
            else:
                params['refund_fund_bill_list'] = self.refund_fund_bill_list
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.tool_code:
            if hasattr(self.tool_code, 'to_alipay_dict'):
                params['tool_code'] = self.tool_code.to_alipay_dict()
            else:
                params['tool_code'] = self.tool_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PaytoolRefundResultDetail()
        if 'gmt_refund' in d:
            o.gmt_refund = d['gmt_refund']
        if 'paytool_bill_no' in d:
            o.paytool_bill_no = d['paytool_bill_no']
        if 'paytool_request_no' in d:
            o.paytool_request_no = d['paytool_request_no']
        if 'refund_amount' in d:
            o.refund_amount = d['refund_amount']
        if 'refund_fund_bill_list' in d:
            o.refund_fund_bill_list = d['refund_fund_bill_list']
        if 'status' in d:
            o.status = d['status']
        if 'tool_code' in d:
            o.tool_code = d['tool_code']
        return o


