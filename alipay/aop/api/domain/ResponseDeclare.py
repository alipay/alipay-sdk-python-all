#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.LoadInfoNode import LoadInfoNode


class ResponseDeclare(object):

    def __init__(self):
        self._target_adjustment = None

    @property
    def target_adjustment(self):
        return self._target_adjustment

    @target_adjustment.setter
    def target_adjustment(self, value):
        if isinstance(value, list):
            self._target_adjustment = list()
            for i in value:
                if isinstance(i, LoadInfoNode):
                    self._target_adjustment.append(i)
                else:
                    self._target_adjustment.append(LoadInfoNode.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.target_adjustment:
            if isinstance(self.target_adjustment, list):
                for i in range(0, len(self.target_adjustment)):
                    element = self.target_adjustment[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.target_adjustment[i] = element.to_alipay_dict()
            if hasattr(self.target_adjustment, 'to_alipay_dict'):
                params['target_adjustment'] = self.target_adjustment.to_alipay_dict()
            else:
                params['target_adjustment'] = self.target_adjustment
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ResponseDeclare()
        if 'target_adjustment' in d:
            o.target_adjustment = d['target_adjustment']
        return o


