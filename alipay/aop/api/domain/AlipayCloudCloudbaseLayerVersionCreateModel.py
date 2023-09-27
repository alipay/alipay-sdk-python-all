#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCloudCloudbaseLayerVersionCreateModel(object):

    def __init__(self):
        self._biz_app_id = None
        self._biz_env_id = None
        self._layer_name = None
        self._upload_id = None
        self._version_description = None
        self._version_display_name = None
        self._version_image_list = None
        self._version_name = None

    @property
    def biz_app_id(self):
        return self._biz_app_id

    @biz_app_id.setter
    def biz_app_id(self, value):
        self._biz_app_id = value
    @property
    def biz_env_id(self):
        return self._biz_env_id

    @biz_env_id.setter
    def biz_env_id(self, value):
        self._biz_env_id = value
    @property
    def layer_name(self):
        return self._layer_name

    @layer_name.setter
    def layer_name(self, value):
        self._layer_name = value
    @property
    def upload_id(self):
        return self._upload_id

    @upload_id.setter
    def upload_id(self, value):
        self._upload_id = value
    @property
    def version_description(self):
        return self._version_description

    @version_description.setter
    def version_description(self, value):
        self._version_description = value
    @property
    def version_display_name(self):
        return self._version_display_name

    @version_display_name.setter
    def version_display_name(self, value):
        self._version_display_name = value
    @property
    def version_image_list(self):
        return self._version_image_list

    @version_image_list.setter
    def version_image_list(self, value):
        if isinstance(value, list):
            self._version_image_list = list()
            for i in value:
                self._version_image_list.append(i)
    @property
    def version_name(self):
        return self._version_name

    @version_name.setter
    def version_name(self, value):
        self._version_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_app_id:
            if hasattr(self.biz_app_id, 'to_alipay_dict'):
                params['biz_app_id'] = self.biz_app_id.to_alipay_dict()
            else:
                params['biz_app_id'] = self.biz_app_id
        if self.biz_env_id:
            if hasattr(self.biz_env_id, 'to_alipay_dict'):
                params['biz_env_id'] = self.biz_env_id.to_alipay_dict()
            else:
                params['biz_env_id'] = self.biz_env_id
        if self.layer_name:
            if hasattr(self.layer_name, 'to_alipay_dict'):
                params['layer_name'] = self.layer_name.to_alipay_dict()
            else:
                params['layer_name'] = self.layer_name
        if self.upload_id:
            if hasattr(self.upload_id, 'to_alipay_dict'):
                params['upload_id'] = self.upload_id.to_alipay_dict()
            else:
                params['upload_id'] = self.upload_id
        if self.version_description:
            if hasattr(self.version_description, 'to_alipay_dict'):
                params['version_description'] = self.version_description.to_alipay_dict()
            else:
                params['version_description'] = self.version_description
        if self.version_display_name:
            if hasattr(self.version_display_name, 'to_alipay_dict'):
                params['version_display_name'] = self.version_display_name.to_alipay_dict()
            else:
                params['version_display_name'] = self.version_display_name
        if self.version_image_list:
            if isinstance(self.version_image_list, list):
                for i in range(0, len(self.version_image_list)):
                    element = self.version_image_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.version_image_list[i] = element.to_alipay_dict()
            if hasattr(self.version_image_list, 'to_alipay_dict'):
                params['version_image_list'] = self.version_image_list.to_alipay_dict()
            else:
                params['version_image_list'] = self.version_image_list
        if self.version_name:
            if hasattr(self.version_name, 'to_alipay_dict'):
                params['version_name'] = self.version_name.to_alipay_dict()
            else:
                params['version_name'] = self.version_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudCloudbaseLayerVersionCreateModel()
        if 'biz_app_id' in d:
            o.biz_app_id = d['biz_app_id']
        if 'biz_env_id' in d:
            o.biz_env_id = d['biz_env_id']
        if 'layer_name' in d:
            o.layer_name = d['layer_name']
        if 'upload_id' in d:
            o.upload_id = d['upload_id']
        if 'version_description' in d:
            o.version_description = d['version_description']
        if 'version_display_name' in d:
            o.version_display_name = d['version_display_name']
        if 'version_image_list' in d:
            o.version_image_list = d['version_image_list']
        if 'version_name' in d:
            o.version_name = d['version_name']
        return o


