#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MultiDataOpenResult(object):

    def __init__(self):
        self._avg_num = None
        self._feature_key = None
        self._object_id = None
        self._object_name = None
        self._object_type = None
        self._user_cnt = None
        self._user_ratio = None

    @property
    def avg_num(self):
        return self._avg_num

    @avg_num.setter
    def avg_num(self, value):
        self._avg_num = value
    @property
    def feature_key(self):
        return self._feature_key

    @feature_key.setter
    def feature_key(self, value):
        self._feature_key = value
    @property
    def object_id(self):
        return self._object_id

    @object_id.setter
    def object_id(self, value):
        self._object_id = value
    @property
    def object_name(self):
        return self._object_name

    @object_name.setter
    def object_name(self, value):
        self._object_name = value
    @property
    def object_type(self):
        return self._object_type

    @object_type.setter
    def object_type(self, value):
        self._object_type = value
    @property
    def user_cnt(self):
        return self._user_cnt

    @user_cnt.setter
    def user_cnt(self, value):
        self._user_cnt = value
    @property
    def user_ratio(self):
        return self._user_ratio

    @user_ratio.setter
    def user_ratio(self, value):
        self._user_ratio = value


    def to_alipay_dict(self):
        params = dict()
        if self.avg_num:
            if hasattr(self.avg_num, 'to_alipay_dict'):
                params['avg_num'] = self.avg_num.to_alipay_dict()
            else:
                params['avg_num'] = self.avg_num
        if self.feature_key:
            if hasattr(self.feature_key, 'to_alipay_dict'):
                params['feature_key'] = self.feature_key.to_alipay_dict()
            else:
                params['feature_key'] = self.feature_key
        if self.object_id:
            if hasattr(self.object_id, 'to_alipay_dict'):
                params['object_id'] = self.object_id.to_alipay_dict()
            else:
                params['object_id'] = self.object_id
        if self.object_name:
            if hasattr(self.object_name, 'to_alipay_dict'):
                params['object_name'] = self.object_name.to_alipay_dict()
            else:
                params['object_name'] = self.object_name
        if self.object_type:
            if hasattr(self.object_type, 'to_alipay_dict'):
                params['object_type'] = self.object_type.to_alipay_dict()
            else:
                params['object_type'] = self.object_type
        if self.user_cnt:
            if hasattr(self.user_cnt, 'to_alipay_dict'):
                params['user_cnt'] = self.user_cnt.to_alipay_dict()
            else:
                params['user_cnt'] = self.user_cnt
        if self.user_ratio:
            if hasattr(self.user_ratio, 'to_alipay_dict'):
                params['user_ratio'] = self.user_ratio.to_alipay_dict()
            else:
                params['user_ratio'] = self.user_ratio
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MultiDataOpenResult()
        if 'avg_num' in d:
            o.avg_num = d['avg_num']
        if 'feature_key' in d:
            o.feature_key = d['feature_key']
        if 'object_id' in d:
            o.object_id = d['object_id']
        if 'object_name' in d:
            o.object_name = d['object_name']
        if 'object_type' in d:
            o.object_type = d['object_type']
        if 'user_cnt' in d:
            o.user_cnt = d['user_cnt']
        if 'user_ratio' in d:
            o.user_ratio = d['user_ratio']
        return o


