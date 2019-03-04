#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayInsSceneHealthGiftQueryModel(object):

    def __init__(self):
        self._end_time = None
        self._product_group_biz_type = None
        self._source = None
        self._start_time = None
        self._user_id = None

    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def product_group_biz_type(self):
        return self._product_group_biz_type

    @product_group_biz_type.setter
    def product_group_biz_type(self, value):
        self._product_group_biz_type = value
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
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.product_group_biz_type:
            if hasattr(self.product_group_biz_type, 'to_alipay_dict'):
                params['product_group_biz_type'] = self.product_group_biz_type.to_alipay_dict()
            else:
                params['product_group_biz_type'] = self.product_group_biz_type
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
        o = AlipayInsSceneHealthGiftQueryModel()
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'product_group_biz_type' in d:
            o.product_group_biz_type = d['product_group_biz_type']
        if 'source' in d:
            o.source = d['source']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


