#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Command import Command


class AlipayInsSceneCommandReceiveModel(object):

    def __init__(self):
        self._command = None

    @property
    def command(self):
        return self._command

    @command.setter
    def command(self, value):
        if isinstance(value, Command):
            self._command = value
        else:
            self._command = Command.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.command:
            if hasattr(self.command, 'to_alipay_dict'):
                params['command'] = self.command.to_alipay_dict()
            else:
                params['command'] = self.command
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsSceneCommandReceiveModel()
        if 'command' in d:
            o.command = d['command']
        return o


