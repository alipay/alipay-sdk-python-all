#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayPassTemplateUpdateModel(object):

    def __init__(self):
        self._tpl_content = None
        self._tpl_id = None

    @property
    def tpl_content(self):
        return self._tpl_content

    @tpl_content.setter
    def tpl_content(self, value):
        self._tpl_content = value
    @property
    def tpl_id(self):
        return self._tpl_id

    @tpl_id.setter
    def tpl_id(self, value):
        self._tpl_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.tpl_content:
            if hasattr(self.tpl_content, 'to_alipay_dict'):
                params['tpl_content'] = self.tpl_content.to_alipay_dict()
            else:
                params['tpl_content'] = self.tpl_content
        if self.tpl_id:
            if hasattr(self.tpl_id, 'to_alipay_dict'):
                params['tpl_id'] = self.tpl_id.to_alipay_dict()
            else:
                params['tpl_id'] = self.tpl_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayPassTemplateUpdateModel()
        if 'tpl_content' in d:
            o.tpl_content = d['tpl_content']
        if 'tpl_id' in d:
            o.tpl_id = d['tpl_id']
        return o


