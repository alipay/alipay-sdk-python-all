#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DivinationBizContextDetail(object):

    def __init__(self):
        self._category = None
        self._conclusion = None
        self._divination_id = None
        self._grade = None
        self._insight = None
        self._interpretation = None
        self._name = None
        self._poem = None
        self._reference = None
        self._sequence_number = None

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        self._category = value
    @property
    def conclusion(self):
        return self._conclusion

    @conclusion.setter
    def conclusion(self, value):
        self._conclusion = value
    @property
    def divination_id(self):
        return self._divination_id

    @divination_id.setter
    def divination_id(self, value):
        self._divination_id = value
    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, value):
        self._grade = value
    @property
    def insight(self):
        return self._insight

    @insight.setter
    def insight(self, value):
        self._insight = value
    @property
    def interpretation(self):
        return self._interpretation

    @interpretation.setter
    def interpretation(self, value):
        self._interpretation = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def poem(self):
        return self._poem

    @poem.setter
    def poem(self, value):
        self._poem = value
    @property
    def reference(self):
        return self._reference

    @reference.setter
    def reference(self, value):
        self._reference = value
    @property
    def sequence_number(self):
        return self._sequence_number

    @sequence_number.setter
    def sequence_number(self, value):
        self._sequence_number = value


    def to_alipay_dict(self):
        params = dict()
        if self.category:
            if hasattr(self.category, 'to_alipay_dict'):
                params['category'] = self.category.to_alipay_dict()
            else:
                params['category'] = self.category
        if self.conclusion:
            if hasattr(self.conclusion, 'to_alipay_dict'):
                params['conclusion'] = self.conclusion.to_alipay_dict()
            else:
                params['conclusion'] = self.conclusion
        if self.divination_id:
            if hasattr(self.divination_id, 'to_alipay_dict'):
                params['divination_id'] = self.divination_id.to_alipay_dict()
            else:
                params['divination_id'] = self.divination_id
        if self.grade:
            if hasattr(self.grade, 'to_alipay_dict'):
                params['grade'] = self.grade.to_alipay_dict()
            else:
                params['grade'] = self.grade
        if self.insight:
            if hasattr(self.insight, 'to_alipay_dict'):
                params['insight'] = self.insight.to_alipay_dict()
            else:
                params['insight'] = self.insight
        if self.interpretation:
            if hasattr(self.interpretation, 'to_alipay_dict'):
                params['interpretation'] = self.interpretation.to_alipay_dict()
            else:
                params['interpretation'] = self.interpretation
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.poem:
            if hasattr(self.poem, 'to_alipay_dict'):
                params['poem'] = self.poem.to_alipay_dict()
            else:
                params['poem'] = self.poem
        if self.reference:
            if hasattr(self.reference, 'to_alipay_dict'):
                params['reference'] = self.reference.to_alipay_dict()
            else:
                params['reference'] = self.reference
        if self.sequence_number:
            if hasattr(self.sequence_number, 'to_alipay_dict'):
                params['sequence_number'] = self.sequence_number.to_alipay_dict()
            else:
                params['sequence_number'] = self.sequence_number
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DivinationBizContextDetail()
        if 'category' in d:
            o.category = d['category']
        if 'conclusion' in d:
            o.conclusion = d['conclusion']
        if 'divination_id' in d:
            o.divination_id = d['divination_id']
        if 'grade' in d:
            o.grade = d['grade']
        if 'insight' in d:
            o.insight = d['insight']
        if 'interpretation' in d:
            o.interpretation = d['interpretation']
        if 'name' in d:
            o.name = d['name']
        if 'poem' in d:
            o.poem = d['poem']
        if 'reference' in d:
            o.reference = d['reference']
        if 'sequence_number' in d:
            o.sequence_number = d['sequence_number']
        return o


