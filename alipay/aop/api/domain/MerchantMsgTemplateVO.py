#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MsgFatigueVO import MsgFatigueVO


class MerchantMsgTemplateVO(object):

    def __init__(self):
        self._delivery_settings = None
        self._fatigue = None
        self._keyword_desc = None
        self._name = None
        self._scene_rule = None
        self._status = None
        self._template_id = None

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
    def scene_rule(self):
        return self._scene_rule

    @scene_rule.setter
    def scene_rule(self, value):
        self._scene_rule = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.scene_rule:
            if hasattr(self.scene_rule, 'to_alipay_dict'):
                params['scene_rule'] = self.scene_rule.to_alipay_dict()
            else:
                params['scene_rule'] = self.scene_rule
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.template_id:
            if hasattr(self.template_id, 'to_alipay_dict'):
                params['template_id'] = self.template_id.to_alipay_dict()
            else:
                params['template_id'] = self.template_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MerchantMsgTemplateVO()
        if 'delivery_settings' in d:
            o.delivery_settings = d['delivery_settings']
        if 'fatigue' in d:
            o.fatigue = d['fatigue']
        if 'keyword_desc' in d:
            o.keyword_desc = d['keyword_desc']
        if 'name' in d:
            o.name = d['name']
        if 'scene_rule' in d:
            o.scene_rule = d['scene_rule']
        if 'status' in d:
            o.status = d['status']
        if 'template_id' in d:
            o.template_id = d['template_id']
        return o


