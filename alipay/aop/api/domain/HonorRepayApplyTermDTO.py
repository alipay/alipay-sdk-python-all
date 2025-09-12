#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class HonorRepayApplyTermDTO(object):

    def __init__(self):
        self._term_amount = None
        self._term_interest = None
        self._term_no = None
        self._term_penalty = None
        self._term_principal = None

    @property
    def term_amount(self):
        return self._term_amount

    @term_amount.setter
    def term_amount(self, value):
        self._term_amount = value
    @property
    def term_interest(self):
        return self._term_interest

    @term_interest.setter
    def term_interest(self, value):
        self._term_interest = value
    @property
    def term_no(self):
        return self._term_no

    @term_no.setter
    def term_no(self, value):
        self._term_no = value
    @property
    def term_penalty(self):
        return self._term_penalty

    @term_penalty.setter
    def term_penalty(self, value):
        self._term_penalty = value
    @property
    def term_principal(self):
        return self._term_principal

    @term_principal.setter
    def term_principal(self, value):
        self._term_principal = value


    def to_alipay_dict(self):
        params = dict()
        if self.term_amount:
            if hasattr(self.term_amount, 'to_alipay_dict'):
                params['term_amount'] = self.term_amount.to_alipay_dict()
            else:
                params['term_amount'] = self.term_amount
        if self.term_interest:
            if hasattr(self.term_interest, 'to_alipay_dict'):
                params['term_interest'] = self.term_interest.to_alipay_dict()
            else:
                params['term_interest'] = self.term_interest
        if self.term_no:
            if hasattr(self.term_no, 'to_alipay_dict'):
                params['term_no'] = self.term_no.to_alipay_dict()
            else:
                params['term_no'] = self.term_no
        if self.term_penalty:
            if hasattr(self.term_penalty, 'to_alipay_dict'):
                params['term_penalty'] = self.term_penalty.to_alipay_dict()
            else:
                params['term_penalty'] = self.term_penalty
        if self.term_principal:
            if hasattr(self.term_principal, 'to_alipay_dict'):
                params['term_principal'] = self.term_principal.to_alipay_dict()
            else:
                params['term_principal'] = self.term_principal
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = HonorRepayApplyTermDTO()
        if 'term_amount' in d:
            o.term_amount = d['term_amount']
        if 'term_interest' in d:
            o.term_interest = d['term_interest']
        if 'term_no' in d:
            o.term_no = d['term_no']
        if 'term_penalty' in d:
            o.term_penalty = d['term_penalty']
        if 'term_principal' in d:
            o.term_principal = d['term_principal']
        return o


