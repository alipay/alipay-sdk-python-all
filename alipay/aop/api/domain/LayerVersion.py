#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class LayerVersion(object):

    def __init__(self):
        self._description = None
        self._display_name = None
        self._enable_delete = None
        self._gmt_create = None
        self._image_display_names = None
        self._image_list = None
        self._layer_name = None
        self._layer_version_name = None

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def display_name(self):
        return self._display_name

    @display_name.setter
    def display_name(self, value):
        self._display_name = value
    @property
    def enable_delete(self):
        return self._enable_delete

    @enable_delete.setter
    def enable_delete(self, value):
        self._enable_delete = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def image_display_names(self):
        return self._image_display_names

    @image_display_names.setter
    def image_display_names(self, value):
        if isinstance(value, list):
            self._image_display_names = list()
            for i in value:
                self._image_display_names.append(i)
    @property
    def image_list(self):
        return self._image_list

    @image_list.setter
    def image_list(self, value):
        if isinstance(value, list):
            self._image_list = list()
            for i in value:
                self._image_list.append(i)
    @property
    def layer_name(self):
        return self._layer_name

    @layer_name.setter
    def layer_name(self, value):
        self._layer_name = value
    @property
    def layer_version_name(self):
        return self._layer_version_name

    @layer_version_name.setter
    def layer_version_name(self, value):
        self._layer_version_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.description:
            if hasattr(self.description, 'to_alipay_dict'):
                params['description'] = self.description.to_alipay_dict()
            else:
                params['description'] = self.description
        if self.display_name:
            if hasattr(self.display_name, 'to_alipay_dict'):
                params['display_name'] = self.display_name.to_alipay_dict()
            else:
                params['display_name'] = self.display_name
        if self.enable_delete:
            if hasattr(self.enable_delete, 'to_alipay_dict'):
                params['enable_delete'] = self.enable_delete.to_alipay_dict()
            else:
                params['enable_delete'] = self.enable_delete
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.image_display_names:
            if isinstance(self.image_display_names, list):
                for i in range(0, len(self.image_display_names)):
                    element = self.image_display_names[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.image_display_names[i] = element.to_alipay_dict()
            if hasattr(self.image_display_names, 'to_alipay_dict'):
                params['image_display_names'] = self.image_display_names.to_alipay_dict()
            else:
                params['image_display_names'] = self.image_display_names
        if self.image_list:
            if isinstance(self.image_list, list):
                for i in range(0, len(self.image_list)):
                    element = self.image_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.image_list[i] = element.to_alipay_dict()
            if hasattr(self.image_list, 'to_alipay_dict'):
                params['image_list'] = self.image_list.to_alipay_dict()
            else:
                params['image_list'] = self.image_list
        if self.layer_name:
            if hasattr(self.layer_name, 'to_alipay_dict'):
                params['layer_name'] = self.layer_name.to_alipay_dict()
            else:
                params['layer_name'] = self.layer_name
        if self.layer_version_name:
            if hasattr(self.layer_version_name, 'to_alipay_dict'):
                params['layer_version_name'] = self.layer_version_name.to_alipay_dict()
            else:
                params['layer_version_name'] = self.layer_version_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LayerVersion()
        if 'description' in d:
            o.description = d['description']
        if 'display_name' in d:
            o.display_name = d['display_name']
        if 'enable_delete' in d:
            o.enable_delete = d['enable_delete']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'image_display_names' in d:
            o.image_display_names = d['image_display_names']
        if 'image_list' in d:
            o.image_list = d['image_list']
        if 'layer_name' in d:
            o.layer_name = d['layer_name']
        if 'layer_version_name' in d:
            o.layer_version_name = d['layer_version_name']
        return o


