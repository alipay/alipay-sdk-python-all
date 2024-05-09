#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntfortuneFinresearchSessionHistoryQueryModel(object):

    def __init__(self):
        self._identity_id = None

    @property
    def identity_id(self):
        return self._identity_id

    @identity_id.setter
    def identity_id(self, value):
        self._identity_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.identity_id:
            if hasattr(self.identity_id, 'to_alipay_dict'):
                params['identity_id'] = self.identity_id.to_alipay_dict()
            else:
                params['identity_id'] = self.identity_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntfortuneFinresearchSessionHistoryQueryModel()
        if 'identity_id' in d:
            o.identity_id = d['identity_id']
        return o


