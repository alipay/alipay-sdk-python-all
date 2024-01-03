#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenBiosearchBiogroupIdentifyModel(object):

    def __init__(self):
        self._biz_id = None
        self._compare_level = None
        self._content = None
        self._group_id = None
        self._scene = None
        self._top_n = None

    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def compare_level(self):
        return self._compare_level

    @compare_level.setter
    def compare_level(self, value):
        self._compare_level = value
    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def group_id(self):
        return self._group_id

    @group_id.setter
    def group_id(self, value):
        self._group_id = value
    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value
    @property
    def top_n(self):
        return self._top_n

    @top_n.setter
    def top_n(self, value):
        self._top_n = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.compare_level:
            if hasattr(self.compare_level, 'to_alipay_dict'):
                params['compare_level'] = self.compare_level.to_alipay_dict()
            else:
                params['compare_level'] = self.compare_level
        if self.content:
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        if self.group_id:
            if hasattr(self.group_id, 'to_alipay_dict'):
                params['group_id'] = self.group_id.to_alipay_dict()
            else:
                params['group_id'] = self.group_id
        if self.scene:
            if hasattr(self.scene, 'to_alipay_dict'):
                params['scene'] = self.scene.to_alipay_dict()
            else:
                params['scene'] = self.scene
        if self.top_n:
            if hasattr(self.top_n, 'to_alipay_dict'):
                params['top_n'] = self.top_n.to_alipay_dict()
            else:
                params['top_n'] = self.top_n
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenBiosearchBiogroupIdentifyModel()
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'compare_level' in d:
            o.compare_level = d['compare_level']
        if 'content' in d:
            o.content = d['content']
        if 'group_id' in d:
            o.group_id = d['group_id']
        if 'scene' in d:
            o.scene = d['scene']
        if 'top_n' in d:
            o.top_n = d['top_n']
        return o


