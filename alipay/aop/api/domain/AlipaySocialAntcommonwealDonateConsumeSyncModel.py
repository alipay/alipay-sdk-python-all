#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySocialAntcommonwealDonateConsumeSyncModel(object):

    def __init__(self):
        self._alipay_trade_no = None
        self._currency = None
        self._ext_info = None
        self._gmt_trade_finished = None
        self._out_merchant_id = None
        self._platform_trade_no = None
        self._product_code = None
        self._scene_code = None
        self._seller_user_id = None
        self._source = None
        self._trade_amount = None
        self._user_id = None

    @property
    def alipay_trade_no(self):
        return self._alipay_trade_no

    @alipay_trade_no.setter
    def alipay_trade_no(self, value):
        self._alipay_trade_no = value
    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def gmt_trade_finished(self):
        return self._gmt_trade_finished

    @gmt_trade_finished.setter
    def gmt_trade_finished(self, value):
        self._gmt_trade_finished = value
    @property
    def out_merchant_id(self):
        return self._out_merchant_id

    @out_merchant_id.setter
    def out_merchant_id(self, value):
        self._out_merchant_id = value
    @property
    def platform_trade_no(self):
        return self._platform_trade_no

    @platform_trade_no.setter
    def platform_trade_no(self, value):
        self._platform_trade_no = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def seller_user_id(self):
        return self._seller_user_id

    @seller_user_id.setter
    def seller_user_id(self, value):
        self._seller_user_id = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def trade_amount(self):
        return self._trade_amount

    @trade_amount.setter
    def trade_amount(self, value):
        self._trade_amount = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_trade_no:
            if hasattr(self.alipay_trade_no, 'to_alipay_dict'):
                params['alipay_trade_no'] = self.alipay_trade_no.to_alipay_dict()
            else:
                params['alipay_trade_no'] = self.alipay_trade_no
        if self.currency:
            if hasattr(self.currency, 'to_alipay_dict'):
                params['currency'] = self.currency.to_alipay_dict()
            else:
                params['currency'] = self.currency
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.gmt_trade_finished:
            if hasattr(self.gmt_trade_finished, 'to_alipay_dict'):
                params['gmt_trade_finished'] = self.gmt_trade_finished.to_alipay_dict()
            else:
                params['gmt_trade_finished'] = self.gmt_trade_finished
        if self.out_merchant_id:
            if hasattr(self.out_merchant_id, 'to_alipay_dict'):
                params['out_merchant_id'] = self.out_merchant_id.to_alipay_dict()
            else:
                params['out_merchant_id'] = self.out_merchant_id
        if self.platform_trade_no:
            if hasattr(self.platform_trade_no, 'to_alipay_dict'):
                params['platform_trade_no'] = self.platform_trade_no.to_alipay_dict()
            else:
                params['platform_trade_no'] = self.platform_trade_no
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.seller_user_id:
            if hasattr(self.seller_user_id, 'to_alipay_dict'):
                params['seller_user_id'] = self.seller_user_id.to_alipay_dict()
            else:
                params['seller_user_id'] = self.seller_user_id
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.trade_amount:
            if hasattr(self.trade_amount, 'to_alipay_dict'):
                params['trade_amount'] = self.trade_amount.to_alipay_dict()
            else:
                params['trade_amount'] = self.trade_amount
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySocialAntcommonwealDonateConsumeSyncModel()
        if 'alipay_trade_no' in d:
            o.alipay_trade_no = d['alipay_trade_no']
        if 'currency' in d:
            o.currency = d['currency']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'gmt_trade_finished' in d:
            o.gmt_trade_finished = d['gmt_trade_finished']
        if 'out_merchant_id' in d:
            o.out_merchant_id = d['out_merchant_id']
        if 'platform_trade_no' in d:
            o.platform_trade_no = d['platform_trade_no']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'seller_user_id' in d:
            o.seller_user_id = d['seller_user_id']
        if 'source' in d:
            o.source = d['source']
        if 'trade_amount' in d:
            o.trade_amount = d['trade_amount']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


