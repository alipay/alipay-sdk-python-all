#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.VoucherUserExternalTradeInfo import VoucherUserExternalTradeInfo


class AlipayOfflineMarketingVoucherUseModel(object):

    def __init__(self):
        self._extend_params = None
        self._external_id = None
        self._external_trade_info = None
        self._external_voucher_code = None

    @property
    def extend_params(self):
        return self._extend_params

    @extend_params.setter
    def extend_params(self, value):
        self._extend_params = value
    @property
    def external_id(self):
        return self._external_id

    @external_id.setter
    def external_id(self, value):
        self._external_id = value
    @property
    def external_trade_info(self):
        return self._external_trade_info

    @external_trade_info.setter
    def external_trade_info(self, value):
        if isinstance(value, VoucherUserExternalTradeInfo):
            self._external_trade_info = value
        else:
            self._external_trade_info = VoucherUserExternalTradeInfo.from_alipay_dict(value)
    @property
    def external_voucher_code(self):
        return self._external_voucher_code

    @external_voucher_code.setter
    def external_voucher_code(self, value):
        self._external_voucher_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.extend_params:
            if hasattr(self.extend_params, 'to_alipay_dict'):
                params['extend_params'] = self.extend_params.to_alipay_dict()
            else:
                params['extend_params'] = self.extend_params
        if self.external_id:
            if hasattr(self.external_id, 'to_alipay_dict'):
                params['external_id'] = self.external_id.to_alipay_dict()
            else:
                params['external_id'] = self.external_id
        if self.external_trade_info:
            if hasattr(self.external_trade_info, 'to_alipay_dict'):
                params['external_trade_info'] = self.external_trade_info.to_alipay_dict()
            else:
                params['external_trade_info'] = self.external_trade_info
        if self.external_voucher_code:
            if hasattr(self.external_voucher_code, 'to_alipay_dict'):
                params['external_voucher_code'] = self.external_voucher_code.to_alipay_dict()
            else:
                params['external_voucher_code'] = self.external_voucher_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOfflineMarketingVoucherUseModel()
        if 'extend_params' in d:
            o.extend_params = d['extend_params']
        if 'external_id' in d:
            o.external_id = d['external_id']
        if 'external_trade_info' in d:
            o.external_trade_info = d['external_trade_info']
        if 'external_voucher_code' in d:
            o.external_voucher_code = d['external_voucher_code']
        return o


