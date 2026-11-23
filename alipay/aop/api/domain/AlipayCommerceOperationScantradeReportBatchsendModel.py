#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ScanTradeItem import ScanTradeItem


class AlipayCommerceOperationScantradeReportBatchsendModel(object):

    def __init__(self):
        self._scene_code = None
        self._trade_list = None

    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def trade_list(self):
        return self._trade_list

    @trade_list.setter
    def trade_list(self, value):
        if isinstance(value, list):
            self._trade_list = list()
            for i in value:
                if isinstance(i, ScanTradeItem):
                    self._trade_list.append(i)
                else:
                    self._trade_list.append(ScanTradeItem.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.trade_list:
            if isinstance(self.trade_list, list):
                for i in range(0, len(self.trade_list)):
                    element = self.trade_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.trade_list[i] = element.to_alipay_dict()
            if hasattr(self.trade_list, 'to_alipay_dict'):
                params['trade_list'] = self.trade_list.to_alipay_dict()
            else:
                params['trade_list'] = self.trade_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceOperationScantradeReportBatchsendModel()
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'trade_list' in d:
            o.trade_list = d['trade_list']
        return o


