#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySecurityProdFacerepoSearchModel(object):

    def __init__(self):
        self._biz_id = None
        self._face_str = None
        self._group_id = None

    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def face_str(self):
        return self._face_str

    @face_str.setter
    def face_str(self, value):
        self._face_str = value
    @property
    def group_id(self):
        return self._group_id

    @group_id.setter
    def group_id(self, value):
        self._group_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.face_str:
            if hasattr(self.face_str, 'to_alipay_dict'):
                params['face_str'] = self.face_str.to_alipay_dict()
            else:
                params['face_str'] = self.face_str
        if self.group_id:
            if hasattr(self.group_id, 'to_alipay_dict'):
                params['group_id'] = self.group_id.to_alipay_dict()
            else:
                params['group_id'] = self.group_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityProdFacerepoSearchModel()
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'face_str' in d:
            o.face_str = d['face_str']
        if 'group_id' in d:
            o.group_id = d['group_id']
        return o


