#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ComprehensiveEvaluation(object):

    def __init__(self):
        self._abnormal_tags = None
        self._elimination_rule_result = None
        self._interview_result = None
        self._interview_summary = None
        self._recommend_tag = None

    @property
    def abnormal_tags(self):
        return self._abnormal_tags

    @abnormal_tags.setter
    def abnormal_tags(self, value):
        if isinstance(value, list):
            self._abnormal_tags = list()
            for i in value:
                self._abnormal_tags.append(i)
    @property
    def elimination_rule_result(self):
        return self._elimination_rule_result

    @elimination_rule_result.setter
    def elimination_rule_result(self, value):
        self._elimination_rule_result = value
    @property
    def interview_result(self):
        return self._interview_result

    @interview_result.setter
    def interview_result(self, value):
        self._interview_result = value
    @property
    def interview_summary(self):
        return self._interview_summary

    @interview_summary.setter
    def interview_summary(self, value):
        self._interview_summary = value
    @property
    def recommend_tag(self):
        return self._recommend_tag

    @recommend_tag.setter
    def recommend_tag(self, value):
        self._recommend_tag = value


    def to_alipay_dict(self):
        params = dict()
        if self.abnormal_tags:
            if isinstance(self.abnormal_tags, list):
                for i in range(0, len(self.abnormal_tags)):
                    element = self.abnormal_tags[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.abnormal_tags[i] = element.to_alipay_dict()
            if hasattr(self.abnormal_tags, 'to_alipay_dict'):
                params['abnormal_tags'] = self.abnormal_tags.to_alipay_dict()
            else:
                params['abnormal_tags'] = self.abnormal_tags
        if self.elimination_rule_result:
            if hasattr(self.elimination_rule_result, 'to_alipay_dict'):
                params['elimination_rule_result'] = self.elimination_rule_result.to_alipay_dict()
            else:
                params['elimination_rule_result'] = self.elimination_rule_result
        if self.interview_result:
            if hasattr(self.interview_result, 'to_alipay_dict'):
                params['interview_result'] = self.interview_result.to_alipay_dict()
            else:
                params['interview_result'] = self.interview_result
        if self.interview_summary:
            if hasattr(self.interview_summary, 'to_alipay_dict'):
                params['interview_summary'] = self.interview_summary.to_alipay_dict()
            else:
                params['interview_summary'] = self.interview_summary
        if self.recommend_tag:
            if hasattr(self.recommend_tag, 'to_alipay_dict'):
                params['recommend_tag'] = self.recommend_tag.to_alipay_dict()
            else:
                params['recommend_tag'] = self.recommend_tag
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ComprehensiveEvaluation()
        if 'abnormal_tags' in d:
            o.abnormal_tags = d['abnormal_tags']
        if 'elimination_rule_result' in d:
            o.elimination_rule_result = d['elimination_rule_result']
        if 'interview_result' in d:
            o.interview_result = d['interview_result']
        if 'interview_summary' in d:
            o.interview_summary = d['interview_summary']
        if 'recommend_tag' in d:
            o.recommend_tag = d['recommend_tag']
        return o


