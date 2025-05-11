#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ChoiceTools import ChoiceTools


class ChatSpecifications(object):

    def __init__(self):
        self._choice_tools = None
        self._reasoning = None

    @property
    def choice_tools(self):
        return self._choice_tools

    @choice_tools.setter
    def choice_tools(self, value):
        if isinstance(value, list):
            self._choice_tools = list()
            for i in value:
                if isinstance(i, ChoiceTools):
                    self._choice_tools.append(i)
                else:
                    self._choice_tools.append(ChoiceTools.from_alipay_dict(i))
    @property
    def reasoning(self):
        return self._reasoning

    @reasoning.setter
    def reasoning(self, value):
        self._reasoning = value


    def to_alipay_dict(self):
        params = dict()
        if self.choice_tools:
            if isinstance(self.choice_tools, list):
                for i in range(0, len(self.choice_tools)):
                    element = self.choice_tools[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.choice_tools[i] = element.to_alipay_dict()
            if hasattr(self.choice_tools, 'to_alipay_dict'):
                params['choice_tools'] = self.choice_tools.to_alipay_dict()
            else:
                params['choice_tools'] = self.choice_tools
        if self.reasoning:
            if hasattr(self.reasoning, 'to_alipay_dict'):
                params['reasoning'] = self.reasoning.to_alipay_dict()
            else:
                params['reasoning'] = self.reasoning
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ChatSpecifications()
        if 'choice_tools' in d:
            o.choice_tools = d['choice_tools']
        if 'reasoning' in d:
            o.reasoning = d['reasoning']
        return o


