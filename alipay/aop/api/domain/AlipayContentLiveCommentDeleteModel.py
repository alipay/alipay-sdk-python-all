#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayContentLiveCommentDeleteModel(object):

    def __init__(self):
        self._alipay_comment_id = None
        self._out_live_id = None
        self._scene = None

    @property
    def alipay_comment_id(self):
        return self._alipay_comment_id

    @alipay_comment_id.setter
    def alipay_comment_id(self, value):
        self._alipay_comment_id = value
    @property
    def out_live_id(self):
        return self._out_live_id

    @out_live_id.setter
    def out_live_id(self, value):
        self._out_live_id = value
    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_comment_id:
            if hasattr(self.alipay_comment_id, 'to_alipay_dict'):
                params['alipay_comment_id'] = self.alipay_comment_id.to_alipay_dict()
            else:
                params['alipay_comment_id'] = self.alipay_comment_id
        if self.out_live_id:
            if hasattr(self.out_live_id, 'to_alipay_dict'):
                params['out_live_id'] = self.out_live_id.to_alipay_dict()
            else:
                params['out_live_id'] = self.out_live_id
        if self.scene:
            if hasattr(self.scene, 'to_alipay_dict'):
                params['scene'] = self.scene.to_alipay_dict()
            else:
                params['scene'] = self.scene
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayContentLiveCommentDeleteModel()
        if 'alipay_comment_id' in d:
            o.alipay_comment_id = d['alipay_comment_id']
        if 'out_live_id' in d:
            o.out_live_id = d['out_live_id']
        if 'scene' in d:
            o.scene = d['scene']
        return o


