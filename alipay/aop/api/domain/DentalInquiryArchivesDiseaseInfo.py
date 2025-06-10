#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DentalInquiryArchivesDiseaseLevelInfo import DentalInquiryArchivesDiseaseLevelInfo


class DentalInquiryArchivesDiseaseInfo(object):

    def __init__(self):
        self._inquiry_status = None
        self._main_demands = None
        self._out_disease_id = None
        self._question = None
        self._question_level = None
        self._question_position = None
        self._question_risk = None
        self._question_suggestion = None
        self._read_status = None

    @property
    def inquiry_status(self):
        return self._inquiry_status

    @inquiry_status.setter
    def inquiry_status(self, value):
        self._inquiry_status = value
    @property
    def main_demands(self):
        return self._main_demands

    @main_demands.setter
    def main_demands(self, value):
        self._main_demands = value
    @property
    def out_disease_id(self):
        return self._out_disease_id

    @out_disease_id.setter
    def out_disease_id(self, value):
        self._out_disease_id = value
    @property
    def question(self):
        return self._question

    @question.setter
    def question(self, value):
        self._question = value
    @property
    def question_level(self):
        return self._question_level

    @question_level.setter
    def question_level(self, value):
        if isinstance(value, DentalInquiryArchivesDiseaseLevelInfo):
            self._question_level = value
        else:
            self._question_level = DentalInquiryArchivesDiseaseLevelInfo.from_alipay_dict(value)
    @property
    def question_position(self):
        return self._question_position

    @question_position.setter
    def question_position(self, value):
        self._question_position = value
    @property
    def question_risk(self):
        return self._question_risk

    @question_risk.setter
    def question_risk(self, value):
        self._question_risk = value
    @property
    def question_suggestion(self):
        return self._question_suggestion

    @question_suggestion.setter
    def question_suggestion(self, value):
        if isinstance(value, list):
            self._question_suggestion = list()
            for i in value:
                self._question_suggestion.append(i)
    @property
    def read_status(self):
        return self._read_status

    @read_status.setter
    def read_status(self, value):
        self._read_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.inquiry_status:
            if hasattr(self.inquiry_status, 'to_alipay_dict'):
                params['inquiry_status'] = self.inquiry_status.to_alipay_dict()
            else:
                params['inquiry_status'] = self.inquiry_status
        if self.main_demands:
            if hasattr(self.main_demands, 'to_alipay_dict'):
                params['main_demands'] = self.main_demands.to_alipay_dict()
            else:
                params['main_demands'] = self.main_demands
        if self.out_disease_id:
            if hasattr(self.out_disease_id, 'to_alipay_dict'):
                params['out_disease_id'] = self.out_disease_id.to_alipay_dict()
            else:
                params['out_disease_id'] = self.out_disease_id
        if self.question:
            if hasattr(self.question, 'to_alipay_dict'):
                params['question'] = self.question.to_alipay_dict()
            else:
                params['question'] = self.question
        if self.question_level:
            if hasattr(self.question_level, 'to_alipay_dict'):
                params['question_level'] = self.question_level.to_alipay_dict()
            else:
                params['question_level'] = self.question_level
        if self.question_position:
            if hasattr(self.question_position, 'to_alipay_dict'):
                params['question_position'] = self.question_position.to_alipay_dict()
            else:
                params['question_position'] = self.question_position
        if self.question_risk:
            if hasattr(self.question_risk, 'to_alipay_dict'):
                params['question_risk'] = self.question_risk.to_alipay_dict()
            else:
                params['question_risk'] = self.question_risk
        if self.question_suggestion:
            if isinstance(self.question_suggestion, list):
                for i in range(0, len(self.question_suggestion)):
                    element = self.question_suggestion[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.question_suggestion[i] = element.to_alipay_dict()
            if hasattr(self.question_suggestion, 'to_alipay_dict'):
                params['question_suggestion'] = self.question_suggestion.to_alipay_dict()
            else:
                params['question_suggestion'] = self.question_suggestion
        if self.read_status:
            if hasattr(self.read_status, 'to_alipay_dict'):
                params['read_status'] = self.read_status.to_alipay_dict()
            else:
                params['read_status'] = self.read_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DentalInquiryArchivesDiseaseInfo()
        if 'inquiry_status' in d:
            o.inquiry_status = d['inquiry_status']
        if 'main_demands' in d:
            o.main_demands = d['main_demands']
        if 'out_disease_id' in d:
            o.out_disease_id = d['out_disease_id']
        if 'question' in d:
            o.question = d['question']
        if 'question_level' in d:
            o.question_level = d['question_level']
        if 'question_position' in d:
            o.question_position = d['question_position']
        if 'question_risk' in d:
            o.question_risk = d['question_risk']
        if 'question_suggestion' in d:
            o.question_suggestion = d['question_suggestion']
        if 'read_status' in d:
            o.read_status = d['read_status']
        return o


