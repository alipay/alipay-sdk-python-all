#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySocialOpengreenEnergyCreateModel(object):

    def __init__(self):
        self._action_time = None
        self._biz_no = None
        self._ext_info = None
        self._green_actions = None
        self._pid = None
        self._request_scene_code = None
        self._request_type = None
        self._source = None

    @property
    def action_time(self):
        return self._action_time

    @action_time.setter
    def action_time(self, value):
        self._action_time = value
    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def green_actions(self):
        return self._green_actions

    @green_actions.setter
    def green_actions(self, value):
        self._green_actions = value
    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, value):
        self._pid = value
    @property
    def request_scene_code(self):
        return self._request_scene_code

    @request_scene_code.setter
    def request_scene_code(self, value):
        self._request_scene_code = value
    @property
    def request_type(self):
        return self._request_type

    @request_type.setter
    def request_type(self, value):
        self._request_type = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value


    def to_alipay_dict(self):
        params = dict()
        if self.action_time:
            if hasattr(self.action_time, 'to_alipay_dict'):
                params['action_time'] = self.action_time.to_alipay_dict()
            else:
                params['action_time'] = self.action_time
        if self.biz_no:
            if hasattr(self.biz_no, 'to_alipay_dict'):
                params['biz_no'] = self.biz_no.to_alipay_dict()
            else:
                params['biz_no'] = self.biz_no
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.green_actions:
            if hasattr(self.green_actions, 'to_alipay_dict'):
                params['green_actions'] = self.green_actions.to_alipay_dict()
            else:
                params['green_actions'] = self.green_actions
        if self.pid:
            if hasattr(self.pid, 'to_alipay_dict'):
                params['pid'] = self.pid.to_alipay_dict()
            else:
                params['pid'] = self.pid
        if self.request_scene_code:
            if hasattr(self.request_scene_code, 'to_alipay_dict'):
                params['request_scene_code'] = self.request_scene_code.to_alipay_dict()
            else:
                params['request_scene_code'] = self.request_scene_code
        if self.request_type:
            if hasattr(self.request_type, 'to_alipay_dict'):
                params['request_type'] = self.request_type.to_alipay_dict()
            else:
                params['request_type'] = self.request_type
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySocialOpengreenEnergyCreateModel()
        if 'action_time' in d:
            o.action_time = d['action_time']
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'green_actions' in d:
            o.green_actions = d['green_actions']
        if 'pid' in d:
            o.pid = d['pid']
        if 'request_scene_code' in d:
            o.request_scene_code = d['request_scene_code']
        if 'request_type' in d:
            o.request_type = d['request_type']
        if 'source' in d:
            o.source = d['source']
        return o


