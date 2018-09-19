#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Matcher import Matcher


class ErrorMatcher(object):

    def __init__(self):
        self._error_msg = None
        self._matcher = None

    @property
    def error_msg(self):
        return self._error_msg

    @error_msg.setter
    def error_msg(self, value):
        self._error_msg = value
    @property
    def matcher(self):
        return self._matcher

    @matcher.setter
    def matcher(self, value):
        if isinstance(value, Matcher):
            self._matcher = value
        else:
            self._matcher = Matcher.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.error_msg:
            if hasattr(self.error_msg, 'to_alipay_dict'):
                params['error_msg'] = self.error_msg.to_alipay_dict()
            else:
                params['error_msg'] = self.error_msg
        if self.matcher:
            if hasattr(self.matcher, 'to_alipay_dict'):
                params['matcher'] = self.matcher.to_alipay_dict()
            else:
                params['matcher'] = self.matcher
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ErrorMatcher()
        if 'error_msg' in d:
            o.error_msg = d['error_msg']
        if 'matcher' in d:
            o.matcher = d['matcher']
        return o


