#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SmartAutomatAssociate(object):

    def __init__(self):
        self._associate_type = None
        self._associate_user_id = None

    @property
    def associate_type(self):
        return self._associate_type

    @associate_type.setter
    def associate_type(self, value):
        self._associate_type = value
    @property
    def associate_user_id(self):
        return self._associate_user_id

    @associate_user_id.setter
    def associate_user_id(self, value):
        self._associate_user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.associate_type:
            if hasattr(self.associate_type, 'to_alipay_dict'):
                params['associate_type'] = self.associate_type.to_alipay_dict()
            else:
                params['associate_type'] = self.associate_type
        if self.associate_user_id:
            if hasattr(self.associate_user_id, 'to_alipay_dict'):
                params['associate_user_id'] = self.associate_user_id.to_alipay_dict()
            else:
                params['associate_user_id'] = self.associate_user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SmartAutomatAssociate()
        if 'associate_type' in d:
            o.associate_type = d['associate_type']
        if 'associate_user_id' in d:
            o.associate_user_id = d['associate_user_id']
        return o


