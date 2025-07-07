#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RecycleOptionConstraint import RecycleOptionConstraint
from alipay.aop.api.domain.RecycleQuetion import RecycleQuetion


class AlipayCommerceRecycleQuestionQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceRecycleQuestionQueryResponse, self).__init__()
        self._option_constraint_relations = None
        self._questions = None

    @property
    def option_constraint_relations(self):
        return self._option_constraint_relations

    @option_constraint_relations.setter
    def option_constraint_relations(self, value):
        if isinstance(value, list):
            self._option_constraint_relations = list()
            for i in value:
                if isinstance(i, RecycleOptionConstraint):
                    self._option_constraint_relations.append(i)
                else:
                    self._option_constraint_relations.append(RecycleOptionConstraint.from_alipay_dict(i))
    @property
    def questions(self):
        return self._questions

    @questions.setter
    def questions(self, value):
        if isinstance(value, list):
            self._questions = list()
            for i in value:
                if isinstance(i, RecycleQuetion):
                    self._questions.append(i)
                else:
                    self._questions.append(RecycleQuetion.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceRecycleQuestionQueryResponse, self).parse_response_content(response_content)
        if 'option_constraint_relations' in response:
            self.option_constraint_relations = response['option_constraint_relations']
        if 'questions' in response:
            self.questions = response['questions']
