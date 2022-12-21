#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCustomerJobworthQuickhireSubmitModel(object):

    def __init__(self):
        self._age = None
        self._contact_no = None
        self._deliver_id = None
        self._deliver_time = None
        self._deliver_type = None
        self._gender = None
        self._identity = None
        self._open_id = None
        self._recruit_code_id = None
        self._service_id = None
        self._user_id = None
        self._user_name = None

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value
    @property
    def contact_no(self):
        return self._contact_no

    @contact_no.setter
    def contact_no(self, value):
        self._contact_no = value
    @property
    def deliver_id(self):
        return self._deliver_id

    @deliver_id.setter
    def deliver_id(self, value):
        self._deliver_id = value
    @property
    def deliver_time(self):
        return self._deliver_time

    @deliver_time.setter
    def deliver_time(self, value):
        self._deliver_time = value
    @property
    def deliver_type(self):
        return self._deliver_type

    @deliver_type.setter
    def deliver_type(self, value):
        self._deliver_type = value
    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        self._gender = value
    @property
    def identity(self):
        return self._identity

    @identity.setter
    def identity(self, value):
        self._identity = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def recruit_code_id(self):
        return self._recruit_code_id

    @recruit_code_id.setter
    def recruit_code_id(self, value):
        self._recruit_code_id = value
    @property
    def service_id(self):
        return self._service_id

    @service_id.setter
    def service_id(self, value):
        self._service_id = value
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
        if self.age:
            if hasattr(self.age, 'to_alipay_dict'):
                params['age'] = self.age.to_alipay_dict()
            else:
                params['age'] = self.age
        if self.contact_no:
            if hasattr(self.contact_no, 'to_alipay_dict'):
                params['contact_no'] = self.contact_no.to_alipay_dict()
            else:
                params['contact_no'] = self.contact_no
        if self.deliver_id:
            if hasattr(self.deliver_id, 'to_alipay_dict'):
                params['deliver_id'] = self.deliver_id.to_alipay_dict()
            else:
                params['deliver_id'] = self.deliver_id
        if self.deliver_time:
            if hasattr(self.deliver_time, 'to_alipay_dict'):
                params['deliver_time'] = self.deliver_time.to_alipay_dict()
            else:
                params['deliver_time'] = self.deliver_time
        if self.deliver_type:
            if hasattr(self.deliver_type, 'to_alipay_dict'):
                params['deliver_type'] = self.deliver_type.to_alipay_dict()
            else:
                params['deliver_type'] = self.deliver_type
        if self.gender:
            if hasattr(self.gender, 'to_alipay_dict'):
                params['gender'] = self.gender.to_alipay_dict()
            else:
                params['gender'] = self.gender
        if self.identity:
            if hasattr(self.identity, 'to_alipay_dict'):
                params['identity'] = self.identity.to_alipay_dict()
            else:
                params['identity'] = self.identity
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.recruit_code_id:
            if hasattr(self.recruit_code_id, 'to_alipay_dict'):
                params['recruit_code_id'] = self.recruit_code_id.to_alipay_dict()
            else:
                params['recruit_code_id'] = self.recruit_code_id
        if self.service_id:
            if hasattr(self.service_id, 'to_alipay_dict'):
                params['service_id'] = self.service_id.to_alipay_dict()
            else:
                params['service_id'] = self.service_id
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
        o = ZhimaCustomerJobworthQuickhireSubmitModel()
        if 'age' in d:
            o.age = d['age']
        if 'contact_no' in d:
            o.contact_no = d['contact_no']
        if 'deliver_id' in d:
            o.deliver_id = d['deliver_id']
        if 'deliver_time' in d:
            o.deliver_time = d['deliver_time']
        if 'deliver_type' in d:
            o.deliver_type = d['deliver_type']
        if 'gender' in d:
            o.gender = d['gender']
        if 'identity' in d:
            o.identity = d['identity']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'recruit_code_id' in d:
            o.recruit_code_id = d['recruit_code_id']
        if 'service_id' in d:
            o.service_id = d['service_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'user_name' in d:
            o.user_name = d['user_name']
        return o


