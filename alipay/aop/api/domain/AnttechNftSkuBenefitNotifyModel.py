#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechNftSkuBenefitNotifyModel(object):

    def __init__(self):
        self._nft_id = None
        self._sku_id = None

    @property
    def nft_id(self):
        return self._nft_id

    @nft_id.setter
    def nft_id(self, value):
        self._nft_id = value
    @property
    def sku_id(self):
        return self._sku_id

    @sku_id.setter
    def sku_id(self, value):
        self._sku_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.nft_id:
            if hasattr(self.nft_id, 'to_alipay_dict'):
                params['nft_id'] = self.nft_id.to_alipay_dict()
            else:
                params['nft_id'] = self.nft_id
        if self.sku_id:
            if hasattr(self.sku_id, 'to_alipay_dict'):
                params['sku_id'] = self.sku_id.to_alipay_dict()
            else:
                params['sku_id'] = self.sku_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechNftSkuBenefitNotifyModel()
        if 'nft_id' in d:
            o.nft_id = d['nft_id']
        if 'sku_id' in d:
            o.sku_id = d['sku_id']
        return o


