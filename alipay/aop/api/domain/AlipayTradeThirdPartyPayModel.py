#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AgreementParams import AgreementParams


class AlipayTradeThirdPartyPayModel(object):

    def __init__(self):
        self._agreement_params = None
        self._extend_params = None
        self._out_biz_no = None
        self._out_trade_no = None
        self._partner_id = None
        self._product_code = None
        self._secondary_merchant_no = None
        self._subject = None
        self._total_amount = None

    @property
    def agreement_params(self):
        return self._agreement_params

    @agreement_params.setter
    def agreement_params(self, value):
        if isinstance(value, AgreementParams):
            self._agreement_params = value
        else:
            self._agreement_params = AgreementParams.from_alipay_dict(value)
    @property
    def extend_params(self):
        return self._extend_params

    @extend_params.setter
    def extend_params(self, value):
        self._extend_params = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def secondary_merchant_no(self):
        return self._secondary_merchant_no

    @secondary_merchant_no.setter
    def secondary_merchant_no(self, value):
        self._secondary_merchant_no = value
    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, value):
        self._subject = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.agreement_params:
            if hasattr(self.agreement_params, 'to_alipay_dict'):
                params['agreement_params'] = self.agreement_params.to_alipay_dict()
            else:
                params['agreement_params'] = self.agreement_params
        if self.extend_params:
            if hasattr(self.extend_params, 'to_alipay_dict'):
                params['extend_params'] = self.extend_params.to_alipay_dict()
            else:
                params['extend_params'] = self.extend_params
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.out_trade_no:
            if hasattr(self.out_trade_no, 'to_alipay_dict'):
                params['out_trade_no'] = self.out_trade_no.to_alipay_dict()
            else:
                params['out_trade_no'] = self.out_trade_no
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.secondary_merchant_no:
            if hasattr(self.secondary_merchant_no, 'to_alipay_dict'):
                params['secondary_merchant_no'] = self.secondary_merchant_no.to_alipay_dict()
            else:
                params['secondary_merchant_no'] = self.secondary_merchant_no
        if self.subject:
            if hasattr(self.subject, 'to_alipay_dict'):
                params['subject'] = self.subject.to_alipay_dict()
            else:
                params['subject'] = self.subject
        if self.total_amount:
            if hasattr(self.total_amount, 'to_alipay_dict'):
                params['total_amount'] = self.total_amount.to_alipay_dict()
            else:
                params['total_amount'] = self.total_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayTradeThirdPartyPayModel()
        if 'agreement_params' in d:
            o.agreement_params = d['agreement_params']
        if 'extend_params' in d:
            o.extend_params = d['extend_params']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'out_trade_no' in d:
            o.out_trade_no = d['out_trade_no']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'secondary_merchant_no' in d:
            o.secondary_merchant_no = d['secondary_merchant_no']
        if 'subject' in d:
            o.subject = d['subject']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        return o


