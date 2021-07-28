#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TemplatePlatformDTO(object):

    def __init__(self):
        self._biz_from_bu = None
        self._biz_from_platform = None
        self._biz_from_scene = None
        self._channel_id = None
        self._web_service_url = None

    @property
    def biz_from_bu(self):
        return self._biz_from_bu

    @biz_from_bu.setter
    def biz_from_bu(self, value):
        self._biz_from_bu = value
    @property
    def biz_from_platform(self):
        return self._biz_from_platform

    @biz_from_platform.setter
    def biz_from_platform(self, value):
        self._biz_from_platform = value
    @property
    def biz_from_scene(self):
        return self._biz_from_scene

    @biz_from_scene.setter
    def biz_from_scene(self, value):
        self._biz_from_scene = value
    @property
    def channel_id(self):
        return self._channel_id

    @channel_id.setter
    def channel_id(self, value):
        self._channel_id = value
    @property
    def web_service_url(self):
        return self._web_service_url

    @web_service_url.setter
    def web_service_url(self, value):
        self._web_service_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_from_bu:
            if hasattr(self.biz_from_bu, 'to_alipay_dict'):
                params['biz_from_bu'] = self.biz_from_bu.to_alipay_dict()
            else:
                params['biz_from_bu'] = self.biz_from_bu
        if self.biz_from_platform:
            if hasattr(self.biz_from_platform, 'to_alipay_dict'):
                params['biz_from_platform'] = self.biz_from_platform.to_alipay_dict()
            else:
                params['biz_from_platform'] = self.biz_from_platform
        if self.biz_from_scene:
            if hasattr(self.biz_from_scene, 'to_alipay_dict'):
                params['biz_from_scene'] = self.biz_from_scene.to_alipay_dict()
            else:
                params['biz_from_scene'] = self.biz_from_scene
        if self.channel_id:
            if hasattr(self.channel_id, 'to_alipay_dict'):
                params['channel_id'] = self.channel_id.to_alipay_dict()
            else:
                params['channel_id'] = self.channel_id
        if self.web_service_url:
            if hasattr(self.web_service_url, 'to_alipay_dict'):
                params['web_service_url'] = self.web_service_url.to_alipay_dict()
            else:
                params['web_service_url'] = self.web_service_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TemplatePlatformDTO()
        if 'biz_from_bu' in d:
            o.biz_from_bu = d['biz_from_bu']
        if 'biz_from_platform' in d:
            o.biz_from_platform = d['biz_from_platform']
        if 'biz_from_scene' in d:
            o.biz_from_scene = d['biz_from_scene']
        if 'channel_id' in d:
            o.channel_id = d['channel_id']
        if 'web_service_url' in d:
            o.web_service_url = d['web_service_url']
        return o


