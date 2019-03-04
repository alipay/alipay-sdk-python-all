#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceOperationContentQueryModel(object):

    def __init__(self):
        self._booth = None
        self._channel = None
        self._city_code = None
        self._content_id_str = None
        self._ext_params = None
        self._page_number = None
        self._page_size = None
        self._scene = None
        self._touch_point = None
        self._user_id = None

    @property
    def booth(self):
        return self._booth

    @booth.setter
    def booth(self, value):
        if isinstance(value, list):
            self._booth = list()
            for i in value:
                self._booth.append(i)
    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def content_id_str(self):
        return self._content_id_str

    @content_id_str.setter
    def content_id_str(self, value):
        self._content_id_str = value
    @property
    def ext_params(self):
        return self._ext_params

    @ext_params.setter
    def ext_params(self, value):
        self._ext_params = value
    @property
    def page_number(self):
        return self._page_number

    @page_number.setter
    def page_number(self, value):
        self._page_number = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value
    @property
    def touch_point(self):
        return self._touch_point

    @touch_point.setter
    def touch_point(self, value):
        self._touch_point = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.booth:
            if isinstance(self.booth, list):
                for i in range(0, len(self.booth)):
                    element = self.booth[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.booth[i] = element.to_alipay_dict()
            if hasattr(self.booth, 'to_alipay_dict'):
                params['booth'] = self.booth.to_alipay_dict()
            else:
                params['booth'] = self.booth
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.content_id_str:
            if hasattr(self.content_id_str, 'to_alipay_dict'):
                params['content_id_str'] = self.content_id_str.to_alipay_dict()
            else:
                params['content_id_str'] = self.content_id_str
        if self.ext_params:
            if hasattr(self.ext_params, 'to_alipay_dict'):
                params['ext_params'] = self.ext_params.to_alipay_dict()
            else:
                params['ext_params'] = self.ext_params
        if self.page_number:
            if hasattr(self.page_number, 'to_alipay_dict'):
                params['page_number'] = self.page_number.to_alipay_dict()
            else:
                params['page_number'] = self.page_number
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.scene:
            if hasattr(self.scene, 'to_alipay_dict'):
                params['scene'] = self.scene.to_alipay_dict()
            else:
                params['scene'] = self.scene
        if self.touch_point:
            if hasattr(self.touch_point, 'to_alipay_dict'):
                params['touch_point'] = self.touch_point.to_alipay_dict()
            else:
                params['touch_point'] = self.touch_point
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
        o = AlipayCommerceOperationContentQueryModel()
        if 'booth' in d:
            o.booth = d['booth']
        if 'channel' in d:
            o.channel = d['channel']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'content_id_str' in d:
            o.content_id_str = d['content_id_str']
        if 'ext_params' in d:
            o.ext_params = d['ext_params']
        if 'page_number' in d:
            o.page_number = d['page_number']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'scene' in d:
            o.scene = d['scene']
        if 'touch_point' in d:
            o.touch_point = d['touch_point']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


