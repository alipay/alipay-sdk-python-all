#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayInsSceneHealthGiftBatchqueryModel(object):

    def __init__(self):
        self._biz_type_list = None
        self._end_time = None
        self._operation_list = None
        self._product_group_biz_type_list = None
        self._source = None
        self._start_time = None
        self._user_id = None

    @property
    def biz_type_list(self):
        return self._biz_type_list

    @biz_type_list.setter
    def biz_type_list(self, value):
        if isinstance(value, list):
            self._biz_type_list = list()
            for i in value:
                self._biz_type_list.append(i)
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def operation_list(self):
        return self._operation_list

    @operation_list.setter
    def operation_list(self, value):
        if isinstance(value, list):
            self._operation_list = list()
            for i in value:
                self._operation_list.append(i)
    @property
    def product_group_biz_type_list(self):
        return self._product_group_biz_type_list

    @product_group_biz_type_list.setter
    def product_group_biz_type_list(self, value):
        if isinstance(value, list):
            self._product_group_biz_type_list = list()
            for i in value:
                self._product_group_biz_type_list.append(i)
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_type_list:
            if isinstance(self.biz_type_list, list):
                for i in range(0, len(self.biz_type_list)):
                    element = self.biz_type_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.biz_type_list[i] = element.to_alipay_dict()
            if hasattr(self.biz_type_list, 'to_alipay_dict'):
                params['biz_type_list'] = self.biz_type_list.to_alipay_dict()
            else:
                params['biz_type_list'] = self.biz_type_list
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.operation_list:
            if isinstance(self.operation_list, list):
                for i in range(0, len(self.operation_list)):
                    element = self.operation_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.operation_list[i] = element.to_alipay_dict()
            if hasattr(self.operation_list, 'to_alipay_dict'):
                params['operation_list'] = self.operation_list.to_alipay_dict()
            else:
                params['operation_list'] = self.operation_list
        if self.product_group_biz_type_list:
            if isinstance(self.product_group_biz_type_list, list):
                for i in range(0, len(self.product_group_biz_type_list)):
                    element = self.product_group_biz_type_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.product_group_biz_type_list[i] = element.to_alipay_dict()
            if hasattr(self.product_group_biz_type_list, 'to_alipay_dict'):
                params['product_group_biz_type_list'] = self.product_group_biz_type_list.to_alipay_dict()
            else:
                params['product_group_biz_type_list'] = self.product_group_biz_type_list
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsSceneHealthGiftBatchqueryModel()
        if 'biz_type_list' in d:
            o.biz_type_list = d['biz_type_list']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'operation_list' in d:
            o.operation_list = d['operation_list']
        if 'product_group_biz_type_list' in d:
            o.product_group_biz_type_list = d['product_group_biz_type_list']
        if 'source' in d:
            o.source = d['source']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


