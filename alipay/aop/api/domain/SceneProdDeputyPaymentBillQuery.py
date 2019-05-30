#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SceneProdDeputyPaymentBillQuery(object):

    def __init__(self):
        self._deputy_account = None
        self._deputy_status = None
        self._term = None

    @property
    def deputy_account(self):
        return self._deputy_account

    @deputy_account.setter
    def deputy_account(self, value):
        self._deputy_account = value
    @property
    def deputy_status(self):
        return self._deputy_status

    @deputy_status.setter
    def deputy_status(self, value):
        self._deputy_status = value
    @property
    def term(self):
        return self._term

    @term.setter
    def term(self, value):
        self._term = value


    def to_alipay_dict(self):
        params = dict()
        if self.deputy_account:
            if hasattr(self.deputy_account, 'to_alipay_dict'):
                params['deputy_account'] = self.deputy_account.to_alipay_dict()
            else:
                params['deputy_account'] = self.deputy_account
        if self.deputy_status:
            if hasattr(self.deputy_status, 'to_alipay_dict'):
                params['deputy_status'] = self.deputy_status.to_alipay_dict()
            else:
                params['deputy_status'] = self.deputy_status
        if self.term:
            if hasattr(self.term, 'to_alipay_dict'):
                params['term'] = self.term.to_alipay_dict()
            else:
                params['term'] = self.term
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SceneProdDeputyPaymentBillQuery()
        if 'deputy_account' in d:
            o.deputy_account = d['deputy_account']
        if 'deputy_status' in d:
            o.deputy_status = d['deputy_status']
        if 'term' in d:
            o.term = d['term']
        return o


