#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TemplateRemindDTO(object):

    def __init__(self):
        self._offset = None

    @property
    def offset(self):
        return self._offset

    @offset.setter
    def offset(self, value):
        self._offset = value


    def to_alipay_dict(self):
        params = dict()
        if self.offset:
            if hasattr(self.offset, 'to_alipay_dict'):
                params['offset'] = self.offset.to_alipay_dict()
            else:
                params['offset'] = self.offset
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TemplateRemindDTO()
        if 'offset' in d:
            o.offset = d['offset']
        return o


