#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class VcpAssetDetail(object):

    def __init__(self):
        self._amount = None
        self._assetamount = None
        self._assetusechannel = None
        self._settleuserid = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def assetamount(self):
        return self._assetamount

    @assetamount.setter
    def assetamount(self, value):
        self._assetamount = value
    @property
    def assetusechannel(self):
        return self._assetusechannel

    @assetusechannel.setter
    def assetusechannel(self, value):
        self._assetusechannel = value
    @property
    def settleuserid(self):
        return self._settleuserid

    @settleuserid.setter
    def settleuserid(self, value):
        self._settleuserid = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.assetamount:
            if hasattr(self.assetamount, 'to_alipay_dict'):
                params['assetamount'] = self.assetamount.to_alipay_dict()
            else:
                params['assetamount'] = self.assetamount
        if self.assetusechannel:
            if hasattr(self.assetusechannel, 'to_alipay_dict'):
                params['assetusechannel'] = self.assetusechannel.to_alipay_dict()
            else:
                params['assetusechannel'] = self.assetusechannel
        if self.settleuserid:
            if hasattr(self.settleuserid, 'to_alipay_dict'):
                params['settleuserid'] = self.settleuserid.to_alipay_dict()
            else:
                params['settleuserid'] = self.settleuserid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VcpAssetDetail()
        if 'amount' in d:
            o.amount = d['amount']
        if 'assetamount' in d:
            o.assetamount = d['assetamount']
        if 'assetusechannel' in d:
            o.assetusechannel = d['assetusechannel']
        if 'settleuserid' in d:
            o.settleuserid = d['settleuserid']
        return o


