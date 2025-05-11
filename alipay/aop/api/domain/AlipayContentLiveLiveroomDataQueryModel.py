#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayContentLiveLiveroomDataQueryModel(object):

    def __init__(self):
        self._encrypted_live_id = None

    @property
    def encrypted_live_id(self):
        return self._encrypted_live_id

    @encrypted_live_id.setter
    def encrypted_live_id(self, value):
        self._encrypted_live_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.encrypted_live_id:
            if hasattr(self.encrypted_live_id, 'to_alipay_dict'):
                params['encrypted_live_id'] = self.encrypted_live_id.to_alipay_dict()
            else:
                params['encrypted_live_id'] = self.encrypted_live_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayContentLiveLiveroomDataQueryModel()
        if 'encrypted_live_id' in d:
            o.encrypted_live_id = d['encrypted_live_id']
        return o


