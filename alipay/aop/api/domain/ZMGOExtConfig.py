#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZMGOExtConfig(object):

    def __init__(self):
        self._text_content_fill_rule_id = None
        self._text_content_fill_variable = None

    @property
    def text_content_fill_rule_id(self):
        return self._text_content_fill_rule_id

    @text_content_fill_rule_id.setter
    def text_content_fill_rule_id(self, value):
        self._text_content_fill_rule_id = value
    @property
    def text_content_fill_variable(self):
        return self._text_content_fill_variable

    @text_content_fill_variable.setter
    def text_content_fill_variable(self, value):
        self._text_content_fill_variable = value


    def to_alipay_dict(self):
        params = dict()
        if self.text_content_fill_rule_id:
            if hasattr(self.text_content_fill_rule_id, 'to_alipay_dict'):
                params['text_content_fill_rule_id'] = self.text_content_fill_rule_id.to_alipay_dict()
            else:
                params['text_content_fill_rule_id'] = self.text_content_fill_rule_id
        if self.text_content_fill_variable:
            if hasattr(self.text_content_fill_variable, 'to_alipay_dict'):
                params['text_content_fill_variable'] = self.text_content_fill_variable.to_alipay_dict()
            else:
                params['text_content_fill_variable'] = self.text_content_fill_variable
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZMGOExtConfig()
        if 'text_content_fill_rule_id' in d:
            o.text_content_fill_rule_id = d['text_content_fill_rule_id']
        if 'text_content_fill_variable' in d:
            o.text_content_fill_variable = d['text_content_fill_variable']
        return o


