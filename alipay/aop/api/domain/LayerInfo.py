#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class LayerInfo(object):

    def __init__(self):
        self._layer_description = None
        self._layer_display_name = None
        self._layer_name = None
        self._layer_version_description = None
        self._layer_version_display_name = None
        self._layer_version_image_display_names = None
        self._layer_version_image_list = None
        self._layer_version_name = None

    @property
    def layer_description(self):
        return self._layer_description

    @layer_description.setter
    def layer_description(self, value):
        self._layer_description = value
    @property
    def layer_display_name(self):
        return self._layer_display_name

    @layer_display_name.setter
    def layer_display_name(self, value):
        self._layer_display_name = value
    @property
    def layer_name(self):
        return self._layer_name

    @layer_name.setter
    def layer_name(self, value):
        self._layer_name = value
    @property
    def layer_version_description(self):
        return self._layer_version_description

    @layer_version_description.setter
    def layer_version_description(self, value):
        self._layer_version_description = value
    @property
    def layer_version_display_name(self):
        return self._layer_version_display_name

    @layer_version_display_name.setter
    def layer_version_display_name(self, value):
        self._layer_version_display_name = value
    @property
    def layer_version_image_display_names(self):
        return self._layer_version_image_display_names

    @layer_version_image_display_names.setter
    def layer_version_image_display_names(self, value):
        if isinstance(value, list):
            self._layer_version_image_display_names = list()
            for i in value:
                self._layer_version_image_display_names.append(i)
    @property
    def layer_version_image_list(self):
        return self._layer_version_image_list

    @layer_version_image_list.setter
    def layer_version_image_list(self, value):
        if isinstance(value, list):
            self._layer_version_image_list = list()
            for i in value:
                self._layer_version_image_list.append(i)
    @property
    def layer_version_name(self):
        return self._layer_version_name

    @layer_version_name.setter
    def layer_version_name(self, value):
        self._layer_version_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.layer_description:
            if hasattr(self.layer_description, 'to_alipay_dict'):
                params['layer_description'] = self.layer_description.to_alipay_dict()
            else:
                params['layer_description'] = self.layer_description
        if self.layer_display_name:
            if hasattr(self.layer_display_name, 'to_alipay_dict'):
                params['layer_display_name'] = self.layer_display_name.to_alipay_dict()
            else:
                params['layer_display_name'] = self.layer_display_name
        if self.layer_name:
            if hasattr(self.layer_name, 'to_alipay_dict'):
                params['layer_name'] = self.layer_name.to_alipay_dict()
            else:
                params['layer_name'] = self.layer_name
        if self.layer_version_description:
            if hasattr(self.layer_version_description, 'to_alipay_dict'):
                params['layer_version_description'] = self.layer_version_description.to_alipay_dict()
            else:
                params['layer_version_description'] = self.layer_version_description
        if self.layer_version_display_name:
            if hasattr(self.layer_version_display_name, 'to_alipay_dict'):
                params['layer_version_display_name'] = self.layer_version_display_name.to_alipay_dict()
            else:
                params['layer_version_display_name'] = self.layer_version_display_name
        if self.layer_version_image_display_names:
            if isinstance(self.layer_version_image_display_names, list):
                for i in range(0, len(self.layer_version_image_display_names)):
                    element = self.layer_version_image_display_names[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.layer_version_image_display_names[i] = element.to_alipay_dict()
            if hasattr(self.layer_version_image_display_names, 'to_alipay_dict'):
                params['layer_version_image_display_names'] = self.layer_version_image_display_names.to_alipay_dict()
            else:
                params['layer_version_image_display_names'] = self.layer_version_image_display_names
        if self.layer_version_image_list:
            if isinstance(self.layer_version_image_list, list):
                for i in range(0, len(self.layer_version_image_list)):
                    element = self.layer_version_image_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.layer_version_image_list[i] = element.to_alipay_dict()
            if hasattr(self.layer_version_image_list, 'to_alipay_dict'):
                params['layer_version_image_list'] = self.layer_version_image_list.to_alipay_dict()
            else:
                params['layer_version_image_list'] = self.layer_version_image_list
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
        o = LayerInfo()
        if 'layer_description' in d:
            o.layer_description = d['layer_description']
        if 'layer_display_name' in d:
            o.layer_display_name = d['layer_display_name']
        if 'layer_name' in d:
            o.layer_name = d['layer_name']
        if 'layer_version_description' in d:
            o.layer_version_description = d['layer_version_description']
        if 'layer_version_display_name' in d:
            o.layer_version_display_name = d['layer_version_display_name']
        if 'layer_version_image_display_names' in d:
            o.layer_version_image_display_names = d['layer_version_image_display_names']
        if 'layer_version_image_list' in d:
            o.layer_version_image_list = d['layer_version_image_list']
        if 'layer_version_name' in d:
            o.layer_version_name = d['layer_version_name']
        return o


