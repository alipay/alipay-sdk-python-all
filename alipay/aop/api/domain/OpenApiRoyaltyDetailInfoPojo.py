#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class OpenApiRoyaltyDetailInfoPojo(object):

    def __init__(self):
        self._amount = None
        self._amount_percentage = None
        self._desc = None
        self._royalty_type = None
        self._trans_in = None
        self._trans_in_type = None
        self._trans_out = None
        self._trans_out_type = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def amount_percentage(self):
        return self._amount_percentage

    @amount_percentage.setter
    def amount_percentage(self, value):
        self._amount_percentage = value
    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def royalty_type(self):
        return self._royalty_type

    @royalty_type.setter
    def royalty_type(self, value):
        self._royalty_type = value
    @property
    def trans_in(self):
        return self._trans_in

    @trans_in.setter
    def trans_in(self, value):
        self._trans_in = value
    @property
    def trans_in_type(self):
        return self._trans_in_type

    @trans_in_type.setter
    def trans_in_type(self, value):
        self._trans_in_type = value
    @property
    def trans_out(self):
        return self._trans_out

    @trans_out.setter
    def trans_out(self, value):
        self._trans_out = value
    @property
    def trans_out_type(self):
        return self._trans_out_type

    @trans_out_type.setter
    def trans_out_type(self, value):
        self._trans_out_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.amount_percentage:
            if hasattr(self.amount_percentage, 'to_alipay_dict'):
                params['amount_percentage'] = self.amount_percentage.to_alipay_dict()
            else:
                params['amount_percentage'] = self.amount_percentage
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
        if self.royalty_type:
            if hasattr(self.royalty_type, 'to_alipay_dict'):
                params['royalty_type'] = self.royalty_type.to_alipay_dict()
            else:
                params['royalty_type'] = self.royalty_type
        if self.trans_in:
            if hasattr(self.trans_in, 'to_alipay_dict'):
                params['trans_in'] = self.trans_in.to_alipay_dict()
            else:
                params['trans_in'] = self.trans_in
        if self.trans_in_type:
            if hasattr(self.trans_in_type, 'to_alipay_dict'):
                params['trans_in_type'] = self.trans_in_type.to_alipay_dict()
            else:
                params['trans_in_type'] = self.trans_in_type
        if self.trans_out:
            if hasattr(self.trans_out, 'to_alipay_dict'):
                params['trans_out'] = self.trans_out.to_alipay_dict()
            else:
                params['trans_out'] = self.trans_out
        if self.trans_out_type:
            if hasattr(self.trans_out_type, 'to_alipay_dict'):
                params['trans_out_type'] = self.trans_out_type.to_alipay_dict()
            else:
                params['trans_out_type'] = self.trans_out_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenApiRoyaltyDetailInfoPojo()
        if 'amount' in d:
            o.amount = d['amount']
        if 'amount_percentage' in d:
            o.amount_percentage = d['amount_percentage']
        if 'desc' in d:
            o.desc = d['desc']
        if 'royalty_type' in d:
            o.royalty_type = d['royalty_type']
        if 'trans_in' in d:
            o.trans_in = d['trans_in']
        if 'trans_in_type' in d:
            o.trans_in_type = d['trans_in_type']
        if 'trans_out' in d:
            o.trans_out = d['trans_out']
        if 'trans_out_type' in d:
            o.trans_out_type = d['trans_out_type']
        return o


