#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechBlockchainTwcPreauthinfoQueryModel(object):

    def __init__(self):
        self._authno = None
        self._buyeruid = None
        self._selleruid = None
        self._totalamount = None

    @property
    def authno(self):
        return self._authno

    @authno.setter
    def authno(self, value):
        self._authno = value
    @property
    def buyeruid(self):
        return self._buyeruid

    @buyeruid.setter
    def buyeruid(self, value):
        self._buyeruid = value
    @property
    def selleruid(self):
        return self._selleruid

    @selleruid.setter
    def selleruid(self, value):
        self._selleruid = value
    @property
    def totalamount(self):
        return self._totalamount

    @totalamount.setter
    def totalamount(self, value):
        self._totalamount = value


    def to_alipay_dict(self):
        params = dict()
        if self.authno:
            if hasattr(self.authno, 'to_alipay_dict'):
                params['authno'] = self.authno.to_alipay_dict()
            else:
                params['authno'] = self.authno
        if self.buyeruid:
            if hasattr(self.buyeruid, 'to_alipay_dict'):
                params['buyeruid'] = self.buyeruid.to_alipay_dict()
            else:
                params['buyeruid'] = self.buyeruid
        if self.selleruid:
            if hasattr(self.selleruid, 'to_alipay_dict'):
                params['selleruid'] = self.selleruid.to_alipay_dict()
            else:
                params['selleruid'] = self.selleruid
        if self.totalamount:
            if hasattr(self.totalamount, 'to_alipay_dict'):
                params['totalamount'] = self.totalamount.to_alipay_dict()
            else:
                params['totalamount'] = self.totalamount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechBlockchainTwcPreauthinfoQueryModel()
        if 'authno' in d:
            o.authno = d['authno']
        if 'buyeruid' in d:
            o.buyeruid = d['buyeruid']
        if 'selleruid' in d:
            o.selleruid = d['selleruid']
        if 'totalamount' in d:
            o.totalamount = d['totalamount']
        return o


