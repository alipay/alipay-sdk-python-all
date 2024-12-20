#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EpStockInfo(object):

    def __init__(self):
        self._board_type = None
        self._code = None
        self._market_date = None
        self._short_name = None

    @property
    def board_type(self):
        return self._board_type

    @board_type.setter
    def board_type(self, value):
        self._board_type = value
    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def market_date(self):
        return self._market_date

    @market_date.setter
    def market_date(self, value):
        self._market_date = value
    @property
    def short_name(self):
        return self._short_name

    @short_name.setter
    def short_name(self, value):
        self._short_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.board_type:
            if hasattr(self.board_type, 'to_alipay_dict'):
                params['board_type'] = self.board_type.to_alipay_dict()
            else:
                params['board_type'] = self.board_type
        if self.code:
            if hasattr(self.code, 'to_alipay_dict'):
                params['code'] = self.code.to_alipay_dict()
            else:
                params['code'] = self.code
        if self.market_date:
            if hasattr(self.market_date, 'to_alipay_dict'):
                params['market_date'] = self.market_date.to_alipay_dict()
            else:
                params['market_date'] = self.market_date
        if self.short_name:
            if hasattr(self.short_name, 'to_alipay_dict'):
                params['short_name'] = self.short_name.to_alipay_dict()
            else:
                params['short_name'] = self.short_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EpStockInfo()
        if 'board_type' in d:
            o.board_type = d['board_type']
        if 'code' in d:
            o.code = d['code']
        if 'market_date' in d:
            o.market_date = d['market_date']
        if 'short_name' in d:
            o.short_name = d['short_name']
        return o


