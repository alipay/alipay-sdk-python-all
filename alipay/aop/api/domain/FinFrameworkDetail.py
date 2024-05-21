#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FinFrameworkDetail(object):

    def __init__(self):
        self._code = None
        self._evaluation_standard = None
        self._expert_knowledge = None
        self._expression_requirements = None
        self._interpretation_thoughts = None
        self._introduction = None
        self._name = None
        self._plan = None
        self._sort = None

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
    @property
    def evaluation_standard(self):
        return self._evaluation_standard

    @evaluation_standard.setter
    def evaluation_standard(self, value):
        self._evaluation_standard = value
    @property
    def expert_knowledge(self):
        return self._expert_knowledge

    @expert_knowledge.setter
    def expert_knowledge(self, value):
        self._expert_knowledge = value
    @property
    def expression_requirements(self):
        return self._expression_requirements

    @expression_requirements.setter
    def expression_requirements(self, value):
        self._expression_requirements = value
    @property
    def interpretation_thoughts(self):
        return self._interpretation_thoughts

    @interpretation_thoughts.setter
    def interpretation_thoughts(self, value):
        self._interpretation_thoughts = value
    @property
    def introduction(self):
        return self._introduction

    @introduction.setter
    def introduction(self, value):
        self._introduction = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def plan(self):
        return self._plan

    @plan.setter
    def plan(self, value):
        self._plan = value
    @property
    def sort(self):
        return self._sort

    @sort.setter
    def sort(self, value):
        self._sort = value


    def to_alipay_dict(self):
        params = dict()
        if self.code:
            if hasattr(self.code, 'to_alipay_dict'):
                params['code'] = self.code.to_alipay_dict()
            else:
                params['code'] = self.code
        if self.evaluation_standard:
            if hasattr(self.evaluation_standard, 'to_alipay_dict'):
                params['evaluation_standard'] = self.evaluation_standard.to_alipay_dict()
            else:
                params['evaluation_standard'] = self.evaluation_standard
        if self.expert_knowledge:
            if hasattr(self.expert_knowledge, 'to_alipay_dict'):
                params['expert_knowledge'] = self.expert_knowledge.to_alipay_dict()
            else:
                params['expert_knowledge'] = self.expert_knowledge
        if self.expression_requirements:
            if hasattr(self.expression_requirements, 'to_alipay_dict'):
                params['expression_requirements'] = self.expression_requirements.to_alipay_dict()
            else:
                params['expression_requirements'] = self.expression_requirements
        if self.interpretation_thoughts:
            if hasattr(self.interpretation_thoughts, 'to_alipay_dict'):
                params['interpretation_thoughts'] = self.interpretation_thoughts.to_alipay_dict()
            else:
                params['interpretation_thoughts'] = self.interpretation_thoughts
        if self.introduction:
            if hasattr(self.introduction, 'to_alipay_dict'):
                params['introduction'] = self.introduction.to_alipay_dict()
            else:
                params['introduction'] = self.introduction
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.plan:
            if hasattr(self.plan, 'to_alipay_dict'):
                params['plan'] = self.plan.to_alipay_dict()
            else:
                params['plan'] = self.plan
        if self.sort:
            if hasattr(self.sort, 'to_alipay_dict'):
                params['sort'] = self.sort.to_alipay_dict()
            else:
                params['sort'] = self.sort
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FinFrameworkDetail()
        if 'code' in d:
            o.code = d['code']
        if 'evaluation_standard' in d:
            o.evaluation_standard = d['evaluation_standard']
        if 'expert_knowledge' in d:
            o.expert_knowledge = d['expert_knowledge']
        if 'expression_requirements' in d:
            o.expression_requirements = d['expression_requirements']
        if 'interpretation_thoughts' in d:
            o.interpretation_thoughts = d['interpretation_thoughts']
        if 'introduction' in d:
            o.introduction = d['introduction']
        if 'name' in d:
            o.name = d['name']
        if 'plan' in d:
            o.plan = d['plan']
        if 'sort' in d:
            o.sort = d['sort']
        return o


