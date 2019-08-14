#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataAiservicePriceoptimizerDataSyncModel(object):

    def __init__(self):
        self._algo_type = None
        self._app_version = None
        self._base_price = None
        self._biz_time = None
        self._card_id = None
        self._city_code = None
        self._ext_info = None
        self._get_coupon_method = None
        self._merchant_id = None
        self._op_type = None
        self._payment_price = None
        self._payment_type = None
        self._product_type = None
        self._promo_price = None
        self._promo_source = None
        self._promo_type = None
        self._scene_code = None
        self._service_name = None
        self._trace_id = None
        self._trade_channel = None
        self._unit_id = None
        self._user_id = None
        self._valid_time = None

    @property
    def algo_type(self):
        return self._algo_type

    @algo_type.setter
    def algo_type(self, value):
        self._algo_type = value
    @property
    def app_version(self):
        return self._app_version

    @app_version.setter
    def app_version(self, value):
        self._app_version = value
    @property
    def base_price(self):
        return self._base_price

    @base_price.setter
    def base_price(self, value):
        self._base_price = value
    @property
    def biz_time(self):
        return self._biz_time

    @biz_time.setter
    def biz_time(self, value):
        self._biz_time = value
    @property
    def card_id(self):
        return self._card_id

    @card_id.setter
    def card_id(self, value):
        self._card_id = value
    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def get_coupon_method(self):
        return self._get_coupon_method

    @get_coupon_method.setter
    def get_coupon_method(self, value):
        self._get_coupon_method = value
    @property
    def merchant_id(self):
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, value):
        self._merchant_id = value
    @property
    def op_type(self):
        return self._op_type

    @op_type.setter
    def op_type(self, value):
        self._op_type = value
    @property
    def payment_price(self):
        return self._payment_price

    @payment_price.setter
    def payment_price(self, value):
        self._payment_price = value
    @property
    def payment_type(self):
        return self._payment_type

    @payment_type.setter
    def payment_type(self, value):
        self._payment_type = value
    @property
    def product_type(self):
        return self._product_type

    @product_type.setter
    def product_type(self, value):
        self._product_type = value
    @property
    def promo_price(self):
        return self._promo_price

    @promo_price.setter
    def promo_price(self, value):
        self._promo_price = value
    @property
    def promo_source(self):
        return self._promo_source

    @promo_source.setter
    def promo_source(self, value):
        self._promo_source = value
    @property
    def promo_type(self):
        return self._promo_type

    @promo_type.setter
    def promo_type(self, value):
        self._promo_type = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def service_name(self):
        return self._service_name

    @service_name.setter
    def service_name(self, value):
        self._service_name = value
    @property
    def trace_id(self):
        return self._trace_id

    @trace_id.setter
    def trace_id(self, value):
        self._trace_id = value
    @property
    def trade_channel(self):
        return self._trade_channel

    @trade_channel.setter
    def trade_channel(self, value):
        self._trade_channel = value
    @property
    def unit_id(self):
        return self._unit_id

    @unit_id.setter
    def unit_id(self, value):
        self._unit_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def valid_time(self):
        return self._valid_time

    @valid_time.setter
    def valid_time(self, value):
        self._valid_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.algo_type:
            if hasattr(self.algo_type, 'to_alipay_dict'):
                params['algo_type'] = self.algo_type.to_alipay_dict()
            else:
                params['algo_type'] = self.algo_type
        if self.app_version:
            if hasattr(self.app_version, 'to_alipay_dict'):
                params['app_version'] = self.app_version.to_alipay_dict()
            else:
                params['app_version'] = self.app_version
        if self.base_price:
            if hasattr(self.base_price, 'to_alipay_dict'):
                params['base_price'] = self.base_price.to_alipay_dict()
            else:
                params['base_price'] = self.base_price
        if self.biz_time:
            if hasattr(self.biz_time, 'to_alipay_dict'):
                params['biz_time'] = self.biz_time.to_alipay_dict()
            else:
                params['biz_time'] = self.biz_time
        if self.card_id:
            if hasattr(self.card_id, 'to_alipay_dict'):
                params['card_id'] = self.card_id.to_alipay_dict()
            else:
                params['card_id'] = self.card_id
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.get_coupon_method:
            if hasattr(self.get_coupon_method, 'to_alipay_dict'):
                params['get_coupon_method'] = self.get_coupon_method.to_alipay_dict()
            else:
                params['get_coupon_method'] = self.get_coupon_method
        if self.merchant_id:
            if hasattr(self.merchant_id, 'to_alipay_dict'):
                params['merchant_id'] = self.merchant_id.to_alipay_dict()
            else:
                params['merchant_id'] = self.merchant_id
        if self.op_type:
            if hasattr(self.op_type, 'to_alipay_dict'):
                params['op_type'] = self.op_type.to_alipay_dict()
            else:
                params['op_type'] = self.op_type
        if self.payment_price:
            if hasattr(self.payment_price, 'to_alipay_dict'):
                params['payment_price'] = self.payment_price.to_alipay_dict()
            else:
                params['payment_price'] = self.payment_price
        if self.payment_type:
            if hasattr(self.payment_type, 'to_alipay_dict'):
                params['payment_type'] = self.payment_type.to_alipay_dict()
            else:
                params['payment_type'] = self.payment_type
        if self.product_type:
            if hasattr(self.product_type, 'to_alipay_dict'):
                params['product_type'] = self.product_type.to_alipay_dict()
            else:
                params['product_type'] = self.product_type
        if self.promo_price:
            if hasattr(self.promo_price, 'to_alipay_dict'):
                params['promo_price'] = self.promo_price.to_alipay_dict()
            else:
                params['promo_price'] = self.promo_price
        if self.promo_source:
            if hasattr(self.promo_source, 'to_alipay_dict'):
                params['promo_source'] = self.promo_source.to_alipay_dict()
            else:
                params['promo_source'] = self.promo_source
        if self.promo_type:
            if hasattr(self.promo_type, 'to_alipay_dict'):
                params['promo_type'] = self.promo_type.to_alipay_dict()
            else:
                params['promo_type'] = self.promo_type
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.service_name:
            if hasattr(self.service_name, 'to_alipay_dict'):
                params['service_name'] = self.service_name.to_alipay_dict()
            else:
                params['service_name'] = self.service_name
        if self.trace_id:
            if hasattr(self.trace_id, 'to_alipay_dict'):
                params['trace_id'] = self.trace_id.to_alipay_dict()
            else:
                params['trace_id'] = self.trace_id
        if self.trade_channel:
            if hasattr(self.trade_channel, 'to_alipay_dict'):
                params['trade_channel'] = self.trade_channel.to_alipay_dict()
            else:
                params['trade_channel'] = self.trade_channel
        if self.unit_id:
            if hasattr(self.unit_id, 'to_alipay_dict'):
                params['unit_id'] = self.unit_id.to_alipay_dict()
            else:
                params['unit_id'] = self.unit_id
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.valid_time:
            if hasattr(self.valid_time, 'to_alipay_dict'):
                params['valid_time'] = self.valid_time.to_alipay_dict()
            else:
                params['valid_time'] = self.valid_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataAiservicePriceoptimizerDataSyncModel()
        if 'algo_type' in d:
            o.algo_type = d['algo_type']
        if 'app_version' in d:
            o.app_version = d['app_version']
        if 'base_price' in d:
            o.base_price = d['base_price']
        if 'biz_time' in d:
            o.biz_time = d['biz_time']
        if 'card_id' in d:
            o.card_id = d['card_id']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'get_coupon_method' in d:
            o.get_coupon_method = d['get_coupon_method']
        if 'merchant_id' in d:
            o.merchant_id = d['merchant_id']
        if 'op_type' in d:
            o.op_type = d['op_type']
        if 'payment_price' in d:
            o.payment_price = d['payment_price']
        if 'payment_type' in d:
            o.payment_type = d['payment_type']
        if 'product_type' in d:
            o.product_type = d['product_type']
        if 'promo_price' in d:
            o.promo_price = d['promo_price']
        if 'promo_source' in d:
            o.promo_source = d['promo_source']
        if 'promo_type' in d:
            o.promo_type = d['promo_type']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'service_name' in d:
            o.service_name = d['service_name']
        if 'trace_id' in d:
            o.trace_id = d['trace_id']
        if 'trade_channel' in d:
            o.trade_channel = d['trade_channel']
        if 'unit_id' in d:
            o.unit_id = d['unit_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'valid_time' in d:
            o.valid_time = d['valid_time']
        return o


