#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportEtccardTradeSyncModel(object):

    def __init__(self):
        self._card_id = None
        self._en_station_id = None
        self._en_station_name = None
        self._en_time = None
        self._ex_station_id = None
        self._ex_station_name = None
        self._ex_time = None
        self._fee = None
        self._plate_color = None
        self._plate_no = None
        self._province_code = None
        self._province_name = None
        self._trade_id = None

    @property
    def card_id(self):
        return self._card_id

    @card_id.setter
    def card_id(self, value):
        self._card_id = value
    @property
    def en_station_id(self):
        return self._en_station_id

    @en_station_id.setter
    def en_station_id(self, value):
        self._en_station_id = value
    @property
    def en_station_name(self):
        return self._en_station_name

    @en_station_name.setter
    def en_station_name(self, value):
        self._en_station_name = value
    @property
    def en_time(self):
        return self._en_time

    @en_time.setter
    def en_time(self, value):
        self._en_time = value
    @property
    def ex_station_id(self):
        return self._ex_station_id

    @ex_station_id.setter
    def ex_station_id(self, value):
        self._ex_station_id = value
    @property
    def ex_station_name(self):
        return self._ex_station_name

    @ex_station_name.setter
    def ex_station_name(self, value):
        self._ex_station_name = value
    @property
    def ex_time(self):
        return self._ex_time

    @ex_time.setter
    def ex_time(self, value):
        self._ex_time = value
    @property
    def fee(self):
        return self._fee

    @fee.setter
    def fee(self, value):
        self._fee = value
    @property
    def plate_color(self):
        return self._plate_color

    @plate_color.setter
    def plate_color(self, value):
        self._plate_color = value
    @property
    def plate_no(self):
        return self._plate_no

    @plate_no.setter
    def plate_no(self, value):
        self._plate_no = value
    @property
    def province_code(self):
        return self._province_code

    @province_code.setter
    def province_code(self, value):
        self._province_code = value
    @property
    def province_name(self):
        return self._province_name

    @province_name.setter
    def province_name(self, value):
        self._province_name = value
    @property
    def trade_id(self):
        return self._trade_id

    @trade_id.setter
    def trade_id(self, value):
        self._trade_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.card_id:
            if hasattr(self.card_id, 'to_alipay_dict'):
                params['card_id'] = self.card_id.to_alipay_dict()
            else:
                params['card_id'] = self.card_id
        if self.en_station_id:
            if hasattr(self.en_station_id, 'to_alipay_dict'):
                params['en_station_id'] = self.en_station_id.to_alipay_dict()
            else:
                params['en_station_id'] = self.en_station_id
        if self.en_station_name:
            if hasattr(self.en_station_name, 'to_alipay_dict'):
                params['en_station_name'] = self.en_station_name.to_alipay_dict()
            else:
                params['en_station_name'] = self.en_station_name
        if self.en_time:
            if hasattr(self.en_time, 'to_alipay_dict'):
                params['en_time'] = self.en_time.to_alipay_dict()
            else:
                params['en_time'] = self.en_time
        if self.ex_station_id:
            if hasattr(self.ex_station_id, 'to_alipay_dict'):
                params['ex_station_id'] = self.ex_station_id.to_alipay_dict()
            else:
                params['ex_station_id'] = self.ex_station_id
        if self.ex_station_name:
            if hasattr(self.ex_station_name, 'to_alipay_dict'):
                params['ex_station_name'] = self.ex_station_name.to_alipay_dict()
            else:
                params['ex_station_name'] = self.ex_station_name
        if self.ex_time:
            if hasattr(self.ex_time, 'to_alipay_dict'):
                params['ex_time'] = self.ex_time.to_alipay_dict()
            else:
                params['ex_time'] = self.ex_time
        if self.fee:
            if hasattr(self.fee, 'to_alipay_dict'):
                params['fee'] = self.fee.to_alipay_dict()
            else:
                params['fee'] = self.fee
        if self.plate_color:
            if hasattr(self.plate_color, 'to_alipay_dict'):
                params['plate_color'] = self.plate_color.to_alipay_dict()
            else:
                params['plate_color'] = self.plate_color
        if self.plate_no:
            if hasattr(self.plate_no, 'to_alipay_dict'):
                params['plate_no'] = self.plate_no.to_alipay_dict()
            else:
                params['plate_no'] = self.plate_no
        if self.province_code:
            if hasattr(self.province_code, 'to_alipay_dict'):
                params['province_code'] = self.province_code.to_alipay_dict()
            else:
                params['province_code'] = self.province_code
        if self.province_name:
            if hasattr(self.province_name, 'to_alipay_dict'):
                params['province_name'] = self.province_name.to_alipay_dict()
            else:
                params['province_name'] = self.province_name
        if self.trade_id:
            if hasattr(self.trade_id, 'to_alipay_dict'):
                params['trade_id'] = self.trade_id.to_alipay_dict()
            else:
                params['trade_id'] = self.trade_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportEtccardTradeSyncModel()
        if 'card_id' in d:
            o.card_id = d['card_id']
        if 'en_station_id' in d:
            o.en_station_id = d['en_station_id']
        if 'en_station_name' in d:
            o.en_station_name = d['en_station_name']
        if 'en_time' in d:
            o.en_time = d['en_time']
        if 'ex_station_id' in d:
            o.ex_station_id = d['ex_station_id']
        if 'ex_station_name' in d:
            o.ex_station_name = d['ex_station_name']
        if 'ex_time' in d:
            o.ex_time = d['ex_time']
        if 'fee' in d:
            o.fee = d['fee']
        if 'plate_color' in d:
            o.plate_color = d['plate_color']
        if 'plate_no' in d:
            o.plate_no = d['plate_no']
        if 'province_code' in d:
            o.province_code = d['province_code']
        if 'province_name' in d:
            o.province_name = d['province_name']
        if 'trade_id' in d:
            o.trade_id = d['trade_id']
        return o


