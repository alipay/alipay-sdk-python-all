#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayTerminalEdgecloudHeyagentCommandSendModel(object):

    def __init__(self):
        self._agent_id = None
        self._command = None
        self._open_id = None
        self._target = None
        self._uid = None
        self._utdid = None

    @property
    def agent_id(self):
        return self._agent_id

    @agent_id.setter
    def agent_id(self, value):
        self._agent_id = value
    @property
    def command(self):
        return self._command

    @command.setter
    def command(self, value):
        self._command = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def target(self):
        return self._target

    @target.setter
    def target(self, value):
        self._target = value
    @property
    def uid(self):
        return self._uid

    @uid.setter
    def uid(self, value):
        self._uid = value
    @property
    def utdid(self):
        return self._utdid

    @utdid.setter
    def utdid(self, value):
        self._utdid = value


    def to_alipay_dict(self):
        params = dict()
        if self.agent_id:
            if hasattr(self.agent_id, 'to_alipay_dict'):
                params['agent_id'] = self.agent_id.to_alipay_dict()
            else:
                params['agent_id'] = self.agent_id
        if self.command:
            if hasattr(self.command, 'to_alipay_dict'):
                params['command'] = self.command.to_alipay_dict()
            else:
                params['command'] = self.command
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.target:
            if hasattr(self.target, 'to_alipay_dict'):
                params['target'] = self.target.to_alipay_dict()
            else:
                params['target'] = self.target
        if self.uid:
            if hasattr(self.uid, 'to_alipay_dict'):
                params['uid'] = self.uid.to_alipay_dict()
            else:
                params['uid'] = self.uid
        if self.utdid:
            if hasattr(self.utdid, 'to_alipay_dict'):
                params['utdid'] = self.utdid.to_alipay_dict()
            else:
                params['utdid'] = self.utdid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayTerminalEdgecloudHeyagentCommandSendModel()
        if 'agent_id' in d:
            o.agent_id = d['agent_id']
        if 'command' in d:
            o.command = d['command']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'target' in d:
            o.target = d['target']
        if 'uid' in d:
            o.uid = d['uid']
        if 'utdid' in d:
            o.utdid = d['utdid']
        return o


