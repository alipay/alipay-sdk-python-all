#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DatadigitalFincloudFinsaasTagDistQueryModel(object):

    def __init__(self):
        self._show_type = None
        self._tag_code = None
        self._tag_version = None

    @property
    def show_type(self):
        return self._show_type

    @show_type.setter
    def show_type(self, value):
        self._show_type = value
    @property
    def tag_code(self):
        return self._tag_code

    @tag_code.setter
    def tag_code(self, value):
        self._tag_code = value
    @property
    def tag_version(self):
        return self._tag_version

    @tag_version.setter
    def tag_version(self, value):
        self._tag_version = value


    def to_alipay_dict(self):
        params = dict()
        if self.show_type:
            if hasattr(self.show_type, 'to_alipay_dict'):
                params['show_type'] = self.show_type.to_alipay_dict()
            else:
                params['show_type'] = self.show_type
        if self.tag_code:
            if hasattr(self.tag_code, 'to_alipay_dict'):
                params['tag_code'] = self.tag_code.to_alipay_dict()
            else:
                params['tag_code'] = self.tag_code
        if self.tag_version:
            if hasattr(self.tag_version, 'to_alipay_dict'):
                params['tag_version'] = self.tag_version.to_alipay_dict()
            else:
                params['tag_version'] = self.tag_version
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DatadigitalFincloudFinsaasTagDistQueryModel()
        if 'show_type' in d:
            o.show_type = d['show_type']
        if 'tag_code' in d:
            o.tag_code = d['tag_code']
        if 'tag_version' in d:
            o.tag_version = d['tag_version']
        return o


