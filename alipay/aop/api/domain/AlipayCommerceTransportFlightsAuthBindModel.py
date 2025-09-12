#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportFlightsAuthBindModel(object):

    def __init__(self):
        self._auth_code = None
        self._auth_scene = None
        self._auto_auth = None
        self._cancel_all = None
        self._channel = None
        self._open_id = None
        self._operate_type = None
        self._out_biz_no = None
        self._user_id = None

    @property
    def auth_code(self):
        return self._auth_code

    @auth_code.setter
    def auth_code(self, value):
        self._auth_code = value
    @property
    def auth_scene(self):
        return self._auth_scene

    @auth_scene.setter
    def auth_scene(self, value):
        self._auth_scene = value
    @property
    def auto_auth(self):
        return self._auto_auth

    @auto_auth.setter
    def auto_auth(self, value):
        self._auto_auth = value
    @property
    def cancel_all(self):
        return self._cancel_all

    @cancel_all.setter
    def cancel_all(self, value):
        self._cancel_all = value
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
    def operate_type(self):
        return self._operate_type

    @operate_type.setter
    def operate_type(self, value):
        self._operate_type = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.auth_code:
            if hasattr(self.auth_code, 'to_alipay_dict'):
                params['auth_code'] = self.auth_code.to_alipay_dict()
            else:
                params['auth_code'] = self.auth_code
        if self.auth_scene:
            if hasattr(self.auth_scene, 'to_alipay_dict'):
                params['auth_scene'] = self.auth_scene.to_alipay_dict()
            else:
                params['auth_scene'] = self.auth_scene
        if self.auto_auth:
            if hasattr(self.auto_auth, 'to_alipay_dict'):
                params['auto_auth'] = self.auto_auth.to_alipay_dict()
            else:
                params['auto_auth'] = self.auto_auth
        if self.cancel_all:
            if hasattr(self.cancel_all, 'to_alipay_dict'):
                params['cancel_all'] = self.cancel_all.to_alipay_dict()
            else:
                params['cancel_all'] = self.cancel_all
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
        if self.operate_type:
            if hasattr(self.operate_type, 'to_alipay_dict'):
                params['operate_type'] = self.operate_type.to_alipay_dict()
            else:
                params['operate_type'] = self.operate_type
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
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
        o = AlipayCommerceTransportFlightsAuthBindModel()
        if 'auth_code' in d:
            o.auth_code = d['auth_code']
        if 'auth_scene' in d:
            o.auth_scene = d['auth_scene']
        if 'auto_auth' in d:
            o.auto_auth = d['auto_auth']
        if 'cancel_all' in d:
            o.cancel_all = d['cancel_all']
        if 'channel' in d:
            o.channel = d['channel']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'operate_type' in d:
            o.operate_type = d['operate_type']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


