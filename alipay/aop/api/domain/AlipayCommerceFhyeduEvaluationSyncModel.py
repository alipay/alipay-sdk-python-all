#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EduAssessmentScore import EduAssessmentScore


class AlipayCommerceFhyeduEvaluationSyncModel(object):

    def __init__(self):
        self._assessment = None
        self._course_id = None
        self._course_name = None
        self._evaluation_id = None
        self._evaluation_time = None
        self._evaluator = None
        self._inst_id = None
        self._sched_id = None
        self._score_list = None
        self._student_id = None

    @property
    def assessment(self):
        return self._assessment

    @assessment.setter
    def assessment(self, value):
        self._assessment = value
    @property
    def course_id(self):
        return self._course_id

    @course_id.setter
    def course_id(self, value):
        self._course_id = value
    @property
    def course_name(self):
        return self._course_name

    @course_name.setter
    def course_name(self, value):
        self._course_name = value
    @property
    def evaluation_id(self):
        return self._evaluation_id

    @evaluation_id.setter
    def evaluation_id(self, value):
        self._evaluation_id = value
    @property
    def evaluation_time(self):
        return self._evaluation_time

    @evaluation_time.setter
    def evaluation_time(self, value):
        self._evaluation_time = value
    @property
    def evaluator(self):
        return self._evaluator

    @evaluator.setter
    def evaluator(self, value):
        self._evaluator = value
    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def sched_id(self):
        return self._sched_id

    @sched_id.setter
    def sched_id(self, value):
        self._sched_id = value
    @property
    def score_list(self):
        return self._score_list

    @score_list.setter
    def score_list(self, value):
        if isinstance(value, list):
            self._score_list = list()
            for i in value:
                if isinstance(i, EduAssessmentScore):
                    self._score_list.append(i)
                else:
                    self._score_list.append(EduAssessmentScore.from_alipay_dict(i))
    @property
    def student_id(self):
        return self._student_id

    @student_id.setter
    def student_id(self, value):
        self._student_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.assessment:
            if hasattr(self.assessment, 'to_alipay_dict'):
                params['assessment'] = self.assessment.to_alipay_dict()
            else:
                params['assessment'] = self.assessment
        if self.course_id:
            if hasattr(self.course_id, 'to_alipay_dict'):
                params['course_id'] = self.course_id.to_alipay_dict()
            else:
                params['course_id'] = self.course_id
        if self.course_name:
            if hasattr(self.course_name, 'to_alipay_dict'):
                params['course_name'] = self.course_name.to_alipay_dict()
            else:
                params['course_name'] = self.course_name
        if self.evaluation_id:
            if hasattr(self.evaluation_id, 'to_alipay_dict'):
                params['evaluation_id'] = self.evaluation_id.to_alipay_dict()
            else:
                params['evaluation_id'] = self.evaluation_id
        if self.evaluation_time:
            if hasattr(self.evaluation_time, 'to_alipay_dict'):
                params['evaluation_time'] = self.evaluation_time.to_alipay_dict()
            else:
                params['evaluation_time'] = self.evaluation_time
        if self.evaluator:
            if hasattr(self.evaluator, 'to_alipay_dict'):
                params['evaluator'] = self.evaluator.to_alipay_dict()
            else:
                params['evaluator'] = self.evaluator
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.sched_id:
            if hasattr(self.sched_id, 'to_alipay_dict'):
                params['sched_id'] = self.sched_id.to_alipay_dict()
            else:
                params['sched_id'] = self.sched_id
        if self.score_list:
            if isinstance(self.score_list, list):
                for i in range(0, len(self.score_list)):
                    element = self.score_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.score_list[i] = element.to_alipay_dict()
            if hasattr(self.score_list, 'to_alipay_dict'):
                params['score_list'] = self.score_list.to_alipay_dict()
            else:
                params['score_list'] = self.score_list
        if self.student_id:
            if hasattr(self.student_id, 'to_alipay_dict'):
                params['student_id'] = self.student_id.to_alipay_dict()
            else:
                params['student_id'] = self.student_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceFhyeduEvaluationSyncModel()
        if 'assessment' in d:
            o.assessment = d['assessment']
        if 'course_id' in d:
            o.course_id = d['course_id']
        if 'course_name' in d:
            o.course_name = d['course_name']
        if 'evaluation_id' in d:
            o.evaluation_id = d['evaluation_id']
        if 'evaluation_time' in d:
            o.evaluation_time = d['evaluation_time']
        if 'evaluator' in d:
            o.evaluator = d['evaluator']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'sched_id' in d:
            o.sched_id = d['sched_id']
        if 'score_list' in d:
            o.score_list = d['score_list']
        if 'student_id' in d:
            o.student_id = d['student_id']
        return o


