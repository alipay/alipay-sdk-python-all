#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceIotVendingmachineProfileQueryModel(object):

    def __init__(self):
        self._biz_tid = None
        self._goods_code = None
        self._pid = None
        self._search_data_list = None
        self._search_data_type = None
        self._time_interval = None

    @property
    def biz_tid(self):
        return self._biz_tid

    @biz_tid.setter
    def biz_tid(self, value):
        self._biz_tid = value
    @property
    def goods_code(self):
        return self._goods_code

    @goods_code.setter
    def goods_code(self, value):
        self._goods_code = value
    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, value):
        self._pid = value
    @property
    def search_data_list(self):
        return self._search_data_list

    @search_data_list.setter
    def search_data_list(self, value):
        self._search_data_list = value
    @property
    def search_data_type(self):
        return self._search_data_type

    @search_data_type.setter
    def search_data_type(self, value):
        self._search_data_type = value
    @property
    def time_interval(self):
        return self._time_interval

    @time_interval.setter
    def time_interval(self, value):
        self._time_interval = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_tid:
            if hasattr(self.biz_tid, 'to_alipay_dict'):
                params['biz_tid'] = self.biz_tid.to_alipay_dict()
            else:
                params['biz_tid'] = self.biz_tid
        if self.goods_code:
            if hasattr(self.goods_code, 'to_alipay_dict'):
                params['goods_code'] = self.goods_code.to_alipay_dict()
            else:
                params['goods_code'] = self.goods_code
        if self.pid:
            if hasattr(self.pid, 'to_alipay_dict'):
                params['pid'] = self.pid.to_alipay_dict()
            else:
                params['pid'] = self.pid
        if self.search_data_list:
            if hasattr(self.search_data_list, 'to_alipay_dict'):
                params['search_data_list'] = self.search_data_list.to_alipay_dict()
            else:
                params['search_data_list'] = self.search_data_list
        if self.search_data_type:
            if hasattr(self.search_data_type, 'to_alipay_dict'):
                params['search_data_type'] = self.search_data_type.to_alipay_dict()
            else:
                params['search_data_type'] = self.search_data_type
        if self.time_interval:
            if hasattr(self.time_interval, 'to_alipay_dict'):
                params['time_interval'] = self.time_interval.to_alipay_dict()
            else:
                params['time_interval'] = self.time_interval
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceIotVendingmachineProfileQueryModel()
        if 'biz_tid' in d:
            o.biz_tid = d['biz_tid']
        if 'goods_code' in d:
            o.goods_code = d['goods_code']
        if 'pid' in d:
            o.pid = d['pid']
        if 'search_data_list' in d:
            o.search_data_list = d['search_data_list']
        if 'search_data_type' in d:
            o.search_data_type = d['search_data_type']
        if 'time_interval' in d:
            o.time_interval = d['time_interval']
        return o


