#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayPassTemplateAddModel(object):

    def __init__(self):
        self._tpl_content = None
        self._unique_id = None

    @property
    def tpl_content(self):
        return self._tpl_content

    @tpl_content.setter
    def tpl_content(self, value):
        self._tpl_content = value
    @property
    def unique_id(self):
        return self._unique_id

    @unique_id.setter
    def unique_id(self, value):
        self._unique_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.tpl_content:
            if hasattr(self.tpl_content, 'to_alipay_dict'):
                params['tpl_content'] = self.tpl_content.to_alipay_dict()
            else:
                params['tpl_content'] = self.tpl_content
        if self.unique_id:
            if hasattr(self.unique_id, 'to_alipay_dict'):
                params['unique_id'] = self.unique_id.to_alipay_dict()
            else:
                params['unique_id'] = self.unique_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayPassTemplateAddModel()
        if 'tpl_content' in d:
            o.tpl_content = d['tpl_content']
        if 'unique_id' in d:
            o.unique_id = d['unique_id']
        return o


