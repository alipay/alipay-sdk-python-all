#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCreditEpAssistantServicecardQueryModel(object):

    def __init__(self):
        self._ali_id = None

    @property
    def ali_id(self):
        return self._ali_id

    @ali_id.setter
    def ali_id(self, value):
        self._ali_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.ali_id:
            if hasattr(self.ali_id, 'to_alipay_dict'):
                params['ali_id'] = self.ali_id.to_alipay_dict()
            else:
                params['ali_id'] = self.ali_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCreditEpAssistantServicecardQueryModel()
        if 'ali_id' in d:
            o.ali_id = d['ali_id']
        return o


