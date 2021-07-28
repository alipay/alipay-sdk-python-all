#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySecurityProdVoiceQuestionQueryModel(object):

    def __init__(self):
        self._cur_answer = None
        self._cur_answer_type = None
        self._event_id = None
        self._phase = None
        self._scene_code = None

    @property
    def cur_answer(self):
        return self._cur_answer

    @cur_answer.setter
    def cur_answer(self, value):
        self._cur_answer = value
    @property
    def cur_answer_type(self):
        return self._cur_answer_type

    @cur_answer_type.setter
    def cur_answer_type(self, value):
        self._cur_answer_type = value
    @property
    def event_id(self):
        return self._event_id

    @event_id.setter
    def event_id(self, value):
        self._event_id = value
    @property
    def phase(self):
        return self._phase

    @phase.setter
    def phase(self, value):
        self._phase = value
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.cur_answer:
            if hasattr(self.cur_answer, 'to_alipay_dict'):
                params['cur_answer'] = self.cur_answer.to_alipay_dict()
            else:
                params['cur_answer'] = self.cur_answer
        if self.cur_answer_type:
            if hasattr(self.cur_answer_type, 'to_alipay_dict'):
                params['cur_answer_type'] = self.cur_answer_type.to_alipay_dict()
            else:
                params['cur_answer_type'] = self.cur_answer_type
        if self.event_id:
            if hasattr(self.event_id, 'to_alipay_dict'):
                params['event_id'] = self.event_id.to_alipay_dict()
            else:
                params['event_id'] = self.event_id
        if self.phase:
            if hasattr(self.phase, 'to_alipay_dict'):
                params['phase'] = self.phase.to_alipay_dict()
            else:
                params['phase'] = self.phase
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
        o = AlipaySecurityProdVoiceQuestionQueryModel()
        if 'cur_answer' in d:
            o.cur_answer = d['cur_answer']
        if 'cur_answer_type' in d:
            o.cur_answer_type = d['cur_answer_type']
        if 'event_id' in d:
            o.event_id = d['event_id']
        if 'phase' in d:
            o.phase = d['phase']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        return o


