#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InteligentSendRule import InteligentSendRule
from alipay.aop.api.domain.InteligentVoucher import InteligentVoucher


class InteligentPromoTool(object):

    def __init__(self):
        self._inteligent_send_rule = None
        self._inteligent_voucher = None
        self._status = None
        self._voucher_no = None

    @property
    def inteligent_send_rule(self):
        return self._inteligent_send_rule

    @inteligent_send_rule.setter
    def inteligent_send_rule(self, value):
        if isinstance(value, InteligentSendRule):
            self._inteligent_send_rule = value
        else:
            self._inteligent_send_rule = InteligentSendRule.from_alipay_dict(value)
    @property
    def inteligent_voucher(self):
        return self._inteligent_voucher

    @inteligent_voucher.setter
    def inteligent_voucher(self, value):
        if isinstance(value, InteligentVoucher):
            self._inteligent_voucher = value
        else:
            self._inteligent_voucher = InteligentVoucher.from_alipay_dict(value)
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def voucher_no(self):
        return self._voucher_no

    @voucher_no.setter
    def voucher_no(self, value):
        self._voucher_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.inteligent_send_rule:
            if hasattr(self.inteligent_send_rule, 'to_alipay_dict'):
                params['inteligent_send_rule'] = self.inteligent_send_rule.to_alipay_dict()
            else:
                params['inteligent_send_rule'] = self.inteligent_send_rule
        if self.inteligent_voucher:
            if hasattr(self.inteligent_voucher, 'to_alipay_dict'):
                params['inteligent_voucher'] = self.inteligent_voucher.to_alipay_dict()
            else:
                params['inteligent_voucher'] = self.inteligent_voucher
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.voucher_no:
            if hasattr(self.voucher_no, 'to_alipay_dict'):
                params['voucher_no'] = self.voucher_no.to_alipay_dict()
            else:
                params['voucher_no'] = self.voucher_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InteligentPromoTool()
        if 'inteligent_send_rule' in d:
            o.inteligent_send_rule = d['inteligent_send_rule']
        if 'inteligent_voucher' in d:
            o.inteligent_voucher = d['inteligent_voucher']
        if 'status' in d:
            o.status = d['status']
        if 'voucher_no' in d:
            o.voucher_no = d['voucher_no']
        return o


