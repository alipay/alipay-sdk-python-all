#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOverseasTravelMessagesSendNotifyModel(object):

    def __init__(self):
        self._message_args = None
        self._message_request_id = None
        self._message_scene = None
        self._open_id = None
        self._psp_id = None

    @property
    def message_args(self):
        return self._message_args

    @message_args.setter
    def message_args(self, value):
        self._message_args = value
    @property
    def message_request_id(self):
        return self._message_request_id

    @message_request_id.setter
    def message_request_id(self, value):
        self._message_request_id = value
    @property
    def message_scene(self):
        return self._message_scene

    @message_scene.setter
    def message_scene(self, value):
        self._message_scene = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def psp_id(self):
        return self._psp_id

    @psp_id.setter
    def psp_id(self, value):
        self._psp_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.message_args:
            if hasattr(self.message_args, 'to_alipay_dict'):
                params['message_args'] = self.message_args.to_alipay_dict()
            else:
                params['message_args'] = self.message_args
        if self.message_request_id:
            if hasattr(self.message_request_id, 'to_alipay_dict'):
                params['message_request_id'] = self.message_request_id.to_alipay_dict()
            else:
                params['message_request_id'] = self.message_request_id
        if self.message_scene:
            if hasattr(self.message_scene, 'to_alipay_dict'):
                params['message_scene'] = self.message_scene.to_alipay_dict()
            else:
                params['message_scene'] = self.message_scene
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.psp_id:
            if hasattr(self.psp_id, 'to_alipay_dict'):
                params['psp_id'] = self.psp_id.to_alipay_dict()
            else:
                params['psp_id'] = self.psp_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOverseasTravelMessagesSendNotifyModel()
        if 'message_args' in d:
            o.message_args = d['message_args']
        if 'message_request_id' in d:
            o.message_request_id = d['message_request_id']
        if 'message_scene' in d:
            o.message_scene = d['message_scene']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'psp_id' in d:
            o.psp_id = d['psp_id']
        return o


