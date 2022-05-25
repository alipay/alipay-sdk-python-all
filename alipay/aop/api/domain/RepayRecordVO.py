#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AmountWf import AmountWf


class RepayRecordVO(object):

    def __init__(self):
        self._accountextno = None
        self._repayamt = None
        self._repaydate = None
        self._repaytype = None

    @property
    def accountextno(self):
        return self._accountextno

    @accountextno.setter
    def accountextno(self, value):
        self._accountextno = value
    @property
    def repayamt(self):
        return self._repayamt

    @repayamt.setter
    def repayamt(self, value):
        if isinstance(value, AmountWf):
            self._repayamt = value
        else:
            self._repayamt = AmountWf.from_alipay_dict(value)
    @property
    def repaydate(self):
        return self._repaydate

    @repaydate.setter
    def repaydate(self, value):
        self._repaydate = value
    @property
    def repaytype(self):
        return self._repaytype

    @repaytype.setter
    def repaytype(self, value):
        self._repaytype = value


    def to_alipay_dict(self):
        params = dict()
        if self.accountextno:
            if hasattr(self.accountextno, 'to_alipay_dict'):
                params['accountextno'] = self.accountextno.to_alipay_dict()
            else:
                params['accountextno'] = self.accountextno
        if self.repayamt:
            if hasattr(self.repayamt, 'to_alipay_dict'):
                params['repayamt'] = self.repayamt.to_alipay_dict()
            else:
                params['repayamt'] = self.repayamt
        if self.repaydate:
            if hasattr(self.repaydate, 'to_alipay_dict'):
                params['repaydate'] = self.repaydate.to_alipay_dict()
            else:
                params['repaydate'] = self.repaydate
        if self.repaytype:
            if hasattr(self.repaytype, 'to_alipay_dict'):
                params['repaytype'] = self.repaytype.to_alipay_dict()
            else:
                params['repaytype'] = self.repaytype
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RepayRecordVO()
        if 'accountextno' in d:
            o.accountextno = d['accountextno']
        if 'repayamt' in d:
            o.repayamt = d['repayamt']
        if 'repaydate' in d:
            o.repaydate = d['repaydate']
        if 'repaytype' in d:
            o.repaytype = d['repaytype']
        return o


