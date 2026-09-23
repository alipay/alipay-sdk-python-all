#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechNftSkuBenefitNotifyModel(object):

    def __init__(self):
        self._code_type = None
        self._nft_id = None
        self._qr_string = None
        self._sku_id = None

    @property
    def code_type(self):
        return self._code_type

    @code_type.setter
    def code_type(self, value):
        self._code_type = value
    @property
    def nft_id(self):
        return self._nft_id

    @nft_id.setter
    def nft_id(self, value):
        self._nft_id = value
    @property
    def qr_string(self):
        return self._qr_string

    @qr_string.setter
    def qr_string(self, value):
        self._qr_string = value
    @property
    def sku_id(self):
        return self._sku_id

    @sku_id.setter
    def sku_id(self, value):
        self._sku_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.code_type:
            if hasattr(self.code_type, 'to_alipay_dict'):
                params['code_type'] = self.code_type.to_alipay_dict()
            else:
                params['code_type'] = self.code_type
        if self.nft_id:
            if hasattr(self.nft_id, 'to_alipay_dict'):
                params['nft_id'] = self.nft_id.to_alipay_dict()
            else:
                params['nft_id'] = self.nft_id
        if self.qr_string:
            if hasattr(self.qr_string, 'to_alipay_dict'):
                params['qr_string'] = self.qr_string.to_alipay_dict()
            else:
                params['qr_string'] = self.qr_string
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
        if 'code_type' in d:
            o.code_type = d['code_type']
        if 'nft_id' in d:
            o.nft_id = d['nft_id']
        if 'qr_string' in d:
            o.qr_string = d['qr_string']
        if 'sku_id' in d:
            o.sku_id = d['sku_id']
        return o


