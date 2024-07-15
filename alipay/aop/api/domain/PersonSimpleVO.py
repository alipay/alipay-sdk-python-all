#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PersonSimpleVO(object):

    def __init__(self):
        self._cert_id = None
        self._id_country = None
        self._id_no = None
        self._id_type = None
        self._memo = None
        self._nick_name = None
        self._person_classfy_type = None
        self._person_gender = None
        self._person_id = None
        self._person_name = None
        self._person_name_en = None
        self._work_no = None

    @property
    def cert_id(self):
        return self._cert_id

    @cert_id.setter
    def cert_id(self, value):
        self._cert_id = value
    @property
    def id_country(self):
        return self._id_country

    @id_country.setter
    def id_country(self, value):
        self._id_country = value
    @property
    def id_no(self):
        return self._id_no

    @id_no.setter
    def id_no(self, value):
        self._id_no = value
    @property
    def id_type(self):
        return self._id_type

    @id_type.setter
    def id_type(self, value):
        self._id_type = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def nick_name(self):
        return self._nick_name

    @nick_name.setter
    def nick_name(self, value):
        self._nick_name = value
    @property
    def person_classfy_type(self):
        return self._person_classfy_type

    @person_classfy_type.setter
    def person_classfy_type(self, value):
        self._person_classfy_type = value
    @property
    def person_gender(self):
        return self._person_gender

    @person_gender.setter
    def person_gender(self, value):
        self._person_gender = value
    @property
    def person_id(self):
        return self._person_id

    @person_id.setter
    def person_id(self, value):
        self._person_id = value
    @property
    def person_name(self):
        return self._person_name

    @person_name.setter
    def person_name(self, value):
        self._person_name = value
    @property
    def person_name_en(self):
        return self._person_name_en

    @person_name_en.setter
    def person_name_en(self, value):
        self._person_name_en = value
    @property
    def work_no(self):
        return self._work_no

    @work_no.setter
    def work_no(self, value):
        self._work_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.cert_id:
            if hasattr(self.cert_id, 'to_alipay_dict'):
                params['cert_id'] = self.cert_id.to_alipay_dict()
            else:
                params['cert_id'] = self.cert_id
        if self.id_country:
            if hasattr(self.id_country, 'to_alipay_dict'):
                params['id_country'] = self.id_country.to_alipay_dict()
            else:
                params['id_country'] = self.id_country
        if self.id_no:
            if hasattr(self.id_no, 'to_alipay_dict'):
                params['id_no'] = self.id_no.to_alipay_dict()
            else:
                params['id_no'] = self.id_no
        if self.id_type:
            if hasattr(self.id_type, 'to_alipay_dict'):
                params['id_type'] = self.id_type.to_alipay_dict()
            else:
                params['id_type'] = self.id_type
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.nick_name:
            if hasattr(self.nick_name, 'to_alipay_dict'):
                params['nick_name'] = self.nick_name.to_alipay_dict()
            else:
                params['nick_name'] = self.nick_name
        if self.person_classfy_type:
            if hasattr(self.person_classfy_type, 'to_alipay_dict'):
                params['person_classfy_type'] = self.person_classfy_type.to_alipay_dict()
            else:
                params['person_classfy_type'] = self.person_classfy_type
        if self.person_gender:
            if hasattr(self.person_gender, 'to_alipay_dict'):
                params['person_gender'] = self.person_gender.to_alipay_dict()
            else:
                params['person_gender'] = self.person_gender
        if self.person_id:
            if hasattr(self.person_id, 'to_alipay_dict'):
                params['person_id'] = self.person_id.to_alipay_dict()
            else:
                params['person_id'] = self.person_id
        if self.person_name:
            if hasattr(self.person_name, 'to_alipay_dict'):
                params['person_name'] = self.person_name.to_alipay_dict()
            else:
                params['person_name'] = self.person_name
        if self.person_name_en:
            if hasattr(self.person_name_en, 'to_alipay_dict'):
                params['person_name_en'] = self.person_name_en.to_alipay_dict()
            else:
                params['person_name_en'] = self.person_name_en
        if self.work_no:
            if hasattr(self.work_no, 'to_alipay_dict'):
                params['work_no'] = self.work_no.to_alipay_dict()
            else:
                params['work_no'] = self.work_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PersonSimpleVO()
        if 'cert_id' in d:
            o.cert_id = d['cert_id']
        if 'id_country' in d:
            o.id_country = d['id_country']
        if 'id_no' in d:
            o.id_no = d['id_no']
        if 'id_type' in d:
            o.id_type = d['id_type']
        if 'memo' in d:
            o.memo = d['memo']
        if 'nick_name' in d:
            o.nick_name = d['nick_name']
        if 'person_classfy_type' in d:
            o.person_classfy_type = d['person_classfy_type']
        if 'person_gender' in d:
            o.person_gender = d['person_gender']
        if 'person_id' in d:
            o.person_id = d['person_id']
        if 'person_name' in d:
            o.person_name = d['person_name']
        if 'person_name_en' in d:
            o.person_name_en = d['person_name_en']
        if 'work_no' in d:
            o.work_no = d['work_no']
        return o


