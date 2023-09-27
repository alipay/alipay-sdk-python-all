#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.LayerVersion import LayerVersion


class Layer(object):

    def __init__(self):
        self._description = None
        self._display_name = None
        self._gmt_modified = None
        self._latest_layer_version_name = None
        self._layer_name = None
        self._layer_version = None

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
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def latest_layer_version_name(self):
        return self._latest_layer_version_name

    @latest_layer_version_name.setter
    def latest_layer_version_name(self, value):
        self._latest_layer_version_name = value
    @property
    def layer_name(self):
        return self._layer_name

    @layer_name.setter
    def layer_name(self, value):
        self._layer_name = value
    @property
    def layer_version(self):
        return self._layer_version

    @layer_version.setter
    def layer_version(self, value):
        if isinstance(value, LayerVersion):
            self._layer_version = value
        else:
            self._layer_version = LayerVersion.from_alipay_dict(value)


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
        if self.gmt_modified:
            if hasattr(self.gmt_modified, 'to_alipay_dict'):
                params['gmt_modified'] = self.gmt_modified.to_alipay_dict()
            else:
                params['gmt_modified'] = self.gmt_modified
        if self.latest_layer_version_name:
            if hasattr(self.latest_layer_version_name, 'to_alipay_dict'):
                params['latest_layer_version_name'] = self.latest_layer_version_name.to_alipay_dict()
            else:
                params['latest_layer_version_name'] = self.latest_layer_version_name
        if self.layer_name:
            if hasattr(self.layer_name, 'to_alipay_dict'):
                params['layer_name'] = self.layer_name.to_alipay_dict()
            else:
                params['layer_name'] = self.layer_name
        if self.layer_version:
            if hasattr(self.layer_version, 'to_alipay_dict'):
                params['layer_version'] = self.layer_version.to_alipay_dict()
            else:
                params['layer_version'] = self.layer_version
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = Layer()
        if 'description' in d:
            o.description = d['description']
        if 'display_name' in d:
            o.display_name = d['display_name']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'latest_layer_version_name' in d:
            o.latest_layer_version_name = d['latest_layer_version_name']
        if 'layer_name' in d:
            o.layer_name = d['layer_name']
        if 'layer_version' in d:
            o.layer_version = d['layer_version']
        return o


