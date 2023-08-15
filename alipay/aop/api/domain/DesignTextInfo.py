#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TextGroup import TextGroup


class DesignTextInfo(object):

    def __init__(self):
        self._design_id = None
        self._text_group = None

    @property
    def design_id(self):
        return self._design_id

    @design_id.setter
    def design_id(self, value):
        self._design_id = value
    @property
    def text_group(self):
        return self._text_group

    @text_group.setter
    def text_group(self, value):
        if isinstance(value, TextGroup):
            self._text_group = value
        else:
            self._text_group = TextGroup.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.design_id:
            if hasattr(self.design_id, 'to_alipay_dict'):
                params['design_id'] = self.design_id.to_alipay_dict()
            else:
                params['design_id'] = self.design_id
        if self.text_group:
            if hasattr(self.text_group, 'to_alipay_dict'):
                params['text_group'] = self.text_group.to_alipay_dict()
            else:
                params['text_group'] = self.text_group
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DesignTextInfo()
        if 'design_id' in d:
            o.design_id = d['design_id']
        if 'text_group' in d:
            o.text_group = d['text_group']
        return o


