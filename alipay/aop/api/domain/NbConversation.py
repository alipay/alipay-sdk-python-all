#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class NbConversation(object):

    def __init__(self):
        self._agent_id = None
        self._create_time = None
        self._id = None
        self._name = None
        self._outer_user_id = None

    @property
    def agent_id(self):
        return self._agent_id

    @agent_id.setter
    def agent_id(self, value):
        self._agent_id = value
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def outer_user_id(self):
        return self._outer_user_id

    @outer_user_id.setter
    def outer_user_id(self, value):
        self._outer_user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.agent_id:
            if hasattr(self.agent_id, 'to_alipay_dict'):
                params['agent_id'] = self.agent_id.to_alipay_dict()
            else:
                params['agent_id'] = self.agent_id
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.outer_user_id:
            if hasattr(self.outer_user_id, 'to_alipay_dict'):
                params['outer_user_id'] = self.outer_user_id.to_alipay_dict()
            else:
                params['outer_user_id'] = self.outer_user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = NbConversation()
        if 'agent_id' in d:
            o.agent_id = d['agent_id']
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'id' in d:
            o.id = d['id']
        if 'name' in d:
            o.name = d['name']
        if 'outer_user_id' in d:
            o.outer_user_id = d['outer_user_id']
        return o


