#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AichatPushMsgVO(object):

    def __init__(self):
        self._msg_content = None
        self._msg_id = None
        self._scene_id = None

    @property
    def msg_content(self):
        return self._msg_content

    @msg_content.setter
    def msg_content(self, value):
        self._msg_content = value
    @property
    def msg_id(self):
        return self._msg_id

    @msg_id.setter
    def msg_id(self, value):
        self._msg_id = value
    @property
    def scene_id(self):
        return self._scene_id

    @scene_id.setter
    def scene_id(self, value):
        self._scene_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.msg_content:
            if hasattr(self.msg_content, 'to_alipay_dict'):
                params['msg_content'] = self.msg_content.to_alipay_dict()
            else:
                params['msg_content'] = self.msg_content
        if self.msg_id:
            if hasattr(self.msg_id, 'to_alipay_dict'):
                params['msg_id'] = self.msg_id.to_alipay_dict()
            else:
                params['msg_id'] = self.msg_id
        if self.scene_id:
            if hasattr(self.scene_id, 'to_alipay_dict'):
                params['scene_id'] = self.scene_id.to_alipay_dict()
            else:
                params['scene_id'] = self.scene_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AichatPushMsgVO()
        if 'msg_content' in d:
            o.msg_content = d['msg_content']
        if 'msg_id' in d:
            o.msg_id = d['msg_id']
        if 'scene_id' in d:
            o.scene_id = d['scene_id']
        return o


