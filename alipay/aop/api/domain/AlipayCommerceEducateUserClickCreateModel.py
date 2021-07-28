#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEducateUserClickCreateModel(object):

    def __init__(self):
        self._city_code = None
        self._click_time = None
        self._company_name = None
        self._date = None
        self._features = None
        self._is_apply_job = None
        self._job_id = None
        self._parttime_job_name = None
        self._stay_avg_time = None
        self._user_id = None

    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def click_time(self):
        return self._click_time

    @click_time.setter
    def click_time(self, value):
        self._click_time = value
    @property
    def company_name(self):
        return self._company_name

    @company_name.setter
    def company_name(self, value):
        self._company_name = value
    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._date = value
    @property
    def features(self):
        return self._features

    @features.setter
    def features(self, value):
        self._features = value
    @property
    def is_apply_job(self):
        return self._is_apply_job

    @is_apply_job.setter
    def is_apply_job(self, value):
        self._is_apply_job = value
    @property
    def job_id(self):
        return self._job_id

    @job_id.setter
    def job_id(self, value):
        self._job_id = value
    @property
    def parttime_job_name(self):
        return self._parttime_job_name

    @parttime_job_name.setter
    def parttime_job_name(self, value):
        self._parttime_job_name = value
    @property
    def stay_avg_time(self):
        return self._stay_avg_time

    @stay_avg_time.setter
    def stay_avg_time(self, value):
        self._stay_avg_time = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.click_time:
            if hasattr(self.click_time, 'to_alipay_dict'):
                params['click_time'] = self.click_time.to_alipay_dict()
            else:
                params['click_time'] = self.click_time
        if self.company_name:
            if hasattr(self.company_name, 'to_alipay_dict'):
                params['company_name'] = self.company_name.to_alipay_dict()
            else:
                params['company_name'] = self.company_name
        if self.date:
            if hasattr(self.date, 'to_alipay_dict'):
                params['date'] = self.date.to_alipay_dict()
            else:
                params['date'] = self.date
        if self.features:
            if hasattr(self.features, 'to_alipay_dict'):
                params['features'] = self.features.to_alipay_dict()
            else:
                params['features'] = self.features
        if self.is_apply_job:
            if hasattr(self.is_apply_job, 'to_alipay_dict'):
                params['is_apply_job'] = self.is_apply_job.to_alipay_dict()
            else:
                params['is_apply_job'] = self.is_apply_job
        if self.job_id:
            if hasattr(self.job_id, 'to_alipay_dict'):
                params['job_id'] = self.job_id.to_alipay_dict()
            else:
                params['job_id'] = self.job_id
        if self.parttime_job_name:
            if hasattr(self.parttime_job_name, 'to_alipay_dict'):
                params['parttime_job_name'] = self.parttime_job_name.to_alipay_dict()
            else:
                params['parttime_job_name'] = self.parttime_job_name
        if self.stay_avg_time:
            if hasattr(self.stay_avg_time, 'to_alipay_dict'):
                params['stay_avg_time'] = self.stay_avg_time.to_alipay_dict()
            else:
                params['stay_avg_time'] = self.stay_avg_time
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEducateUserClickCreateModel()
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'click_time' in d:
            o.click_time = d['click_time']
        if 'company_name' in d:
            o.company_name = d['company_name']
        if 'date' in d:
            o.date = d['date']
        if 'features' in d:
            o.features = d['features']
        if 'is_apply_job' in d:
            o.is_apply_job = d['is_apply_job']
        if 'job_id' in d:
            o.job_id = d['job_id']
        if 'parttime_job_name' in d:
            o.parttime_job_name = d['parttime_job_name']
        if 'stay_avg_time' in d:
            o.stay_avg_time = d['stay_avg_time']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


