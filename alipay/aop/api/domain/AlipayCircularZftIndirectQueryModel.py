#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCircularZftIndirectQueryModel(object):

    def __init__(self):
        self._binding_alipay_logon_id = None
        self._relation_openid = None
        self._relation_uid = None
        self._scene_code = None

    @property
    def binding_alipay_logon_id(self):
        return self._binding_alipay_logon_id

    @binding_alipay_logon_id.setter
    def binding_alipay_logon_id(self, value):
        self._binding_alipay_logon_id = value
    @property
    def relation_openid(self):
        return self._relation_openid

    @relation_openid.setter
    def relation_openid(self, value):
        self._relation_openid = value
    @property
    def relation_uid(self):
        return self._relation_uid

    @relation_uid.setter
    def relation_uid(self, value):
        self._relation_uid = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.binding_alipay_logon_id:
            if hasattr(self.binding_alipay_logon_id, 'to_alipay_dict'):
                params['binding_alipay_logon_id'] = self.binding_alipay_logon_id.to_alipay_dict()
            else:
                params['binding_alipay_logon_id'] = self.binding_alipay_logon_id
        if self.relation_openid:
            if hasattr(self.relation_openid, 'to_alipay_dict'):
                params['relation_openid'] = self.relation_openid.to_alipay_dict()
            else:
                params['relation_openid'] = self.relation_openid
        if self.relation_uid:
            if hasattr(self.relation_uid, 'to_alipay_dict'):
                params['relation_uid'] = self.relation_uid.to_alipay_dict()
            else:
                params['relation_uid'] = self.relation_uid
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCircularZftIndirectQueryModel()
        if 'binding_alipay_logon_id' in d:
            o.binding_alipay_logon_id = d['binding_alipay_logon_id']
        if 'relation_openid' in d:
            o.relation_openid = d['relation_openid']
        if 'relation_uid' in d:
            o.relation_uid = d['relation_uid']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        return o


