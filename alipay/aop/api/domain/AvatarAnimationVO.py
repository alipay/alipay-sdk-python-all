#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AvatarAnimationVO(object):

    def __init__(self):
        self._animation_desc = None
        self._animation_gltf_url = None
        self._animation_name = None
        self._animation_type = None
        self._avatar_types = None
        self._icon = None
        self._id = None

    @property
    def animation_desc(self):
        return self._animation_desc

    @animation_desc.setter
    def animation_desc(self, value):
        self._animation_desc = value
    @property
    def animation_gltf_url(self):
        return self._animation_gltf_url

    @animation_gltf_url.setter
    def animation_gltf_url(self, value):
        self._animation_gltf_url = value
    @property
    def animation_name(self):
        return self._animation_name

    @animation_name.setter
    def animation_name(self, value):
        self._animation_name = value
    @property
    def animation_type(self):
        return self._animation_type

    @animation_type.setter
    def animation_type(self, value):
        self._animation_type = value
    @property
    def avatar_types(self):
        return self._avatar_types

    @avatar_types.setter
    def avatar_types(self, value):
        if isinstance(value, list):
            self._avatar_types = list()
            for i in value:
                self._avatar_types.append(i)
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


    def to_alipay_dict(self):
        params = dict()
        if self.animation_desc:
            if hasattr(self.animation_desc, 'to_alipay_dict'):
                params['animation_desc'] = self.animation_desc.to_alipay_dict()
            else:
                params['animation_desc'] = self.animation_desc
        if self.animation_gltf_url:
            if hasattr(self.animation_gltf_url, 'to_alipay_dict'):
                params['animation_gltf_url'] = self.animation_gltf_url.to_alipay_dict()
            else:
                params['animation_gltf_url'] = self.animation_gltf_url
        if self.animation_name:
            if hasattr(self.animation_name, 'to_alipay_dict'):
                params['animation_name'] = self.animation_name.to_alipay_dict()
            else:
                params['animation_name'] = self.animation_name
        if self.animation_type:
            if hasattr(self.animation_type, 'to_alipay_dict'):
                params['animation_type'] = self.animation_type.to_alipay_dict()
            else:
                params['animation_type'] = self.animation_type
        if self.avatar_types:
            if isinstance(self.avatar_types, list):
                for i in range(0, len(self.avatar_types)):
                    element = self.avatar_types[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.avatar_types[i] = element.to_alipay_dict()
            if hasattr(self.avatar_types, 'to_alipay_dict'):
                params['avatar_types'] = self.avatar_types.to_alipay_dict()
            else:
                params['avatar_types'] = self.avatar_types
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AvatarAnimationVO()
        if 'animation_desc' in d:
            o.animation_desc = d['animation_desc']
        if 'animation_gltf_url' in d:
            o.animation_gltf_url = d['animation_gltf_url']
        if 'animation_name' in d:
            o.animation_name = d['animation_name']
        if 'animation_type' in d:
            o.animation_type = d['animation_type']
        if 'avatar_types' in d:
            o.avatar_types = d['avatar_types']
        if 'icon' in d:
            o.icon = d['icon']
        if 'id' in d:
            o.id = d['id']
        return o


