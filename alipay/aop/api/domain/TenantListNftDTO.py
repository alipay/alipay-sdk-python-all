#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TenantListNftDTO(object):

    def __init__(self):
        self._amount = None
        self._nft_id = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def nft_id(self):
        return self._nft_id

    @nft_id.setter
    def nft_id(self, value):
        self._nft_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.nft_id:
            if hasattr(self.nft_id, 'to_alipay_dict'):
                params['nft_id'] = self.nft_id.to_alipay_dict()
            else:
                params['nft_id'] = self.nft_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TenantListNftDTO()
        if 'amount' in d:
            o.amount = d['amount']
        if 'nft_id' in d:
            o.nft_id = d['nft_id']
        return o


