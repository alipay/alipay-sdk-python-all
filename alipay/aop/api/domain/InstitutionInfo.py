#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InstitutionInfo(object):

    def __init__(self):
        self._face_in_time = None
        self._id = None

    @property
    def face_in_time(self):
        return self._face_in_time

    @face_in_time.setter
    def face_in_time(self, value):
        self._face_in_time = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value


    def to_alipay_dict(self):
        params = dict()
        if self.face_in_time:
            if hasattr(self.face_in_time, 'to_alipay_dict'):
                params['face_in_time'] = self.face_in_time.to_alipay_dict()
            else:
                params['face_in_time'] = self.face_in_time
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InstitutionInfo()
        if 'face_in_time' in d:
            o.face_in_time = d['face_in_time']
        if 'id' in d:
            o.id = d['id']
        return o


