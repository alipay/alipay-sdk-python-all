#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayPayAppSmartwearManagementSyncModel(object):

    def __init__(self):
        self._command = None
        self._payload = None

    @property
    def command(self):
        return self._command

    @command.setter
    def command(self, value):
        self._command = value
    @property
    def payload(self):
        return self._payload

    @payload.setter
    def payload(self, value):
        self._payload = value


    def to_alipay_dict(self):
        params = dict()
        if self.command:
            if hasattr(self.command, 'to_alipay_dict'):
                params['command'] = self.command.to_alipay_dict()
            else:
                params['command'] = self.command
        if self.payload:
            if hasattr(self.payload, 'to_alipay_dict'):
                params['payload'] = self.payload.to_alipay_dict()
            else:
                params['payload'] = self.payload
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayPayAppSmartwearManagementSyncModel()
        if 'command' in d:
            o.command = d['command']
        if 'payload' in d:
            o.payload = d['payload']
        return o


