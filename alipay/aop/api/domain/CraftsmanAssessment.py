#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CraftsmanSubAssessment import CraftsmanSubAssessment


class CraftsmanAssessment(object):

    def __init__(self):
        self._sub_assessments = None
        self._total_no = None
        self._total_score = None

    @property
    def sub_assessments(self):
        return self._sub_assessments

    @sub_assessments.setter
    def sub_assessments(self, value):
        if isinstance(value, list):
            self._sub_assessments = list()
            for i in value:
                if isinstance(i, CraftsmanSubAssessment):
                    self._sub_assessments.append(i)
                else:
                    self._sub_assessments.append(CraftsmanSubAssessment.from_alipay_dict(i))
    @property
    def total_no(self):
        return self._total_no

    @total_no.setter
    def total_no(self, value):
        self._total_no = value
    @property
    def total_score(self):
        return self._total_score

    @total_score.setter
    def total_score(self, value):
        self._total_score = value


    def to_alipay_dict(self):
        params = dict()
        if self.sub_assessments:
            if isinstance(self.sub_assessments, list):
                for i in range(0, len(self.sub_assessments)):
                    element = self.sub_assessments[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sub_assessments[i] = element.to_alipay_dict()
            if hasattr(self.sub_assessments, 'to_alipay_dict'):
                params['sub_assessments'] = self.sub_assessments.to_alipay_dict()
            else:
                params['sub_assessments'] = self.sub_assessments
        if self.total_no:
            if hasattr(self.total_no, 'to_alipay_dict'):
                params['total_no'] = self.total_no.to_alipay_dict()
            else:
                params['total_no'] = self.total_no
        if self.total_score:
            if hasattr(self.total_score, 'to_alipay_dict'):
                params['total_score'] = self.total_score.to_alipay_dict()
            else:
                params['total_score'] = self.total_score
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CraftsmanAssessment()
        if 'sub_assessments' in d:
            o.sub_assessments = d['sub_assessments']
        if 'total_no' in d:
            o.total_no = d['total_no']
        if 'total_score' in d:
            o.total_score = d['total_score']
        return o


