#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class IndirectLegalPersonInfo(object):

    def __init__(self):
        self._auth_letter_img = None
        self._card_back_img = None
        self._card_front_img = None
        self._card_no = None
        self._card_type = None
        self._effect_time = None
        self._expire_time = None
        self._is_benefit_person = None
        self._legal_type = None
        self._person_name = None

    @property
    def auth_letter_img(self):
        return self._auth_letter_img

    @auth_letter_img.setter
    def auth_letter_img(self, value):
        self._auth_letter_img = value
    @property
    def card_back_img(self):
        return self._card_back_img

    @card_back_img.setter
    def card_back_img(self, value):
        self._card_back_img = value
    @property
    def card_front_img(self):
        return self._card_front_img

    @card_front_img.setter
    def card_front_img(self, value):
        self._card_front_img = value
    @property
    def card_no(self):
        return self._card_no

    @card_no.setter
    def card_no(self, value):
        self._card_no = value
    @property
    def card_type(self):
        return self._card_type

    @card_type.setter
    def card_type(self, value):
        self._card_type = value
    @property
    def effect_time(self):
        return self._effect_time

    @effect_time.setter
    def effect_time(self, value):
        self._effect_time = value
    @property
    def expire_time(self):
        return self._expire_time

    @expire_time.setter
    def expire_time(self, value):
        self._expire_time = value
    @property
    def is_benefit_person(self):
        return self._is_benefit_person

    @is_benefit_person.setter
    def is_benefit_person(self, value):
        self._is_benefit_person = value
    @property
    def legal_type(self):
        return self._legal_type

    @legal_type.setter
    def legal_type(self, value):
        self._legal_type = value
    @property
    def person_name(self):
        return self._person_name

    @person_name.setter
    def person_name(self, value):
        self._person_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.auth_letter_img:
            if hasattr(self.auth_letter_img, 'to_alipay_dict'):
                params['auth_letter_img'] = self.auth_letter_img.to_alipay_dict()
            else:
                params['auth_letter_img'] = self.auth_letter_img
        if self.card_back_img:
            if hasattr(self.card_back_img, 'to_alipay_dict'):
                params['card_back_img'] = self.card_back_img.to_alipay_dict()
            else:
                params['card_back_img'] = self.card_back_img
        if self.card_front_img:
            if hasattr(self.card_front_img, 'to_alipay_dict'):
                params['card_front_img'] = self.card_front_img.to_alipay_dict()
            else:
                params['card_front_img'] = self.card_front_img
        if self.card_no:
            if hasattr(self.card_no, 'to_alipay_dict'):
                params['card_no'] = self.card_no.to_alipay_dict()
            else:
                params['card_no'] = self.card_no
        if self.card_type:
            if hasattr(self.card_type, 'to_alipay_dict'):
                params['card_type'] = self.card_type.to_alipay_dict()
            else:
                params['card_type'] = self.card_type
        if self.effect_time:
            if hasattr(self.effect_time, 'to_alipay_dict'):
                params['effect_time'] = self.effect_time.to_alipay_dict()
            else:
                params['effect_time'] = self.effect_time
        if self.expire_time:
            if hasattr(self.expire_time, 'to_alipay_dict'):
                params['expire_time'] = self.expire_time.to_alipay_dict()
            else:
                params['expire_time'] = self.expire_time
        if self.is_benefit_person:
            if hasattr(self.is_benefit_person, 'to_alipay_dict'):
                params['is_benefit_person'] = self.is_benefit_person.to_alipay_dict()
            else:
                params['is_benefit_person'] = self.is_benefit_person
        if self.legal_type:
            if hasattr(self.legal_type, 'to_alipay_dict'):
                params['legal_type'] = self.legal_type.to_alipay_dict()
            else:
                params['legal_type'] = self.legal_type
        if self.person_name:
            if hasattr(self.person_name, 'to_alipay_dict'):
                params['person_name'] = self.person_name.to_alipay_dict()
            else:
                params['person_name'] = self.person_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IndirectLegalPersonInfo()
        if 'auth_letter_img' in d:
            o.auth_letter_img = d['auth_letter_img']
        if 'card_back_img' in d:
            o.card_back_img = d['card_back_img']
        if 'card_front_img' in d:
            o.card_front_img = d['card_front_img']
        if 'card_no' in d:
            o.card_no = d['card_no']
        if 'card_type' in d:
            o.card_type = d['card_type']
        if 'effect_time' in d:
            o.effect_time = d['effect_time']
        if 'expire_time' in d:
            o.expire_time = d['expire_time']
        if 'is_benefit_person' in d:
            o.is_benefit_person = d['is_benefit_person']
        if 'legal_type' in d:
            o.legal_type = d['legal_type']
        if 'person_name' in d:
            o.person_name = d['person_name']
        return o


