#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PaymentAssetInfo import PaymentAssetInfo
from alipay.aop.api.domain.PaymentAssetInfo import PaymentAssetInfo


class PaymentFundInfo(object):

    def __init__(self):
        self._payee_asset_info = None
        self._payer_asset_info = None

    @property
    def payee_asset_info(self):
        return self._payee_asset_info

    @payee_asset_info.setter
    def payee_asset_info(self, value):
        if isinstance(value, PaymentAssetInfo):
            self._payee_asset_info = value
        else:
            self._payee_asset_info = PaymentAssetInfo.from_alipay_dict(value)
    @property
    def payer_asset_info(self):
        return self._payer_asset_info

    @payer_asset_info.setter
    def payer_asset_info(self, value):
        if isinstance(value, PaymentAssetInfo):
            self._payer_asset_info = value
        else:
            self._payer_asset_info = PaymentAssetInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.payee_asset_info:
            if hasattr(self.payee_asset_info, 'to_alipay_dict'):
                params['payee_asset_info'] = self.payee_asset_info.to_alipay_dict()
            else:
                params['payee_asset_info'] = self.payee_asset_info
        if self.payer_asset_info:
            if hasattr(self.payer_asset_info, 'to_alipay_dict'):
                params['payer_asset_info'] = self.payer_asset_info.to_alipay_dict()
            else:
                params['payer_asset_info'] = self.payer_asset_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PaymentFundInfo()
        if 'payee_asset_info' in d:
            o.payee_asset_info = d['payee_asset_info']
        if 'payer_asset_info' in d:
            o.payer_asset_info = d['payer_asset_info']
        return o


