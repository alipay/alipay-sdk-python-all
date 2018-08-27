#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEcoEduCampusJobstudentApplyModel(object):

    def __init__(self):
        self._alipay_user_id = None
        self._content_var = None

    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def content_var(self):
        return self._content_var

    @content_var.setter
    def content_var(self, value):
        self._content_var = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.content_var:
            if hasattr(self.content_var, 'to_alipay_dict'):
                params['content_var'] = self.content_var.to_alipay_dict()
            else:
                params['content_var'] = self.content_var
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoEduCampusJobstudentApplyModel()
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'content_var' in d:
            o.content_var = d['content_var']
        return o


