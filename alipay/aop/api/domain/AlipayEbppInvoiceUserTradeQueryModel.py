#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppInvoiceUserTradeQueryModel(object):

    def __init__(self):
        self._einv_trade_id = None
        self._random = None
        self._timestamp = None
        self._token = None

    @property
    def einv_trade_id(self):
        return self._einv_trade_id

    @einv_trade_id.setter
    def einv_trade_id(self, value):
        self._einv_trade_id = value
    @property
    def random(self):
        return self._random

    @random.setter
    def random(self, value):
        self._random = value
    @property
    def timestamp(self):
        return self._timestamp

    @timestamp.setter
    def timestamp(self, value):
        self._timestamp = value
    @property
    def token(self):
        return self._token

    @token.setter
    def token(self, value):
        self._token = value


    def to_alipay_dict(self):
        params = dict()
        if self.einv_trade_id:
            if hasattr(self.einv_trade_id, 'to_alipay_dict'):
                params['einv_trade_id'] = self.einv_trade_id.to_alipay_dict()
            else:
                params['einv_trade_id'] = self.einv_trade_id
        if self.random:
            if hasattr(self.random, 'to_alipay_dict'):
                params['random'] = self.random.to_alipay_dict()
            else:
                params['random'] = self.random
        if self.timestamp:
            if hasattr(self.timestamp, 'to_alipay_dict'):
                params['timestamp'] = self.timestamp.to_alipay_dict()
            else:
                params['timestamp'] = self.timestamp
        if self.token:
            if hasattr(self.token, 'to_alipay_dict'):
                params['token'] = self.token.to_alipay_dict()
            else:
                params['token'] = self.token
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppInvoiceUserTradeQueryModel()
        if 'einv_trade_id' in d:
            o.einv_trade_id = d['einv_trade_id']
        if 'random' in d:
            o.random = d['random']
        if 'timestamp' in d:
            o.timestamp = d['timestamp']
        if 'token' in d:
            o.token = d['token']
        return o


