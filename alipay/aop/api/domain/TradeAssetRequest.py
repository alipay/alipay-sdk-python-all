#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TradeAssetRequest(object):

    def __init__(self):
        self._agreement_no = None
        self._asset_amount = None
        self._asset_code = None
        self._portable = None
        self._subject = None

    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def asset_amount(self):
        return self._asset_amount

    @asset_amount.setter
    def asset_amount(self, value):
        self._asset_amount = value
    @property
    def asset_code(self):
        return self._asset_code

    @asset_code.setter
    def asset_code(self, value):
        self._asset_code = value
    @property
    def portable(self):
        return self._portable

    @portable.setter
    def portable(self, value):
        self._portable = value
    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, value):
        self._subject = value


    def to_alipay_dict(self):
        params = dict()
        if self.agreement_no:
            if hasattr(self.agreement_no, 'to_alipay_dict'):
                params['agreement_no'] = self.agreement_no.to_alipay_dict()
            else:
                params['agreement_no'] = self.agreement_no
        if self.asset_amount:
            if hasattr(self.asset_amount, 'to_alipay_dict'):
                params['asset_amount'] = self.asset_amount.to_alipay_dict()
            else:
                params['asset_amount'] = self.asset_amount
        if self.asset_code:
            if hasattr(self.asset_code, 'to_alipay_dict'):
                params['asset_code'] = self.asset_code.to_alipay_dict()
            else:
                params['asset_code'] = self.asset_code
        if self.portable:
            if hasattr(self.portable, 'to_alipay_dict'):
                params['portable'] = self.portable.to_alipay_dict()
            else:
                params['portable'] = self.portable
        if self.subject:
            if hasattr(self.subject, 'to_alipay_dict'):
                params['subject'] = self.subject.to_alipay_dict()
            else:
                params['subject'] = self.subject
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TradeAssetRequest()
        if 'agreement_no' in d:
            o.agreement_no = d['agreement_no']
        if 'asset_amount' in d:
            o.asset_amount = d['asset_amount']
        if 'asset_code' in d:
            o.asset_code = d['asset_code']
        if 'portable' in d:
            o.portable = d['portable']
        if 'subject' in d:
            o.subject = d['subject']
        return o


