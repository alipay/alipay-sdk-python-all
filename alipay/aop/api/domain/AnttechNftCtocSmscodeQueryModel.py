#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechNftCtocSmscodeQueryModel(object):

    def __init__(self):
        self._id_no = None
        self._id_type = None
        self._sms_biz_scene = None

    @property
    def id_no(self):
        return self._id_no

    @id_no.setter
    def id_no(self, value):
        self._id_no = value
    @property
    def id_type(self):
        return self._id_type

    @id_type.setter
    def id_type(self, value):
        self._id_type = value
    @property
    def sms_biz_scene(self):
        return self._sms_biz_scene

    @sms_biz_scene.setter
    def sms_biz_scene(self, value):
        self._sms_biz_scene = value


    def to_alipay_dict(self):
        params = dict()
        if self.id_no:
            if hasattr(self.id_no, 'to_alipay_dict'):
                params['id_no'] = self.id_no.to_alipay_dict()
            else:
                params['id_no'] = self.id_no
        if self.id_type:
            if hasattr(self.id_type, 'to_alipay_dict'):
                params['id_type'] = self.id_type.to_alipay_dict()
            else:
                params['id_type'] = self.id_type
        if self.sms_biz_scene:
            if hasattr(self.sms_biz_scene, 'to_alipay_dict'):
                params['sms_biz_scene'] = self.sms_biz_scene.to_alipay_dict()
            else:
                params['sms_biz_scene'] = self.sms_biz_scene
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechNftCtocSmscodeQueryModel()
        if 'id_no' in d:
            o.id_no = d['id_no']
        if 'id_type' in d:
            o.id_type = d['id_type']
        if 'sms_biz_scene' in d:
            o.sms_biz_scene = d['sms_biz_scene']
        return o


