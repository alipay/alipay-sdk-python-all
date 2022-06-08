#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class NiukeExamCallbackRequest(object):

    def __init__(self):
        self._category_scores = None
        self._is_cheated = None
        self._key = None
        self._paper_id = None
        self._paper_name = None
        self._paper_score = None
        self._result_pdf_url = None
        self._score = None
        self._status = None
        self._test_finish_time = None
        self._test_start_time = None

    @property
    def category_scores(self):
        return self._category_scores

    @category_scores.setter
    def category_scores(self, value):
        if isinstance(value, list):
            self._category_scores = list()
            for i in value:
                self._category_scores.append(i)
    @property
    def is_cheated(self):
        return self._is_cheated

    @is_cheated.setter
    def is_cheated(self, value):
        self._is_cheated = value
    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, value):
        self._key = value
    @property
    def paper_id(self):
        return self._paper_id

    @paper_id.setter
    def paper_id(self, value):
        self._paper_id = value
    @property
    def paper_name(self):
        return self._paper_name

    @paper_name.setter
    def paper_name(self, value):
        self._paper_name = value
    @property
    def paper_score(self):
        return self._paper_score

    @paper_score.setter
    def paper_score(self, value):
        self._paper_score = value
    @property
    def result_pdf_url(self):
        return self._result_pdf_url

    @result_pdf_url.setter
    def result_pdf_url(self, value):
        self._result_pdf_url = value
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def test_finish_time(self):
        return self._test_finish_time

    @test_finish_time.setter
    def test_finish_time(self, value):
        self._test_finish_time = value
    @property
    def test_start_time(self):
        return self._test_start_time

    @test_start_time.setter
    def test_start_time(self, value):
        self._test_start_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.category_scores:
            if isinstance(self.category_scores, list):
                for i in range(0, len(self.category_scores)):
                    element = self.category_scores[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.category_scores[i] = element.to_alipay_dict()
            if hasattr(self.category_scores, 'to_alipay_dict'):
                params['category_scores'] = self.category_scores.to_alipay_dict()
            else:
                params['category_scores'] = self.category_scores
        if self.is_cheated:
            if hasattr(self.is_cheated, 'to_alipay_dict'):
                params['is_cheated'] = self.is_cheated.to_alipay_dict()
            else:
                params['is_cheated'] = self.is_cheated
        if self.key:
            if hasattr(self.key, 'to_alipay_dict'):
                params['key'] = self.key.to_alipay_dict()
            else:
                params['key'] = self.key
        if self.paper_id:
            if hasattr(self.paper_id, 'to_alipay_dict'):
                params['paper_id'] = self.paper_id.to_alipay_dict()
            else:
                params['paper_id'] = self.paper_id
        if self.paper_name:
            if hasattr(self.paper_name, 'to_alipay_dict'):
                params['paper_name'] = self.paper_name.to_alipay_dict()
            else:
                params['paper_name'] = self.paper_name
        if self.paper_score:
            if hasattr(self.paper_score, 'to_alipay_dict'):
                params['paper_score'] = self.paper_score.to_alipay_dict()
            else:
                params['paper_score'] = self.paper_score
        if self.result_pdf_url:
            if hasattr(self.result_pdf_url, 'to_alipay_dict'):
                params['result_pdf_url'] = self.result_pdf_url.to_alipay_dict()
            else:
                params['result_pdf_url'] = self.result_pdf_url
        if self.score:
            if hasattr(self.score, 'to_alipay_dict'):
                params['score'] = self.score.to_alipay_dict()
            else:
                params['score'] = self.score
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.test_finish_time:
            if hasattr(self.test_finish_time, 'to_alipay_dict'):
                params['test_finish_time'] = self.test_finish_time.to_alipay_dict()
            else:
                params['test_finish_time'] = self.test_finish_time
        if self.test_start_time:
            if hasattr(self.test_start_time, 'to_alipay_dict'):
                params['test_start_time'] = self.test_start_time.to_alipay_dict()
            else:
                params['test_start_time'] = self.test_start_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = NiukeExamCallbackRequest()
        if 'category_scores' in d:
            o.category_scores = d['category_scores']
        if 'is_cheated' in d:
            o.is_cheated = d['is_cheated']
        if 'key' in d:
            o.key = d['key']
        if 'paper_id' in d:
            o.paper_id = d['paper_id']
        if 'paper_name' in d:
            o.paper_name = d['paper_name']
        if 'paper_score' in d:
            o.paper_score = d['paper_score']
        if 'result_pdf_url' in d:
            o.result_pdf_url = d['result_pdf_url']
        if 'score' in d:
            o.score = d['score']
        if 'status' in d:
            o.status = d['status']
        if 'test_finish_time' in d:
            o.test_finish_time = d['test_finish_time']
        if 'test_start_time' in d:
            o.test_start_time = d['test_start_time']
        return o


