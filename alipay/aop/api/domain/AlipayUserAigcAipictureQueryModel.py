#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserAigcAipictureQueryModel(object):

    def __init__(self):
        self._alipay_order_id = None
        self._image_id = None
        self._open_id = None
        self._order_id = None
        self._retry_count = None
        self._trace_id = None
        self._user_id = None

    @property
    def alipay_order_id(self):
        return self._alipay_order_id

    @alipay_order_id.setter
    def alipay_order_id(self, value):
        self._alipay_order_id = value
    @property
    def image_id(self):
        return self._image_id

    @image_id.setter
    def image_id(self, value):
        self._image_id = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def retry_count(self):
        return self._retry_count

    @retry_count.setter
    def retry_count(self, value):
        self._retry_count = value
    @property
    def trace_id(self):
        return self._trace_id

    @trace_id.setter
    def trace_id(self, value):
        self._trace_id = value
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
        if self.image_id:
            if hasattr(self.image_id, 'to_alipay_dict'):
                params['image_id'] = self.image_id.to_alipay_dict()
            else:
                params['image_id'] = self.image_id
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.retry_count:
            if hasattr(self.retry_count, 'to_alipay_dict'):
                params['retry_count'] = self.retry_count.to_alipay_dict()
            else:
                params['retry_count'] = self.retry_count
        if self.trace_id:
            if hasattr(self.trace_id, 'to_alipay_dict'):
                params['trace_id'] = self.trace_id.to_alipay_dict()
            else:
                params['trace_id'] = self.trace_id
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
        o = AlipayUserAigcAipictureQueryModel()
        if 'alipay_order_id' in d:
            o.alipay_order_id = d['alipay_order_id']
        if 'image_id' in d:
            o.image_id = d['image_id']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'retry_count' in d:
            o.retry_count = d['retry_count']
        if 'trace_id' in d:
            o.trace_id = d['trace_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


