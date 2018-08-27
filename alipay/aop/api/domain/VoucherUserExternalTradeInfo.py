#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class VoucherUserExternalTradeInfo(object):

    def __init__(self):
        self._amount = None
        self._consume_date = None
        self._consume_shop_id = None
        self._external_trade_no = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def consume_date(self):
        return self._consume_date

    @consume_date.setter
    def consume_date(self, value):
        self._consume_date = value
    @property
    def consume_shop_id(self):
        return self._consume_shop_id

    @consume_shop_id.setter
    def consume_shop_id(self, value):
        self._consume_shop_id = value
    @property
    def external_trade_no(self):
        return self._external_trade_no

    @external_trade_no.setter
    def external_trade_no(self, value):
        self._external_trade_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.consume_date:
            if hasattr(self.consume_date, 'to_alipay_dict'):
                params['consume_date'] = self.consume_date.to_alipay_dict()
            else:
                params['consume_date'] = self.consume_date
        if self.consume_shop_id:
            if hasattr(self.consume_shop_id, 'to_alipay_dict'):
                params['consume_shop_id'] = self.consume_shop_id.to_alipay_dict()
            else:
                params['consume_shop_id'] = self.consume_shop_id
        if self.external_trade_no:
            if hasattr(self.external_trade_no, 'to_alipay_dict'):
                params['external_trade_no'] = self.external_trade_no.to_alipay_dict()
            else:
                params['external_trade_no'] = self.external_trade_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VoucherUserExternalTradeInfo()
        if 'amount' in d:
            o.amount = d['amount']
        if 'consume_date' in d:
            o.consume_date = d['consume_date']
        if 'consume_shop_id' in d:
            o.consume_shop_id = d['consume_shop_id']
        if 'external_trade_no' in d:
            o.external_trade_no = d['external_trade_no']
        return o


