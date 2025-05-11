#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class NDeviceWorkAttach(object):

    def __init__(self):
        self._attachment_name = None
        self._attachment_scene = None
        self._attachment_type = None
        self._attachment_url = None

    @property
    def attachment_name(self):
        return self._attachment_name

    @attachment_name.setter
    def attachment_name(self, value):
        self._attachment_name = value
    @property
    def attachment_scene(self):
        return self._attachment_scene

    @attachment_scene.setter
    def attachment_scene(self, value):
        self._attachment_scene = value
    @property
    def attachment_type(self):
        return self._attachment_type

    @attachment_type.setter
    def attachment_type(self, value):
        self._attachment_type = value
    @property
    def attachment_url(self):
        return self._attachment_url

    @attachment_url.setter
    def attachment_url(self, value):
        self._attachment_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.attachment_name:
            if hasattr(self.attachment_name, 'to_alipay_dict'):
                params['attachment_name'] = self.attachment_name.to_alipay_dict()
            else:
                params['attachment_name'] = self.attachment_name
        if self.attachment_scene:
            if hasattr(self.attachment_scene, 'to_alipay_dict'):
                params['attachment_scene'] = self.attachment_scene.to_alipay_dict()
            else:
                params['attachment_scene'] = self.attachment_scene
        if self.attachment_type:
            if hasattr(self.attachment_type, 'to_alipay_dict'):
                params['attachment_type'] = self.attachment_type.to_alipay_dict()
            else:
                params['attachment_type'] = self.attachment_type
        if self.attachment_url:
            if hasattr(self.attachment_url, 'to_alipay_dict'):
                params['attachment_url'] = self.attachment_url.to_alipay_dict()
            else:
                params['attachment_url'] = self.attachment_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = NDeviceWorkAttach()
        if 'attachment_name' in d:
            o.attachment_name = d['attachment_name']
        if 'attachment_scene' in d:
            o.attachment_scene = d['attachment_scene']
        if 'attachment_type' in d:
            o.attachment_type = d['attachment_type']
        if 'attachment_url' in d:
            o.attachment_url = d['attachment_url']
        return o


