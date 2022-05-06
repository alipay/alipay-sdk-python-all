#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportIndustryDataSyncModel(object):

    def __init__(self):
        self._sync_content = None
        self._sync_event = None
        self._sync_scene = None
        self._sys_service_provider_id = None

    @property
    def sync_content(self):
        return self._sync_content

    @sync_content.setter
    def sync_content(self, value):
        self._sync_content = value
    @property
    def sync_event(self):
        return self._sync_event

    @sync_event.setter
    def sync_event(self, value):
        self._sync_event = value
    @property
    def sync_scene(self):
        return self._sync_scene

    @sync_scene.setter
    def sync_scene(self, value):
        self._sync_scene = value
    @property
    def sys_service_provider_id(self):
        return self._sys_service_provider_id

    @sys_service_provider_id.setter
    def sys_service_provider_id(self, value):
        self._sys_service_provider_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.sync_content:
            if hasattr(self.sync_content, 'to_alipay_dict'):
                params['sync_content'] = self.sync_content.to_alipay_dict()
            else:
                params['sync_content'] = self.sync_content
        if self.sync_event:
            if hasattr(self.sync_event, 'to_alipay_dict'):
                params['sync_event'] = self.sync_event.to_alipay_dict()
            else:
                params['sync_event'] = self.sync_event
        if self.sync_scene:
            if hasattr(self.sync_scene, 'to_alipay_dict'):
                params['sync_scene'] = self.sync_scene.to_alipay_dict()
            else:
                params['sync_scene'] = self.sync_scene
        if self.sys_service_provider_id:
            if hasattr(self.sys_service_provider_id, 'to_alipay_dict'):
                params['sys_service_provider_id'] = self.sys_service_provider_id.to_alipay_dict()
            else:
                params['sys_service_provider_id'] = self.sys_service_provider_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportIndustryDataSyncModel()
        if 'sync_content' in d:
            o.sync_content = d['sync_content']
        if 'sync_event' in d:
            o.sync_event = d['sync_event']
        if 'sync_scene' in d:
            o.sync_scene = d['sync_scene']
        if 'sys_service_provider_id' in d:
            o.sys_service_provider_id = d['sys_service_provider_id']
        return o


