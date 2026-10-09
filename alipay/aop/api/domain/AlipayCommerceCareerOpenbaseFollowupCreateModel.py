#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FollowupCreateContext import FollowupCreateContext


class AlipayCommerceCareerOpenbaseFollowupCreateModel(object):

    def __init__(self):
        self._candidate_name = None
        self._candidate_phone = None
        self._context = None
        self._deadline = None
        self._out_biz_no = None
        self._plan_id = None

    @property
    def candidate_name(self):
        return self._candidate_name

    @candidate_name.setter
    def candidate_name(self, value):
        self._candidate_name = value
    @property
    def candidate_phone(self):
        return self._candidate_phone

    @candidate_phone.setter
    def candidate_phone(self, value):
        self._candidate_phone = value
    @property
    def context(self):
        return self._context

    @context.setter
    def context(self, value):
        if isinstance(value, FollowupCreateContext):
            self._context = value
        else:
            self._context = FollowupCreateContext.from_alipay_dict(value)
    @property
    def deadline(self):
        return self._deadline

    @deadline.setter
    def deadline(self, value):
        self._deadline = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def plan_id(self):
        return self._plan_id

    @plan_id.setter
    def plan_id(self, value):
        self._plan_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.candidate_name:
            if hasattr(self.candidate_name, 'to_alipay_dict'):
                params['candidate_name'] = self.candidate_name.to_alipay_dict()
            else:
                params['candidate_name'] = self.candidate_name
        if self.candidate_phone:
            if hasattr(self.candidate_phone, 'to_alipay_dict'):
                params['candidate_phone'] = self.candidate_phone.to_alipay_dict()
            else:
                params['candidate_phone'] = self.candidate_phone
        if self.context:
            if hasattr(self.context, 'to_alipay_dict'):
                params['context'] = self.context.to_alipay_dict()
            else:
                params['context'] = self.context
        if self.deadline:
            if hasattr(self.deadline, 'to_alipay_dict'):
                params['deadline'] = self.deadline.to_alipay_dict()
            else:
                params['deadline'] = self.deadline
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.plan_id:
            if hasattr(self.plan_id, 'to_alipay_dict'):
                params['plan_id'] = self.plan_id.to_alipay_dict()
            else:
                params['plan_id'] = self.plan_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceCareerOpenbaseFollowupCreateModel()
        if 'candidate_name' in d:
            o.candidate_name = d['candidate_name']
        if 'candidate_phone' in d:
            o.candidate_phone = d['candidate_phone']
        if 'context' in d:
            o.context = d['context']
        if 'deadline' in d:
            o.deadline = d['deadline']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'plan_id' in d:
            o.plan_id = d['plan_id']
        return o


