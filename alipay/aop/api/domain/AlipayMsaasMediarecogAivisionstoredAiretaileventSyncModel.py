#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMsaasMediarecogAivisionstoredAiretaileventSyncModel(object):

    def __init__(self):
        self._content = None
        self._date_time = None
        self._isv_pid = None
        self._order_id = None
        self._report_type = None
        self._shop_pid = None

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def date_time(self):
        return self._date_time

    @date_time.setter
    def date_time(self, value):
        self._date_time = value
    @property
    def isv_pid(self):
        return self._isv_pid

    @isv_pid.setter
    def isv_pid(self, value):
        self._isv_pid = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def report_type(self):
        return self._report_type

    @report_type.setter
    def report_type(self, value):
        self._report_type = value
    @property
    def shop_pid(self):
        return self._shop_pid

    @shop_pid.setter
    def shop_pid(self, value):
        self._shop_pid = value


    def to_alipay_dict(self):
        params = dict()
        if self.content:
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        if self.date_time:
            if hasattr(self.date_time, 'to_alipay_dict'):
                params['date_time'] = self.date_time.to_alipay_dict()
            else:
                params['date_time'] = self.date_time
        if self.isv_pid:
            if hasattr(self.isv_pid, 'to_alipay_dict'):
                params['isv_pid'] = self.isv_pid.to_alipay_dict()
            else:
                params['isv_pid'] = self.isv_pid
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.report_type:
            if hasattr(self.report_type, 'to_alipay_dict'):
                params['report_type'] = self.report_type.to_alipay_dict()
            else:
                params['report_type'] = self.report_type
        if self.shop_pid:
            if hasattr(self.shop_pid, 'to_alipay_dict'):
                params['shop_pid'] = self.shop_pid.to_alipay_dict()
            else:
                params['shop_pid'] = self.shop_pid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMsaasMediarecogAivisionstoredAiretaileventSyncModel()
        if 'content' in d:
            o.content = d['content']
        if 'date_time' in d:
            o.date_time = d['date_time']
        if 'isv_pid' in d:
            o.isv_pid = d['isv_pid']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'report_type' in d:
            o.report_type = d['report_type']
        if 'shop_pid' in d:
            o.shop_pid = d['shop_pid']
        return o


