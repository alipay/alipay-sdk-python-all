#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.UserIdentity import UserIdentity


class PaytoolRequestDetail(object):

    def __init__(self):
        self._amount = None
        self._payer_identity = None
        self._paytool_business_info = None
        self._paytool_request_no = None
        self._tool_code = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def payer_identity(self):
        return self._payer_identity

    @payer_identity.setter
    def payer_identity(self, value):
        if isinstance(value, UserIdentity):
            self._payer_identity = value
        else:
            self._payer_identity = UserIdentity.from_alipay_dict(value)
    @property
    def paytool_business_info(self):
        return self._paytool_business_info

    @paytool_business_info.setter
    def paytool_business_info(self, value):
        self._paytool_business_info = value
    @property
    def paytool_request_no(self):
        return self._paytool_request_no

    @paytool_request_no.setter
    def paytool_request_no(self, value):
        self._paytool_request_no = value
    @property
    def tool_code(self):
        return self._tool_code

    @tool_code.setter
    def tool_code(self, value):
        self._tool_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.payer_identity:
            if hasattr(self.payer_identity, 'to_alipay_dict'):
                params['payer_identity'] = self.payer_identity.to_alipay_dict()
            else:
                params['payer_identity'] = self.payer_identity
        if self.paytool_business_info:
            if hasattr(self.paytool_business_info, 'to_alipay_dict'):
                params['paytool_business_info'] = self.paytool_business_info.to_alipay_dict()
            else:
                params['paytool_business_info'] = self.paytool_business_info
        if self.paytool_request_no:
            if hasattr(self.paytool_request_no, 'to_alipay_dict'):
                params['paytool_request_no'] = self.paytool_request_no.to_alipay_dict()
            else:
                params['paytool_request_no'] = self.paytool_request_no
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
        o = PaytoolRequestDetail()
        if 'amount' in d:
            o.amount = d['amount']
        if 'payer_identity' in d:
            o.payer_identity = d['payer_identity']
        if 'paytool_business_info' in d:
            o.paytool_business_info = d['paytool_business_info']
        if 'paytool_request_no' in d:
            o.paytool_request_no = d['paytool_request_no']
        if 'tool_code' in d:
            o.tool_code = d['tool_code']
        return o


