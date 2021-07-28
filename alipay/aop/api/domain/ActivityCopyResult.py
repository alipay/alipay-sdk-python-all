#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ActivityCopyResult(object):

    def __init__(self):
        self._copy_content = None
        self._error_msg = None
        self._result = None

    @property
    def copy_content(self):
        return self._copy_content

    @copy_content.setter
    def copy_content(self, value):
        self._copy_content = value
    @property
    def error_msg(self):
        return self._error_msg

    @error_msg.setter
    def error_msg(self, value):
        self._error_msg = value
    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        self._result = value


    def to_alipay_dict(self):
        params = dict()
        if self.copy_content:
            if hasattr(self.copy_content, 'to_alipay_dict'):
                params['copy_content'] = self.copy_content.to_alipay_dict()
            else:
                params['copy_content'] = self.copy_content
        if self.error_msg:
            if hasattr(self.error_msg, 'to_alipay_dict'):
                params['error_msg'] = self.error_msg.to_alipay_dict()
            else:
                params['error_msg'] = self.error_msg
        if self.result:
            if hasattr(self.result, 'to_alipay_dict'):
                params['result'] = self.result.to_alipay_dict()
            else:
                params['result'] = self.result
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ActivityCopyResult()
        if 'copy_content' in d:
            o.copy_content = d['copy_content']
        if 'error_msg' in d:
            o.error_msg = d['error_msg']
        if 'result' in d:
            o.result = d['result']
        return o


