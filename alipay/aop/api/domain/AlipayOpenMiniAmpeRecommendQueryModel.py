#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AmpeDeviceInfo import AmpeDeviceInfo


class AlipayOpenMiniAmpeRecommendQueryModel(object):

    def __init__(self):
        self._biz_scene = None
        self._device_id = None
        self._device_info = None
        self._open_id = None
        self._product_id = None
        self._req_no = None
        self._user_id = None

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
    def device_info(self):
        return self._device_info

    @device_info.setter
    def device_info(self, value):
        if isinstance(value, AmpeDeviceInfo):
            self._device_info = value
        else:
            self._device_info = AmpeDeviceInfo.from_alipay_dict(value)
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def product_id(self):
        return self._product_id

    @product_id.setter
    def product_id(self, value):
        self._product_id = value
    @property
    def req_no(self):
        return self._req_no

    @req_no.setter
    def req_no(self, value):
        self._req_no = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.device_info:
            if hasattr(self.device_info, 'to_alipay_dict'):
                params['device_info'] = self.device_info.to_alipay_dict()
            else:
                params['device_info'] = self.device_info
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.product_id:
            if hasattr(self.product_id, 'to_alipay_dict'):
                params['product_id'] = self.product_id.to_alipay_dict()
            else:
                params['product_id'] = self.product_id
        if self.req_no:
            if hasattr(self.req_no, 'to_alipay_dict'):
                params['req_no'] = self.req_no.to_alipay_dict()
            else:
                params['req_no'] = self.req_no
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
        o = AlipayOpenMiniAmpeRecommendQueryModel()
        if 'biz_scene' in d:
            o.biz_scene = d['biz_scene']
        if 'device_id' in d:
            o.device_id = d['device_id']
        if 'device_info' in d:
            o.device_info = d['device_info']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'product_id' in d:
            o.product_id = d['product_id']
        if 'req_no' in d:
            o.req_no = d['req_no']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


