#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class HKStockConnSymbolDTO(object):

    def __init__(self):
        self._code = None
        self._conn_type = None
        self._currency = None
        self._date = None
        self._listed_join_date = None
        self._listed_leave_date = None
        self._listed_status = None
        self._lot_size = None
        self._name = None
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
    def conn_type(self):
        return self._conn_type

    @conn_type.setter
    def conn_type(self, value):
        self._conn_type = value
    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value
    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._date = value
    @property
    def listed_join_date(self):
        return self._listed_join_date

    @listed_join_date.setter
    def listed_join_date(self, value):
        self._listed_join_date = value
    @property
    def listed_leave_date(self):
        return self._listed_leave_date

    @listed_leave_date.setter
    def listed_leave_date(self, value):
        self._listed_leave_date = value
    @property
    def listed_status(self):
        return self._listed_status

    @listed_status.setter
    def listed_status(self, value):
        self._listed_status = value
    @property
    def lot_size(self):
        return self._lot_size

    @lot_size.setter
    def lot_size(self, value):
        self._lot_size = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
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
        if self.conn_type:
            if hasattr(self.conn_type, 'to_alipay_dict'):
                params['conn_type'] = self.conn_type.to_alipay_dict()
            else:
                params['conn_type'] = self.conn_type
        if self.currency:
            if hasattr(self.currency, 'to_alipay_dict'):
                params['currency'] = self.currency.to_alipay_dict()
            else:
                params['currency'] = self.currency
        if self.date:
            if hasattr(self.date, 'to_alipay_dict'):
                params['date'] = self.date.to_alipay_dict()
            else:
                params['date'] = self.date
        if self.listed_join_date:
            if hasattr(self.listed_join_date, 'to_alipay_dict'):
                params['listed_join_date'] = self.listed_join_date.to_alipay_dict()
            else:
                params['listed_join_date'] = self.listed_join_date
        if self.listed_leave_date:
            if hasattr(self.listed_leave_date, 'to_alipay_dict'):
                params['listed_leave_date'] = self.listed_leave_date.to_alipay_dict()
            else:
                params['listed_leave_date'] = self.listed_leave_date
        if self.listed_status:
            if hasattr(self.listed_status, 'to_alipay_dict'):
                params['listed_status'] = self.listed_status.to_alipay_dict()
            else:
                params['listed_status'] = self.listed_status
        if self.lot_size:
            if hasattr(self.lot_size, 'to_alipay_dict'):
                params['lot_size'] = self.lot_size.to_alipay_dict()
            else:
                params['lot_size'] = self.lot_size
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
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
        o = HKStockConnSymbolDTO()
        if 'code' in d:
            o.code = d['code']
        if 'conn_type' in d:
            o.conn_type = d['conn_type']
        if 'currency' in d:
            o.currency = d['currency']
        if 'date' in d:
            o.date = d['date']
        if 'listed_join_date' in d:
            o.listed_join_date = d['listed_join_date']
        if 'listed_leave_date' in d:
            o.listed_leave_date = d['listed_leave_date']
        if 'listed_status' in d:
            o.listed_status = d['listed_status']
        if 'lot_size' in d:
            o.lot_size = d['lot_size']
        if 'name' in d:
            o.name = d['name']
        if 'sub_type' in d:
            o.sub_type = d['sub_type']
        if 'symbol' in d:
            o.symbol = d['symbol']
        if 'type' in d:
            o.type = d['type']
        return o


