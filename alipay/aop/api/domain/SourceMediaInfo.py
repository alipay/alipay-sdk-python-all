#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SourceMediaInfo(object):

    def __init__(self):
        self._media_id = None
        self._media_type = None

    @property
    def media_id(self):
        return self._media_id

    @media_id.setter
    def media_id(self, value):
        self._media_id = value
    @property
    def media_type(self):
        return self._media_type

    @media_type.setter
    def media_type(self, value):
        self._media_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.media_id:
            if hasattr(self.media_id, 'to_alipay_dict'):
                params['media_id'] = self.media_id.to_alipay_dict()
            else:
                params['media_id'] = self.media_id
        if self.media_type:
            if hasattr(self.media_type, 'to_alipay_dict'):
                params['media_type'] = self.media_type.to_alipay_dict()
            else:
                params['media_type'] = self.media_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SourceMediaInfo()
        if 'media_id' in d:
            o.media_id = d['media_id']
        if 'media_type' in d:
            o.media_type = d['media_type']
        return o


