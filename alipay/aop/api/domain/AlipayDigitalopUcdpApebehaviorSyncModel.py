#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDigitalopUcdpApebehaviorSyncModel(object):

    def __init__(self):
        self._action_type = None
        self._channel = None
        self._item_id_list = None
        self._log_time = None
        self._pos = None
        self._project_id = None
        self._spm = None
        self._trace_id = None
        self._user_id = None

    @property
    def action_type(self):
        return self._action_type

    @action_type.setter
    def action_type(self, value):
        self._action_type = value
    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def item_id_list(self):
        return self._item_id_list

    @item_id_list.setter
    def item_id_list(self, value):
        self._item_id_list = value
    @property
    def log_time(self):
        return self._log_time

    @log_time.setter
    def log_time(self, value):
        self._log_time = value
    @property
    def pos(self):
        return self._pos

    @pos.setter
    def pos(self, value):
        self._pos = value
    @property
    def project_id(self):
        return self._project_id

    @project_id.setter
    def project_id(self, value):
        self._project_id = value
    @property
    def spm(self):
        return self._spm

    @spm.setter
    def spm(self, value):
        self._spm = value
    @property
    def trace_id(self):
        return self._trace_id

    @trace_id.setter
    def trace_id(self, value):
        self._trace_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.action_type:
            if hasattr(self.action_type, 'to_alipay_dict'):
                params['action_type'] = self.action_type.to_alipay_dict()
            else:
                params['action_type'] = self.action_type
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.item_id_list:
            if hasattr(self.item_id_list, 'to_alipay_dict'):
                params['item_id_list'] = self.item_id_list.to_alipay_dict()
            else:
                params['item_id_list'] = self.item_id_list
        if self.log_time:
            if hasattr(self.log_time, 'to_alipay_dict'):
                params['log_time'] = self.log_time.to_alipay_dict()
            else:
                params['log_time'] = self.log_time
        if self.pos:
            if hasattr(self.pos, 'to_alipay_dict'):
                params['pos'] = self.pos.to_alipay_dict()
            else:
                params['pos'] = self.pos
        if self.project_id:
            if hasattr(self.project_id, 'to_alipay_dict'):
                params['project_id'] = self.project_id.to_alipay_dict()
            else:
                params['project_id'] = self.project_id
        if self.spm:
            if hasattr(self.spm, 'to_alipay_dict'):
                params['spm'] = self.spm.to_alipay_dict()
            else:
                params['spm'] = self.spm
        if self.trace_id:
            if hasattr(self.trace_id, 'to_alipay_dict'):
                params['trace_id'] = self.trace_id.to_alipay_dict()
            else:
                params['trace_id'] = self.trace_id
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
        o = AlipayDigitalopUcdpApebehaviorSyncModel()
        if 'action_type' in d:
            o.action_type = d['action_type']
        if 'channel' in d:
            o.channel = d['channel']
        if 'item_id_list' in d:
            o.item_id_list = d['item_id_list']
        if 'log_time' in d:
            o.log_time = d['log_time']
        if 'pos' in d:
            o.pos = d['pos']
        if 'project_id' in d:
            o.project_id = d['project_id']
        if 'spm' in d:
            o.spm = d['spm']
        if 'trace_id' in d:
            o.trace_id = d['trace_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


