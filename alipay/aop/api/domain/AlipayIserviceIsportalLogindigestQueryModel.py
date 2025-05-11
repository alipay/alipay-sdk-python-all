#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayIserviceIsportalLogindigestQueryModel(object):

    def __init__(self):
        self._ur_id = None

    @property
    def ur_id(self):
        return self._ur_id

    @ur_id.setter
    def ur_id(self, value):
        self._ur_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.ur_id:
            if hasattr(self.ur_id, 'to_alipay_dict'):
                params['ur_id'] = self.ur_id.to_alipay_dict()
            else:
                params['ur_id'] = self.ur_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayIserviceIsportalLogindigestQueryModel()
        if 'ur_id' in d:
            o.ur_id = d['ur_id']
        return o


