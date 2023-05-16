#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BsPlanBrandInfo import BsPlanBrandInfo
from alipay.aop.api.domain.BsBrandPlanIntro import BsBrandPlanIntro
from alipay.aop.api.domain.BsPlanInviteConfig import BsPlanInviteConfig


class BsBrandPlanDetail(object):

    def __init__(self):
        self._brand_info = None
        self._intro = None
        self._invite_config = None
        self._plan_id = None
        self._solution_code = None

    @property
    def brand_info(self):
        return self._brand_info

    @brand_info.setter
    def brand_info(self, value):
        if isinstance(value, BsPlanBrandInfo):
            self._brand_info = value
        else:
            self._brand_info = BsPlanBrandInfo.from_alipay_dict(value)
    @property
    def intro(self):
        return self._intro

    @intro.setter
    def intro(self, value):
        if isinstance(value, BsBrandPlanIntro):
            self._intro = value
        else:
            self._intro = BsBrandPlanIntro.from_alipay_dict(value)
    @property
    def invite_config(self):
        return self._invite_config

    @invite_config.setter
    def invite_config(self, value):
        if isinstance(value, BsPlanInviteConfig):
            self._invite_config = value
        else:
            self._invite_config = BsPlanInviteConfig.from_alipay_dict(value)
    @property
    def plan_id(self):
        return self._plan_id

    @plan_id.setter
    def plan_id(self, value):
        self._plan_id = value
    @property
    def solution_code(self):
        return self._solution_code

    @solution_code.setter
    def solution_code(self, value):
        self._solution_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.brand_info:
            if hasattr(self.brand_info, 'to_alipay_dict'):
                params['brand_info'] = self.brand_info.to_alipay_dict()
            else:
                params['brand_info'] = self.brand_info
        if self.intro:
            if hasattr(self.intro, 'to_alipay_dict'):
                params['intro'] = self.intro.to_alipay_dict()
            else:
                params['intro'] = self.intro
        if self.invite_config:
            if hasattr(self.invite_config, 'to_alipay_dict'):
                params['invite_config'] = self.invite_config.to_alipay_dict()
            else:
                params['invite_config'] = self.invite_config
        if self.plan_id:
            if hasattr(self.plan_id, 'to_alipay_dict'):
                params['plan_id'] = self.plan_id.to_alipay_dict()
            else:
                params['plan_id'] = self.plan_id
        if self.solution_code:
            if hasattr(self.solution_code, 'to_alipay_dict'):
                params['solution_code'] = self.solution_code.to_alipay_dict()
            else:
                params['solution_code'] = self.solution_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BsBrandPlanDetail()
        if 'brand_info' in d:
            o.brand_info = d['brand_info']
        if 'intro' in d:
            o.intro = d['intro']
        if 'invite_config' in d:
            o.invite_config = d['invite_config']
        if 'plan_id' in d:
            o.plan_id = d['plan_id']
        if 'solution_code' in d:
            o.solution_code = d['solution_code']
        return o


