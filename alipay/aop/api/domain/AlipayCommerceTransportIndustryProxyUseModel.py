#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportIndustryProxyUseModel(object):

    def __init__(self):
        self._industry_event = None
        self._industry_request = None
        self._industry_scene = None
        self._sys_service_provider_id = None
        self._user_id = None

    @property
    def industry_event(self):
        return self._industry_event

    @industry_event.setter
    def industry_event(self, value):
        self._industry_event = value
    @property
    def industry_request(self):
        return self._industry_request

    @industry_request.setter
    def industry_request(self, value):
        self._industry_request = value
    @property
    def industry_scene(self):
        return self._industry_scene

    @industry_scene.setter
    def industry_scene(self, value):
        self._industry_scene = value
    @property
    def sys_service_provider_id(self):
        return self._sys_service_provider_id

    @sys_service_provider_id.setter
    def sys_service_provider_id(self, value):
        self._sys_service_provider_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.industry_event:
            if hasattr(self.industry_event, 'to_alipay_dict'):
                params['industry_event'] = self.industry_event.to_alipay_dict()
            else:
                params['industry_event'] = self.industry_event
        if self.industry_request:
            if hasattr(self.industry_request, 'to_alipay_dict'):
                params['industry_request'] = self.industry_request.to_alipay_dict()
            else:
                params['industry_request'] = self.industry_request
        if self.industry_scene:
            if hasattr(self.industry_scene, 'to_alipay_dict'):
                params['industry_scene'] = self.industry_scene.to_alipay_dict()
            else:
                params['industry_scene'] = self.industry_scene
        if self.sys_service_provider_id:
            if hasattr(self.sys_service_provider_id, 'to_alipay_dict'):
                params['sys_service_provider_id'] = self.sys_service_provider_id.to_alipay_dict()
            else:
                params['sys_service_provider_id'] = self.sys_service_provider_id
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
        o = AlipayCommerceTransportIndustryProxyUseModel()
        if 'industry_event' in d:
            o.industry_event = d['industry_event']
        if 'industry_request' in d:
            o.industry_request = d['industry_request']
        if 'industry_scene' in d:
            o.industry_scene = d['industry_scene']
        if 'sys_service_provider_id' in d:
            o.sys_service_provider_id = d['sys_service_provider_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


