#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.GFAOpenAPIBaseAcceptance import GFAOpenAPIBaseAcceptance
from alipay.aop.api.domain.GFAOpenAPICommand import GFAOpenAPICommand


class GFAOpenAPIDetailQueryResult(object):

    def __init__(self):
        self._acceptance_list = None
        self._command_list = None

    @property
    def acceptance_list(self):
        return self._acceptance_list

    @acceptance_list.setter
    def acceptance_list(self, value):
        if isinstance(value, list):
            self._acceptance_list = list()
            for i in value:
                if isinstance(i, GFAOpenAPIBaseAcceptance):
                    self._acceptance_list.append(i)
                else:
                    self._acceptance_list.append(GFAOpenAPIBaseAcceptance.from_alipay_dict(i))
    @property
    def command_list(self):
        return self._command_list

    @command_list.setter
    def command_list(self, value):
        if isinstance(value, list):
            self._command_list = list()
            for i in value:
                if isinstance(i, GFAOpenAPICommand):
                    self._command_list.append(i)
                else:
                    self._command_list.append(GFAOpenAPICommand.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.acceptance_list:
            if isinstance(self.acceptance_list, list):
                for i in range(0, len(self.acceptance_list)):
                    element = self.acceptance_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.acceptance_list[i] = element.to_alipay_dict()
            if hasattr(self.acceptance_list, 'to_alipay_dict'):
                params['acceptance_list'] = self.acceptance_list.to_alipay_dict()
            else:
                params['acceptance_list'] = self.acceptance_list
        if self.command_list:
            if isinstance(self.command_list, list):
                for i in range(0, len(self.command_list)):
                    element = self.command_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.command_list[i] = element.to_alipay_dict()
            if hasattr(self.command_list, 'to_alipay_dict'):
                params['command_list'] = self.command_list.to_alipay_dict()
            else:
                params['command_list'] = self.command_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GFAOpenAPIDetailQueryResult()
        if 'acceptance_list' in d:
            o.acceptance_list = d['acceptance_list']
        if 'command_list' in d:
            o.command_list = d['command_list']
        return o


