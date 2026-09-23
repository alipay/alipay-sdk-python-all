#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CompetencyDetails(object):

    def __init__(self):
        self._competency_item = None
        self._competency_level_tag = None
        self._competency_summary = None
        self._competency_weight = None
        self._question_count = None
        self._score = None

    @property
    def competency_item(self):
        return self._competency_item

    @competency_item.setter
    def competency_item(self, value):
        self._competency_item = value
    @property
    def competency_level_tag(self):
        return self._competency_level_tag

    @competency_level_tag.setter
    def competency_level_tag(self, value):
        self._competency_level_tag = value
    @property
    def competency_summary(self):
        return self._competency_summary

    @competency_summary.setter
    def competency_summary(self, value):
        self._competency_summary = value
    @property
    def competency_weight(self):
        return self._competency_weight

    @competency_weight.setter
    def competency_weight(self, value):
        self._competency_weight = value
    @property
    def question_count(self):
        return self._question_count

    @question_count.setter
    def question_count(self, value):
        self._question_count = value
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = value


    def to_alipay_dict(self):
        params = dict()
        if self.competency_item:
            if hasattr(self.competency_item, 'to_alipay_dict'):
                params['competency_item'] = self.competency_item.to_alipay_dict()
            else:
                params['competency_item'] = self.competency_item
        if self.competency_level_tag:
            if hasattr(self.competency_level_tag, 'to_alipay_dict'):
                params['competency_level_tag'] = self.competency_level_tag.to_alipay_dict()
            else:
                params['competency_level_tag'] = self.competency_level_tag
        if self.competency_summary:
            if hasattr(self.competency_summary, 'to_alipay_dict'):
                params['competency_summary'] = self.competency_summary.to_alipay_dict()
            else:
                params['competency_summary'] = self.competency_summary
        if self.competency_weight:
            if hasattr(self.competency_weight, 'to_alipay_dict'):
                params['competency_weight'] = self.competency_weight.to_alipay_dict()
            else:
                params['competency_weight'] = self.competency_weight
        if self.question_count:
            if hasattr(self.question_count, 'to_alipay_dict'):
                params['question_count'] = self.question_count.to_alipay_dict()
            else:
                params['question_count'] = self.question_count
        if self.score:
            if hasattr(self.score, 'to_alipay_dict'):
                params['score'] = self.score.to_alipay_dict()
            else:
                params['score'] = self.score
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CompetencyDetails()
        if 'competency_item' in d:
            o.competency_item = d['competency_item']
        if 'competency_level_tag' in d:
            o.competency_level_tag = d['competency_level_tag']
        if 'competency_summary' in d:
            o.competency_summary = d['competency_summary']
        if 'competency_weight' in d:
            o.competency_weight = d['competency_weight']
        if 'question_count' in d:
            o.question_count = d['question_count']
        if 'score' in d:
            o.score = d['score']
        return o


