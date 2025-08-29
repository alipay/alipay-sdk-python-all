#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppIndustryCareertrainingExamSyncModel(object):

    def __init__(self):
        self._exam_id = None
        self._exam_status = None

    @property
    def exam_id(self):
        return self._exam_id

    @exam_id.setter
    def exam_id(self, value):
        self._exam_id = value
    @property
    def exam_status(self):
        return self._exam_status

    @exam_status.setter
    def exam_status(self, value):
        self._exam_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.exam_id:
            if hasattr(self.exam_id, 'to_alipay_dict'):
                params['exam_id'] = self.exam_id.to_alipay_dict()
            else:
                params['exam_id'] = self.exam_id
        if self.exam_status:
            if hasattr(self.exam_status, 'to_alipay_dict'):
                params['exam_status'] = self.exam_status.to_alipay_dict()
            else:
                params['exam_status'] = self.exam_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppIndustryCareertrainingExamSyncModel()
        if 'exam_id' in d:
            o.exam_id = d['exam_id']
        if 'exam_status' in d:
            o.exam_status = d['exam_status']
        return o


