#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.GiveConfigVO import GiveConfigVO


class AvatarAsianAssetVO(object):

    def __init__(self):
        self._ext_model_info = None
        self._give_config = None
        self._give_type = None
        self._gltf_url = None
        self._gmt_create = None
        self._id = None
        self._init_behavior = None
        self._name = None
        self._preview = None
        self._reward_status = None
        self._tag_name = None
        self._type = None
        self._type_name = None

    @property
    def ext_model_info(self):
        return self._ext_model_info

    @ext_model_info.setter
    def ext_model_info(self, value):
        self._ext_model_info = value
    @property
    def give_config(self):
        return self._give_config

    @give_config.setter
    def give_config(self, value):
        if isinstance(value, GiveConfigVO):
            self._give_config = value
        else:
            self._give_config = GiveConfigVO.from_alipay_dict(value)
    @property
    def give_type(self):
        return self._give_type

    @give_type.setter
    def give_type(self, value):
        self._give_type = value
    @property
    def gltf_url(self):
        return self._gltf_url

    @gltf_url.setter
    def gltf_url(self, value):
        self._gltf_url = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def init_behavior(self):
        return self._init_behavior

    @init_behavior.setter
    def init_behavior(self, value):
        self._init_behavior = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def preview(self):
        return self._preview

    @preview.setter
    def preview(self, value):
        self._preview = value
    @property
    def reward_status(self):
        return self._reward_status

    @reward_status.setter
    def reward_status(self, value):
        self._reward_status = value
    @property
    def tag_name(self):
        return self._tag_name

    @tag_name.setter
    def tag_name(self, value):
        self._tag_name = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
    @property
    def type_name(self):
        return self._type_name

    @type_name.setter
    def type_name(self, value):
        self._type_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.ext_model_info:
            if hasattr(self.ext_model_info, 'to_alipay_dict'):
                params['ext_model_info'] = self.ext_model_info.to_alipay_dict()
            else:
                params['ext_model_info'] = self.ext_model_info
        if self.give_config:
            if hasattr(self.give_config, 'to_alipay_dict'):
                params['give_config'] = self.give_config.to_alipay_dict()
            else:
                params['give_config'] = self.give_config
        if self.give_type:
            if hasattr(self.give_type, 'to_alipay_dict'):
                params['give_type'] = self.give_type.to_alipay_dict()
            else:
                params['give_type'] = self.give_type
        if self.gltf_url:
            if hasattr(self.gltf_url, 'to_alipay_dict'):
                params['gltf_url'] = self.gltf_url.to_alipay_dict()
            else:
                params['gltf_url'] = self.gltf_url
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.init_behavior:
            if hasattr(self.init_behavior, 'to_alipay_dict'):
                params['init_behavior'] = self.init_behavior.to_alipay_dict()
            else:
                params['init_behavior'] = self.init_behavior
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.preview:
            if hasattr(self.preview, 'to_alipay_dict'):
                params['preview'] = self.preview.to_alipay_dict()
            else:
                params['preview'] = self.preview
        if self.reward_status:
            if hasattr(self.reward_status, 'to_alipay_dict'):
                params['reward_status'] = self.reward_status.to_alipay_dict()
            else:
                params['reward_status'] = self.reward_status
        if self.tag_name:
            if hasattr(self.tag_name, 'to_alipay_dict'):
                params['tag_name'] = self.tag_name.to_alipay_dict()
            else:
                params['tag_name'] = self.tag_name
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        if self.type_name:
            if hasattr(self.type_name, 'to_alipay_dict'):
                params['type_name'] = self.type_name.to_alipay_dict()
            else:
                params['type_name'] = self.type_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AvatarAsianAssetVO()
        if 'ext_model_info' in d:
            o.ext_model_info = d['ext_model_info']
        if 'give_config' in d:
            o.give_config = d['give_config']
        if 'give_type' in d:
            o.give_type = d['give_type']
        if 'gltf_url' in d:
            o.gltf_url = d['gltf_url']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'id' in d:
            o.id = d['id']
        if 'init_behavior' in d:
            o.init_behavior = d['init_behavior']
        if 'name' in d:
            o.name = d['name']
        if 'preview' in d:
            o.preview = d['preview']
        if 'reward_status' in d:
            o.reward_status = d['reward_status']
        if 'tag_name' in d:
            o.tag_name = d['tag_name']
        if 'type' in d:
            o.type = d['type']
        if 'type_name' in d:
            o.type_name = d['type_name']
        return o


