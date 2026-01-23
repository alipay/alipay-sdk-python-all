#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppIndustryCareertrainingExamauditCancelModel(object):

    def __init__(self):
        self._exam_id = None

    @property
    def exam_id(self):
        return self._exam_id

    @exam_id.setter
    def exam_id(self, value):
        self._exam_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.exam_id:
            if hasattr(self.exam_id, 'to_alipay_dict'):
                params['exam_id'] = self.exam_id.to_alipay_dict()
            else:
                params['exam_id'] = self.exam_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppIndustryCareertrainingExamauditCancelModel()
        if 'exam_id' in d:
            o.exam_id = d['exam_id']
        return o


