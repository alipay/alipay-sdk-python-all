#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceAcommunicationUnionmemberActionSyncModel(object):

    def __init__(self):
        self._action = None
        self._alipay_open_id = None
        self._alipay_user_id = None
        self._execute_time = None
        self._flow_id = None
        self._mobile = None
        self._out_user_id = None
        self._params = None

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, value):
        self._action = value
    @property
    def alipay_open_id(self):
        return self._alipay_open_id

    @alipay_open_id.setter
    def alipay_open_id(self, value):
        self._alipay_open_id = value
    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def execute_time(self):
        return self._execute_time

    @execute_time.setter
    def execute_time(self, value):
        self._execute_time = value
    @property
    def flow_id(self):
        return self._flow_id

    @flow_id.setter
    def flow_id(self, value):
        self._flow_id = value
    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, value):
        self._mobile = value
    @property
    def out_user_id(self):
        return self._out_user_id

    @out_user_id.setter
    def out_user_id(self, value):
        self._out_user_id = value
    @property
    def params(self):
        return self._params

    @params.setter
    def params(self, value):
        self._params = value


    def to_alipay_dict(self):
        params = dict()
        if self.action:
            if hasattr(self.action, 'to_alipay_dict'):
                params['action'] = self.action.to_alipay_dict()
            else:
                params['action'] = self.action
        if self.alipay_open_id:
            if hasattr(self.alipay_open_id, 'to_alipay_dict'):
                params['alipay_open_id'] = self.alipay_open_id.to_alipay_dict()
            else:
                params['alipay_open_id'] = self.alipay_open_id
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.execute_time:
            if hasattr(self.execute_time, 'to_alipay_dict'):
                params['execute_time'] = self.execute_time.to_alipay_dict()
            else:
                params['execute_time'] = self.execute_time
        if self.flow_id:
            if hasattr(self.flow_id, 'to_alipay_dict'):
                params['flow_id'] = self.flow_id.to_alipay_dict()
            else:
                params['flow_id'] = self.flow_id
        if self.mobile:
            if hasattr(self.mobile, 'to_alipay_dict'):
                params['mobile'] = self.mobile.to_alipay_dict()
            else:
                params['mobile'] = self.mobile
        if self.out_user_id:
            if hasattr(self.out_user_id, 'to_alipay_dict'):
                params['out_user_id'] = self.out_user_id.to_alipay_dict()
            else:
                params['out_user_id'] = self.out_user_id
        if self.params:
            if hasattr(self.params, 'to_alipay_dict'):
                params['params'] = self.params.to_alipay_dict()
            else:
                params['params'] = self.params
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceAcommunicationUnionmemberActionSyncModel()
        if 'action' in d:
            o.action = d['action']
        if 'alipay_open_id' in d:
            o.alipay_open_id = d['alipay_open_id']
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'execute_time' in d:
            o.execute_time = d['execute_time']
        if 'flow_id' in d:
            o.flow_id = d['flow_id']
        if 'mobile' in d:
            o.mobile = d['mobile']
        if 'out_user_id' in d:
            o.out_user_id = d['out_user_id']
        if 'params' in d:
            o.params = d['params']
        return o


