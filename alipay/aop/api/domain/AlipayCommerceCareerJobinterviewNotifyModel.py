#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceCareerJobinterviewNotifyModel(object):

    def __init__(self):
        self._ai_interview_review_reason = None
        self._ai_interview_review_result = None
        self._entry_status = None
        self._manual_interview_reason = None
        self._manual_interview_result = None
        self._order_no = None
        self._out_biz_no = None

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
    def entry_status(self):
        return self._entry_status

    @entry_status.setter
    def entry_status(self, value):
        self._entry_status = value
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
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value


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
        if self.entry_status:
            if hasattr(self.entry_status, 'to_alipay_dict'):
                params['entry_status'] = self.entry_status.to_alipay_dict()
            else:
                params['entry_status'] = self.entry_status
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
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceCareerJobinterviewNotifyModel()
        if 'ai_interview_review_reason' in d:
            o.ai_interview_review_reason = d['ai_interview_review_reason']
        if 'ai_interview_review_result' in d:
            o.ai_interview_review_result = d['ai_interview_review_result']
        if 'entry_status' in d:
            o.entry_status = d['entry_status']
        if 'manual_interview_reason' in d:
            o.manual_interview_reason = d['manual_interview_reason']
        if 'manual_interview_result' in d:
            o.manual_interview_result = d['manual_interview_result']
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        return o


