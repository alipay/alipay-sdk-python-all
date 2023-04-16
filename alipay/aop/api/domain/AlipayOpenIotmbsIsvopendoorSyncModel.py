#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenIotmbsIsvopendoorSyncModel(object):

    def __init__(self):
        self._face_id = None
        self._project_id = None
        self._room_num = None
        self._sn = None

    @property
    def face_id(self):
        return self._face_id

    @face_id.setter
    def face_id(self, value):
        self._face_id = value
    @property
    def project_id(self):
        return self._project_id

    @project_id.setter
    def project_id(self, value):
        self._project_id = value
    @property
    def room_num(self):
        return self._room_num

    @room_num.setter
    def room_num(self, value):
        self._room_num = value
    @property
    def sn(self):
        return self._sn

    @sn.setter
    def sn(self, value):
        self._sn = value


    def to_alipay_dict(self):
        params = dict()
        if self.face_id:
            if hasattr(self.face_id, 'to_alipay_dict'):
                params['face_id'] = self.face_id.to_alipay_dict()
            else:
                params['face_id'] = self.face_id
        if self.project_id:
            if hasattr(self.project_id, 'to_alipay_dict'):
                params['project_id'] = self.project_id.to_alipay_dict()
            else:
                params['project_id'] = self.project_id
        if self.room_num:
            if hasattr(self.room_num, 'to_alipay_dict'):
                params['room_num'] = self.room_num.to_alipay_dict()
            else:
                params['room_num'] = self.room_num
        if self.sn:
            if hasattr(self.sn, 'to_alipay_dict'):
                params['sn'] = self.sn.to_alipay_dict()
            else:
                params['sn'] = self.sn
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenIotmbsIsvopendoorSyncModel()
        if 'face_id' in d:
            o.face_id = d['face_id']
        if 'project_id' in d:
            o.project_id = d['project_id']
        if 'room_num' in d:
            o.room_num = d['room_num']
        if 'sn' in d:
            o.sn = d['sn']
        return o


