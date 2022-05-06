#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PetMarkIdDTO(object):

    def __init__(self):
        self._encryption_mark_id = None
        self._mark_id = None

    @property
    def encryption_mark_id(self):
        return self._encryption_mark_id

    @encryption_mark_id.setter
    def encryption_mark_id(self, value):
        self._encryption_mark_id = value
    @property
    def mark_id(self):
        return self._mark_id

    @mark_id.setter
    def mark_id(self, value):
        self._mark_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.encryption_mark_id:
            if hasattr(self.encryption_mark_id, 'to_alipay_dict'):
                params['encryption_mark_id'] = self.encryption_mark_id.to_alipay_dict()
            else:
                params['encryption_mark_id'] = self.encryption_mark_id
        if self.mark_id:
            if hasattr(self.mark_id, 'to_alipay_dict'):
                params['mark_id'] = self.mark_id.to_alipay_dict()
            else:
                params['mark_id'] = self.mark_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PetMarkIdDTO()
        if 'encryption_mark_id' in d:
            o.encryption_mark_id = d['encryption_mark_id']
        if 'mark_id' in d:
            o.mark_id = d['mark_id']
        return o


