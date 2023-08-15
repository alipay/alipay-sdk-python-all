#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceWaterUsertaskSendModel(object):

    def __init__(self):
        self._open_id = None
        self._out_biz_no = None
        self._send_shop_name = None
        self._task_id = None
        self._user_id = None
        self._user_task_id = None

    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def send_shop_name(self):
        return self._send_shop_name

    @send_shop_name.setter
    def send_shop_name(self, value):
        self._send_shop_name = value
    @property
    def task_id(self):
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        self._task_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def user_task_id(self):
        return self._user_task_id

    @user_task_id.setter
    def user_task_id(self, value):
        self._user_task_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.send_shop_name:
            if hasattr(self.send_shop_name, 'to_alipay_dict'):
                params['send_shop_name'] = self.send_shop_name.to_alipay_dict()
            else:
                params['send_shop_name'] = self.send_shop_name
        if self.task_id:
            if hasattr(self.task_id, 'to_alipay_dict'):
                params['task_id'] = self.task_id.to_alipay_dict()
            else:
                params['task_id'] = self.task_id
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.user_task_id:
            if hasattr(self.user_task_id, 'to_alipay_dict'):
                params['user_task_id'] = self.user_task_id.to_alipay_dict()
            else:
                params['user_task_id'] = self.user_task_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceWaterUsertaskSendModel()
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'send_shop_name' in d:
            o.send_shop_name = d['send_shop_name']
        if 'task_id' in d:
            o.task_id = d['task_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'user_task_id' in d:
            o.user_task_id = d['user_task_id']
        return o


