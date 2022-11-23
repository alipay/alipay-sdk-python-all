#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EnterpriseCustomerInfoVO import EnterpriseCustomerInfoVO
from alipay.aop.api.domain.CreditPayMoneyVO import CreditPayMoneyVO
from alipay.aop.api.domain.ReceiveInfoVO import ReceiveInfoVO


class MybankCreditLoantradeGuarletterNewinvoiceApplyModel(object):

    def __init__(self):
        self._apply_user_info = None
        self._guar_order_no = None
        self._invoice_amt = None
        self._invoice_type = None
        self._receive_info = None
        self._request_id = None

    @property
    def apply_user_info(self):
        return self._apply_user_info

    @apply_user_info.setter
    def apply_user_info(self, value):
        if isinstance(value, EnterpriseCustomerInfoVO):
            self._apply_user_info = value
        else:
            self._apply_user_info = EnterpriseCustomerInfoVO.from_alipay_dict(value)
    @property
    def guar_order_no(self):
        return self._guar_order_no

    @guar_order_no.setter
    def guar_order_no(self, value):
        self._guar_order_no = value
    @property
    def invoice_amt(self):
        return self._invoice_amt

    @invoice_amt.setter
    def invoice_amt(self, value):
        if isinstance(value, CreditPayMoneyVO):
            self._invoice_amt = value
        else:
            self._invoice_amt = CreditPayMoneyVO.from_alipay_dict(value)
    @property
    def invoice_type(self):
        return self._invoice_type

    @invoice_type.setter
    def invoice_type(self, value):
        self._invoice_type = value
    @property
    def receive_info(self):
        return self._receive_info

    @receive_info.setter
    def receive_info(self, value):
        if isinstance(value, ReceiveInfoVO):
            self._receive_info = value
        else:
            self._receive_info = ReceiveInfoVO.from_alipay_dict(value)
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_user_info:
            if hasattr(self.apply_user_info, 'to_alipay_dict'):
                params['apply_user_info'] = self.apply_user_info.to_alipay_dict()
            else:
                params['apply_user_info'] = self.apply_user_info
        if self.guar_order_no:
            if hasattr(self.guar_order_no, 'to_alipay_dict'):
                params['guar_order_no'] = self.guar_order_no.to_alipay_dict()
            else:
                params['guar_order_no'] = self.guar_order_no
        if self.invoice_amt:
            if hasattr(self.invoice_amt, 'to_alipay_dict'):
                params['invoice_amt'] = self.invoice_amt.to_alipay_dict()
            else:
                params['invoice_amt'] = self.invoice_amt
        if self.invoice_type:
            if hasattr(self.invoice_type, 'to_alipay_dict'):
                params['invoice_type'] = self.invoice_type.to_alipay_dict()
            else:
                params['invoice_type'] = self.invoice_type
        if self.receive_info:
            if hasattr(self.receive_info, 'to_alipay_dict'):
                params['receive_info'] = self.receive_info.to_alipay_dict()
            else:
                params['receive_info'] = self.receive_info
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankCreditLoantradeGuarletterNewinvoiceApplyModel()
        if 'apply_user_info' in d:
            o.apply_user_info = d['apply_user_info']
        if 'guar_order_no' in d:
            o.guar_order_no = d['guar_order_no']
        if 'invoice_amt' in d:
            o.invoice_amt = d['invoice_amt']
        if 'invoice_type' in d:
            o.invoice_type = d['invoice_type']
        if 'receive_info' in d:
            o.receive_info = d['receive_info']
        if 'request_id' in d:
            o.request_id = d['request_id']
        return o


