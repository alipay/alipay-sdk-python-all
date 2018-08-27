#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ClaimProgress import ClaimProgress


class InsClaim(object):

    def __init__(self):
        self._biz_data = None
        self._claim_fee = None
        self._claim_no = None
        self._claim_pay_time = None
        self._claim_progress = None
        self._claim_status = None
        self._out_request_no = None
        self._reject_reason = None

    @property
    def biz_data(self):
        return self._biz_data

    @biz_data.setter
    def biz_data(self, value):
        self._biz_data = value
    @property
    def claim_fee(self):
        return self._claim_fee

    @claim_fee.setter
    def claim_fee(self, value):
        self._claim_fee = value
    @property
    def claim_no(self):
        return self._claim_no

    @claim_no.setter
    def claim_no(self, value):
        self._claim_no = value
    @property
    def claim_pay_time(self):
        return self._claim_pay_time

    @claim_pay_time.setter
    def claim_pay_time(self, value):
        self._claim_pay_time = value
    @property
    def claim_progress(self):
        return self._claim_progress

    @claim_progress.setter
    def claim_progress(self, value):
        if isinstance(value, list):
            self._claim_progress = list()
            for i in value:
                if isinstance(i, ClaimProgress):
                    self._claim_progress.append(i)
                else:
                    self._claim_progress.append(ClaimProgress.from_alipay_dict(i))
    @property
    def claim_status(self):
        return self._claim_status

    @claim_status.setter
    def claim_status(self, value):
        self._claim_status = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def reject_reason(self):
        return self._reject_reason

    @reject_reason.setter
    def reject_reason(self, value):
        self._reject_reason = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_data:
            if hasattr(self.biz_data, 'to_alipay_dict'):
                params['biz_data'] = self.biz_data.to_alipay_dict()
            else:
                params['biz_data'] = self.biz_data
        if self.claim_fee:
            if hasattr(self.claim_fee, 'to_alipay_dict'):
                params['claim_fee'] = self.claim_fee.to_alipay_dict()
            else:
                params['claim_fee'] = self.claim_fee
        if self.claim_no:
            if hasattr(self.claim_no, 'to_alipay_dict'):
                params['claim_no'] = self.claim_no.to_alipay_dict()
            else:
                params['claim_no'] = self.claim_no
        if self.claim_pay_time:
            if hasattr(self.claim_pay_time, 'to_alipay_dict'):
                params['claim_pay_time'] = self.claim_pay_time.to_alipay_dict()
            else:
                params['claim_pay_time'] = self.claim_pay_time
        if self.claim_progress:
            if isinstance(self.claim_progress, list):
                for i in range(0, len(self.claim_progress)):
                    element = self.claim_progress[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.claim_progress[i] = element.to_alipay_dict()
            if hasattr(self.claim_progress, 'to_alipay_dict'):
                params['claim_progress'] = self.claim_progress.to_alipay_dict()
            else:
                params['claim_progress'] = self.claim_progress
        if self.claim_status:
            if hasattr(self.claim_status, 'to_alipay_dict'):
                params['claim_status'] = self.claim_status.to_alipay_dict()
            else:
                params['claim_status'] = self.claim_status
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        if self.reject_reason:
            if hasattr(self.reject_reason, 'to_alipay_dict'):
                params['reject_reason'] = self.reject_reason.to_alipay_dict()
            else:
                params['reject_reason'] = self.reject_reason
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InsClaim()
        if 'biz_data' in d:
            o.biz_data = d['biz_data']
        if 'claim_fee' in d:
            o.claim_fee = d['claim_fee']
        if 'claim_no' in d:
            o.claim_no = d['claim_no']
        if 'claim_pay_time' in d:
            o.claim_pay_time = d['claim_pay_time']
        if 'claim_progress' in d:
            o.claim_progress = d['claim_progress']
        if 'claim_status' in d:
            o.claim_status = d['claim_status']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'reject_reason' in d:
            o.reject_reason = d['reject_reason']
        return o


