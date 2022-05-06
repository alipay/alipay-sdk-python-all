#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SceneInfo(object):

    def __init__(self):
        self._cert_no = None
        self._company_id = None
        self._company_name = None
        self._employer_visit = None
        self._job_category = None
        self._job_category_id = None
        self._job_id = None
        self._job_name = None
        self._scene_time = None
        self._self_visit = None
        self._source = None
        self._type = None
        self._user_id = None
        self._user_name = None

    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def company_id(self):
        return self._company_id

    @company_id.setter
    def company_id(self, value):
        self._company_id = value
    @property
    def company_name(self):
        return self._company_name

    @company_name.setter
    def company_name(self, value):
        self._company_name = value
    @property
    def employer_visit(self):
        return self._employer_visit

    @employer_visit.setter
    def employer_visit(self, value):
        self._employer_visit = value
    @property
    def job_category(self):
        return self._job_category

    @job_category.setter
    def job_category(self, value):
        self._job_category = value
    @property
    def job_category_id(self):
        return self._job_category_id

    @job_category_id.setter
    def job_category_id(self, value):
        self._job_category_id = value
    @property
    def job_id(self):
        return self._job_id

    @job_id.setter
    def job_id(self, value):
        self._job_id = value
    @property
    def job_name(self):
        return self._job_name

    @job_name.setter
    def job_name(self, value):
        self._job_name = value
    @property
    def scene_time(self):
        return self._scene_time

    @scene_time.setter
    def scene_time(self, value):
        self._scene_time = value
    @property
    def self_visit(self):
        return self._self_visit

    @self_visit.setter
    def self_visit(self, value):
        self._self_visit = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.company_id:
            if hasattr(self.company_id, 'to_alipay_dict'):
                params['company_id'] = self.company_id.to_alipay_dict()
            else:
                params['company_id'] = self.company_id
        if self.company_name:
            if hasattr(self.company_name, 'to_alipay_dict'):
                params['company_name'] = self.company_name.to_alipay_dict()
            else:
                params['company_name'] = self.company_name
        if self.employer_visit:
            if hasattr(self.employer_visit, 'to_alipay_dict'):
                params['employer_visit'] = self.employer_visit.to_alipay_dict()
            else:
                params['employer_visit'] = self.employer_visit
        if self.job_category:
            if hasattr(self.job_category, 'to_alipay_dict'):
                params['job_category'] = self.job_category.to_alipay_dict()
            else:
                params['job_category'] = self.job_category
        if self.job_category_id:
            if hasattr(self.job_category_id, 'to_alipay_dict'):
                params['job_category_id'] = self.job_category_id.to_alipay_dict()
            else:
                params['job_category_id'] = self.job_category_id
        if self.job_id:
            if hasattr(self.job_id, 'to_alipay_dict'):
                params['job_id'] = self.job_id.to_alipay_dict()
            else:
                params['job_id'] = self.job_id
        if self.job_name:
            if hasattr(self.job_name, 'to_alipay_dict'):
                params['job_name'] = self.job_name.to_alipay_dict()
            else:
                params['job_name'] = self.job_name
        if self.scene_time:
            if hasattr(self.scene_time, 'to_alipay_dict'):
                params['scene_time'] = self.scene_time.to_alipay_dict()
            else:
                params['scene_time'] = self.scene_time
        if self.self_visit:
            if hasattr(self.self_visit, 'to_alipay_dict'):
                params['self_visit'] = self.self_visit.to_alipay_dict()
            else:
                params['self_visit'] = self.self_visit
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.user_name:
            if hasattr(self.user_name, 'to_alipay_dict'):
                params['user_name'] = self.user_name.to_alipay_dict()
            else:
                params['user_name'] = self.user_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SceneInfo()
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'company_id' in d:
            o.company_id = d['company_id']
        if 'company_name' in d:
            o.company_name = d['company_name']
        if 'employer_visit' in d:
            o.employer_visit = d['employer_visit']
        if 'job_category' in d:
            o.job_category = d['job_category']
        if 'job_category_id' in d:
            o.job_category_id = d['job_category_id']
        if 'job_id' in d:
            o.job_id = d['job_id']
        if 'job_name' in d:
            o.job_name = d['job_name']
        if 'scene_time' in d:
            o.scene_time = d['scene_time']
        if 'self_visit' in d:
            o.self_visit = d['self_visit']
        if 'source' in d:
            o.source = d['source']
        if 'type' in d:
            o.type = d['type']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'user_name' in d:
            o.user_name = d['user_name']
        return o


