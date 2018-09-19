#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CaptchaInfo(object):

    def __init__(self):
        self._captcha_desc = None
        self._image_content = None
        self._image_type = None

    @property
    def captcha_desc(self):
        return self._captcha_desc

    @captcha_desc.setter
    def captcha_desc(self, value):
        self._captcha_desc = value
    @property
    def image_content(self):
        return self._image_content

    @image_content.setter
    def image_content(self, value):
        self._image_content = value
    @property
    def image_type(self):
        return self._image_type

    @image_type.setter
    def image_type(self, value):
        self._image_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.captcha_desc:
            if hasattr(self.captcha_desc, 'to_alipay_dict'):
                params['captcha_desc'] = self.captcha_desc.to_alipay_dict()
            else:
                params['captcha_desc'] = self.captcha_desc
        if self.image_content:
            if hasattr(self.image_content, 'to_alipay_dict'):
                params['image_content'] = self.image_content.to_alipay_dict()
            else:
                params['image_content'] = self.image_content
        if self.image_type:
            if hasattr(self.image_type, 'to_alipay_dict'):
                params['image_type'] = self.image_type.to_alipay_dict()
            else:
                params['image_type'] = self.image_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CaptchaInfo()
        if 'captcha_desc' in d:
            o.captcha_desc = d['captcha_desc']
        if 'image_content' in d:
            o.image_content = d['image_content']
        if 'image_type' in d:
            o.image_type = d['image_type']
        return o


