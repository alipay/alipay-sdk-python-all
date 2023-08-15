#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCloudCloudrunStaticsiteUploadurlCreateModel(object):

    def __init__(self):
        self._assume_token = None
        self._content_type = None
        self._env = None
        self._path = None

    @property
    def assume_token(self):
        return self._assume_token

    @assume_token.setter
    def assume_token(self, value):
        self._assume_token = value
    @property
    def content_type(self):
        return self._content_type

    @content_type.setter
    def content_type(self, value):
        self._content_type = value
    @property
    def env(self):
        return self._env

    @env.setter
    def env(self, value):
        self._env = value
    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, value):
        self._path = value


    def to_alipay_dict(self):
        params = dict()
        if self.assume_token:
            if hasattr(self.assume_token, 'to_alipay_dict'):
                params['assume_token'] = self.assume_token.to_alipay_dict()
            else:
                params['assume_token'] = self.assume_token
        if self.content_type:
            if hasattr(self.content_type, 'to_alipay_dict'):
                params['content_type'] = self.content_type.to_alipay_dict()
            else:
                params['content_type'] = self.content_type
        if self.env:
            if hasattr(self.env, 'to_alipay_dict'):
                params['env'] = self.env.to_alipay_dict()
            else:
                params['env'] = self.env
        if self.path:
            if hasattr(self.path, 'to_alipay_dict'):
                params['path'] = self.path.to_alipay_dict()
            else:
                params['path'] = self.path
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudCloudrunStaticsiteUploadurlCreateModel()
        if 'assume_token' in d:
            o.assume_token = d['assume_token']
        if 'content_type' in d:
            o.content_type = d['content_type']
        if 'env' in d:
            o.env = d['env']
        if 'path' in d:
            o.path = d['path']
        return o


