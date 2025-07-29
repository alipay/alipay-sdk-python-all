#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayContentLiveLiveroomCommentsbannedModifyModel(object):

    def __init__(self):
        self._alipay_live_id = None
        self._alipay_public_id = None
        self._operate_object_public_id = None
        self._operate_type = None

    @property
    def alipay_live_id(self):
        return self._alipay_live_id

    @alipay_live_id.setter
    def alipay_live_id(self, value):
        self._alipay_live_id = value
    @property
    def alipay_public_id(self):
        return self._alipay_public_id

    @alipay_public_id.setter
    def alipay_public_id(self, value):
        self._alipay_public_id = value
    @property
    def operate_object_public_id(self):
        return self._operate_object_public_id

    @operate_object_public_id.setter
    def operate_object_public_id(self, value):
        self._operate_object_public_id = value
    @property
    def operate_type(self):
        return self._operate_type

    @operate_type.setter
    def operate_type(self, value):
        self._operate_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_live_id:
            if hasattr(self.alipay_live_id, 'to_alipay_dict'):
                params['alipay_live_id'] = self.alipay_live_id.to_alipay_dict()
            else:
                params['alipay_live_id'] = self.alipay_live_id
        if self.alipay_public_id:
            if hasattr(self.alipay_public_id, 'to_alipay_dict'):
                params['alipay_public_id'] = self.alipay_public_id.to_alipay_dict()
            else:
                params['alipay_public_id'] = self.alipay_public_id
        if self.operate_object_public_id:
            if hasattr(self.operate_object_public_id, 'to_alipay_dict'):
                params['operate_object_public_id'] = self.operate_object_public_id.to_alipay_dict()
            else:
                params['operate_object_public_id'] = self.operate_object_public_id
        if self.operate_type:
            if hasattr(self.operate_type, 'to_alipay_dict'):
                params['operate_type'] = self.operate_type.to_alipay_dict()
            else:
                params['operate_type'] = self.operate_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayContentLiveLiveroomCommentsbannedModifyModel()
        if 'alipay_live_id' in d:
            o.alipay_live_id = d['alipay_live_id']
        if 'alipay_public_id' in d:
            o.alipay_public_id = d['alipay_public_id']
        if 'operate_object_public_id' in d:
            o.operate_object_public_id = d['operate_object_public_id']
        if 'operate_type' in d:
            o.operate_type = d['operate_type']
        return o


