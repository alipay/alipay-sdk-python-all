#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MsgFatigueVO import MsgFatigueVO
from alipay.aop.api.domain.AccessFailReasonVO import AccessFailReasonVO


class MerchantMsgTemplateLibVO(object):

    def __init__(self):
        self._code = None
        self._delivery_settings = None
        self._fatigue = None
        self._has_push = None
        self._industry_code = None
        self._industry_scenario = None
        self._keyword_desc = None
        self._name = None
        self._not_selectable_reason = None
        self._scene_rule = None
        self._selectable = None
        self._status = None

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def delivery_settings(self):
        return self._delivery_settings

    @delivery_settings.setter
    def delivery_settings(self, value):
        self._delivery_settings = value
    @property
    def fatigue(self):
        return self._fatigue

    @fatigue.setter
    def fatigue(self, value):
        if isinstance(value, MsgFatigueVO):
            self._fatigue = value
        else:
            self._fatigue = MsgFatigueVO.from_alipay_dict(value)
    @property
    def has_push(self):
        return self._has_push

    @has_push.setter
    def has_push(self, value):
        self._has_push = value
    @property
    def industry_code(self):
        return self._industry_code

    @industry_code.setter
    def industry_code(self, value):
        self._industry_code = value
    @property
    def industry_scenario(self):
        return self._industry_scenario

    @industry_scenario.setter
    def industry_scenario(self, value):
        self._industry_scenario = value
    @property
    def keyword_desc(self):
        return self._keyword_desc

    @keyword_desc.setter
    def keyword_desc(self, value):
        self._keyword_desc = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def not_selectable_reason(self):
        return self._not_selectable_reason

    @not_selectable_reason.setter
    def not_selectable_reason(self, value):
        if isinstance(value, AccessFailReasonVO):
            self._not_selectable_reason = value
        else:
            self._not_selectable_reason = AccessFailReasonVO.from_alipay_dict(value)
    @property
    def scene_rule(self):
        return self._scene_rule

    @scene_rule.setter
    def scene_rule(self, value):
        self._scene_rule = value
    @property
    def selectable(self):
        return self._selectable

    @selectable.setter
    def selectable(self, value):
        self._selectable = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.code:
            if hasattr(self.code, 'to_alipay_dict'):
                params['code'] = self.code.to_alipay_dict()
            else:
                params['code'] = self.code
        if self.delivery_settings:
            if hasattr(self.delivery_settings, 'to_alipay_dict'):
                params['delivery_settings'] = self.delivery_settings.to_alipay_dict()
            else:
                params['delivery_settings'] = self.delivery_settings
        if self.fatigue:
            if hasattr(self.fatigue, 'to_alipay_dict'):
                params['fatigue'] = self.fatigue.to_alipay_dict()
            else:
                params['fatigue'] = self.fatigue
        if self.has_push:
            if hasattr(self.has_push, 'to_alipay_dict'):
                params['has_push'] = self.has_push.to_alipay_dict()
            else:
                params['has_push'] = self.has_push
        if self.industry_code:
            if hasattr(self.industry_code, 'to_alipay_dict'):
                params['industry_code'] = self.industry_code.to_alipay_dict()
            else:
                params['industry_code'] = self.industry_code
        if self.industry_scenario:
            if hasattr(self.industry_scenario, 'to_alipay_dict'):
                params['industry_scenario'] = self.industry_scenario.to_alipay_dict()
            else:
                params['industry_scenario'] = self.industry_scenario
        if self.keyword_desc:
            if hasattr(self.keyword_desc, 'to_alipay_dict'):
                params['keyword_desc'] = self.keyword_desc.to_alipay_dict()
            else:
                params['keyword_desc'] = self.keyword_desc
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.not_selectable_reason:
            if hasattr(self.not_selectable_reason, 'to_alipay_dict'):
                params['not_selectable_reason'] = self.not_selectable_reason.to_alipay_dict()
            else:
                params['not_selectable_reason'] = self.not_selectable_reason
        if self.scene_rule:
            if hasattr(self.scene_rule, 'to_alipay_dict'):
                params['scene_rule'] = self.scene_rule.to_alipay_dict()
            else:
                params['scene_rule'] = self.scene_rule
        if self.selectable:
            if hasattr(self.selectable, 'to_alipay_dict'):
                params['selectable'] = self.selectable.to_alipay_dict()
            else:
                params['selectable'] = self.selectable
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MerchantMsgTemplateLibVO()
        if 'code' in d:
            o.code = d['code']
        if 'delivery_settings' in d:
            o.delivery_settings = d['delivery_settings']
        if 'fatigue' in d:
            o.fatigue = d['fatigue']
        if 'has_push' in d:
            o.has_push = d['has_push']
        if 'industry_code' in d:
            o.industry_code = d['industry_code']
        if 'industry_scenario' in d:
            o.industry_scenario = d['industry_scenario']
        if 'keyword_desc' in d:
            o.keyword_desc = d['keyword_desc']
        if 'name' in d:
            o.name = d['name']
        if 'not_selectable_reason' in d:
            o.not_selectable_reason = d['not_selectable_reason']
        if 'scene_rule' in d:
            o.scene_rule = d['scene_rule']
        if 'selectable' in d:
            o.selectable = d['selectable']
        if 'status' in d:
            o.status = d['status']
        return o


