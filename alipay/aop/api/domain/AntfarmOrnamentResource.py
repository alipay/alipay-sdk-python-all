#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntfarmOrnamentResource(object):

    def __init__(self):
        self._resource_for_3_d = None
        self._resource_for_spine = None
        self._resource_for_static_image = None
        self._resource_key = None

    @property
    def resource_for_3_d(self):
        return self._resource_for_3_d

    @resource_for_3_d.setter
    def resource_for_3_d(self, value):
        self._resource_for_3_d = value
    @property
    def resource_for_spine(self):
        return self._resource_for_spine

    @resource_for_spine.setter
    def resource_for_spine(self, value):
        self._resource_for_spine = value
    @property
    def resource_for_static_image(self):
        return self._resource_for_static_image

    @resource_for_static_image.setter
    def resource_for_static_image(self, value):
        self._resource_for_static_image = value
    @property
    def resource_key(self):
        return self._resource_key

    @resource_key.setter
    def resource_key(self, value):
        self._resource_key = value


    def to_alipay_dict(self):
        params = dict()
        if self.resource_for_3_d:
            if hasattr(self.resource_for_3_d, 'to_alipay_dict'):
                params['resource_for_3_d'] = self.resource_for_3_d.to_alipay_dict()
            else:
                params['resource_for_3_d'] = self.resource_for_3_d
        if self.resource_for_spine:
            if hasattr(self.resource_for_spine, 'to_alipay_dict'):
                params['resource_for_spine'] = self.resource_for_spine.to_alipay_dict()
            else:
                params['resource_for_spine'] = self.resource_for_spine
        if self.resource_for_static_image:
            if hasattr(self.resource_for_static_image, 'to_alipay_dict'):
                params['resource_for_static_image'] = self.resource_for_static_image.to_alipay_dict()
            else:
                params['resource_for_static_image'] = self.resource_for_static_image
        if self.resource_key:
            if hasattr(self.resource_key, 'to_alipay_dict'):
                params['resource_key'] = self.resource_key.to_alipay_dict()
            else:
                params['resource_key'] = self.resource_key
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntfarmOrnamentResource()
        if 'resource_for_3_d' in d:
            o.resource_for_3_d = d['resource_for_3_d']
        if 'resource_for_spine' in d:
            o.resource_for_spine = d['resource_for_spine']
        if 'resource_for_static_image' in d:
            o.resource_for_static_image = d['resource_for_static_image']
        if 'resource_key' in d:
            o.resource_key = d['resource_key']
        return o


