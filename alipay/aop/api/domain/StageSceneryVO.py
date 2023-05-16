#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class StageSceneryVO(object):

    def __init__(self):
        self._icon = None
        self._id = None
        self._scenery_gltf_url = None
        self._scenery_name = None

    @property
    def icon(self):
        return self._icon

    @icon.setter
    def icon(self, value):
        self._icon = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def scenery_gltf_url(self):
        return self._scenery_gltf_url

    @scenery_gltf_url.setter
    def scenery_gltf_url(self, value):
        self._scenery_gltf_url = value
    @property
    def scenery_name(self):
        return self._scenery_name

    @scenery_name.setter
    def scenery_name(self, value):
        self._scenery_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.icon:
            if hasattr(self.icon, 'to_alipay_dict'):
                params['icon'] = self.icon.to_alipay_dict()
            else:
                params['icon'] = self.icon
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.scenery_gltf_url:
            if hasattr(self.scenery_gltf_url, 'to_alipay_dict'):
                params['scenery_gltf_url'] = self.scenery_gltf_url.to_alipay_dict()
            else:
                params['scenery_gltf_url'] = self.scenery_gltf_url
        if self.scenery_name:
            if hasattr(self.scenery_name, 'to_alipay_dict'):
                params['scenery_name'] = self.scenery_name.to_alipay_dict()
            else:
                params['scenery_name'] = self.scenery_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = StageSceneryVO()
        if 'icon' in d:
            o.icon = d['icon']
        if 'id' in d:
            o.id = d['id']
        if 'scenery_gltf_url' in d:
            o.scenery_gltf_url = d['scenery_gltf_url']
        if 'scenery_name' in d:
            o.scenery_name = d['scenery_name']
        return o


