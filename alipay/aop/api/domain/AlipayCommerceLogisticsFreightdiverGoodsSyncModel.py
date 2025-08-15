#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceLogisticsFreightdiverGoodsSyncModel(object):

    def __init__(self):
        self._open_id = None
        self._order_name = None
        self._order_no = None
        self._order_time = None
        self._order_url = None
        self._user_id = None

    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def order_name(self):
        return self._order_name

    @order_name.setter
    def order_name(self, value):
        self._order_name = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def order_time(self):
        return self._order_time

    @order_time.setter
    def order_time(self, value):
        self._order_time = value
    @property
    def order_url(self):
        return self._order_url

    @order_url.setter
    def order_url(self, value):
        self._order_url = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.order_name:
            if hasattr(self.order_name, 'to_alipay_dict'):
                params['order_name'] = self.order_name.to_alipay_dict()
            else:
                params['order_name'] = self.order_name
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        if self.order_time:
            if hasattr(self.order_time, 'to_alipay_dict'):
                params['order_time'] = self.order_time.to_alipay_dict()
            else:
                params['order_time'] = self.order_time
        if self.order_url:
            if hasattr(self.order_url, 'to_alipay_dict'):
                params['order_url'] = self.order_url.to_alipay_dict()
            else:
                params['order_url'] = self.order_url
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
        o = AlipayCommerceLogisticsFreightdiverGoodsSyncModel()
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'order_name' in d:
            o.order_name = d['order_name']
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'order_time' in d:
            o.order_time = d['order_time']
        if 'order_url' in d:
            o.order_url = d['order_url']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


