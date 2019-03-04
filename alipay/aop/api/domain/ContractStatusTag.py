#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ContractStatusTag(object):

    def __init__(self):
        self._tag_code = None
        self._tag_desc = None
        self._tag_view = None

    @property
    def tag_code(self):
        return self._tag_code

    @tag_code.setter
    def tag_code(self, value):
        self._tag_code = value
    @property
    def tag_desc(self):
        return self._tag_desc

    @tag_desc.setter
    def tag_desc(self, value):
        self._tag_desc = value
    @property
    def tag_view(self):
        return self._tag_view

    @tag_view.setter
    def tag_view(self, value):
        self._tag_view = value


    def to_alipay_dict(self):
        params = dict()
        if self.tag_code:
            if hasattr(self.tag_code, 'to_alipay_dict'):
                params['tag_code'] = self.tag_code.to_alipay_dict()
            else:
                params['tag_code'] = self.tag_code
        if self.tag_desc:
            if hasattr(self.tag_desc, 'to_alipay_dict'):
                params['tag_desc'] = self.tag_desc.to_alipay_dict()
            else:
                params['tag_desc'] = self.tag_desc
        if self.tag_view:
            if hasattr(self.tag_view, 'to_alipay_dict'):
                params['tag_view'] = self.tag_view.to_alipay_dict()
            else:
                params['tag_view'] = self.tag_view
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ContractStatusTag()
        if 'tag_code' in d:
            o.tag_code = d['tag_code']
        if 'tag_desc' in d:
            o.tag_desc = d['tag_desc']
        if 'tag_view' in d:
            o.tag_view = d['tag_view']
        return o


