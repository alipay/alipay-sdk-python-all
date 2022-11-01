#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenIotContentSyncModel(object):

    def __init__(self):
        self._content_list = None
        self._request_id = None
        self._scene_code = None

    @property
    def content_list(self):
        return self._content_list

    @content_list.setter
    def content_list(self, value):
        if isinstance(value, list):
            self._content_list = list()
            for i in value:
                self._content_list.append(i)
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.content_list:
            if isinstance(self.content_list, list):
                for i in range(0, len(self.content_list)):
                    element = self.content_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.content_list[i] = element.to_alipay_dict()
            if hasattr(self.content_list, 'to_alipay_dict'):
                params['content_list'] = self.content_list.to_alipay_dict()
            else:
                params['content_list'] = self.content_list
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenIotContentSyncModel()
        if 'content_list' in d:
            o.content_list = d['content_list']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        return o


