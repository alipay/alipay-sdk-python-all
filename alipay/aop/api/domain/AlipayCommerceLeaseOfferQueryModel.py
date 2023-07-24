#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceLeaseOfferQueryModel(object):

    def __init__(self):
        self._lessor_pid = None
        self._plan_id = None

    @property
    def lessor_pid(self):
        return self._lessor_pid

    @lessor_pid.setter
    def lessor_pid(self, value):
        self._lessor_pid = value
    @property
    def plan_id(self):
        return self._plan_id

    @plan_id.setter
    def plan_id(self, value):
        self._plan_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.lessor_pid:
            if hasattr(self.lessor_pid, 'to_alipay_dict'):
                params['lessor_pid'] = self.lessor_pid.to_alipay_dict()
            else:
                params['lessor_pid'] = self.lessor_pid
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
        o = AlipayCommerceLeaseOfferQueryModel()
        if 'lessor_pid' in d:
            o.lessor_pid = d['lessor_pid']
        if 'plan_id' in d:
            o.plan_id = d['plan_id']
        return o


