#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PrintMessageVO(object):

    def __init__(self):
        self._cmd_type = None
        self._cmds = None

    @property
    def cmd_type(self):
        return self._cmd_type

    @cmd_type.setter
    def cmd_type(self, value):
        self._cmd_type = value
    @property
    def cmds(self):
        return self._cmds

    @cmds.setter
    def cmds(self, value):
        self._cmds = value


    def to_alipay_dict(self):
        params = dict()
        if self.cmd_type:
            if hasattr(self.cmd_type, 'to_alipay_dict'):
                params['cmd_type'] = self.cmd_type.to_alipay_dict()
            else:
                params['cmd_type'] = self.cmd_type
        if self.cmds:
            if hasattr(self.cmds, 'to_alipay_dict'):
                params['cmds'] = self.cmds.to_alipay_dict()
            else:
                params['cmds'] = self.cmds
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PrintMessageVO()
        if 'cmd_type' in d:
            o.cmd_type = d['cmd_type']
        if 'cmds' in d:
            o.cmds = d['cmds']
        return o


