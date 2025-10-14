#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ZftContactInfo import ZftContactInfo
from alipay.aop.api.domain.ZftDefaultSettleRule import ZftDefaultSettleRule


class AlipayCircularZftIndirectCreateModel(object):

    def __init__(self):
        self._binding_alipay_logon_id = None
        self._contact_info = None
        self._default_settle_rule = None
        self._scene_code = None

    @property
    def binding_alipay_logon_id(self):
        return self._binding_alipay_logon_id

    @binding_alipay_logon_id.setter
    def binding_alipay_logon_id(self, value):
        self._binding_alipay_logon_id = value
    @property
    def contact_info(self):
        return self._contact_info

    @contact_info.setter
    def contact_info(self, value):
        if isinstance(value, ZftContactInfo):
            self._contact_info = value
        else:
            self._contact_info = ZftContactInfo.from_alipay_dict(value)
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
        if self.contact_info:
            if hasattr(self.contact_info, 'to_alipay_dict'):
                params['contact_info'] = self.contact_info.to_alipay_dict()
            else:
                params['contact_info'] = self.contact_info
        if self.default_settle_rule:
            if hasattr(self.default_settle_rule, 'to_alipay_dict'):
                params['default_settle_rule'] = self.default_settle_rule.to_alipay_dict()
            else:
                params['default_settle_rule'] = self.default_settle_rule
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
        o = AlipayCircularZftIndirectCreateModel()
        if 'binding_alipay_logon_id' in d:
            o.binding_alipay_logon_id = d['binding_alipay_logon_id']
        if 'contact_info' in d:
            o.contact_info = d['contact_info']
        if 'default_settle_rule' in d:
            o.default_settle_rule = d['default_settle_rule']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        return o


