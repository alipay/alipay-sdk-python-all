#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayPayAppOperationPromoTriggerModel(object):

    def __init__(self):
        self._app_mobile = None
        self._biz_scene = None
        self._device_id = None
        self._device_type = None
        self._open_id = None
        self._pay_operation_info = None
        self._request_id = None
        self._trigger_type = None
        self._user_id = None

    @property
    def app_mobile(self):
        return self._app_mobile

    @app_mobile.setter
    def app_mobile(self, value):
        self._app_mobile = value
    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def device_id(self):
        return self._device_id

    @device_id.setter
    def device_id(self, value):
        self._device_id = value
    @property
    def device_type(self):
        return self._device_type

    @device_type.setter
    def device_type(self, value):
        self._device_type = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def pay_operation_info(self):
        return self._pay_operation_info

    @pay_operation_info.setter
    def pay_operation_info(self, value):
        self._pay_operation_info = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def trigger_type(self):
        return self._trigger_type

    @trigger_type.setter
    def trigger_type(self, value):
        self._trigger_type = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_mobile:
            if hasattr(self.app_mobile, 'to_alipay_dict'):
                params['app_mobile'] = self.app_mobile.to_alipay_dict()
            else:
                params['app_mobile'] = self.app_mobile
        if self.biz_scene:
            if hasattr(self.biz_scene, 'to_alipay_dict'):
                params['biz_scene'] = self.biz_scene.to_alipay_dict()
            else:
                params['biz_scene'] = self.biz_scene
        if self.device_id:
            if hasattr(self.device_id, 'to_alipay_dict'):
                params['device_id'] = self.device_id.to_alipay_dict()
            else:
                params['device_id'] = self.device_id
        if self.device_type:
            if hasattr(self.device_type, 'to_alipay_dict'):
                params['device_type'] = self.device_type.to_alipay_dict()
            else:
                params['device_type'] = self.device_type
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.pay_operation_info:
            if hasattr(self.pay_operation_info, 'to_alipay_dict'):
                params['pay_operation_info'] = self.pay_operation_info.to_alipay_dict()
            else:
                params['pay_operation_info'] = self.pay_operation_info
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.trigger_type:
            if hasattr(self.trigger_type, 'to_alipay_dict'):
                params['trigger_type'] = self.trigger_type.to_alipay_dict()
            else:
                params['trigger_type'] = self.trigger_type
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
        o = AlipayPayAppOperationPromoTriggerModel()
        if 'app_mobile' in d:
            o.app_mobile = d['app_mobile']
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'device_id' in d:
            o.device_id = d['device_id']
        if 'device_type' in d:
            o.device_type = d['device_type']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'pay_operation_info' in d:
            o.pay_operation_info = d['pay_operation_info']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'trigger_type' in d:
            o.trigger_type = d['trigger_type']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


