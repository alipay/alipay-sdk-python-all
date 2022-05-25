#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AmountWf import AmountWf
from alipay.aop.api.domain.AmountWf import AmountWf
from alipay.aop.api.domain.AmountWf import AmountWf
from alipay.aop.api.domain.AmountWf import AmountWf
from alipay.aop.api.domain.AmountWf import AmountWf
from alipay.aop.api.domain.AmountWf import AmountWf


class MybankCreditSupplychainWfSinglepaymentQueryResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditSupplychainWfSinglepaymentQueryResponse, self).__init__()
        self._balanceamt = None
        self._billno = None
        self._displayrate = None
        self._duedate = None
        self._encashamt = None
        self._fipname = None
        self._grantaccount = None
        self._interest = None
        self._intpenalty = None
        self._paidbillamt = None
        self._prinbalamt = None
        self._rate = None
        self._sellerid = None
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
    def displayrate(self):
        return self._displayrate

    @displayrate.setter
    def displayrate(self, value):
        self._displayrate = value
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
    def fipname(self):
        return self._fipname

    @fipname.setter
    def fipname(self, value):
        self._fipname = value
    @property
    def grantaccount(self):
        return self._grantaccount

    @grantaccount.setter
    def grantaccount(self, value):
        self._grantaccount = value
    @property
    def interest(self):
        return self._interest

    @interest.setter
    def interest(self, value):
        if isinstance(value, AmountWf):
            self._interest = value
        else:
            self._interest = AmountWf.from_alipay_dict(value)
    @property
    def intpenalty(self):
        return self._intpenalty

    @intpenalty.setter
    def intpenalty(self, value):
        if isinstance(value, AmountWf):
            self._intpenalty = value
        else:
            self._intpenalty = AmountWf.from_alipay_dict(value)
    @property
    def paidbillamt(self):
        return self._paidbillamt

    @paidbillamt.setter
    def paidbillamt(self, value):
        if isinstance(value, AmountWf):
            self._paidbillamt = value
        else:
            self._paidbillamt = AmountWf.from_alipay_dict(value)
    @property
    def prinbalamt(self):
        return self._prinbalamt

    @prinbalamt.setter
    def prinbalamt(self, value):
        if isinstance(value, AmountWf):
            self._prinbalamt = value
        else:
            self._prinbalamt = AmountWf.from_alipay_dict(value)
    @property
    def rate(self):
        return self._rate

    @rate.setter
    def rate(self, value):
        self._rate = value
    @property
    def sellerid(self):
        return self._sellerid

    @sellerid.setter
    def sellerid(self, value):
        self._sellerid = value
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

    def parse_response_content(self, response_content):
        response = super(MybankCreditSupplychainWfSinglepaymentQueryResponse, self).parse_response_content(response_content)
        if 'balanceamt' in response:
            self.balanceamt = response['balanceamt']
        if 'billno' in response:
            self.billno = response['billno']
        if 'displayrate' in response:
            self.displayrate = response['displayrate']
        if 'duedate' in response:
            self.duedate = response['duedate']
        if 'encashamt' in response:
            self.encashamt = response['encashamt']
        if 'fipname' in response:
            self.fipname = response['fipname']
        if 'grantaccount' in response:
            self.grantaccount = response['grantaccount']
        if 'interest' in response:
            self.interest = response['interest']
        if 'intpenalty' in response:
            self.intpenalty = response['intpenalty']
        if 'paidbillamt' in response:
            self.paidbillamt = response['paidbillamt']
        if 'prinbalamt' in response:
            self.prinbalamt = response['prinbalamt']
        if 'rate' in response:
            self.rate = response['rate']
        if 'sellerid' in response:
            self.sellerid = response['sellerid']
        if 'startdate' in response:
            self.startdate = response['startdate']
        if 'status' in response:
            self.status = response['status']
