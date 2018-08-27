#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.KbAdvertCommissionClauseResponse import KbAdvertCommissionClauseResponse
from alipay.aop.api.domain.KbAdvertSubjectVoucherResponse import KbAdvertSubjectVoucherResponse


class KbAdvertSubjectResponse(object):

    def __init__(self):
        self._commission_clause = None
        self._type = None
        self._voucher = None

    @property
    def commission_clause(self):
        return self._commission_clause

    @commission_clause.setter
    def commission_clause(self, value):
        if isinstance(value, KbAdvertCommissionClauseResponse):
            self._commission_clause = value
        else:
            self._commission_clause = KbAdvertCommissionClauseResponse.from_alipay_dict(value)
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
    @property
    def voucher(self):
        return self._voucher

    @voucher.setter
    def voucher(self, value):
        if isinstance(value, KbAdvertSubjectVoucherResponse):
            self._voucher = value
        else:
            self._voucher = KbAdvertSubjectVoucherResponse.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.commission_clause:
            if hasattr(self.commission_clause, 'to_alipay_dict'):
                params['commission_clause'] = self.commission_clause.to_alipay_dict()
            else:
                params['commission_clause'] = self.commission_clause
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        if self.voucher:
            if hasattr(self.voucher, 'to_alipay_dict'):
                params['voucher'] = self.voucher.to_alipay_dict()
            else:
                params['voucher'] = self.voucher
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KbAdvertSubjectResponse()
        if 'commission_clause' in d:
            o.commission_clause = d['commission_clause']
        if 'type' in d:
            o.type = d['type']
        if 'voucher' in d:
            o.voucher = d['voucher']
        return o


