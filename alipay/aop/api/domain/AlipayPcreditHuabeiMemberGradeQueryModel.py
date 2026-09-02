#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayPcreditHuabeiMemberGradeQueryModel(object):

    def __init__(self):
        self._biz_time = None
        self._merchant_name = None
        self._open_id = None
        self._out_biz_no = None
        self._register_channel = None
        self._scene = None
        self._user_id = None
        self._vendor = None

    @property
    def biz_time(self):
        return self._biz_time

    @biz_time.setter
    def biz_time(self, value):
        self._biz_time = value
    @property
    def merchant_name(self):
        return self._merchant_name

    @merchant_name.setter
    def merchant_name(self, value):
        self._merchant_name = value
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
    def register_channel(self):
        return self._register_channel

    @register_channel.setter
    def register_channel(self, value):
        self._register_channel = value
    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def vendor(self):
        return self._vendor

    @vendor.setter
    def vendor(self, value):
        self._vendor = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_time:
            if hasattr(self.biz_time, 'to_alipay_dict'):
                params['biz_time'] = self.biz_time.to_alipay_dict()
            else:
                params['biz_time'] = self.biz_time
        if self.merchant_name:
            if hasattr(self.merchant_name, 'to_alipay_dict'):
                params['merchant_name'] = self.merchant_name.to_alipay_dict()
            else:
                params['merchant_name'] = self.merchant_name
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
        if self.register_channel:
            if hasattr(self.register_channel, 'to_alipay_dict'):
                params['register_channel'] = self.register_channel.to_alipay_dict()
            else:
                params['register_channel'] = self.register_channel
        if self.scene:
            if hasattr(self.scene, 'to_alipay_dict'):
                params['scene'] = self.scene.to_alipay_dict()
            else:
                params['scene'] = self.scene
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.vendor:
            if hasattr(self.vendor, 'to_alipay_dict'):
                params['vendor'] = self.vendor.to_alipay_dict()
            else:
                params['vendor'] = self.vendor
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayPcreditHuabeiMemberGradeQueryModel()
        if 'biz_time' in d:
            o.biz_time = d['biz_time']
        if 'merchant_name' in d:
            o.merchant_name = d['merchant_name']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'register_channel' in d:
            o.register_channel = d['register_channel']
        if 'scene' in d:
            o.scene = d['scene']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'vendor' in d:
            o.vendor = d['vendor']
        return o


