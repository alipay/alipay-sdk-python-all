#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalInsuranceFulfillmenttransitCancelModel(object):

    def __init__(self):
        self._channel = None
        self._open_id = None
        self._out_unique_biz_no = None
        self._product_code = None
        self._product_name = None
        self._user_id = None
        self._valid_cancel_time = None

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def out_unique_biz_no(self):
        return self._out_unique_biz_no

    @out_unique_biz_no.setter
    def out_unique_biz_no(self, value):
        self._out_unique_biz_no = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def product_name(self):
        return self._product_name

    @product_name.setter
    def product_name(self, value):
        self._product_name = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def valid_cancel_time(self):
        return self._valid_cancel_time

    @valid_cancel_time.setter
    def valid_cancel_time(self, value):
        self._valid_cancel_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.out_unique_biz_no:
            if hasattr(self.out_unique_biz_no, 'to_alipay_dict'):
                params['out_unique_biz_no'] = self.out_unique_biz_no.to_alipay_dict()
            else:
                params['out_unique_biz_no'] = self.out_unique_biz_no
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.product_name:
            if hasattr(self.product_name, 'to_alipay_dict'):
                params['product_name'] = self.product_name.to_alipay_dict()
            else:
                params['product_name'] = self.product_name
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.valid_cancel_time:
            if hasattr(self.valid_cancel_time, 'to_alipay_dict'):
                params['valid_cancel_time'] = self.valid_cancel_time.to_alipay_dict()
            else:
                params['valid_cancel_time'] = self.valid_cancel_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalInsuranceFulfillmenttransitCancelModel()
        if 'channel' in d:
            o.channel = d['channel']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'out_unique_biz_no' in d:
            o.out_unique_biz_no = d['out_unique_biz_no']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'product_name' in d:
            o.product_name = d['product_name']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'valid_cancel_time' in d:
            o.valid_cancel_time = d['valid_cancel_time']
        return o


