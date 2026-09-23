#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FollowQuestions import FollowQuestions
from alipay.aop.api.domain.Options import Options


class QuestionDetails(object):

    def __init__(self):
        self._ai_comment = None
        self._competency_dimensions = None
        self._detect_result = None
        self._elimination_rule_result = None
        self._follow_questions = None
        self._options = None
        self._question_no = None
        self._question_score = None
        self._question_title = None
        self._question_type = None
        self._type_code = None
        self._user_answer = None
        self._user_score = None

    @property
    def ai_comment(self):
        return self._ai_comment

    @ai_comment.setter
    def ai_comment(self, value):
        self._ai_comment = value
    @property
    def competency_dimensions(self):
        return self._competency_dimensions

    @competency_dimensions.setter
    def competency_dimensions(self, value):
        if isinstance(value, list):
            self._competency_dimensions = list()
            for i in value:
                self._competency_dimensions.append(i)
    @property
    def detect_result(self):
        return self._detect_result

    @detect_result.setter
    def detect_result(self, value):
        self._detect_result = value
    @property
    def elimination_rule_result(self):
        return self._elimination_rule_result

    @elimination_rule_result.setter
    def elimination_rule_result(self, value):
        self._elimination_rule_result = value
    @property
    def follow_questions(self):
        return self._follow_questions

    @follow_questions.setter
    def follow_questions(self, value):
        if isinstance(value, list):
            self._follow_questions = list()
            for i in value:
                if isinstance(i, FollowQuestions):
                    self._follow_questions.append(i)
                else:
                    self._follow_questions.append(FollowQuestions.from_alipay_dict(i))
    @property
    def options(self):
        return self._options

    @options.setter
    def options(self, value):
        if isinstance(value, list):
            self._options = list()
            for i in value:
                if isinstance(i, Options):
                    self._options.append(i)
                else:
                    self._options.append(Options.from_alipay_dict(i))
    @property
    def question_no(self):
        return self._question_no

    @question_no.setter
    def question_no(self, value):
        self._question_no = value
    @property
    def question_score(self):
        return self._question_score

    @question_score.setter
    def question_score(self, value):
        self._question_score = value
    @property
    def question_title(self):
        return self._question_title

    @question_title.setter
    def question_title(self, value):
        self._question_title = value
    @property
    def question_type(self):
        return self._question_type

    @question_type.setter
    def question_type(self, value):
        self._question_type = value
    @property
    def type_code(self):
        return self._type_code

    @type_code.setter
    def type_code(self, value):
        self._type_code = value
    @property
    def user_answer(self):
        return self._user_answer

    @user_answer.setter
    def user_answer(self, value):
        self._user_answer = value
    @property
    def user_score(self):
        return self._user_score

    @user_score.setter
    def user_score(self, value):
        self._user_score = value


    def to_alipay_dict(self):
        params = dict()
        if self.ai_comment:
            if hasattr(self.ai_comment, 'to_alipay_dict'):
                params['ai_comment'] = self.ai_comment.to_alipay_dict()
            else:
                params['ai_comment'] = self.ai_comment
        if self.competency_dimensions:
            if isinstance(self.competency_dimensions, list):
                for i in range(0, len(self.competency_dimensions)):
                    element = self.competency_dimensions[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.competency_dimensions[i] = element.to_alipay_dict()
            if hasattr(self.competency_dimensions, 'to_alipay_dict'):
                params['competency_dimensions'] = self.competency_dimensions.to_alipay_dict()
            else:
                params['competency_dimensions'] = self.competency_dimensions
        if self.detect_result:
            if hasattr(self.detect_result, 'to_alipay_dict'):
                params['detect_result'] = self.detect_result.to_alipay_dict()
            else:
                params['detect_result'] = self.detect_result
        if self.elimination_rule_result:
            if hasattr(self.elimination_rule_result, 'to_alipay_dict'):
                params['elimination_rule_result'] = self.elimination_rule_result.to_alipay_dict()
            else:
                params['elimination_rule_result'] = self.elimination_rule_result
        if self.follow_questions:
            if isinstance(self.follow_questions, list):
                for i in range(0, len(self.follow_questions)):
                    element = self.follow_questions[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.follow_questions[i] = element.to_alipay_dict()
            if hasattr(self.follow_questions, 'to_alipay_dict'):
                params['follow_questions'] = self.follow_questions.to_alipay_dict()
            else:
                params['follow_questions'] = self.follow_questions
        if self.options:
            if isinstance(self.options, list):
                for i in range(0, len(self.options)):
                    element = self.options[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.options[i] = element.to_alipay_dict()
            if hasattr(self.options, 'to_alipay_dict'):
                params['options'] = self.options.to_alipay_dict()
            else:
                params['options'] = self.options
        if self.question_no:
            if hasattr(self.question_no, 'to_alipay_dict'):
                params['question_no'] = self.question_no.to_alipay_dict()
            else:
                params['question_no'] = self.question_no
        if self.question_score:
            if hasattr(self.question_score, 'to_alipay_dict'):
                params['question_score'] = self.question_score.to_alipay_dict()
            else:
                params['question_score'] = self.question_score
        if self.question_title:
            if hasattr(self.question_title, 'to_alipay_dict'):
                params['question_title'] = self.question_title.to_alipay_dict()
            else:
                params['question_title'] = self.question_title
        if self.question_type:
            if hasattr(self.question_type, 'to_alipay_dict'):
                params['question_type'] = self.question_type.to_alipay_dict()
            else:
                params['question_type'] = self.question_type
        if self.type_code:
            if hasattr(self.type_code, 'to_alipay_dict'):
                params['type_code'] = self.type_code.to_alipay_dict()
            else:
                params['type_code'] = self.type_code
        if self.user_answer:
            if hasattr(self.user_answer, 'to_alipay_dict'):
                params['user_answer'] = self.user_answer.to_alipay_dict()
            else:
                params['user_answer'] = self.user_answer
        if self.user_score:
            if hasattr(self.user_score, 'to_alipay_dict'):
                params['user_score'] = self.user_score.to_alipay_dict()
            else:
                params['user_score'] = self.user_score
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = QuestionDetails()
        if 'ai_comment' in d:
            o.ai_comment = d['ai_comment']
        if 'competency_dimensions' in d:
            o.competency_dimensions = d['competency_dimensions']
        if 'detect_result' in d:
            o.detect_result = d['detect_result']
        if 'elimination_rule_result' in d:
            o.elimination_rule_result = d['elimination_rule_result']
        if 'follow_questions' in d:
            o.follow_questions = d['follow_questions']
        if 'options' in d:
            o.options = d['options']
        if 'question_no' in d:
            o.question_no = d['question_no']
        if 'question_score' in d:
            o.question_score = d['question_score']
        if 'question_title' in d:
            o.question_title = d['question_title']
        if 'question_type' in d:
            o.question_type = d['question_type']
        if 'type_code' in d:
            o.type_code = d['type_code']
        if 'user_answer' in d:
            o.user_answer = d['user_answer']
        if 'user_score' in d:
            o.user_score = d['user_score']
        return o


