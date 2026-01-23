#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayIservicePromotioncoreChatCreateModel(object):

    def __init__(self):
        self._channel = None
        self._history = None
        self._message_id = None
        self._message_info = None
        self._return_type = None
        self._scene = None
        self._session_id = None
        self._tenant_id = None

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def history(self):
        return self._history

    @history.setter
    def history(self, value):
        self._history = value
    @property
    def message_id(self):
        return self._message_id

    @message_id.setter
    def message_id(self, value):
        self._message_id = value
    @property
    def message_info(self):
        return self._message_info

    @message_info.setter
    def message_info(self, value):
        self._message_info = value
    @property
    def return_type(self):
        return self._return_type

    @return_type.setter
    def return_type(self, value):
        self._return_type = value
    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value
    @property
    def session_id(self):
        return self._session_id

    @session_id.setter
    def session_id(self, value):
        self._session_id = value
    @property
    def tenant_id(self):
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, value):
        self._tenant_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.history:
            if hasattr(self.history, 'to_alipay_dict'):
                params['history'] = self.history.to_alipay_dict()
            else:
                params['history'] = self.history
        if self.message_id:
            if hasattr(self.message_id, 'to_alipay_dict'):
                params['message_id'] = self.message_id.to_alipay_dict()
            else:
                params['message_id'] = self.message_id
        if self.message_info:
            if hasattr(self.message_info, 'to_alipay_dict'):
                params['message_info'] = self.message_info.to_alipay_dict()
            else:
                params['message_info'] = self.message_info
        if self.return_type:
            if hasattr(self.return_type, 'to_alipay_dict'):
                params['return_type'] = self.return_type.to_alipay_dict()
            else:
                params['return_type'] = self.return_type
        if self.scene:
            if hasattr(self.scene, 'to_alipay_dict'):
                params['scene'] = self.scene.to_alipay_dict()
            else:
                params['scene'] = self.scene
        if self.session_id:
            if hasattr(self.session_id, 'to_alipay_dict'):
                params['session_id'] = self.session_id.to_alipay_dict()
            else:
                params['session_id'] = self.session_id
        if self.tenant_id:
            if hasattr(self.tenant_id, 'to_alipay_dict'):
                params['tenant_id'] = self.tenant_id.to_alipay_dict()
            else:
                params['tenant_id'] = self.tenant_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayIservicePromotioncoreChatCreateModel()
        if 'channel' in d:
            o.channel = d['channel']
        if 'history' in d:
            o.history = d['history']
        if 'message_id' in d:
            o.message_id = d['message_id']
        if 'message_info' in d:
            o.message_info = d['message_info']
        if 'return_type' in d:
            o.return_type = d['return_type']
        if 'scene' in d:
            o.scene = d['scene']
        if 'session_id' in d:
            o.session_id = d['session_id']
        if 'tenant_id' in d:
            o.tenant_id = d['tenant_id']
        return o


