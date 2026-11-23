#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CompetencyDetails import CompetencyDetails
from alipay.aop.api.domain.ComprehensiveEvaluation import ComprehensiveEvaluation
from alipay.aop.api.domain.DetectionDetail import DetectionDetail
from alipay.aop.api.domain.QuestionDetails import QuestionDetails


class InterviewDetail(object):

    def __init__(self):
        self._competency_details = None
        self._comprehensive_evaluation = None
        self._detection_detail = None
        self._question_details = None

    @property
    def competency_details(self):
        return self._competency_details

    @competency_details.setter
    def competency_details(self, value):
        if isinstance(value, list):
            self._competency_details = list()
            for i in value:
                if isinstance(i, CompetencyDetails):
                    self._competency_details.append(i)
                else:
                    self._competency_details.append(CompetencyDetails.from_alipay_dict(i))
    @property
    def comprehensive_evaluation(self):
        return self._comprehensive_evaluation

    @comprehensive_evaluation.setter
    def comprehensive_evaluation(self, value):
        if isinstance(value, ComprehensiveEvaluation):
            self._comprehensive_evaluation = value
        else:
            self._comprehensive_evaluation = ComprehensiveEvaluation.from_alipay_dict(value)
    @property
    def detection_detail(self):
        return self._detection_detail

    @detection_detail.setter
    def detection_detail(self, value):
        if isinstance(value, list):
            self._detection_detail = list()
            for i in value:
                if isinstance(i, DetectionDetail):
                    self._detection_detail.append(i)
                else:
                    self._detection_detail.append(DetectionDetail.from_alipay_dict(i))
    @property
    def question_details(self):
        return self._question_details

    @question_details.setter
    def question_details(self, value):
        if isinstance(value, list):
            self._question_details = list()
            for i in value:
                if isinstance(i, QuestionDetails):
                    self._question_details.append(i)
                else:
                    self._question_details.append(QuestionDetails.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.competency_details:
            if isinstance(self.competency_details, list):
                for i in range(0, len(self.competency_details)):
                    element = self.competency_details[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.competency_details[i] = element.to_alipay_dict()
            if hasattr(self.competency_details, 'to_alipay_dict'):
                params['competency_details'] = self.competency_details.to_alipay_dict()
            else:
                params['competency_details'] = self.competency_details
        if self.comprehensive_evaluation:
            if hasattr(self.comprehensive_evaluation, 'to_alipay_dict'):
                params['comprehensive_evaluation'] = self.comprehensive_evaluation.to_alipay_dict()
            else:
                params['comprehensive_evaluation'] = self.comprehensive_evaluation
        if self.detection_detail:
            if isinstance(self.detection_detail, list):
                for i in range(0, len(self.detection_detail)):
                    element = self.detection_detail[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.detection_detail[i] = element.to_alipay_dict()
            if hasattr(self.detection_detail, 'to_alipay_dict'):
                params['detection_detail'] = self.detection_detail.to_alipay_dict()
            else:
                params['detection_detail'] = self.detection_detail
        if self.question_details:
            if isinstance(self.question_details, list):
                for i in range(0, len(self.question_details)):
                    element = self.question_details[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.question_details[i] = element.to_alipay_dict()
            if hasattr(self.question_details, 'to_alipay_dict'):
                params['question_details'] = self.question_details.to_alipay_dict()
            else:
                params['question_details'] = self.question_details
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InterviewDetail()
        if 'competency_details' in d:
            o.competency_details = d['competency_details']
        if 'comprehensive_evaluation' in d:
            o.comprehensive_evaluation = d['comprehensive_evaluation']
        if 'detection_detail' in d:
            o.detection_detail = d['detection_detail']
        if 'question_details' in d:
            o.question_details = d['question_details']
        return o


