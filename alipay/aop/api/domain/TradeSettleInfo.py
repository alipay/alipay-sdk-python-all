#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TradeSettleDetail import TradeSettleDetail


class TradeSettleInfo(object):

    def __init__(self):
        self._trade_settle_detail_list = None

    @property
    def trade_settle_detail_list(self):
        return self._trade_settle_detail_list

    @trade_settle_detail_list.setter
    def trade_settle_detail_list(self, value):
        if isinstance(value, list):
            self._trade_settle_detail_list = list()
            for i in value:
                if isinstance(i, TradeSettleDetail):
                    self._trade_settle_detail_list.append(i)
                else:
                    self._trade_settle_detail_list.append(TradeSettleDetail.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.trade_settle_detail_list:
            if isinstance(self.trade_settle_detail_list, list):
                for i in range(0, len(self.trade_settle_detail_list)):
                    element = self.trade_settle_detail_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.trade_settle_detail_list[i] = element.to_alipay_dict()
            if hasattr(self.trade_settle_detail_list, 'to_alipay_dict'):
                params['trade_settle_detail_list'] = self.trade_settle_detail_list.to_alipay_dict()
            else:
                params['trade_settle_detail_list'] = self.trade_settle_detail_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TradeSettleInfo()
        if 'trade_settle_detail_list' in d:
            o.trade_settle_detail_list = d['trade_settle_detail_list']
        return o


