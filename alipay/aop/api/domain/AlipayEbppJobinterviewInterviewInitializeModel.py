#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayEbppJobinterviewInterviewInitializeModel(object):

    def __init__(self):
        self._channel = None
        self._external_candidate_id = None
        self._gender = None
        self._id_card = None
        self._job_city_code = None
        self._job_id = None
        self._job_name = None
        self._name = None
        self._phone = None
        self._room_id = None
        self._tenant_id = None

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def external_candidate_id(self):
        return self._external_candidate_id

    @external_candidate_id.setter
    def external_candidate_id(self, value):
        self._external_candidate_id = value
    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        self._gender = value
    @property
    def id_card(self):
        return self._id_card

    @id_card.setter
    def id_card(self, value):
        self._id_card = value
    @property
    def job_city_code(self):
        return self._job_city_code

    @job_city_code.setter
    def job_city_code(self, value):
        self._job_city_code = value
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
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value
    @property
    def room_id(self):
        return self._room_id

    @room_id.setter
    def room_id(self, value):
        self._room_id = value
    @property
    def tenant_id(self):
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, value):
        self._tenant_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.external_candidate_id:
            if hasattr(self.external_candidate_id, 'to_alipay_dict'):
                params['external_candidate_id'] = self.external_candidate_id.to_alipay_dict()
            else:
                params['external_candidate_id'] = self.external_candidate_id
        if self.gender:
            if hasattr(self.gender, 'to_alipay_dict'):
                params['gender'] = self.gender.to_alipay_dict()
            else:
                params['gender'] = self.gender
        if self.id_card:
            if hasattr(self.id_card, 'to_alipay_dict'):
                params['id_card'] = self.id_card.to_alipay_dict()
            else:
                params['id_card'] = self.id_card
        if self.job_city_code:
            if hasattr(self.job_city_code, 'to_alipay_dict'):
                params['job_city_code'] = self.job_city_code.to_alipay_dict()
            else:
                params['job_city_code'] = self.job_city_code
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
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.phone:
            if hasattr(self.phone, 'to_alipay_dict'):
                params['phone'] = self.phone.to_alipay_dict()
            else:
                params['phone'] = self.phone
        if self.room_id:
            if hasattr(self.room_id, 'to_alipay_dict'):
                params['room_id'] = self.room_id.to_alipay_dict()
            else:
                params['room_id'] = self.room_id
        if self.tenant_id:
            if hasattr(self.tenant_id, 'to_alipay_dict'):
                params['tenant_id'] = self.tenant_id.to_alipay_dict()
            else:
                params['tenant_id'] = self.tenant_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppJobinterviewInterviewInitializeModel()
        if 'channel' in d:
            o.channel = d['channel']
        if 'external_candidate_id' in d:
            o.external_candidate_id = d['external_candidate_id']
        if 'gender' in d:
            o.gender = d['gender']
        if 'id_card' in d:
            o.id_card = d['id_card']
        if 'job_city_code' in d:
            o.job_city_code = d['job_city_code']
        if 'job_id' in d:
            o.job_id = d['job_id']
        if 'job_name' in d:
            o.job_name = d['job_name']
        if 'name' in d:
            o.name = d['name']
        if 'phone' in d:
            o.phone = d['phone']
        if 'room_id' in d:
            o.room_id = d['room_id']
        if 'tenant_id' in d:
            o.tenant_id = d['tenant_id']
        return o


