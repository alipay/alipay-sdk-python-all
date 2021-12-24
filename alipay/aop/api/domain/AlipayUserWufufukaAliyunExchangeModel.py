#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserWufufukaAliyunExchangeModel(object):

    def __init__(self):
        self._alipay_order_id = None
        self._aliyun_item_id = None
        self._ext_info = None
        self._request_id = None
        self._request_time = None
        self._user_id = None

    @property
    def alipay_order_id(self):
        return self._alipay_order_id

    @alipay_order_id.setter
    def alipay_order_id(self, value):
        self._alipay_order_id = value
    @property
    def aliyun_item_id(self):
        return self._aliyun_item_id

    @aliyun_item_id.setter
    def aliyun_item_id(self, value):
        self._aliyun_item_id = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def request_time(self):
        return self._request_time

    @request_time.setter
    def request_time(self, value):
        self._request_time = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_order_id:
            if hasattr(self.alipay_order_id, 'to_alipay_dict'):
                params['alipay_order_id'] = self.alipay_order_id.to_alipay_dict()
            else:
                params['alipay_order_id'] = self.alipay_order_id
        if self.aliyun_item_id:
            if hasattr(self.aliyun_item_id, 'to_alipay_dict'):
                params['aliyun_item_id'] = self.aliyun_item_id.to_alipay_dict()
            else:
                params['aliyun_item_id'] = self.aliyun_item_id
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.request_time:
            if hasattr(self.request_time, 'to_alipay_dict'):
                params['request_time'] = self.request_time.to_alipay_dict()
            else:
                params['request_time'] = self.request_time
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
        o = AlipayUserWufufukaAliyunExchangeModel()
        if 'alipay_order_id' in d:
            o.alipay_order_id = d['alipay_order_id']
        if 'aliyun_item_id' in d:
            o.aliyun_item_id = d['aliyun_item_id']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'request_time' in d:
            o.request_time = d['request_time']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


