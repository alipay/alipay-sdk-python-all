#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Template import Template


class AlipayOpenPublicMessageSingleSendModel(object):

    def __init__(self):
        self._template = None
        self._to_user_id = None

    @property
    def template(self):
        return self._template

    @template.setter
    def template(self, value):
        if isinstance(value, Template):
            self._template = value
        else:
            self._template = Template.from_alipay_dict(value)
    @property
    def to_user_id(self):
        return self._to_user_id

    @to_user_id.setter
    def to_user_id(self, value):
        self._to_user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.template:
            if hasattr(self.template, 'to_alipay_dict'):
                params['template'] = self.template.to_alipay_dict()
            else:
                params['template'] = self.template
        if self.to_user_id:
            if hasattr(self.to_user_id, 'to_alipay_dict'):
                params['to_user_id'] = self.to_user_id.to_alipay_dict()
            else:
                params['to_user_id'] = self.to_user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenPublicMessageSingleSendModel()
        if 'template' in d:
            o.template = d['template']
        if 'to_user_id' in d:
            o.to_user_id = d['to_user_id']
        return o


