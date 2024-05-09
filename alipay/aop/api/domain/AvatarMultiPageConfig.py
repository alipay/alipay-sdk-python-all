#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AvatarMultiPageConfig(object):

    def __init__(self):
        self._ori_text = None
        self._picture_url = None

    @property
    def ori_text(self):
        return self._ori_text

    @ori_text.setter
    def ori_text(self, value):
        self._ori_text = value
    @property
    def picture_url(self):
        return self._picture_url

    @picture_url.setter
    def picture_url(self, value):
        self._picture_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.ori_text:
            if hasattr(self.ori_text, 'to_alipay_dict'):
                params['ori_text'] = self.ori_text.to_alipay_dict()
            else:
                params['ori_text'] = self.ori_text
        if self.picture_url:
            if hasattr(self.picture_url, 'to_alipay_dict'):
                params['picture_url'] = self.picture_url.to_alipay_dict()
            else:
                params['picture_url'] = self.picture_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AvatarMultiPageConfig()
        if 'ori_text' in d:
            o.ori_text = d['ori_text']
        if 'picture_url' in d:
            o.picture_url = d['picture_url']
        return o


