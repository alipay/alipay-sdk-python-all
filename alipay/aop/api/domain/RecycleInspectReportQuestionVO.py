#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RecycleInspectReportAnswerVO import RecycleInspectReportAnswerVO


class RecycleInspectReportQuestionVO(object):

    def __init__(self):
        self._question_code = None
        self._question_name = None
        self._question_type = None
        self._report_answer_list = None
        self._template_type = None

    @property
    def question_code(self):
        return self._question_code

    @question_code.setter
    def question_code(self, value):
        self._question_code = value
    @property
    def question_name(self):
        return self._question_name

    @question_name.setter
    def question_name(self, value):
        self._question_name = value
    @property
    def question_type(self):
        return self._question_type

    @question_type.setter
    def question_type(self, value):
        self._question_type = value
    @property
    def report_answer_list(self):
        return self._report_answer_list

    @report_answer_list.setter
    def report_answer_list(self, value):
        if isinstance(value, list):
            self._report_answer_list = list()
            for i in value:
                if isinstance(i, RecycleInspectReportAnswerVO):
                    self._report_answer_list.append(i)
                else:
                    self._report_answer_list.append(RecycleInspectReportAnswerVO.from_alipay_dict(i))
    @property
    def template_type(self):
        return self._template_type

    @template_type.setter
    def template_type(self, value):
        self._template_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.question_code:
            if hasattr(self.question_code, 'to_alipay_dict'):
                params['question_code'] = self.question_code.to_alipay_dict()
            else:
                params['question_code'] = self.question_code
        if self.question_name:
            if hasattr(self.question_name, 'to_alipay_dict'):
                params['question_name'] = self.question_name.to_alipay_dict()
            else:
                params['question_name'] = self.question_name
        if self.question_type:
            if hasattr(self.question_type, 'to_alipay_dict'):
                params['question_type'] = self.question_type.to_alipay_dict()
            else:
                params['question_type'] = self.question_type
        if self.report_answer_list:
            if isinstance(self.report_answer_list, list):
                for i in range(0, len(self.report_answer_list)):
                    element = self.report_answer_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.report_answer_list[i] = element.to_alipay_dict()
            if hasattr(self.report_answer_list, 'to_alipay_dict'):
                params['report_answer_list'] = self.report_answer_list.to_alipay_dict()
            else:
                params['report_answer_list'] = self.report_answer_list
        if self.template_type:
            if hasattr(self.template_type, 'to_alipay_dict'):
                params['template_type'] = self.template_type.to_alipay_dict()
            else:
                params['template_type'] = self.template_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RecycleInspectReportQuestionVO()
        if 'question_code' in d:
            o.question_code = d['question_code']
        if 'question_name' in d:
            o.question_name = d['question_name']
        if 'question_type' in d:
            o.question_type = d['question_type']
        if 'report_answer_list' in d:
            o.report_answer_list = d['report_answer_list']
        if 'template_type' in d:
            o.template_type = d['template_type']
        return o


