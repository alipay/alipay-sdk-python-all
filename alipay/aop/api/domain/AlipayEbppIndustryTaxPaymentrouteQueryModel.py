#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppIndustryTaxPaymentrouteQueryModel(object):

    def __init__(self):
        self._bt = None
        self._ck = None
        self._open_id = None
        self._source = None
        self._txn_amt = None
        self._user_id = None
        self._v = None

    @property
    def bt(self):
        return self._bt

    @bt.setter
    def bt(self, value):
        self._bt = value
    @property
    def ck(self):
        return self._ck

    @ck.setter
    def ck(self, value):
        self._ck = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def txn_amt(self):
        return self._txn_amt

    @txn_amt.setter
    def txn_amt(self, value):
        self._txn_amt = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def v(self):
        return self._v

    @v.setter
    def v(self, value):
        self._v = value


    def to_alipay_dict(self):
        params = dict()
        if self.bt:
            if hasattr(self.bt, 'to_alipay_dict'):
                params['bt'] = self.bt.to_alipay_dict()
            else:
                params['bt'] = self.bt
        if self.ck:
            if hasattr(self.ck, 'to_alipay_dict'):
                params['ck'] = self.ck.to_alipay_dict()
            else:
                params['ck'] = self.ck
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.txn_amt:
            if hasattr(self.txn_amt, 'to_alipay_dict'):
                params['txn_amt'] = self.txn_amt.to_alipay_dict()
            else:
                params['txn_amt'] = self.txn_amt
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.v:
            if hasattr(self.v, 'to_alipay_dict'):
                params['v'] = self.v.to_alipay_dict()
            else:
                params['v'] = self.v
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppIndustryTaxPaymentrouteQueryModel()
        if 'bt' in d:
            o.bt = d['bt']
        if 'ck' in d:
            o.ck = d['ck']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'source' in d:
            o.source = d['source']
        if 'txn_amt' in d:
            o.txn_amt = d['txn_amt']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'v' in d:
            o.v = d['v']
        return o


