#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InsOpenSimplestIssueCustomParamDTO(object):

    def __init__(self):
        self._city = None
        self._job = None
        self._job_category = None
        self._province = None
        self._skip_risk_underwrite = None

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value
    @property
    def job(self):
        return self._job

    @job.setter
    def job(self, value):
        self._job = value
    @property
    def job_category(self):
        return self._job_category

    @job_category.setter
    def job_category(self, value):
        self._job_category = value
    @property
    def province(self):
        return self._province

    @province.setter
    def province(self, value):
        self._province = value
    @property
    def skip_risk_underwrite(self):
        return self._skip_risk_underwrite

    @skip_risk_underwrite.setter
    def skip_risk_underwrite(self, value):
        self._skip_risk_underwrite = value


    def to_alipay_dict(self):
        params = dict()
        if self.city:
            if hasattr(self.city, 'to_alipay_dict'):
                params['city'] = self.city.to_alipay_dict()
            else:
                params['city'] = self.city
        if self.job:
            if hasattr(self.job, 'to_alipay_dict'):
                params['job'] = self.job.to_alipay_dict()
            else:
                params['job'] = self.job
        if self.job_category:
            if hasattr(self.job_category, 'to_alipay_dict'):
                params['job_category'] = self.job_category.to_alipay_dict()
            else:
                params['job_category'] = self.job_category
        if self.province:
            if hasattr(self.province, 'to_alipay_dict'):
                params['province'] = self.province.to_alipay_dict()
            else:
                params['province'] = self.province
        if self.skip_risk_underwrite:
            if hasattr(self.skip_risk_underwrite, 'to_alipay_dict'):
                params['skip_risk_underwrite'] = self.skip_risk_underwrite.to_alipay_dict()
            else:
                params['skip_risk_underwrite'] = self.skip_risk_underwrite
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InsOpenSimplestIssueCustomParamDTO()
        if 'city' in d:
            o.city = d['city']
        if 'job' in d:
            o.job = d['job']
        if 'job_category' in d:
            o.job_category = d['job_category']
        if 'province' in d:
            o.province = d['province']
        if 'skip_risk_underwrite' in d:
            o.skip_risk_underwrite = d['skip_risk_underwrite']
        return o


