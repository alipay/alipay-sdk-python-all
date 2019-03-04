#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TradeFundBill import TradeFundBill
from alipay.aop.api.domain.UserDetailInfo import UserDetailInfo


class PaytoolResultDetail(object):

    def __init__(self):
        self._alipay_trade_no = None
        self._amount = None
        self._fund_bill_list = None
        self._gmt_pay = None
        self._payer_info = None
        self._paytool_bill_no = None
        self._paytool_request_no = None
        self._status = None
        self._tool_code = None

    @property
    def alipay_trade_no(self):
        return self._alipay_trade_no

    @alipay_trade_no.setter
    def alipay_trade_no(self, value):
        self._alipay_trade_no = value
    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def fund_bill_list(self):
        return self._fund_bill_list

    @fund_bill_list.setter
    def fund_bill_list(self, value):
        if isinstance(value, list):
            self._fund_bill_list = list()
            for i in value:
                if isinstance(i, TradeFundBill):
                    self._fund_bill_list.append(i)
                else:
                    self._fund_bill_list.append(TradeFundBill.from_alipay_dict(i))
    @property
    def gmt_pay(self):
        return self._gmt_pay

    @gmt_pay.setter
    def gmt_pay(self, value):
        self._gmt_pay = value
    @property
    def payer_info(self):
        return self._payer_info

    @payer_info.setter
    def payer_info(self, value):
        if isinstance(value, UserDetailInfo):
            self._payer_info = value
        else:
            self._payer_info = UserDetailInfo.from_alipay_dict(value)
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
        if self.alipay_trade_no:
            if hasattr(self.alipay_trade_no, 'to_alipay_dict'):
                params['alipay_trade_no'] = self.alipay_trade_no.to_alipay_dict()
            else:
                params['alipay_trade_no'] = self.alipay_trade_no
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.fund_bill_list:
            if isinstance(self.fund_bill_list, list):
                for i in range(0, len(self.fund_bill_list)):
                    element = self.fund_bill_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.fund_bill_list[i] = element.to_alipay_dict()
            if hasattr(self.fund_bill_list, 'to_alipay_dict'):
                params['fund_bill_list'] = self.fund_bill_list.to_alipay_dict()
            else:
                params['fund_bill_list'] = self.fund_bill_list
        if self.gmt_pay:
            if hasattr(self.gmt_pay, 'to_alipay_dict'):
                params['gmt_pay'] = self.gmt_pay.to_alipay_dict()
            else:
                params['gmt_pay'] = self.gmt_pay
        if self.payer_info:
            if hasattr(self.payer_info, 'to_alipay_dict'):
                params['payer_info'] = self.payer_info.to_alipay_dict()
            else:
                params['payer_info'] = self.payer_info
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
        o = PaytoolResultDetail()
        if 'alipay_trade_no' in d:
            o.alipay_trade_no = d['alipay_trade_no']
        if 'amount' in d:
            o.amount = d['amount']
        if 'fund_bill_list' in d:
            o.fund_bill_list = d['fund_bill_list']
        if 'gmt_pay' in d:
            o.gmt_pay = d['gmt_pay']
        if 'payer_info' in d:
            o.payer_info = d['payer_info']
        if 'paytool_bill_no' in d:
            o.paytool_bill_no = d['paytool_bill_no']
        if 'paytool_request_no' in d:
            o.paytool_request_no = d['paytool_request_no']
        if 'status' in d:
            o.status = d['status']
        if 'tool_code' in d:
            o.tool_code = d['tool_code']
        return o


