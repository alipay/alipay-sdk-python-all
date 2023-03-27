#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntLinkeAlcollectioncenterPreviewurlQueryModel(object):

    def __init__(self):
        self._affair_id = None

    @property
    def affair_id(self):
        return self._affair_id

    @affair_id.setter
    def affair_id(self, value):
        self._affair_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.affair_id:
            if hasattr(self.affair_id, 'to_alipay_dict'):
                params['affair_id'] = self.affair_id.to_alipay_dict()
            else:
                params['affair_id'] = self.affair_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntLinkeAlcollectioncenterPreviewurlQueryModel()
        if 'affair_id' in d:
            o.affair_id = d['affair_id']
        return o


