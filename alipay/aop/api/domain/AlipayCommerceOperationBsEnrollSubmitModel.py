#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BsEnrollParticipant import BsEnrollParticipant
from alipay.aop.api.domain.BsEnrollNewParticipant import BsEnrollNewParticipant


class AlipayCommerceOperationBsEnrollSubmitModel(object):

    def __init__(self):
        self._out_activity_id = None
        self._participants = None
        self._participants_new = None
        self._plan_id = None
        self._solution_code = None

    @property
    def out_activity_id(self):
        return self._out_activity_id

    @out_activity_id.setter
    def out_activity_id(self, value):
        self._out_activity_id = value
    @property
    def participants(self):
        return self._participants

    @participants.setter
    def participants(self, value):
        if isinstance(value, list):
            self._participants = list()
            for i in value:
                if isinstance(i, BsEnrollParticipant):
                    self._participants.append(i)
                else:
                    self._participants.append(BsEnrollParticipant.from_alipay_dict(i))
    @property
    def participants_new(self):
        return self._participants_new

    @participants_new.setter
    def participants_new(self, value):
        if isinstance(value, list):
            self._participants_new = list()
            for i in value:
                if isinstance(i, BsEnrollNewParticipant):
                    self._participants_new.append(i)
                else:
                    self._participants_new.append(BsEnrollNewParticipant.from_alipay_dict(i))
    @property
    def plan_id(self):
        return self._plan_id

    @plan_id.setter
    def plan_id(self, value):
        self._plan_id = value
    @property
    def solution_code(self):
        return self._solution_code

    @solution_code.setter
    def solution_code(self, value):
        self._solution_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.out_activity_id:
            if hasattr(self.out_activity_id, 'to_alipay_dict'):
                params['out_activity_id'] = self.out_activity_id.to_alipay_dict()
            else:
                params['out_activity_id'] = self.out_activity_id
        if self.participants:
            if isinstance(self.participants, list):
                for i in range(0, len(self.participants)):
                    element = self.participants[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.participants[i] = element.to_alipay_dict()
            if hasattr(self.participants, 'to_alipay_dict'):
                params['participants'] = self.participants.to_alipay_dict()
            else:
                params['participants'] = self.participants
        if self.participants_new:
            if isinstance(self.participants_new, list):
                for i in range(0, len(self.participants_new)):
                    element = self.participants_new[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.participants_new[i] = element.to_alipay_dict()
            if hasattr(self.participants_new, 'to_alipay_dict'):
                params['participants_new'] = self.participants_new.to_alipay_dict()
            else:
                params['participants_new'] = self.participants_new
        if self.plan_id:
            if hasattr(self.plan_id, 'to_alipay_dict'):
                params['plan_id'] = self.plan_id.to_alipay_dict()
            else:
                params['plan_id'] = self.plan_id
        if self.solution_code:
            if hasattr(self.solution_code, 'to_alipay_dict'):
                params['solution_code'] = self.solution_code.to_alipay_dict()
            else:
                params['solution_code'] = self.solution_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceOperationBsEnrollSubmitModel()
        if 'out_activity_id' in d:
            o.out_activity_id = d['out_activity_id']
        if 'participants' in d:
            o.participants = d['participants']
        if 'participants_new' in d:
            o.participants_new = d['participants_new']
        if 'plan_id' in d:
            o.plan_id = d['plan_id']
        if 'solution_code' in d:
            o.solution_code = d['solution_code']
        return o


