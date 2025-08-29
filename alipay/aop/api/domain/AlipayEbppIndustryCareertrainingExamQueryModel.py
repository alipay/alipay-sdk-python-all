#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppIndustryCareertrainingExamQueryModel(object):

    def __init__(self):
        self._exam_id = None
        self._out_exam_id = None

    @property
    def exam_id(self):
        return self._exam_id

    @exam_id.setter
    def exam_id(self, value):
        self._exam_id = value
    @property
    def out_exam_id(self):
        return self._out_exam_id

    @out_exam_id.setter
    def out_exam_id(self, value):
        self._out_exam_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.exam_id:
            if hasattr(self.exam_id, 'to_alipay_dict'):
                params['exam_id'] = self.exam_id.to_alipay_dict()
            else:
                params['exam_id'] = self.exam_id
        if self.out_exam_id:
            if hasattr(self.out_exam_id, 'to_alipay_dict'):
                params['out_exam_id'] = self.out_exam_id.to_alipay_dict()
            else:
                params['out_exam_id'] = self.out_exam_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppIndustryCareertrainingExamQueryModel()
        if 'exam_id' in d:
            o.exam_id = d['exam_id']
        if 'out_exam_id' in d:
            o.out_exam_id = d['out_exam_id']
        return o


