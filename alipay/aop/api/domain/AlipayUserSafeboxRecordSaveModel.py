#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserSafeboxRecordSaveModel(object):

    def __init__(self):
        self._content = None
        self._key_version = None
        self._scene_code = None
        self._title = None
        self._unique_id = None
        self._user_id = None

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def key_version(self):
        return self._key_version

    @key_version.setter
    def key_version(self, value):
        self._key_version = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
    @property
    def unique_id(self):
        return self._unique_id

    @unique_id.setter
    def unique_id(self, value):
        self._unique_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.content:
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        if self.key_version:
            if hasattr(self.key_version, 'to_alipay_dict'):
                params['key_version'] = self.key_version.to_alipay_dict()
            else:
                params['key_version'] = self.key_version
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        if self.unique_id:
            if hasattr(self.unique_id, 'to_alipay_dict'):
                params['unique_id'] = self.unique_id.to_alipay_dict()
            else:
                params['unique_id'] = self.unique_id
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserSafeboxRecordSaveModel()
        if 'content' in d:
            o.content = d['content']
        if 'key_version' in d:
            o.key_version = d['key_version']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'title' in d:
            o.title = d['title']
        if 'unique_id' in d:
            o.unique_id = d['unique_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


