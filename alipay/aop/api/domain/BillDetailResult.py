#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AmountWf import AmountWf
from alipay.aop.api.domain.AmountWf import AmountWf


class BillDetailResult(object):

    def __init__(self):
        self._balanceamt = None
        self._billno = None
        self._duedate = None
        self._encashamt = None
        self._startdate = None
        self._status = None

    @property
    def balanceamt(self):
        return self._balanceamt

    @balanceamt.setter
    def balanceamt(self, value):
        if isinstance(value, AmountWf):
            self._balanceamt = value
        else:
            self._balanceamt = AmountWf.from_alipay_dict(value)
    @property
    def billno(self):
        return self._billno

    @billno.setter
    def billno(self, value):
        self._billno = value
    @property
    def duedate(self):
        return self._duedate

    @duedate.setter
    def duedate(self, value):
        self._duedate = value
    @property
    def encashamt(self):
        return self._encashamt

    @encashamt.setter
    def encashamt(self, value):
        if isinstance(value, AmountWf):
            self._encashamt = value
        else:
            self._encashamt = AmountWf.from_alipay_dict(value)
    @property
    def startdate(self):
        return self._startdate

    @startdate.setter
    def startdate(self, value):
        self._startdate = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.balanceamt:
            if hasattr(self.balanceamt, 'to_alipay_dict'):
                params['balanceamt'] = self.balanceamt.to_alipay_dict()
            else:
                params['balanceamt'] = self.balanceamt
        if self.billno:
            if hasattr(self.billno, 'to_alipay_dict'):
                params['billno'] = self.billno.to_alipay_dict()
            else:
                params['billno'] = self.billno
        if self.duedate:
            if hasattr(self.duedate, 'to_alipay_dict'):
                params['duedate'] = self.duedate.to_alipay_dict()
            else:
                params['duedate'] = self.duedate
        if self.encashamt:
            if hasattr(self.encashamt, 'to_alipay_dict'):
                params['encashamt'] = self.encashamt.to_alipay_dict()
            else:
                params['encashamt'] = self.encashamt
        if self.startdate:
            if hasattr(self.startdate, 'to_alipay_dict'):
                params['startdate'] = self.startdate.to_alipay_dict()
            else:
                params['startdate'] = self.startdate
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BillDetailResult()
        if 'balanceamt' in d:
            o.balanceamt = d['balanceamt']
        if 'billno' in d:
            o.billno = d['billno']
        if 'duedate' in d:
            o.duedate = d['duedate']
        if 'encashamt' in d:
            o.encashamt = d['encashamt']
        if 'startdate' in d:
            o.startdate = d['startdate']
        if 'status' in d:
            o.status = d['status']
        return o


