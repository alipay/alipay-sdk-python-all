#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MerchantIndirectCollectionAnalysisChannelTradeInfo import MerchantIndirectCollectionAnalysisChannelTradeInfo


class MerchantIndirectCollectionAnalysisTimeLineRecord(object):

    def __init__(self):
        self._channel_trade = None
        self._end_time = None
        self._refund_amount = None
        self._settle_amount = None
        self._start_time = None
        self._total_amount = None
        self._total_trade_count = None

    @property
    def channel_trade(self):
        return self._channel_trade

    @channel_trade.setter
    def channel_trade(self, value):
        if isinstance(value, list):
            self._channel_trade = list()
            for i in value:
                if isinstance(i, MerchantIndirectCollectionAnalysisChannelTradeInfo):
                    self._channel_trade.append(i)
                else:
                    self._channel_trade.append(MerchantIndirectCollectionAnalysisChannelTradeInfo.from_alipay_dict(i))
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def refund_amount(self):
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        self._refund_amount = value
    @property
    def settle_amount(self):
        return self._settle_amount

    @settle_amount.setter
    def settle_amount(self, value):
        self._settle_amount = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value
    @property
    def total_trade_count(self):
        return self._total_trade_count

    @total_trade_count.setter
    def total_trade_count(self, value):
        self._total_trade_count = value


    def to_alipay_dict(self):
        params = dict()
        if self.channel_trade:
            if isinstance(self.channel_trade, list):
                for i in range(0, len(self.channel_trade)):
                    element = self.channel_trade[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.channel_trade[i] = element.to_alipay_dict()
            if hasattr(self.channel_trade, 'to_alipay_dict'):
                params['channel_trade'] = self.channel_trade.to_alipay_dict()
            else:
                params['channel_trade'] = self.channel_trade
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.refund_amount:
            if hasattr(self.refund_amount, 'to_alipay_dict'):
                params['refund_amount'] = self.refund_amount.to_alipay_dict()
            else:
                params['refund_amount'] = self.refund_amount
        if self.settle_amount:
            if hasattr(self.settle_amount, 'to_alipay_dict'):
                params['settle_amount'] = self.settle_amount.to_alipay_dict()
            else:
                params['settle_amount'] = self.settle_amount
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.total_amount:
            if hasattr(self.total_amount, 'to_alipay_dict'):
                params['total_amount'] = self.total_amount.to_alipay_dict()
            else:
                params['total_amount'] = self.total_amount
        if self.total_trade_count:
            if hasattr(self.total_trade_count, 'to_alipay_dict'):
                params['total_trade_count'] = self.total_trade_count.to_alipay_dict()
            else:
                params['total_trade_count'] = self.total_trade_count
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MerchantIndirectCollectionAnalysisTimeLineRecord()
        if 'channel_trade' in d:
            o.channel_trade = d['channel_trade']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'refund_amount' in d:
            o.refund_amount = d['refund_amount']
        if 'settle_amount' in d:
            o.settle_amount = d['settle_amount']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        if 'total_trade_count' in d:
            o.total_trade_count = d['total_trade_count']
        return o


