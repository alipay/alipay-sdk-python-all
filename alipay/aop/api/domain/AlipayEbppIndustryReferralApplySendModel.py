#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppIndustryReferralApplySendModel(object):

    def __init__(self):
        self._candidate_name = None
        self._candidate_phone = None
        self._city_code = None
        self._job_id = None
        self._out_biz_no = None
        self._recommender_id = None
        self._test_order = None

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
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def job_id(self):
        return self._job_id

    @job_id.setter
    def job_id(self, value):
        self._job_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def recommender_id(self):
        return self._recommender_id

    @recommender_id.setter
    def recommender_id(self, value):
        self._recommender_id = value
    @property
    def test_order(self):
        return self._test_order

    @test_order.setter
    def test_order(self, value):
        self._test_order = value


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
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.job_id:
            if hasattr(self.job_id, 'to_alipay_dict'):
                params['job_id'] = self.job_id.to_alipay_dict()
            else:
                params['job_id'] = self.job_id
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.recommender_id:
            if hasattr(self.recommender_id, 'to_alipay_dict'):
                params['recommender_id'] = self.recommender_id.to_alipay_dict()
            else:
                params['recommender_id'] = self.recommender_id
        if self.test_order:
            if hasattr(self.test_order, 'to_alipay_dict'):
                params['test_order'] = self.test_order.to_alipay_dict()
            else:
                params['test_order'] = self.test_order
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppIndustryReferralApplySendModel()
        if 'candidate_name' in d:
            o.candidate_name = d['candidate_name']
        if 'candidate_phone' in d:
            o.candidate_phone = d['candidate_phone']
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'job_id' in d:
            o.job_id = d['job_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'recommender_id' in d:
            o.recommender_id = d['recommender_id']
        if 'test_order' in d:
            o.test_order = d['test_order']
        return o


