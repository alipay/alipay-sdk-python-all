#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.WidgetActivityInfo import WidgetActivityInfo
from alipay.aop.api.domain.WidgetGoodsInfo import WidgetGoodsInfo


class AlipayOpenMiniWidgetDataSyncModel(object):

    def __init__(self):
        self._activity_list = None
        self._data_type = None
        self._goods_list = None
        self._mini_app_id = None
        self._pid = None

    @property
    def activity_list(self):
        return self._activity_list

    @activity_list.setter
    def activity_list(self, value):
        if isinstance(value, list):
            self._activity_list = list()
            for i in value:
                if isinstance(i, WidgetActivityInfo):
                    self._activity_list.append(i)
                else:
                    self._activity_list.append(WidgetActivityInfo.from_alipay_dict(i))
    @property
    def data_type(self):
        return self._data_type

    @data_type.setter
    def data_type(self, value):
        self._data_type = value
    @property
    def goods_list(self):
        return self._goods_list

    @goods_list.setter
    def goods_list(self, value):
        if isinstance(value, list):
            self._goods_list = list()
            for i in value:
                if isinstance(i, WidgetGoodsInfo):
                    self._goods_list.append(i)
                else:
                    self._goods_list.append(WidgetGoodsInfo.from_alipay_dict(i))
    @property
    def mini_app_id(self):
        return self._mini_app_id

    @mini_app_id.setter
    def mini_app_id(self, value):
        self._mini_app_id = value
    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, value):
        self._pid = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_list:
            if isinstance(self.activity_list, list):
                for i in range(0, len(self.activity_list)):
                    element = self.activity_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.activity_list[i] = element.to_alipay_dict()
            if hasattr(self.activity_list, 'to_alipay_dict'):
                params['activity_list'] = self.activity_list.to_alipay_dict()
            else:
                params['activity_list'] = self.activity_list
        if self.data_type:
            if hasattr(self.data_type, 'to_alipay_dict'):
                params['data_type'] = self.data_type.to_alipay_dict()
            else:
                params['data_type'] = self.data_type
        if self.goods_list:
            if isinstance(self.goods_list, list):
                for i in range(0, len(self.goods_list)):
                    element = self.goods_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.goods_list[i] = element.to_alipay_dict()
            if hasattr(self.goods_list, 'to_alipay_dict'):
                params['goods_list'] = self.goods_list.to_alipay_dict()
            else:
                params['goods_list'] = self.goods_list
        if self.mini_app_id:
            if hasattr(self.mini_app_id, 'to_alipay_dict'):
                params['mini_app_id'] = self.mini_app_id.to_alipay_dict()
            else:
                params['mini_app_id'] = self.mini_app_id
        if self.pid:
            if hasattr(self.pid, 'to_alipay_dict'):
                params['pid'] = self.pid.to_alipay_dict()
            else:
                params['pid'] = self.pid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenMiniWidgetDataSyncModel()
        if 'activity_list' in d:
            o.activity_list = d['activity_list']
        if 'data_type' in d:
            o.data_type = d['data_type']
        if 'goods_list' in d:
            o.goods_list = d['goods_list']
        if 'mini_app_id' in d:
            o.mini_app_id = d['mini_app_id']
        if 'pid' in d:
            o.pid = d['pid']
        return o


