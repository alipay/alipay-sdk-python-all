#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CissExerciseReportRecord(object):

    def __init__(self):
        self._evaluate = None
        self._grade = None
        self._id = None
        self._item_code = None
        self._item_name = None
        self._score = None
        self._test_value = None
        self._unit = None

    @property
    def evaluate(self):
        return self._evaluate

    @evaluate.setter
    def evaluate(self, value):
        self._evaluate = value
    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, value):
        self._grade = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def item_code(self):
        return self._item_code

    @item_code.setter
    def item_code(self, value):
        self._item_code = value
    @property
    def item_name(self):
        return self._item_name

    @item_name.setter
    def item_name(self, value):
        self._item_name = value
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = value
    @property
    def test_value(self):
        return self._test_value

    @test_value.setter
    def test_value(self, value):
        self._test_value = value
    @property
    def unit(self):
        return self._unit

    @unit.setter
    def unit(self, value):
        self._unit = value


    def to_alipay_dict(self):
        params = dict()
        if self.evaluate:
            if hasattr(self.evaluate, 'to_alipay_dict'):
                params['evaluate'] = self.evaluate.to_alipay_dict()
            else:
                params['evaluate'] = self.evaluate
        if self.grade:
            if hasattr(self.grade, 'to_alipay_dict'):
                params['grade'] = self.grade.to_alipay_dict()
            else:
                params['grade'] = self.grade
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.item_code:
            if hasattr(self.item_code, 'to_alipay_dict'):
                params['item_code'] = self.item_code.to_alipay_dict()
            else:
                params['item_code'] = self.item_code
        if self.item_name:
            if hasattr(self.item_name, 'to_alipay_dict'):
                params['item_name'] = self.item_name.to_alipay_dict()
            else:
                params['item_name'] = self.item_name
        if self.score:
            if hasattr(self.score, 'to_alipay_dict'):
                params['score'] = self.score.to_alipay_dict()
            else:
                params['score'] = self.score
        if self.test_value:
            if hasattr(self.test_value, 'to_alipay_dict'):
                params['test_value'] = self.test_value.to_alipay_dict()
            else:
                params['test_value'] = self.test_value
        if self.unit:
            if hasattr(self.unit, 'to_alipay_dict'):
                params['unit'] = self.unit.to_alipay_dict()
            else:
                params['unit'] = self.unit
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CissExerciseReportRecord()
        if 'evaluate' in d:
            o.evaluate = d['evaluate']
        if 'grade' in d:
            o.grade = d['grade']
        if 'id' in d:
            o.id = d['id']
        if 'item_code' in d:
            o.item_code = d['item_code']
        if 'item_name' in d:
            o.item_name = d['item_name']
        if 'score' in d:
            o.score = d['score']
        if 'test_value' in d:
            o.test_value = d['test_value']
        if 'unit' in d:
            o.unit = d['unit']
        return o


