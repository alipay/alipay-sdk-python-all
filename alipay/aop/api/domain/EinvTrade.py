#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EinvTrade(object):

    def __init__(self):
        self._bill_no = None
        self._bill_time = None
        self._city_name = None
        self._detail_json = None
        self._download_url = None
        self._extend_map = None
        self._merchant_name = None
        self._out_json = None
        self._payee_name = None
        self._payment_amount = None
        self._payment_time = None
        self._souce = None
        self._trade_type = None

    @property
    def bill_no(self):
        return self._bill_no

    @bill_no.setter
    def bill_no(self, value):
        self._bill_no = value
    @property
    def bill_time(self):
        return self._bill_time

    @bill_time.setter
    def bill_time(self, value):
        self._bill_time = value
    @property
    def city_name(self):
        return self._city_name

    @city_name.setter
    def city_name(self, value):
        self._city_name = value
    @property
    def detail_json(self):
        return self._detail_json

    @detail_json.setter
    def detail_json(self, value):
        self._detail_json = value
    @property
    def download_url(self):
        return self._download_url

    @download_url.setter
    def download_url(self, value):
        self._download_url = value
    @property
    def extend_map(self):
        return self._extend_map

    @extend_map.setter
    def extend_map(self, value):
        self._extend_map = value
    @property
    def merchant_name(self):
        return self._merchant_name

    @merchant_name.setter
    def merchant_name(self, value):
        self._merchant_name = value
    @property
    def out_json(self):
        return self._out_json

    @out_json.setter
    def out_json(self, value):
        self._out_json = value
    @property
    def payee_name(self):
        return self._payee_name

    @payee_name.setter
    def payee_name(self, value):
        self._payee_name = value
    @property
    def payment_amount(self):
        return self._payment_amount

    @payment_amount.setter
    def payment_amount(self, value):
        self._payment_amount = value
    @property
    def payment_time(self):
        return self._payment_time

    @payment_time.setter
    def payment_time(self, value):
        self._payment_time = value
    @property
    def souce(self):
        return self._souce

    @souce.setter
    def souce(self, value):
        self._souce = value
    @property
    def trade_type(self):
        return self._trade_type

    @trade_type.setter
    def trade_type(self, value):
        self._trade_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.bill_no:
            if hasattr(self.bill_no, 'to_alipay_dict'):
                params['bill_no'] = self.bill_no.to_alipay_dict()
            else:
                params['bill_no'] = self.bill_no
        if self.bill_time:
            if hasattr(self.bill_time, 'to_alipay_dict'):
                params['bill_time'] = self.bill_time.to_alipay_dict()
            else:
                params['bill_time'] = self.bill_time
        if self.city_name:
            if hasattr(self.city_name, 'to_alipay_dict'):
                params['city_name'] = self.city_name.to_alipay_dict()
            else:
                params['city_name'] = self.city_name
        if self.detail_json:
            if hasattr(self.detail_json, 'to_alipay_dict'):
                params['detail_json'] = self.detail_json.to_alipay_dict()
            else:
                params['detail_json'] = self.detail_json
        if self.download_url:
            if hasattr(self.download_url, 'to_alipay_dict'):
                params['download_url'] = self.download_url.to_alipay_dict()
            else:
                params['download_url'] = self.download_url
        if self.extend_map:
            if hasattr(self.extend_map, 'to_alipay_dict'):
                params['extend_map'] = self.extend_map.to_alipay_dict()
            else:
                params['extend_map'] = self.extend_map
        if self.merchant_name:
            if hasattr(self.merchant_name, 'to_alipay_dict'):
                params['merchant_name'] = self.merchant_name.to_alipay_dict()
            else:
                params['merchant_name'] = self.merchant_name
        if self.out_json:
            if hasattr(self.out_json, 'to_alipay_dict'):
                params['out_json'] = self.out_json.to_alipay_dict()
            else:
                params['out_json'] = self.out_json
        if self.payee_name:
            if hasattr(self.payee_name, 'to_alipay_dict'):
                params['payee_name'] = self.payee_name.to_alipay_dict()
            else:
                params['payee_name'] = self.payee_name
        if self.payment_amount:
            if hasattr(self.payment_amount, 'to_alipay_dict'):
                params['payment_amount'] = self.payment_amount.to_alipay_dict()
            else:
                params['payment_amount'] = self.payment_amount
        if self.payment_time:
            if hasattr(self.payment_time, 'to_alipay_dict'):
                params['payment_time'] = self.payment_time.to_alipay_dict()
            else:
                params['payment_time'] = self.payment_time
        if self.souce:
            if hasattr(self.souce, 'to_alipay_dict'):
                params['souce'] = self.souce.to_alipay_dict()
            else:
                params['souce'] = self.souce
        if self.trade_type:
            if hasattr(self.trade_type, 'to_alipay_dict'):
                params['trade_type'] = self.trade_type.to_alipay_dict()
            else:
                params['trade_type'] = self.trade_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EinvTrade()
        if 'bill_no' in d:
            o.bill_no = d['bill_no']
        if 'bill_time' in d:
            o.bill_time = d['bill_time']
        if 'city_name' in d:
            o.city_name = d['city_name']
        if 'detail_json' in d:
            o.detail_json = d['detail_json']
        if 'download_url' in d:
            o.download_url = d['download_url']
        if 'extend_map' in d:
            o.extend_map = d['extend_map']
        if 'merchant_name' in d:
            o.merchant_name = d['merchant_name']
        if 'out_json' in d:
            o.out_json = d['out_json']
        if 'payee_name' in d:
            o.payee_name = d['payee_name']
        if 'payment_amount' in d:
            o.payment_amount = d['payment_amount']
        if 'payment_time' in d:
            o.payment_time = d['payment_time']
        if 'souce' in d:
            o.souce = d['souce']
        if 'trade_type' in d:
            o.trade_type = d['trade_type']
        return o


