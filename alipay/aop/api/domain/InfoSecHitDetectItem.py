#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InfoSecHitDetectItem(object):

    def __init__(self):
        self._detect_resource_level = None
        self._detect_type_code = None
        self._hit_content = None
        self._hit_detect_resource = None

    @property
    def detect_resource_level(self):
        return self._detect_resource_level

    @detect_resource_level.setter
    def detect_resource_level(self, value):
        self._detect_resource_level = value
    @property
    def detect_type_code(self):
        return self._detect_type_code

    @detect_type_code.setter
    def detect_type_code(self, value):
        self._detect_type_code = value
    @property
    def hit_content(self):
        return self._hit_content

    @hit_content.setter
    def hit_content(self, value):
        self._hit_content = value
    @property
    def hit_detect_resource(self):
        return self._hit_detect_resource

    @hit_detect_resource.setter
    def hit_detect_resource(self, value):
        self._hit_detect_resource = value


    def to_alipay_dict(self):
        params = dict()
        if self.detect_resource_level:
            if hasattr(self.detect_resource_level, 'to_alipay_dict'):
                params['detect_resource_level'] = self.detect_resource_level.to_alipay_dict()
            else:
                params['detect_resource_level'] = self.detect_resource_level
        if self.detect_type_code:
            if hasattr(self.detect_type_code, 'to_alipay_dict'):
                params['detect_type_code'] = self.detect_type_code.to_alipay_dict()
            else:
                params['detect_type_code'] = self.detect_type_code
        if self.hit_content:
            if hasattr(self.hit_content, 'to_alipay_dict'):
                params['hit_content'] = self.hit_content.to_alipay_dict()
            else:
                params['hit_content'] = self.hit_content
        if self.hit_detect_resource:
            if hasattr(self.hit_detect_resource, 'to_alipay_dict'):
                params['hit_detect_resource'] = self.hit_detect_resource.to_alipay_dict()
            else:
                params['hit_detect_resource'] = self.hit_detect_resource
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InfoSecHitDetectItem()
        if 'detect_resource_level' in d:
            o.detect_resource_level = d['detect_resource_level']
        if 'detect_type_code' in d:
            o.detect_type_code = d['detect_type_code']
        if 'hit_content' in d:
            o.hit_content = d['hit_content']
        if 'hit_detect_resource' in d:
            o.hit_detect_resource = d['hit_detect_resource']
        return o


