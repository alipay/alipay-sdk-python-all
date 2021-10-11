#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayIserviceCliveFeedbackSubmitModel(object):

    def __init__(self):
        self._conversation_id = None
        self._feedback_note = None
        self._score = None
        self._visitor_id = None

    @property
    def conversation_id(self):
        return self._conversation_id

    @conversation_id.setter
    def conversation_id(self, value):
        self._conversation_id = value
    @property
    def feedback_note(self):
        return self._feedback_note

    @feedback_note.setter
    def feedback_note(self, value):
        self._feedback_note = value
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = value
    @property
    def visitor_id(self):
        return self._visitor_id

    @visitor_id.setter
    def visitor_id(self, value):
        self._visitor_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.conversation_id:
            if hasattr(self.conversation_id, 'to_alipay_dict'):
                params['conversation_id'] = self.conversation_id.to_alipay_dict()
            else:
                params['conversation_id'] = self.conversation_id
        if self.feedback_note:
            if hasattr(self.feedback_note, 'to_alipay_dict'):
                params['feedback_note'] = self.feedback_note.to_alipay_dict()
            else:
                params['feedback_note'] = self.feedback_note
        if self.score:
            if hasattr(self.score, 'to_alipay_dict'):
                params['score'] = self.score.to_alipay_dict()
            else:
                params['score'] = self.score
        if self.visitor_id:
            if hasattr(self.visitor_id, 'to_alipay_dict'):
                params['visitor_id'] = self.visitor_id.to_alipay_dict()
            else:
                params['visitor_id'] = self.visitor_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayIserviceCliveFeedbackSubmitModel()
        if 'conversation_id' in d:
            o.conversation_id = d['conversation_id']
        if 'feedback_note' in d:
            o.feedback_note = d['feedback_note']
        if 'score' in d:
            o.score = d['score']
        if 'visitor_id' in d:
            o.visitor_id = d['visitor_id']
        return o


