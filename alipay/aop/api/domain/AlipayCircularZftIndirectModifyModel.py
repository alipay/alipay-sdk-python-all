#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ZftDefaultSettleRule import ZftDefaultSettleRule


class AlipayCircularZftIndirectModifyModel(object):

    def __init__(self):
        self._default_settle_rule = None
        self._relation_openid = None
        self._relation_uid = None
        self._scene_code = None

    @property
    def default_settle_rule(self):
        return self._default_settle_rule

    @default_settle_rule.setter
    def default_settle_rule(self, value):
        if isinstance(value, ZftDefaultSettleRule):
            self._default_settle_rule = value
        else:
            self._default_settle_rule = ZftDefaultSettleRule.from_alipay_dict(value)
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
        if self.default_settle_rule:
            if hasattr(self.default_settle_rule, 'to_alipay_dict'):
                params['default_settle_rule'] = self.default_settle_rule.to_alipay_dict()
            else:
                params['default_settle_rule'] = self.default_settle_rule
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
        o = AlipayCircularZftIndirectModifyModel()
        if 'default_settle_rule' in d:
            o.default_settle_rule = d['default_settle_rule']
        if 'relation_openid' in d:
            o.relation_openid = d['relation_openid']
        if 'relation_uid' in d:
            o.relation_uid = d['relation_uid']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        return o


