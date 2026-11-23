#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EvalInfo import EvalInfo


class AlipayOpenSpSkillAuditSubmitModel(object):

    def __init__(self):
        self._ability_code = None
        self._eval_info = None

    @property
    def ability_code(self):
        return self._ability_code

    @ability_code.setter
    def ability_code(self, value):
        self._ability_code = value
    @property
    def eval_info(self):
        return self._eval_info

    @eval_info.setter
    def eval_info(self, value):
        if isinstance(value, EvalInfo):
            self._eval_info = value
        else:
            self._eval_info = EvalInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.ability_code:
            if hasattr(self.ability_code, 'to_alipay_dict'):
                params['ability_code'] = self.ability_code.to_alipay_dict()
            else:
                params['ability_code'] = self.ability_code
        if self.eval_info:
            if hasattr(self.eval_info, 'to_alipay_dict'):
                params['eval_info'] = self.eval_info.to_alipay_dict()
            else:
                params['eval_info'] = self.eval_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenSpSkillAuditSubmitModel()
        if 'ability_code' in d:
            o.ability_code = d['ability_code']
        if 'eval_info' in d:
            o.eval_info = d['eval_info']
        return o


