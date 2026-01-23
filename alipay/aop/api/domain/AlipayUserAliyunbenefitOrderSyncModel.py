#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserAliyunbenefitOrderSyncModel(object):

    def __init__(self):
        self._lm_order_id = None
        self._modified_time = None
        self._open_id = None
        self._order_status = None
        self._out_biz_no = None
        self._pre_order_status = None
        self._user_id = None

    @property
    def lm_order_id(self):
        return self._lm_order_id

    @lm_order_id.setter
    def lm_order_id(self, value):
        self._lm_order_id = value
    @property
    def modified_time(self):
        return self._modified_time

    @modified_time.setter
    def modified_time(self, value):
        self._modified_time = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def pre_order_status(self):
        return self._pre_order_status

    @pre_order_status.setter
    def pre_order_status(self, value):
        self._pre_order_status = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.lm_order_id:
            if hasattr(self.lm_order_id, 'to_alipay_dict'):
                params['lm_order_id'] = self.lm_order_id.to_alipay_dict()
            else:
                params['lm_order_id'] = self.lm_order_id
        if self.modified_time:
            if hasattr(self.modified_time, 'to_alipay_dict'):
                params['modified_time'] = self.modified_time.to_alipay_dict()
            else:
                params['modified_time'] = self.modified_time
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.order_status:
            if hasattr(self.order_status, 'to_alipay_dict'):
                params['order_status'] = self.order_status.to_alipay_dict()
            else:
                params['order_status'] = self.order_status
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.pre_order_status:
            if hasattr(self.pre_order_status, 'to_alipay_dict'):
                params['pre_order_status'] = self.pre_order_status.to_alipay_dict()
            else:
                params['pre_order_status'] = self.pre_order_status
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
        o = AlipayUserAliyunbenefitOrderSyncModel()
        if 'lm_order_id' in d:
            o.lm_order_id = d['lm_order_id']
        if 'modified_time' in d:
            o.modified_time = d['modified_time']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'order_status' in d:
            o.order_status = d['order_status']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'pre_order_status' in d:
            o.pre_order_status = d['pre_order_status']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


