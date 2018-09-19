#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RecommendInfo(object):

    def __init__(self):
        self._jump_url = None
        self._recommend_content = None
        self._recommend_img = None
        self._recommend_type = None

    @property
    def jump_url(self):
        return self._jump_url

    @jump_url.setter
    def jump_url(self, value):
        self._jump_url = value
    @property
    def recommend_content(self):
        return self._recommend_content

    @recommend_content.setter
    def recommend_content(self, value):
        self._recommend_content = value
    @property
    def recommend_img(self):
        return self._recommend_img

    @recommend_img.setter
    def recommend_img(self, value):
        self._recommend_img = value
    @property
    def recommend_type(self):
        return self._recommend_type

    @recommend_type.setter
    def recommend_type(self, value):
        self._recommend_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.jump_url:
            if hasattr(self.jump_url, 'to_alipay_dict'):
                params['jump_url'] = self.jump_url.to_alipay_dict()
            else:
                params['jump_url'] = self.jump_url
        if self.recommend_content:
            if hasattr(self.recommend_content, 'to_alipay_dict'):
                params['recommend_content'] = self.recommend_content.to_alipay_dict()
            else:
                params['recommend_content'] = self.recommend_content
        if self.recommend_img:
            if hasattr(self.recommend_img, 'to_alipay_dict'):
                params['recommend_img'] = self.recommend_img.to_alipay_dict()
            else:
                params['recommend_img'] = self.recommend_img
        if self.recommend_type:
            if hasattr(self.recommend_type, 'to_alipay_dict'):
                params['recommend_type'] = self.recommend_type.to_alipay_dict()
            else:
                params['recommend_type'] = self.recommend_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RecommendInfo()
        if 'jump_url' in d:
            o.jump_url = d['jump_url']
        if 'recommend_content' in d:
            o.recommend_content = d['recommend_content']
        if 'recommend_img' in d:
            o.recommend_img = d['recommend_img']
        if 'recommend_type' in d:
            o.recommend_type = d['recommend_type']
        return o


