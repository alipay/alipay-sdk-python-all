#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EpOperationAbnormalInfo(object):

    def __init__(self):
        self._decision_making_organ_in = None
        self._decision_making_organ_out = None
        self._error_reason = None
        self._in_date = None
        self._out_date = None
        self._out_reason = None

    @property
    def decision_making_organ_in(self):
        return self._decision_making_organ_in

    @decision_making_organ_in.setter
    def decision_making_organ_in(self, value):
        self._decision_making_organ_in = value
    @property
    def decision_making_organ_out(self):
        return self._decision_making_organ_out

    @decision_making_organ_out.setter
    def decision_making_organ_out(self, value):
        self._decision_making_organ_out = value
    @property
    def error_reason(self):
        return self._error_reason

    @error_reason.setter
    def error_reason(self, value):
        self._error_reason = value
    @property
    def in_date(self):
        return self._in_date

    @in_date.setter
    def in_date(self, value):
        self._in_date = value
    @property
    def out_date(self):
        return self._out_date

    @out_date.setter
    def out_date(self, value):
        self._out_date = value
    @property
    def out_reason(self):
        return self._out_reason

    @out_reason.setter
    def out_reason(self, value):
        self._out_reason = value


    def to_alipay_dict(self):
        params = dict()
        if self.decision_making_organ_in:
            if hasattr(self.decision_making_organ_in, 'to_alipay_dict'):
                params['decision_making_organ_in'] = self.decision_making_organ_in.to_alipay_dict()
            else:
                params['decision_making_organ_in'] = self.decision_making_organ_in
        if self.decision_making_organ_out:
            if hasattr(self.decision_making_organ_out, 'to_alipay_dict'):
                params['decision_making_organ_out'] = self.decision_making_organ_out.to_alipay_dict()
            else:
                params['decision_making_organ_out'] = self.decision_making_organ_out
        if self.error_reason:
            if hasattr(self.error_reason, 'to_alipay_dict'):
                params['error_reason'] = self.error_reason.to_alipay_dict()
            else:
                params['error_reason'] = self.error_reason
        if self.in_date:
            if hasattr(self.in_date, 'to_alipay_dict'):
                params['in_date'] = self.in_date.to_alipay_dict()
            else:
                params['in_date'] = self.in_date
        if self.out_date:
            if hasattr(self.out_date, 'to_alipay_dict'):
                params['out_date'] = self.out_date.to_alipay_dict()
            else:
                params['out_date'] = self.out_date
        if self.out_reason:
            if hasattr(self.out_reason, 'to_alipay_dict'):
                params['out_reason'] = self.out_reason.to_alipay_dict()
            else:
                params['out_reason'] = self.out_reason
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EpOperationAbnormalInfo()
        if 'decision_making_organ_in' in d:
            o.decision_making_organ_in = d['decision_making_organ_in']
        if 'decision_making_organ_out' in d:
            o.decision_making_organ_out = d['decision_making_organ_out']
        if 'error_reason' in d:
            o.error_reason = d['error_reason']
        if 'in_date' in d:
            o.in_date = d['in_date']
        if 'out_date' in d:
            o.out_date = d['out_date']
        if 'out_reason' in d:
            o.out_reason = d['out_reason']
        return o


