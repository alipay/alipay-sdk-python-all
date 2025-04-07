#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppIndustryRecruitEmployerAddModel(object):

    def __init__(self):
        self._new_register = None
        self._open_id = None
        self._out_hire_user_id = None
        self._register_time = None
        self._release_job = None
        self._user_id = None

    @property
    def new_register(self):
        return self._new_register

    @new_register.setter
    def new_register(self, value):
        self._new_register = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def out_hire_user_id(self):
        return self._out_hire_user_id

    @out_hire_user_id.setter
    def out_hire_user_id(self, value):
        self._out_hire_user_id = value
    @property
    def register_time(self):
        return self._register_time

    @register_time.setter
    def register_time(self, value):
        self._register_time = value
    @property
    def release_job(self):
        return self._release_job

    @release_job.setter
    def release_job(self, value):
        self._release_job = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.new_register:
            if hasattr(self.new_register, 'to_alipay_dict'):
                params['new_register'] = self.new_register.to_alipay_dict()
            else:
                params['new_register'] = self.new_register
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.out_hire_user_id:
            if hasattr(self.out_hire_user_id, 'to_alipay_dict'):
                params['out_hire_user_id'] = self.out_hire_user_id.to_alipay_dict()
            else:
                params['out_hire_user_id'] = self.out_hire_user_id
        if self.register_time:
            if hasattr(self.register_time, 'to_alipay_dict'):
                params['register_time'] = self.register_time.to_alipay_dict()
            else:
                params['register_time'] = self.register_time
        if self.release_job:
            if hasattr(self.release_job, 'to_alipay_dict'):
                params['release_job'] = self.release_job.to_alipay_dict()
            else:
                params['release_job'] = self.release_job
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
        o = AlipayEbppIndustryRecruitEmployerAddModel()
        if 'new_register' in d:
            o.new_register = d['new_register']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'out_hire_user_id' in d:
            o.out_hire_user_id = d['out_hire_user_id']
        if 'register_time' in d:
            o.register_time = d['register_time']
        if 'release_job' in d:
            o.release_job = d['release_job']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


