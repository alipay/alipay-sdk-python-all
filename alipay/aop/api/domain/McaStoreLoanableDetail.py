#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AmountWf import AmountWf


class McaStoreLoanableDetail(object):

    def __init__(self):
        self._admit = None
        self._loanableamt = None
        self._sellerid = None

    @property
    def admit(self):
        return self._admit

    @admit.setter
    def admit(self, value):
        self._admit = value
    @property
    def loanableamt(self):
        return self._loanableamt

    @loanableamt.setter
    def loanableamt(self, value):
        if isinstance(value, AmountWf):
            self._loanableamt = value
        else:
            self._loanableamt = AmountWf.from_alipay_dict(value)
    @property
    def sellerid(self):
        return self._sellerid

    @sellerid.setter
    def sellerid(self, value):
        self._sellerid = value


    def to_alipay_dict(self):
        params = dict()
        if self.admit:
            if hasattr(self.admit, 'to_alipay_dict'):
                params['admit'] = self.admit.to_alipay_dict()
            else:
                params['admit'] = self.admit
        if self.loanableamt:
            if hasattr(self.loanableamt, 'to_alipay_dict'):
                params['loanableamt'] = self.loanableamt.to_alipay_dict()
            else:
                params['loanableamt'] = self.loanableamt
        if self.sellerid:
            if hasattr(self.sellerid, 'to_alipay_dict'):
                params['sellerid'] = self.sellerid.to_alipay_dict()
            else:
                params['sellerid'] = self.sellerid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = McaStoreLoanableDetail()
        if 'admit' in d:
            o.admit = d['admit']
        if 'loanableamt' in d:
            o.loanableamt = d['loanableamt']
        if 'sellerid' in d:
            o.sellerid = d['sellerid']
        return o


