#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InteOpMiniAppInfo(object):

    def __init__(self):
        self._mini_app_id = None
        self._mini_app_name = None
        self._mini_app_screenshot = None

    @property
    def mini_app_id(self):
        return self._mini_app_id

    @mini_app_id.setter
    def mini_app_id(self, value):
        self._mini_app_id = value
    @property
    def mini_app_name(self):
        return self._mini_app_name

    @mini_app_name.setter
    def mini_app_name(self, value):
        self._mini_app_name = value
    @property
    def mini_app_screenshot(self):
        return self._mini_app_screenshot

    @mini_app_screenshot.setter
    def mini_app_screenshot(self, value):
        self._mini_app_screenshot = value


    def to_alipay_dict(self):
        params = dict()
        if self.mini_app_id:
            if hasattr(self.mini_app_id, 'to_alipay_dict'):
                params['mini_app_id'] = self.mini_app_id.to_alipay_dict()
            else:
                params['mini_app_id'] = self.mini_app_id
        if self.mini_app_name:
            if hasattr(self.mini_app_name, 'to_alipay_dict'):
                params['mini_app_name'] = self.mini_app_name.to_alipay_dict()
            else:
                params['mini_app_name'] = self.mini_app_name
        if self.mini_app_screenshot:
            if hasattr(self.mini_app_screenshot, 'to_alipay_dict'):
                params['mini_app_screenshot'] = self.mini_app_screenshot.to_alipay_dict()
            else:
                params['mini_app_screenshot'] = self.mini_app_screenshot
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InteOpMiniAppInfo()
        if 'mini_app_id' in d:
            o.mini_app_id = d['mini_app_id']
        if 'mini_app_name' in d:
            o.mini_app_name = d['mini_app_name']
        if 'mini_app_screenshot' in d:
            o.mini_app_screenshot = d['mini_app_screenshot']
        return o


