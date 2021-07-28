#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayPcreditHuabeiAuthRefundApplyModel(object):

    def __init__(self):
        self._agreement_no = None
        self._alipay_user_id = None
        self._auth_opt_id = None
        self._memo = None
        self._out_request_no = None
        self._partner_id = None
        self._refund_amount = None
        self._refund_type = None
        self._trade_no = None

    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def auth_opt_id(self):
        return self._auth_opt_id

    @auth_opt_id.setter
    def auth_opt_id(self, value):
        self._auth_opt_id = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def refund_amount(self):
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        self._refund_amount = value
    @property
    def refund_type(self):
        return self._refund_type

    @refund_type.setter
    def refund_type(self, value):
        self._refund_type = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.agreement_no:
            if hasattr(self.agreement_no, 'to_alipay_dict'):
                params['agreement_no'] = self.agreement_no.to_alipay_dict()
            else:
                params['agreement_no'] = self.agreement_no
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.auth_opt_id:
            if hasattr(self.auth_opt_id, 'to_alipay_dict'):
                params['auth_opt_id'] = self.auth_opt_id.to_alipay_dict()
            else:
                params['auth_opt_id'] = self.auth_opt_id
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        if self.refund_amount:
            if hasattr(self.refund_amount, 'to_alipay_dict'):
                params['refund_amount'] = self.refund_amount.to_alipay_dict()
            else:
                params['refund_amount'] = self.refund_amount
        if self.refund_type:
            if hasattr(self.refund_type, 'to_alipay_dict'):
                params['refund_type'] = self.refund_type.to_alipay_dict()
            else:
                params['refund_type'] = self.refund_type
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayPcreditHuabeiAuthRefundApplyModel()
        if 'agreement_no' in d:
            o.agreement_no = d['agreement_no']
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'auth_opt_id' in d:
            o.auth_opt_id = d['auth_opt_id']
        if 'memo' in d:
            o.memo = d['memo']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'refund_amount' in d:
            o.refund_amount = d['refund_amount']
        if 'refund_type' in d:
            o.refund_type = d['refund_type']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        return o


