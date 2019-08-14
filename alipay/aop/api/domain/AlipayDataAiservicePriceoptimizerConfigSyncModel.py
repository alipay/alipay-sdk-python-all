#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataAiservicePriceoptimizerConfigSyncModel(object):

    def __init__(self):
        self._app_version = None
        self._biz_time = None
        self._op_content = None
        self._operate_type = None
        self._product_type = None
        self._scene_code = None
        self._service_name = None
        self._trade_channel = None

    @property
    def app_version(self):
        return self._app_version

    @app_version.setter
    def app_version(self, value):
        self._app_version = value
    @property
    def biz_time(self):
        return self._biz_time

    @biz_time.setter
    def biz_time(self, value):
        self._biz_time = value
    @property
    def op_content(self):
        return self._op_content

    @op_content.setter
    def op_content(self, value):
        self._op_content = value
    @property
    def operate_type(self):
        return self._operate_type

    @operate_type.setter
    def operate_type(self, value):
        self._operate_type = value
    @property
    def product_type(self):
        return self._product_type

    @product_type.setter
    def product_type(self, value):
        self._product_type = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def service_name(self):
        return self._service_name

    @service_name.setter
    def service_name(self, value):
        self._service_name = value
    @property
    def trade_channel(self):
        return self._trade_channel

    @trade_channel.setter
    def trade_channel(self, value):
        self._trade_channel = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_version:
            if hasattr(self.app_version, 'to_alipay_dict'):
                params['app_version'] = self.app_version.to_alipay_dict()
            else:
                params['app_version'] = self.app_version
        if self.biz_time:
            if hasattr(self.biz_time, 'to_alipay_dict'):
                params['biz_time'] = self.biz_time.to_alipay_dict()
            else:
                params['biz_time'] = self.biz_time
        if self.op_content:
            if hasattr(self.op_content, 'to_alipay_dict'):
                params['op_content'] = self.op_content.to_alipay_dict()
            else:
                params['op_content'] = self.op_content
        if self.operate_type:
            if hasattr(self.operate_type, 'to_alipay_dict'):
                params['operate_type'] = self.operate_type.to_alipay_dict()
            else:
                params['operate_type'] = self.operate_type
        if self.product_type:
            if hasattr(self.product_type, 'to_alipay_dict'):
                params['product_type'] = self.product_type.to_alipay_dict()
            else:
                params['product_type'] = self.product_type
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.service_name:
            if hasattr(self.service_name, 'to_alipay_dict'):
                params['service_name'] = self.service_name.to_alipay_dict()
            else:
                params['service_name'] = self.service_name
        if self.trade_channel:
            if hasattr(self.trade_channel, 'to_alipay_dict'):
                params['trade_channel'] = self.trade_channel.to_alipay_dict()
            else:
                params['trade_channel'] = self.trade_channel
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataAiservicePriceoptimizerConfigSyncModel()
        if 'app_version' in d:
            o.app_version = d['app_version']
        if 'biz_time' in d:
            o.biz_time = d['biz_time']
        if 'op_content' in d:
            o.op_content = d['op_content']
        if 'operate_type' in d:
            o.operate_type = d['operate_type']
        if 'product_type' in d:
            o.product_type = d['product_type']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'service_name' in d:
            o.service_name = d['service_name']
        if 'trade_channel' in d:
            o.trade_channel = d['trade_channel']
        return o


