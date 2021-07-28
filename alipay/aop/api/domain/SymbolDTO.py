#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SymbolDTO(object):

    def __init__(self):
        self._code = None
        self._currency = None
        self._hand = None
        self._hand_unit = None
        self._list_type = None
        self._market = None
        self._name = None
        self._price_decimal = None
        self._sub_type = None
        self._symbol = None
        self._type = None

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value
    @property
    def hand(self):
        return self._hand

    @hand.setter
    def hand(self, value):
        self._hand = value
    @property
    def hand_unit(self):
        return self._hand_unit

    @hand_unit.setter
    def hand_unit(self, value):
        self._hand_unit = value
    @property
    def list_type(self):
        return self._list_type

    @list_type.setter
    def list_type(self, value):
        self._list_type = value
    @property
    def market(self):
        return self._market

    @market.setter
    def market(self, value):
        self._market = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def price_decimal(self):
        return self._price_decimal

    @price_decimal.setter
    def price_decimal(self, value):
        self._price_decimal = value
    @property
    def sub_type(self):
        return self._sub_type

    @sub_type.setter
    def sub_type(self, value):
        self._sub_type = value
    @property
    def symbol(self):
        return self._symbol

    @symbol.setter
    def symbol(self, value):
        self._symbol = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.code:
            if hasattr(self.code, 'to_alipay_dict'):
                params['code'] = self.code.to_alipay_dict()
            else:
                params['code'] = self.code
        if self.currency:
            if hasattr(self.currency, 'to_alipay_dict'):
                params['currency'] = self.currency.to_alipay_dict()
            else:
                params['currency'] = self.currency
        if self.hand:
            if hasattr(self.hand, 'to_alipay_dict'):
                params['hand'] = self.hand.to_alipay_dict()
            else:
                params['hand'] = self.hand
        if self.hand_unit:
            if hasattr(self.hand_unit, 'to_alipay_dict'):
                params['hand_unit'] = self.hand_unit.to_alipay_dict()
            else:
                params['hand_unit'] = self.hand_unit
        if self.list_type:
            if hasattr(self.list_type, 'to_alipay_dict'):
                params['list_type'] = self.list_type.to_alipay_dict()
            else:
                params['list_type'] = self.list_type
        if self.market:
            if hasattr(self.market, 'to_alipay_dict'):
                params['market'] = self.market.to_alipay_dict()
            else:
                params['market'] = self.market
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.price_decimal:
            if hasattr(self.price_decimal, 'to_alipay_dict'):
                params['price_decimal'] = self.price_decimal.to_alipay_dict()
            else:
                params['price_decimal'] = self.price_decimal
        if self.sub_type:
            if hasattr(self.sub_type, 'to_alipay_dict'):
                params['sub_type'] = self.sub_type.to_alipay_dict()
            else:
                params['sub_type'] = self.sub_type
        if self.symbol:
            if hasattr(self.symbol, 'to_alipay_dict'):
                params['symbol'] = self.symbol.to_alipay_dict()
            else:
                params['symbol'] = self.symbol
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SymbolDTO()
        if 'code' in d:
            o.code = d['code']
        if 'currency' in d:
            o.currency = d['currency']
        if 'hand' in d:
            o.hand = d['hand']
        if 'hand_unit' in d:
            o.hand_unit = d['hand_unit']
        if 'list_type' in d:
            o.list_type = d['list_type']
        if 'market' in d:
            o.market = d['market']
        if 'name' in d:
            o.name = d['name']
        if 'price_decimal' in d:
            o.price_decimal = d['price_decimal']
        if 'sub_type' in d:
            o.sub_type = d['sub_type']
        if 'symbol' in d:
            o.symbol = d['symbol']
        if 'type' in d:
            o.type = d['type']
        return o


