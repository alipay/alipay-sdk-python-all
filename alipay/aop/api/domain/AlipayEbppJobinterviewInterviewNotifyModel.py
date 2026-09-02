#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppJobinterviewInterviewNotifyModel(object):

    def __init__(self):
        self._ai_interview_review_reason = None
        self._ai_interview_review_result = None
        self._candidate_id = None
        self._manual_interview_reason = None
        self._manual_interview_result = None
        self._tenant_id = None

    @property
    def ai_interview_review_reason(self):
        return self._ai_interview_review_reason

    @ai_interview_review_reason.setter
    def ai_interview_review_reason(self, value):
        self._ai_interview_review_reason = value
    @property
    def ai_interview_review_result(self):
        return self._ai_interview_review_result

    @ai_interview_review_result.setter
    def ai_interview_review_result(self, value):
        self._ai_interview_review_result = value
    @property
    def candidate_id(self):
        return self._candidate_id

    @candidate_id.setter
    def candidate_id(self, value):
        self._candidate_id = value
    @property
    def manual_interview_reason(self):
        return self._manual_interview_reason

    @manual_interview_reason.setter
    def manual_interview_reason(self, value):
        self._manual_interview_reason = value
    @property
    def manual_interview_result(self):
        return self._manual_interview_result

    @manual_interview_result.setter
    def manual_interview_result(self, value):
        self._manual_interview_result = value
    @property
    def tenant_id(self):
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, value):
        self._tenant_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.ai_interview_review_reason:
            if hasattr(self.ai_interview_review_reason, 'to_alipay_dict'):
                params['ai_interview_review_reason'] = self.ai_interview_review_reason.to_alipay_dict()
            else:
                params['ai_interview_review_reason'] = self.ai_interview_review_reason
        if self.ai_interview_review_result:
            if hasattr(self.ai_interview_review_result, 'to_alipay_dict'):
                params['ai_interview_review_result'] = self.ai_interview_review_result.to_alipay_dict()
            else:
                params['ai_interview_review_result'] = self.ai_interview_review_result
        if self.candidate_id:
            if hasattr(self.candidate_id, 'to_alipay_dict'):
                params['candidate_id'] = self.candidate_id.to_alipay_dict()
            else:
                params['candidate_id'] = self.candidate_id
        if self.manual_interview_reason:
            if hasattr(self.manual_interview_reason, 'to_alipay_dict'):
                params['manual_interview_reason'] = self.manual_interview_reason.to_alipay_dict()
            else:
                params['manual_interview_reason'] = self.manual_interview_reason
        if self.manual_interview_result:
            if hasattr(self.manual_interview_result, 'to_alipay_dict'):
                params['manual_interview_result'] = self.manual_interview_result.to_alipay_dict()
            else:
                params['manual_interview_result'] = self.manual_interview_result
        if self.tenant_id:
            if hasattr(self.tenant_id, 'to_alipay_dict'):
                params['tenant_id'] = self.tenant_id.to_alipay_dict()
            else:
                params['tenant_id'] = self.tenant_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppJobinterviewInterviewNotifyModel()
        if 'ai_interview_review_reason' in d:
            o.ai_interview_review_reason = d['ai_interview_review_reason']
        if 'ai_interview_review_result' in d:
            o.ai_interview_review_result = d['ai_interview_review_result']
        if 'candidate_id' in d:
            o.candidate_id = d['candidate_id']
        if 'manual_interview_reason' in d:
            o.manual_interview_reason = d['manual_interview_reason']
        if 'manual_interview_result' in d:
            o.manual_interview_result = d['manual_interview_result']
        if 'tenant_id' in d:
            o.tenant_id = d['tenant_id']
        return o


