#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceAcommunicationPointRollbackModel(object):

    def __init__(self):
        self._open_id = None
        self._order_type = None
        self._out_biz_no = None
        self._to_roll_back_order_id = None
        self._to_roll_back_out_biz_no = None
        self._user_id = None

    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def order_type(self):
        return self._order_type

    @order_type.setter
    def order_type(self, value):
        self._order_type = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def to_roll_back_order_id(self):
        return self._to_roll_back_order_id

    @to_roll_back_order_id.setter
    def to_roll_back_order_id(self, value):
        self._to_roll_back_order_id = value
    @property
    def to_roll_back_out_biz_no(self):
        return self._to_roll_back_out_biz_no

    @to_roll_back_out_biz_no.setter
    def to_roll_back_out_biz_no(self, value):
        self._to_roll_back_out_biz_no = value
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
        if self.order_type:
            if hasattr(self.order_type, 'to_alipay_dict'):
                params['order_type'] = self.order_type.to_alipay_dict()
            else:
                params['order_type'] = self.order_type
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.to_roll_back_order_id:
            if hasattr(self.to_roll_back_order_id, 'to_alipay_dict'):
                params['to_roll_back_order_id'] = self.to_roll_back_order_id.to_alipay_dict()
            else:
                params['to_roll_back_order_id'] = self.to_roll_back_order_id
        if self.to_roll_back_out_biz_no:
            if hasattr(self.to_roll_back_out_biz_no, 'to_alipay_dict'):
                params['to_roll_back_out_biz_no'] = self.to_roll_back_out_biz_no.to_alipay_dict()
            else:
                params['to_roll_back_out_biz_no'] = self.to_roll_back_out_biz_no
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
        o = AlipayCommerceAcommunicationPointRollbackModel()
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'order_type' in d:
            o.order_type = d['order_type']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'to_roll_back_order_id' in d:
            o.to_roll_back_order_id = d['to_roll_back_order_id']
        if 'to_roll_back_out_biz_no' in d:
            o.to_roll_back_out_biz_no = d['to_roll_back_out_biz_no']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


