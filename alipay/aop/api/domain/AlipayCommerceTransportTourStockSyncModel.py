#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TourStockInfo import TourStockInfo


class AlipayCommerceTransportTourStockSyncModel(object):

    def __init__(self):
        self._scenic_id = None
        self._stock_info_list = None

    @property
    def scenic_id(self):
        return self._scenic_id

    @scenic_id.setter
    def scenic_id(self, value):
        self._scenic_id = value
    @property
    def stock_info_list(self):
        return self._stock_info_list

    @stock_info_list.setter
    def stock_info_list(self, value):
        if isinstance(value, list):
            self._stock_info_list = list()
            for i in value:
                if isinstance(i, TourStockInfo):
                    self._stock_info_list.append(i)
                else:
                    self._stock_info_list.append(TourStockInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.scenic_id:
            if hasattr(self.scenic_id, 'to_alipay_dict'):
                params['scenic_id'] = self.scenic_id.to_alipay_dict()
            else:
                params['scenic_id'] = self.scenic_id
        if self.stock_info_list:
            if isinstance(self.stock_info_list, list):
                for i in range(0, len(self.stock_info_list)):
                    element = self.stock_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.stock_info_list[i] = element.to_alipay_dict()
            if hasattr(self.stock_info_list, 'to_alipay_dict'):
                params['stock_info_list'] = self.stock_info_list.to_alipay_dict()
            else:
                params['stock_info_list'] = self.stock_info_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportTourStockSyncModel()
        if 'scenic_id' in d:
            o.scenic_id = d['scenic_id']
        if 'stock_info_list' in d:
            o.stock_info_list = d['stock_info_list']
        return o


