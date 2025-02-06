#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.UnifiedSettleExtendParams import UnifiedSettleExtendParams
from alipay.aop.api.domain.SettleInfo import SettleInfo
from alipay.aop.api.domain.SubMerchant import SubMerchant


class AlipayTradeUnifiedsettleSyncModel(object):

    def __init__(self):
        self._acquire_mode = None
        self._amount = None
        self._extend_params = None
        self._external_inst_biz_date = None
        self._external_inst_channel = None
        self._external_inst_create_date = None
        self._out_request_no = None
        self._out_trade_no = None
        self._product_code = None
        self._request_type = None
        self._settle_info = None
        self._sub_merchant = None

    @property
    def acquire_mode(self):
        return self._acquire_mode

    @acquire_mode.setter
    def acquire_mode(self, value):
        self._acquire_mode = value
    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def extend_params(self):
        return self._extend_params

    @extend_params.setter
    def extend_params(self, value):
        if isinstance(value, UnifiedSettleExtendParams):
            self._extend_params = value
        else:
            self._extend_params = UnifiedSettleExtendParams.from_alipay_dict(value)
    @property
    def external_inst_biz_date(self):
        return self._external_inst_biz_date

    @external_inst_biz_date.setter
    def external_inst_biz_date(self, value):
        self._external_inst_biz_date = value
    @property
    def external_inst_channel(self):
        return self._external_inst_channel

    @external_inst_channel.setter
    def external_inst_channel(self, value):
        self._external_inst_channel = value
    @property
    def external_inst_create_date(self):
        return self._external_inst_create_date

    @external_inst_create_date.setter
    def external_inst_create_date(self, value):
        self._external_inst_create_date = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def request_type(self):
        return self._request_type

    @request_type.setter
    def request_type(self, value):
        self._request_type = value
    @property
    def settle_info(self):
        return self._settle_info

    @settle_info.setter
    def settle_info(self, value):
        if isinstance(value, SettleInfo):
            self._settle_info = value
        else:
            self._settle_info = SettleInfo.from_alipay_dict(value)
    @property
    def sub_merchant(self):
        return self._sub_merchant

    @sub_merchant.setter
    def sub_merchant(self, value):
        if isinstance(value, SubMerchant):
            self._sub_merchant = value
        else:
            self._sub_merchant = SubMerchant.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.acquire_mode:
            if hasattr(self.acquire_mode, 'to_alipay_dict'):
                params['acquire_mode'] = self.acquire_mode.to_alipay_dict()
            else:
                params['acquire_mode'] = self.acquire_mode
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.extend_params:
            if hasattr(self.extend_params, 'to_alipay_dict'):
                params['extend_params'] = self.extend_params.to_alipay_dict()
            else:
                params['extend_params'] = self.extend_params
        if self.external_inst_biz_date:
            if hasattr(self.external_inst_biz_date, 'to_alipay_dict'):
                params['external_inst_biz_date'] = self.external_inst_biz_date.to_alipay_dict()
            else:
                params['external_inst_biz_date'] = self.external_inst_biz_date
        if self.external_inst_channel:
            if hasattr(self.external_inst_channel, 'to_alipay_dict'):
                params['external_inst_channel'] = self.external_inst_channel.to_alipay_dict()
            else:
                params['external_inst_channel'] = self.external_inst_channel
        if self.external_inst_create_date:
            if hasattr(self.external_inst_create_date, 'to_alipay_dict'):
                params['external_inst_create_date'] = self.external_inst_create_date.to_alipay_dict()
            else:
                params['external_inst_create_date'] = self.external_inst_create_date
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        if self.out_trade_no:
            if hasattr(self.out_trade_no, 'to_alipay_dict'):
                params['out_trade_no'] = self.out_trade_no.to_alipay_dict()
            else:
                params['out_trade_no'] = self.out_trade_no
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.request_type:
            if hasattr(self.request_type, 'to_alipay_dict'):
                params['request_type'] = self.request_type.to_alipay_dict()
            else:
                params['request_type'] = self.request_type
        if self.settle_info:
            if hasattr(self.settle_info, 'to_alipay_dict'):
                params['settle_info'] = self.settle_info.to_alipay_dict()
            else:
                params['settle_info'] = self.settle_info
        if self.sub_merchant:
            if hasattr(self.sub_merchant, 'to_alipay_dict'):
                params['sub_merchant'] = self.sub_merchant.to_alipay_dict()
            else:
                params['sub_merchant'] = self.sub_merchant
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayTradeUnifiedsettleSyncModel()
        if 'acquire_mode' in d:
            o.acquire_mode = d['acquire_mode']
        if 'amount' in d:
            o.amount = d['amount']
        if 'extend_params' in d:
            o.extend_params = d['extend_params']
        if 'external_inst_biz_date' in d:
            o.external_inst_biz_date = d['external_inst_biz_date']
        if 'external_inst_channel' in d:
            o.external_inst_channel = d['external_inst_channel']
        if 'external_inst_create_date' in d:
            o.external_inst_create_date = d['external_inst_create_date']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'out_trade_no' in d:
            o.out_trade_no = d['out_trade_no']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'request_type' in d:
            o.request_type = d['request_type']
        if 'settle_info' in d:
            o.settle_info = d['settle_info']
        if 'sub_merchant' in d:
            o.sub_merchant = d['sub_merchant']
        return o


