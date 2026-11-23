#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceCareerJobinterviewInitializeModel(object):

    def __init__(self):
        self._candidate_gender = None
        self._candidate_id_card = None
        self._candidate_name = None
        self._candidate_phone = None
        self._channel = None
        self._job_city_code = None
        self._job_id = None
        self._job_name = None
        self._out_biz_no = None
        self._room_id = None

    @property
    def candidate_gender(self):
        return self._candidate_gender

    @candidate_gender.setter
    def candidate_gender(self, value):
        self._candidate_gender = value
    @property
    def candidate_id_card(self):
        return self._candidate_id_card

    @candidate_id_card.setter
    def candidate_id_card(self, value):
        self._candidate_id_card = value
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
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
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
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def room_id(self):
        return self._room_id

    @room_id.setter
    def room_id(self, value):
        self._room_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.candidate_gender:
            if hasattr(self.candidate_gender, 'to_alipay_dict'):
                params['candidate_gender'] = self.candidate_gender.to_alipay_dict()
            else:
                params['candidate_gender'] = self.candidate_gender
        if self.candidate_id_card:
            if hasattr(self.candidate_id_card, 'to_alipay_dict'):
                params['candidate_id_card'] = self.candidate_id_card.to_alipay_dict()
            else:
                params['candidate_id_card'] = self.candidate_id_card
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
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
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
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.room_id:
            if hasattr(self.room_id, 'to_alipay_dict'):
                params['room_id'] = self.room_id.to_alipay_dict()
            else:
                params['room_id'] = self.room_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceCareerJobinterviewInitializeModel()
        if 'candidate_gender' in d:
            o.candidate_gender = d['candidate_gender']
        if 'candidate_id_card' in d:
            o.candidate_id_card = d['candidate_id_card']
        if 'candidate_name' in d:
            o.candidate_name = d['candidate_name']
        if 'candidate_phone' in d:
            o.candidate_phone = d['candidate_phone']
        if 'channel' in d:
            o.channel = d['channel']
        if 'job_city_code' in d:
            o.job_city_code = d['job_city_code']
        if 'job_id' in d:
            o.job_id = d['job_id']
        if 'job_name' in d:
            o.job_name = d['job_name']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'room_id' in d:
            o.room_id = d['room_id']
        return o


