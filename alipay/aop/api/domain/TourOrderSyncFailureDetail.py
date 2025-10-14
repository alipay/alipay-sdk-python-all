#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TourOrderSyncFailureDetail(object):

    def __init__(self):
        self._failure_reason = None
        self._out_biz_no = None

    @property
    def failure_reason(self):
        return self._failure_reason

    @failure_reason.setter
    def failure_reason(self, value):
        self._failure_reason = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.failure_reason:
            if hasattr(self.failure_reason, 'to_alipay_dict'):
                params['failure_reason'] = self.failure_reason.to_alipay_dict()
            else:
                params['failure_reason'] = self.failure_reason
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
        o = TourOrderSyncFailureDetail()
        if 'failure_reason' in d:
            o.failure_reason = d['failure_reason']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        return o


