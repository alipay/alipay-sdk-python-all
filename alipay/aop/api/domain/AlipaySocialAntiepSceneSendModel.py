#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySocialAntiepSceneSendModel(object):

    def __init__(self):
        self._action_biz_info = None
        self._action_biz_no = None
        self._action_code = None
        self._action_time = None
        self._request_type = None
        self._scene_code = None
        self._source = None
        self._user_id = None

    @property
    def action_biz_info(self):
        return self._action_biz_info

    @action_biz_info.setter
    def action_biz_info(self, value):
        self._action_biz_info = value
    @property
    def action_biz_no(self):
        return self._action_biz_no

    @action_biz_no.setter
    def action_biz_no(self, value):
        self._action_biz_no = value
    @property
    def action_code(self):
        return self._action_code

    @action_code.setter
    def action_code(self, value):
        self._action_code = value
    @property
    def action_time(self):
        return self._action_time

    @action_time.setter
    def action_time(self, value):
        self._action_time = value
    @property
    def request_type(self):
        return self._request_type

    @request_type.setter
    def request_type(self, value):
        self._request_type = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.action_biz_info:
            if hasattr(self.action_biz_info, 'to_alipay_dict'):
                params['action_biz_info'] = self.action_biz_info.to_alipay_dict()
            else:
                params['action_biz_info'] = self.action_biz_info
        if self.action_biz_no:
            if hasattr(self.action_biz_no, 'to_alipay_dict'):
                params['action_biz_no'] = self.action_biz_no.to_alipay_dict()
            else:
                params['action_biz_no'] = self.action_biz_no
        if self.action_code:
            if hasattr(self.action_code, 'to_alipay_dict'):
                params['action_code'] = self.action_code.to_alipay_dict()
            else:
                params['action_code'] = self.action_code
        if self.action_time:
            if hasattr(self.action_time, 'to_alipay_dict'):
                params['action_time'] = self.action_time.to_alipay_dict()
            else:
                params['action_time'] = self.action_time
        if self.request_type:
            if hasattr(self.request_type, 'to_alipay_dict'):
                params['request_type'] = self.request_type.to_alipay_dict()
            else:
                params['request_type'] = self.request_type
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
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
        o = AlipaySocialAntiepSceneSendModel()
        if 'action_biz_info' in d:
            o.action_biz_info = d['action_biz_info']
        if 'action_biz_no' in d:
            o.action_biz_no = d['action_biz_no']
        if 'action_code' in d:
            o.action_code = d['action_code']
        if 'action_time' in d:
            o.action_time = d['action_time']
        if 'request_type' in d:
            o.request_type = d['request_type']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'source' in d:
            o.source = d['source']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


