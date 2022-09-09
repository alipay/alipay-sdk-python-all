#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InsUserTraceDTO(object):

    def __init__(self):
        self._action = None
        self._ext_info = None
        self._object = None
        self._time = None
        self._user_id = None

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, value):
        self._action = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def object(self):
        return self._object

    @object.setter
    def object(self, value):
        self._object = value
    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, value):
        self._time = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.action:
            if hasattr(self.action, 'to_alipay_dict'):
                params['action'] = self.action.to_alipay_dict()
            else:
                params['action'] = self.action
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.object:
            if hasattr(self.object, 'to_alipay_dict'):
                params['object'] = self.object.to_alipay_dict()
            else:
                params['object'] = self.object
        if self.time:
            if hasattr(self.time, 'to_alipay_dict'):
                params['time'] = self.time.to_alipay_dict()
            else:
                params['time'] = self.time
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
        o = InsUserTraceDTO()
        if 'action' in d:
            o.action = d['action']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'object' in d:
            o.object = d['object']
        if 'time' in d:
            o.time = d['time']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


