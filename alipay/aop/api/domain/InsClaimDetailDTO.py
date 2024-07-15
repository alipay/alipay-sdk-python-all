#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InsClaimDetailDTO(object):

    def __init__(self):
        self._claim_fee = None
        self._liability_code = None
        self._liability_name = None
        self._resolve_reason = None

    @property
    def claim_fee(self):
        return self._claim_fee

    @claim_fee.setter
    def claim_fee(self, value):
        self._claim_fee = value
    @property
    def liability_code(self):
        return self._liability_code

    @liability_code.setter
    def liability_code(self, value):
        self._liability_code = value
    @property
    def liability_name(self):
        return self._liability_name

    @liability_name.setter
    def liability_name(self, value):
        self._liability_name = value
    @property
    def resolve_reason(self):
        return self._resolve_reason

    @resolve_reason.setter
    def resolve_reason(self, value):
        self._resolve_reason = value


    def to_alipay_dict(self):
        params = dict()
        if self.claim_fee:
            if hasattr(self.claim_fee, 'to_alipay_dict'):
                params['claim_fee'] = self.claim_fee.to_alipay_dict()
            else:
                params['claim_fee'] = self.claim_fee
        if self.liability_code:
            if hasattr(self.liability_code, 'to_alipay_dict'):
                params['liability_code'] = self.liability_code.to_alipay_dict()
            else:
                params['liability_code'] = self.liability_code
        if self.liability_name:
            if hasattr(self.liability_name, 'to_alipay_dict'):
                params['liability_name'] = self.liability_name.to_alipay_dict()
            else:
                params['liability_name'] = self.liability_name
        if self.resolve_reason:
            if hasattr(self.resolve_reason, 'to_alipay_dict'):
                params['resolve_reason'] = self.resolve_reason.to_alipay_dict()
            else:
                params['resolve_reason'] = self.resolve_reason
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InsClaimDetailDTO()
        if 'claim_fee' in d:
            o.claim_fee = d['claim_fee']
        if 'liability_code' in d:
            o.liability_code = d['liability_code']
        if 'liability_name' in d:
            o.liability_name = d['liability_name']
        if 'resolve_reason' in d:
            o.resolve_reason = d['resolve_reason']
        return o


