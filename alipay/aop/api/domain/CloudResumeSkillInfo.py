#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CloudResumeSkillInfo(object):

    def __init__(self):
        self._skill_name = None

    @property
    def skill_name(self):
        return self._skill_name

    @skill_name.setter
    def skill_name(self, value):
        self._skill_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.skill_name:
            if hasattr(self.skill_name, 'to_alipay_dict'):
                params['skill_name'] = self.skill_name.to_alipay_dict()
            else:
                params['skill_name'] = self.skill_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CloudResumeSkillInfo()
        if 'skill_name' in d:
            o.skill_name = d['skill_name']
        return o


