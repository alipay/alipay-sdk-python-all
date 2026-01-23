#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppIndustryCareertrainingExamPublishModel(object):

    def __init__(self):
        self._exam_id = None
        self._publish_status = None

    @property
    def exam_id(self):
        return self._exam_id

    @exam_id.setter
    def exam_id(self, value):
        self._exam_id = value
    @property
    def publish_status(self):
        return self._publish_status

    @publish_status.setter
    def publish_status(self, value):
        self._publish_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.exam_id:
            if hasattr(self.exam_id, 'to_alipay_dict'):
                params['exam_id'] = self.exam_id.to_alipay_dict()
            else:
                params['exam_id'] = self.exam_id
        if self.publish_status:
            if hasattr(self.publish_status, 'to_alipay_dict'):
                params['publish_status'] = self.publish_status.to_alipay_dict()
            else:
                params['publish_status'] = self.publish_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppIndustryCareertrainingExamPublishModel()
        if 'exam_id' in d:
            o.exam_id = d['exam_id']
        if 'publish_status' in d:
            o.publish_status = d['publish_status']
        return o


