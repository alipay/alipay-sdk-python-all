#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.LabelFeedbackDetailModel import LabelFeedbackDetailModel


class ZhimaCreditEpAcceptanceLabelUseModel(object):

    def __init__(self):
        self._feedback_data = None
        self._scene_code = None

    @property
    def feedback_data(self):
        return self._feedback_data

    @feedback_data.setter
    def feedback_data(self, value):
        if isinstance(value, list):
            self._feedback_data = list()
            for i in value:
                if isinstance(i, LabelFeedbackDetailModel):
                    self._feedback_data.append(i)
                else:
                    self._feedback_data.append(LabelFeedbackDetailModel.from_alipay_dict(i))
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.feedback_data:
            if isinstance(self.feedback_data, list):
                for i in range(0, len(self.feedback_data)):
                    element = self.feedback_data[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.feedback_data[i] = element.to_alipay_dict()
            if hasattr(self.feedback_data, 'to_alipay_dict'):
                params['feedback_data'] = self.feedback_data.to_alipay_dict()
            else:
                params['feedback_data'] = self.feedback_data
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCreditEpAcceptanceLabelUseModel()
        if 'feedback_data' in d:
            o.feedback_data = d['feedback_data']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        return o


