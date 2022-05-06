#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class QueryProfileDTO(object):

    def __init__(self):
        self._has_profile = None
        self._mark_id = None

    @property
    def has_profile(self):
        return self._has_profile

    @has_profile.setter
    def has_profile(self, value):
        self._has_profile = value
    @property
    def mark_id(self):
        return self._mark_id

    @mark_id.setter
    def mark_id(self, value):
        self._mark_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.has_profile:
            if hasattr(self.has_profile, 'to_alipay_dict'):
                params['has_profile'] = self.has_profile.to_alipay_dict()
            else:
                params['has_profile'] = self.has_profile
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
        o = QueryProfileDTO()
        if 'has_profile' in d:
            o.has_profile = d['has_profile']
        if 'mark_id' in d:
            o.mark_id = d['mark_id']
        return o


