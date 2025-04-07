#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCreditPePayafteruseTaskSyncModel(object):

    def __init__(self):
        self._biz_time = None
        self._goal_type = None
        self._goal_value = None
        self._open_id = None
        self._out_order_no = None
        self._out_request_no = None
        self._update_type = None
        self._user_id = None

    @property
    def biz_time(self):
        return self._biz_time

    @biz_time.setter
    def biz_time(self, value):
        self._biz_time = value
    @property
    def goal_type(self):
        return self._goal_type

    @goal_type.setter
    def goal_type(self, value):
        self._goal_type = value
    @property
    def goal_value(self):
        return self._goal_value

    @goal_value.setter
    def goal_value(self, value):
        self._goal_value = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def update_type(self):
        return self._update_type

    @update_type.setter
    def update_type(self, value):
        self._update_type = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_time:
            if hasattr(self.biz_time, 'to_alipay_dict'):
                params['biz_time'] = self.biz_time.to_alipay_dict()
            else:
                params['biz_time'] = self.biz_time
        if self.goal_type:
            if hasattr(self.goal_type, 'to_alipay_dict'):
                params['goal_type'] = self.goal_type.to_alipay_dict()
            else:
                params['goal_type'] = self.goal_type
        if self.goal_value:
            if hasattr(self.goal_value, 'to_alipay_dict'):
                params['goal_value'] = self.goal_value.to_alipay_dict()
            else:
                params['goal_value'] = self.goal_value
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        if self.update_type:
            if hasattr(self.update_type, 'to_alipay_dict'):
                params['update_type'] = self.update_type.to_alipay_dict()
            else:
                params['update_type'] = self.update_type
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
        o = ZhimaCreditPePayafteruseTaskSyncModel()
        if 'biz_time' in d:
            o.biz_time = d['biz_time']
        if 'goal_type' in d:
            o.goal_type = d['goal_type']
        if 'goal_value' in d:
            o.goal_value = d['goal_value']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'update_type' in d:
            o.update_type = d['update_type']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


