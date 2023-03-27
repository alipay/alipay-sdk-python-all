#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DeliveryFatigueContent import DeliveryFatigueContent
from alipay.aop.api.domain.CreativityFatigue import CreativityFatigue


class DeliveryFatigue(object):

    def __init__(self):
        self._action = None
        self._content_fatigue = None
        self._creativity_fatigue = None
        self._position_code = None
        self._scm = None

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, value):
        self._action = value
    @property
    def content_fatigue(self):
        return self._content_fatigue

    @content_fatigue.setter
    def content_fatigue(self, value):
        if isinstance(value, DeliveryFatigueContent):
            self._content_fatigue = value
        else:
            self._content_fatigue = DeliveryFatigueContent.from_alipay_dict(value)
    @property
    def creativity_fatigue(self):
        return self._creativity_fatigue

    @creativity_fatigue.setter
    def creativity_fatigue(self, value):
        if isinstance(value, CreativityFatigue):
            self._creativity_fatigue = value
        else:
            self._creativity_fatigue = CreativityFatigue.from_alipay_dict(value)
    @property
    def position_code(self):
        return self._position_code

    @position_code.setter
    def position_code(self, value):
        self._position_code = value
    @property
    def scm(self):
        return self._scm

    @scm.setter
    def scm(self, value):
        self._scm = value


    def to_alipay_dict(self):
        params = dict()
        if self.action:
            if hasattr(self.action, 'to_alipay_dict'):
                params['action'] = self.action.to_alipay_dict()
            else:
                params['action'] = self.action
        if self.content_fatigue:
            if hasattr(self.content_fatigue, 'to_alipay_dict'):
                params['content_fatigue'] = self.content_fatigue.to_alipay_dict()
            else:
                params['content_fatigue'] = self.content_fatigue
        if self.creativity_fatigue:
            if hasattr(self.creativity_fatigue, 'to_alipay_dict'):
                params['creativity_fatigue'] = self.creativity_fatigue.to_alipay_dict()
            else:
                params['creativity_fatigue'] = self.creativity_fatigue
        if self.position_code:
            if hasattr(self.position_code, 'to_alipay_dict'):
                params['position_code'] = self.position_code.to_alipay_dict()
            else:
                params['position_code'] = self.position_code
        if self.scm:
            if hasattr(self.scm, 'to_alipay_dict'):
                params['scm'] = self.scm.to_alipay_dict()
            else:
                params['scm'] = self.scm
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DeliveryFatigue()
        if 'action' in d:
            o.action = d['action']
        if 'content_fatigue' in d:
            o.content_fatigue = d['content_fatigue']
        if 'creativity_fatigue' in d:
            o.creativity_fatigue = d['creativity_fatigue']
        if 'position_code' in d:
            o.position_code = d['position_code']
        if 'scm' in d:
            o.scm = d['scm']
        return o


