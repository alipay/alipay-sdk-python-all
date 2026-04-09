#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayTradeProductCreateModel(object):

    def __init__(self):
        self._description = None
        self._images = None
        self._marketing_features = None
        self._metadata = None
        self._name = None
        self._unit_label = None
        self._url = None

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
    @property
    def images(self):
        return self._images

    @images.setter
    def images(self, value):
        self._images = value
    @property
    def marketing_features(self):
        return self._marketing_features

    @marketing_features.setter
    def marketing_features(self, value):
        self._marketing_features = value
    @property
    def metadata(self):
        return self._metadata

    @metadata.setter
    def metadata(self, value):
        self._metadata = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def unit_label(self):
        return self._unit_label

    @unit_label.setter
    def unit_label(self, value):
        self._unit_label = value
    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value


    def to_alipay_dict(self):
        params = dict()
        if self.description:
            if hasattr(self.description, 'to_alipay_dict'):
                params['description'] = self.description.to_alipay_dict()
            else:
                params['description'] = self.description
        if self.images:
            if hasattr(self.images, 'to_alipay_dict'):
                params['images'] = self.images.to_alipay_dict()
            else:
                params['images'] = self.images
        if self.marketing_features:
            if hasattr(self.marketing_features, 'to_alipay_dict'):
                params['marketing_features'] = self.marketing_features.to_alipay_dict()
            else:
                params['marketing_features'] = self.marketing_features
        if self.metadata:
            if hasattr(self.metadata, 'to_alipay_dict'):
                params['metadata'] = self.metadata.to_alipay_dict()
            else:
                params['metadata'] = self.metadata
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.unit_label:
            if hasattr(self.unit_label, 'to_alipay_dict'):
                params['unit_label'] = self.unit_label.to_alipay_dict()
            else:
                params['unit_label'] = self.unit_label
        if self.url:
            if hasattr(self.url, 'to_alipay_dict'):
                params['url'] = self.url.to_alipay_dict()
            else:
                params['url'] = self.url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayTradeProductCreateModel()
        if 'description' in d:
            o.description = d['description']
        if 'images' in d:
            o.images = d['images']
        if 'marketing_features' in d:
            o.marketing_features = d['marketing_features']
        if 'metadata' in d:
            o.metadata = d['metadata']
        if 'name' in d:
            o.name = d['name']
        if 'unit_label' in d:
            o.unit_label = d['unit_label']
        if 'url' in d:
            o.url = d['url']
        return o


