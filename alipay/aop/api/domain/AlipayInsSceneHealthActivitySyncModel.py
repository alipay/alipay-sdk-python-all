#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayInsSceneHealthActivitySyncModel(object):

    def __init__(self):
        self._activity_no = None
        self._apply_no = None
        self._biz_data = None
        self._order_no = None
        self._status = None
        self._user_id = None

    @property
    def activity_no(self):
        return self._activity_no

    @activity_no.setter
    def activity_no(self, value):
        self._activity_no = value
    @property
    def apply_no(self):
        return self._apply_no

    @apply_no.setter
    def apply_no(self, value):
        self._apply_no = value
    @property
    def biz_data(self):
        return self._biz_data

    @biz_data.setter
    def biz_data(self, value):
        self._biz_data = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.activity_no:
            if hasattr(self.activity_no, 'to_alipay_dict'):
                params['activity_no'] = self.activity_no.to_alipay_dict()
            else:
                params['activity_no'] = self.activity_no
        if self.apply_no:
            if hasattr(self.apply_no, 'to_alipay_dict'):
                params['apply_no'] = self.apply_no.to_alipay_dict()
            else:
                params['apply_no'] = self.apply_no
        if self.biz_data:
            if hasattr(self.biz_data, 'to_alipay_dict'):
                params['biz_data'] = self.biz_data.to_alipay_dict()
            else:
                params['biz_data'] = self.biz_data
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
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
        o = AlipayInsSceneHealthActivitySyncModel()
        if 'activity_no' in d:
            o.activity_no = d['activity_no']
        if 'apply_no' in d:
            o.apply_no = d['apply_no']
        if 'biz_data' in d:
            o.biz_data = d['biz_data']
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'status' in d:
            o.status = d['status']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


