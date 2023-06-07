#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AvatarVO(object):

    def __init__(self):
        self._avatar_gltf_info = None
        self._avatar_id = None
        self._avatar_name = None
        self._avatar_type = None
        self._default_avatar = None
        self._gender = None
        self._real_gender = None

    @property
    def avatar_gltf_info(self):
        return self._avatar_gltf_info

    @avatar_gltf_info.setter
    def avatar_gltf_info(self, value):
        self._avatar_gltf_info = value
    @property
    def avatar_id(self):
        return self._avatar_id

    @avatar_id.setter
    def avatar_id(self, value):
        self._avatar_id = value
    @property
    def avatar_name(self):
        return self._avatar_name

    @avatar_name.setter
    def avatar_name(self, value):
        self._avatar_name = value
    @property
    def avatar_type(self):
        return self._avatar_type

    @avatar_type.setter
    def avatar_type(self, value):
        self._avatar_type = value
    @property
    def default_avatar(self):
        return self._default_avatar

    @default_avatar.setter
    def default_avatar(self, value):
        self._default_avatar = value
    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        self._gender = value
    @property
    def real_gender(self):
        return self._real_gender

    @real_gender.setter
    def real_gender(self, value):
        self._real_gender = value


    def to_alipay_dict(self):
        params = dict()
        if self.avatar_gltf_info:
            if hasattr(self.avatar_gltf_info, 'to_alipay_dict'):
                params['avatar_gltf_info'] = self.avatar_gltf_info.to_alipay_dict()
            else:
                params['avatar_gltf_info'] = self.avatar_gltf_info
        if self.avatar_id:
            if hasattr(self.avatar_id, 'to_alipay_dict'):
                params['avatar_id'] = self.avatar_id.to_alipay_dict()
            else:
                params['avatar_id'] = self.avatar_id
        if self.avatar_name:
            if hasattr(self.avatar_name, 'to_alipay_dict'):
                params['avatar_name'] = self.avatar_name.to_alipay_dict()
            else:
                params['avatar_name'] = self.avatar_name
        if self.avatar_type:
            if hasattr(self.avatar_type, 'to_alipay_dict'):
                params['avatar_type'] = self.avatar_type.to_alipay_dict()
            else:
                params['avatar_type'] = self.avatar_type
        if self.default_avatar:
            if hasattr(self.default_avatar, 'to_alipay_dict'):
                params['default_avatar'] = self.default_avatar.to_alipay_dict()
            else:
                params['default_avatar'] = self.default_avatar
        if self.gender:
            if hasattr(self.gender, 'to_alipay_dict'):
                params['gender'] = self.gender.to_alipay_dict()
            else:
                params['gender'] = self.gender
        if self.real_gender:
            if hasattr(self.real_gender, 'to_alipay_dict'):
                params['real_gender'] = self.real_gender.to_alipay_dict()
            else:
                params['real_gender'] = self.real_gender
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AvatarVO()
        if 'avatar_gltf_info' in d:
            o.avatar_gltf_info = d['avatar_gltf_info']
        if 'avatar_id' in d:
            o.avatar_id = d['avatar_id']
        if 'avatar_name' in d:
            o.avatar_name = d['avatar_name']
        if 'avatar_type' in d:
            o.avatar_type = d['avatar_type']
        if 'default_avatar' in d:
            o.default_avatar = d['default_avatar']
        if 'gender' in d:
            o.gender = d['gender']
        if 'real_gender' in d:
            o.real_gender = d['real_gender']
        return o


