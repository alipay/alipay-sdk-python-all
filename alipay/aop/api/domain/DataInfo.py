#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DataInfo(object):

    def __init__(self):
        self._arrangement = None
        self._contact_time = None
        self._fail_detail = None
        self._fail_reason = None
        self._follow_up_plan = None
        self._reject_detail = None
        self._reject_reason = None

    @property
    def arrangement(self):
        return self._arrangement

    @arrangement.setter
    def arrangement(self, value):
        self._arrangement = value
    @property
    def contact_time(self):
        return self._contact_time

    @contact_time.setter
    def contact_time(self, value):
        self._contact_time = value
    @property
    def fail_detail(self):
        return self._fail_detail

    @fail_detail.setter
    def fail_detail(self, value):
        self._fail_detail = value
    @property
    def fail_reason(self):
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, value):
        self._fail_reason = value
    @property
    def follow_up_plan(self):
        return self._follow_up_plan

    @follow_up_plan.setter
    def follow_up_plan(self, value):
        self._follow_up_plan = value
    @property
    def reject_detail(self):
        return self._reject_detail

    @reject_detail.setter
    def reject_detail(self, value):
        self._reject_detail = value
    @property
    def reject_reason(self):
        return self._reject_reason

    @reject_reason.setter
    def reject_reason(self, value):
        self._reject_reason = value


    def to_alipay_dict(self):
        params = dict()
        if self.arrangement:
            if hasattr(self.arrangement, 'to_alipay_dict'):
                params['arrangement'] = self.arrangement.to_alipay_dict()
            else:
                params['arrangement'] = self.arrangement
        if self.contact_time:
            if hasattr(self.contact_time, 'to_alipay_dict'):
                params['contact_time'] = self.contact_time.to_alipay_dict()
            else:
                params['contact_time'] = self.contact_time
        if self.fail_detail:
            if hasattr(self.fail_detail, 'to_alipay_dict'):
                params['fail_detail'] = self.fail_detail.to_alipay_dict()
            else:
                params['fail_detail'] = self.fail_detail
        if self.fail_reason:
            if hasattr(self.fail_reason, 'to_alipay_dict'):
                params['fail_reason'] = self.fail_reason.to_alipay_dict()
            else:
                params['fail_reason'] = self.fail_reason
        if self.follow_up_plan:
            if hasattr(self.follow_up_plan, 'to_alipay_dict'):
                params['follow_up_plan'] = self.follow_up_plan.to_alipay_dict()
            else:
                params['follow_up_plan'] = self.follow_up_plan
        if self.reject_detail:
            if hasattr(self.reject_detail, 'to_alipay_dict'):
                params['reject_detail'] = self.reject_detail.to_alipay_dict()
            else:
                params['reject_detail'] = self.reject_detail
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
        o = DataInfo()
        if 'arrangement' in d:
            o.arrangement = d['arrangement']
        if 'contact_time' in d:
            o.contact_time = d['contact_time']
        if 'fail_detail' in d:
            o.fail_detail = d['fail_detail']
        if 'fail_reason' in d:
            o.fail_reason = d['fail_reason']
        if 'follow_up_plan' in d:
            o.follow_up_plan = d['follow_up_plan']
        if 'reject_detail' in d:
            o.reject_detail = d['reject_detail']
        if 'reject_reason' in d:
            o.reject_reason = d['reject_reason']
        return o


