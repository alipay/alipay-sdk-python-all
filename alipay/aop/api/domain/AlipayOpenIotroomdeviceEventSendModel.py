#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenIotroomdeviceEventSendModel(object):

    def __init__(self):
        self._biztid = None
        self._face_id = None

    @property
    def biztid(self):
        return self._biztid

    @biztid.setter
    def biztid(self, value):
        self._biztid = value
    @property
    def face_id(self):
        return self._face_id

    @face_id.setter
    def face_id(self, value):
        self._face_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biztid:
            if hasattr(self.biztid, 'to_alipay_dict'):
                params['biztid'] = self.biztid.to_alipay_dict()
            else:
                params['biztid'] = self.biztid
        if self.face_id:
            if hasattr(self.face_id, 'to_alipay_dict'):
                params['face_id'] = self.face_id.to_alipay_dict()
            else:
                params['face_id'] = self.face_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenIotroomdeviceEventSendModel()
        if 'biztid' in d:
            o.biztid = d['biztid']
        if 'face_id' in d:
            o.face_id = d['face_id']
        return o


