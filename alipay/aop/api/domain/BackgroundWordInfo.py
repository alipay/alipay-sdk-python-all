#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BackgroundWordInfo(object):

    def __init__(self):
        self._background_word = None
        self._fail_reason = None
        self._status = None

    @property
    def background_word(self):
        return self._background_word

    @background_word.setter
    def background_word(self, value):
        self._background_word = value
    @property
    def fail_reason(self):
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, value):
        self._fail_reason = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.background_word:
            if hasattr(self.background_word, 'to_alipay_dict'):
                params['background_word'] = self.background_word.to_alipay_dict()
            else:
                params['background_word'] = self.background_word
        if self.fail_reason:
            if hasattr(self.fail_reason, 'to_alipay_dict'):
                params['fail_reason'] = self.fail_reason.to_alipay_dict()
            else:
                params['fail_reason'] = self.fail_reason
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BackgroundWordInfo()
        if 'background_word' in d:
            o.background_word = d['background_word']
        if 'fail_reason' in d:
            o.fail_reason = d['fail_reason']
        if 'status' in d:
            o.status = d['status']
        return o


