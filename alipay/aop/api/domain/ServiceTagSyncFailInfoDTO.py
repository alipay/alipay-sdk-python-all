#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ServiceTagSyncFailInfoDTO(object):

    def __init__(self):
        self._desc = None
        self._tag_code = None

    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def tag_code(self):
        return self._tag_code

    @tag_code.setter
    def tag_code(self, value):
        self._tag_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.desc:
            if hasattr(self.desc, 'to_alipay_dict'):
                params['desc'] = self.desc.to_alipay_dict()
            else:
                params['desc'] = self.desc
        if self.tag_code:
            if hasattr(self.tag_code, 'to_alipay_dict'):
                params['tag_code'] = self.tag_code.to_alipay_dict()
            else:
                params['tag_code'] = self.tag_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ServiceTagSyncFailInfoDTO()
        if 'desc' in d:
            o.desc = d['desc']
        if 'tag_code' in d:
            o.tag_code = d['tag_code']
        return o


