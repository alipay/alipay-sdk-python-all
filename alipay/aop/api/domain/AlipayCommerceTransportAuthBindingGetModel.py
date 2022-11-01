#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportAuthBindingGetModel(object):

    def __init__(self):
        self._alipay_cert_type = None
        self._biz_cert_type = None
        self._cert_no = None
        self._cert_type = None
        self._channel = None
        self._open_id = None
        self._out_biz_no = None
        self._scene = None
        self._user_id = None

    @property
    def alipay_cert_type(self):
        return self._alipay_cert_type

    @alipay_cert_type.setter
    def alipay_cert_type(self, value):
        self._alipay_cert_type = value
    @property
    def biz_cert_type(self):
        return self._biz_cert_type

    @biz_cert_type.setter
    def biz_cert_type(self, value):
        self._biz_cert_type = value
    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def cert_type(self):
        return self._cert_type

    @cert_type.setter
    def cert_type(self, value):
        self._cert_type = value
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
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_cert_type:
            if hasattr(self.alipay_cert_type, 'to_alipay_dict'):
                params['alipay_cert_type'] = self.alipay_cert_type.to_alipay_dict()
            else:
                params['alipay_cert_type'] = self.alipay_cert_type
        if self.biz_cert_type:
            if hasattr(self.biz_cert_type, 'to_alipay_dict'):
                params['biz_cert_type'] = self.biz_cert_type.to_alipay_dict()
            else:
                params['biz_cert_type'] = self.biz_cert_type
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.cert_type:
            if hasattr(self.cert_type, 'to_alipay_dict'):
                params['cert_type'] = self.cert_type.to_alipay_dict()
            else:
                params['cert_type'] = self.cert_type
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
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportAuthBindingGetModel()
        if 'alipay_cert_type' in d:
            o.alipay_cert_type = d['alipay_cert_type']
        if 'biz_cert_type' in d:
            o.biz_cert_type = d['biz_cert_type']
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'channel' in d:
            o.channel = d['channel']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'scene' in d:
            o.scene = d['scene']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


