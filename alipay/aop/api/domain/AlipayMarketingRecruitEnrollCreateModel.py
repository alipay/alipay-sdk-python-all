#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RecruitEnrollInfo import RecruitEnrollInfo


class AlipayMarketingRecruitEnrollCreateModel(object):

    def __init__(self):
        self._enroll_info = None
        self._out_biz_no = None
        self._plan_id = None

    @property
    def enroll_info(self):
        return self._enroll_info

    @enroll_info.setter
    def enroll_info(self, value):
        if isinstance(value, RecruitEnrollInfo):
            self._enroll_info = value
        else:
            self._enroll_info = RecruitEnrollInfo.from_alipay_dict(value)
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
        if self.enroll_info:
            if hasattr(self.enroll_info, 'to_alipay_dict'):
                params['enroll_info'] = self.enroll_info.to_alipay_dict()
            else:
                params['enroll_info'] = self.enroll_info
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
        o = AlipayMarketingRecruitEnrollCreateModel()
        if 'enroll_info' in d:
            o.enroll_info = d['enroll_info']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'plan_id' in d:
            o.plan_id = d['plan_id']
        return o


