#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZMGOQuitConfig(object):

    def __init__(self):
        self._quit_desc = None
        self._quit_jump_url = None
        self._quit_type = None

    @property
    def quit_desc(self):
        return self._quit_desc

    @quit_desc.setter
    def quit_desc(self, value):
        self._quit_desc = value
    @property
    def quit_jump_url(self):
        return self._quit_jump_url

    @quit_jump_url.setter
    def quit_jump_url(self, value):
        self._quit_jump_url = value
    @property
    def quit_type(self):
        return self._quit_type

    @quit_type.setter
    def quit_type(self, value):
        self._quit_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.quit_desc:
            if hasattr(self.quit_desc, 'to_alipay_dict'):
                params['quit_desc'] = self.quit_desc.to_alipay_dict()
            else:
                params['quit_desc'] = self.quit_desc
        if self.quit_jump_url:
            if hasattr(self.quit_jump_url, 'to_alipay_dict'):
                params['quit_jump_url'] = self.quit_jump_url.to_alipay_dict()
            else:
                params['quit_jump_url'] = self.quit_jump_url
        if self.quit_type:
            if hasattr(self.quit_type, 'to_alipay_dict'):
                params['quit_type'] = self.quit_type.to_alipay_dict()
            else:
                params['quit_type'] = self.quit_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZMGOQuitConfig()
        if 'quit_desc' in d:
            o.quit_desc = d['quit_desc']
        if 'quit_jump_url' in d:
            o.quit_jump_url = d['quit_jump_url']
        if 'quit_type' in d:
            o.quit_type = d['quit_type']
        return o


