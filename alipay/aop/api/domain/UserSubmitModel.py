#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AnswerModel import AnswerModel


class UserSubmitModel(object):

    def __init__(self):
        self._answers = None
        self._gmt_submit = None
        self._job_id = None
        self._referrer = None
        self._score = None
        self._snapshot_id = None
        self._submit_id = None
        self._user_id = None
        self._user_type = None

    @property
    def answers(self):
        return self._answers

    @answers.setter
    def answers(self, value):
        if isinstance(value, list):
            self._answers = list()
            for i in value:
                if isinstance(i, AnswerModel):
                    self._answers.append(i)
                else:
                    self._answers.append(AnswerModel.from_alipay_dict(i))
    @property
    def gmt_submit(self):
        return self._gmt_submit

    @gmt_submit.setter
    def gmt_submit(self, value):
        self._gmt_submit = value
    @property
    def job_id(self):
        return self._job_id

    @job_id.setter
    def job_id(self, value):
        self._job_id = value
    @property
    def referrer(self):
        return self._referrer

    @referrer.setter
    def referrer(self, value):
        self._referrer = value
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = value
    @property
    def snapshot_id(self):
        return self._snapshot_id

    @snapshot_id.setter
    def snapshot_id(self, value):
        self._snapshot_id = value
    @property
    def submit_id(self):
        return self._submit_id

    @submit_id.setter
    def submit_id(self, value):
        self._submit_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def user_type(self):
        return self._user_type

    @user_type.setter
    def user_type(self, value):
        self._user_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.answers:
            if isinstance(self.answers, list):
                for i in range(0, len(self.answers)):
                    element = self.answers[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.answers[i] = element.to_alipay_dict()
            if hasattr(self.answers, 'to_alipay_dict'):
                params['answers'] = self.answers.to_alipay_dict()
            else:
                params['answers'] = self.answers
        if self.gmt_submit:
            if hasattr(self.gmt_submit, 'to_alipay_dict'):
                params['gmt_submit'] = self.gmt_submit.to_alipay_dict()
            else:
                params['gmt_submit'] = self.gmt_submit
        if self.job_id:
            if hasattr(self.job_id, 'to_alipay_dict'):
                params['job_id'] = self.job_id.to_alipay_dict()
            else:
                params['job_id'] = self.job_id
        if self.referrer:
            if hasattr(self.referrer, 'to_alipay_dict'):
                params['referrer'] = self.referrer.to_alipay_dict()
            else:
                params['referrer'] = self.referrer
        if self.score:
            if hasattr(self.score, 'to_alipay_dict'):
                params['score'] = self.score.to_alipay_dict()
            else:
                params['score'] = self.score
        if self.snapshot_id:
            if hasattr(self.snapshot_id, 'to_alipay_dict'):
                params['snapshot_id'] = self.snapshot_id.to_alipay_dict()
            else:
                params['snapshot_id'] = self.snapshot_id
        if self.submit_id:
            if hasattr(self.submit_id, 'to_alipay_dict'):
                params['submit_id'] = self.submit_id.to_alipay_dict()
            else:
                params['submit_id'] = self.submit_id
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.user_type:
            if hasattr(self.user_type, 'to_alipay_dict'):
                params['user_type'] = self.user_type.to_alipay_dict()
            else:
                params['user_type'] = self.user_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = UserSubmitModel()
        if 'answers' in d:
            o.answers = d['answers']
        if 'gmt_submit' in d:
            o.gmt_submit = d['gmt_submit']
        if 'job_id' in d:
            o.job_id = d['job_id']
        if 'referrer' in d:
            o.referrer = d['referrer']
        if 'score' in d:
            o.score = d['score']
        if 'snapshot_id' in d:
            o.snapshot_id = d['snapshot_id']
        if 'submit_id' in d:
            o.submit_id = d['submit_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'user_type' in d:
            o.user_type = d['user_type']
        return o


