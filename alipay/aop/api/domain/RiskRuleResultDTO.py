#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RiskRuleResultDTO(object):

    def __init__(self):
        self._risk_evaluation_detail = None
        self._risk_event = None
        self._risk_level = None
        self._risk_note = None
        self._risk_score = None
        self._source_type = None

    @property
    def risk_evaluation_detail(self):
        return self._risk_evaluation_detail

    @risk_evaluation_detail.setter
    def risk_evaluation_detail(self, value):
        self._risk_evaluation_detail = value
    @property
    def risk_event(self):
        return self._risk_event

    @risk_event.setter
    def risk_event(self, value):
        self._risk_event = value
    @property
    def risk_level(self):
        return self._risk_level

    @risk_level.setter
    def risk_level(self, value):
        self._risk_level = value
    @property
    def risk_note(self):
        return self._risk_note

    @risk_note.setter
    def risk_note(self, value):
        self._risk_note = value
    @property
    def risk_score(self):
        return self._risk_score

    @risk_score.setter
    def risk_score(self, value):
        self._risk_score = value
    @property
    def source_type(self):
        return self._source_type

    @source_type.setter
    def source_type(self, value):
        self._source_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.risk_evaluation_detail:
            if hasattr(self.risk_evaluation_detail, 'to_alipay_dict'):
                params['risk_evaluation_detail'] = self.risk_evaluation_detail.to_alipay_dict()
            else:
                params['risk_evaluation_detail'] = self.risk_evaluation_detail
        if self.risk_event:
            if hasattr(self.risk_event, 'to_alipay_dict'):
                params['risk_event'] = self.risk_event.to_alipay_dict()
            else:
                params['risk_event'] = self.risk_event
        if self.risk_level:
            if hasattr(self.risk_level, 'to_alipay_dict'):
                params['risk_level'] = self.risk_level.to_alipay_dict()
            else:
                params['risk_level'] = self.risk_level
        if self.risk_note:
            if hasattr(self.risk_note, 'to_alipay_dict'):
                params['risk_note'] = self.risk_note.to_alipay_dict()
            else:
                params['risk_note'] = self.risk_note
        if self.risk_score:
            if hasattr(self.risk_score, 'to_alipay_dict'):
                params['risk_score'] = self.risk_score.to_alipay_dict()
            else:
                params['risk_score'] = self.risk_score
        if self.source_type:
            if hasattr(self.source_type, 'to_alipay_dict'):
                params['source_type'] = self.source_type.to_alipay_dict()
            else:
                params['source_type'] = self.source_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RiskRuleResultDTO()
        if 'risk_evaluation_detail' in d:
            o.risk_evaluation_detail = d['risk_evaluation_detail']
        if 'risk_event' in d:
            o.risk_event = d['risk_event']
        if 'risk_level' in d:
            o.risk_level = d['risk_level']
        if 'risk_note' in d:
            o.risk_note = d['risk_note']
        if 'risk_score' in d:
            o.risk_score = d['risk_score']
        if 'source_type' in d:
            o.source_type = d['source_type']
        return o


