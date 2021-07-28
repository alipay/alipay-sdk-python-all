#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ScenicFaceInfo(object):

    def __init__(self):
        self._face_id = None
        self._zid = None

    @property
    def face_id(self):
        return self._face_id

    @face_id.setter
    def face_id(self, value):
        self._face_id = value
    @property
    def zid(self):
        return self._zid

    @zid.setter
    def zid(self, value):
        self._zid = value


    def to_alipay_dict(self):
        params = dict()
        if self.face_id:
            if hasattr(self.face_id, 'to_alipay_dict'):
                params['face_id'] = self.face_id.to_alipay_dict()
            else:
                params['face_id'] = self.face_id
        if self.zid:
            if hasattr(self.zid, 'to_alipay_dict'):
                params['zid'] = self.zid.to_alipay_dict()
            else:
                params['zid'] = self.zid
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ScenicFaceInfo()
        if 'face_id' in d:
            o.face_id = d['face_id']
        if 'zid' in d:
            o.zid = d['zid']
        return o


