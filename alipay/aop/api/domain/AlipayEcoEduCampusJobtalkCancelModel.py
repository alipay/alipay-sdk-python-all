#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoEduCampusJobtalkCancelModel(object):

    def __init__(self):
        self._content_var = None
        self._talk_source_code = None
        self._talk_source_id = None

    @property
    def content_var(self):
        return self._content_var

    @content_var.setter
    def content_var(self, value):
        self._content_var = value
    @property
    def talk_source_code(self):
        return self._talk_source_code

    @talk_source_code.setter
    def talk_source_code(self, value):
        self._talk_source_code = value
    @property
    def talk_source_id(self):
        return self._talk_source_id

    @talk_source_id.setter
    def talk_source_id(self, value):
        self._talk_source_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.content_var:
            if hasattr(self.content_var, 'to_alipay_dict'):
                params['content_var'] = self.content_var.to_alipay_dict()
            else:
                params['content_var'] = self.content_var
        if self.talk_source_code:
            if hasattr(self.talk_source_code, 'to_alipay_dict'):
                params['talk_source_code'] = self.talk_source_code.to_alipay_dict()
            else:
                params['talk_source_code'] = self.talk_source_code
        if self.talk_source_id:
            if hasattr(self.talk_source_id, 'to_alipay_dict'):
                params['talk_source_id'] = self.talk_source_id.to_alipay_dict()
            else:
                params['talk_source_id'] = self.talk_source_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoEduCampusJobtalkCancelModel()
        if 'content_var' in d:
            o.content_var = d['content_var']
        if 'talk_source_code' in d:
            o.talk_source_code = d['talk_source_code']
        if 'talk_source_id' in d:
            o.talk_source_id = d['talk_source_id']
        return o


