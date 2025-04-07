#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalLargermodelFeedbackQueryModel(object):

    def __init__(self):
        self._feedback_channel = None
        self._scene_code = None
        self._service_status = None

    @property
    def feedback_channel(self):
        return self._feedback_channel

    @feedback_channel.setter
    def feedback_channel(self, value):
        self._feedback_channel = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value
    @property
    def service_status(self):
        return self._service_status

    @service_status.setter
    def service_status(self, value):
        self._service_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.feedback_channel:
            if hasattr(self.feedback_channel, 'to_alipay_dict'):
                params['feedback_channel'] = self.feedback_channel.to_alipay_dict()
            else:
                params['feedback_channel'] = self.feedback_channel
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        if self.service_status:
            if hasattr(self.service_status, 'to_alipay_dict'):
                params['service_status'] = self.service_status.to_alipay_dict()
            else:
                params['service_status'] = self.service_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalLargermodelFeedbackQueryModel()
        if 'feedback_channel' in d:
            o.feedback_channel = d['feedback_channel']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        if 'service_status' in d:
            o.service_status = d['service_status']
        return o


