#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserCertifyInfoPersonApplyModel(object):

    def __init__(self):
        self._address = None
        self._biz_from = None
        self._cert_expired_date = None
        self._cert_no = None
        self._cert_type = None
        self._city = None
        self._country = None
        self._face_url = None
        self._mobile = None
        self._province = None
        self._sex = None
        self._user_id = None
        self._user_name = None
        self._verso_url = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def biz_from(self):
        return self._biz_from

    @biz_from.setter
    def biz_from(self, value):
        self._biz_from = value
    @property
    def cert_expired_date(self):
        return self._cert_expired_date

    @cert_expired_date.setter
    def cert_expired_date(self, value):
        self._cert_expired_date = value
    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def cert_type(self):
        return self._cert_type

    @cert_type.setter
    def cert_type(self, value):
        self._cert_type = value
    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value
    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, value):
        self._country = value
    @property
    def face_url(self):
        return self._face_url

    @face_url.setter
    def face_url(self, value):
        self._face_url = value
    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, value):
        self._mobile = value
    @property
    def province(self):
        return self._province

    @province.setter
    def province(self, value):
        self._province = value
    @property
    def sex(self):
        return self._sex

    @sex.setter
    def sex(self, value):
        self._sex = value
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
    @property
    def verso_url(self):
        return self._verso_url

    @verso_url.setter
    def verso_url(self, value):
        self._verso_url = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.biz_from:
            if hasattr(self.biz_from, 'to_alipay_dict'):
                params['biz_from'] = self.biz_from.to_alipay_dict()
            else:
                params['biz_from'] = self.biz_from
        if self.cert_expired_date:
            if hasattr(self.cert_expired_date, 'to_alipay_dict'):
                params['cert_expired_date'] = self.cert_expired_date.to_alipay_dict()
            else:
                params['cert_expired_date'] = self.cert_expired_date
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.cert_type:
            if hasattr(self.cert_type, 'to_alipay_dict'):
                params['cert_type'] = self.cert_type.to_alipay_dict()
            else:
                params['cert_type'] = self.cert_type
        if self.city:
            if hasattr(self.city, 'to_alipay_dict'):
                params['city'] = self.city.to_alipay_dict()
            else:
                params['city'] = self.city
        if self.country:
            if hasattr(self.country, 'to_alipay_dict'):
                params['country'] = self.country.to_alipay_dict()
            else:
                params['country'] = self.country
        if self.face_url:
            if hasattr(self.face_url, 'to_alipay_dict'):
                params['face_url'] = self.face_url.to_alipay_dict()
            else:
                params['face_url'] = self.face_url
        if self.mobile:
            if hasattr(self.mobile, 'to_alipay_dict'):
                params['mobile'] = self.mobile.to_alipay_dict()
            else:
                params['mobile'] = self.mobile
        if self.province:
            if hasattr(self.province, 'to_alipay_dict'):
                params['province'] = self.province.to_alipay_dict()
            else:
                params['province'] = self.province
        if self.sex:
            if hasattr(self.sex, 'to_alipay_dict'):
                params['sex'] = self.sex.to_alipay_dict()
            else:
                params['sex'] = self.sex
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
        if self.verso_url:
            if hasattr(self.verso_url, 'to_alipay_dict'):
                params['verso_url'] = self.verso_url.to_alipay_dict()
            else:
                params['verso_url'] = self.verso_url
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserCertifyInfoPersonApplyModel()
        if 'address' in d:
            o.address = d['address']
        if 'biz_from' in d:
            o.biz_from = d['biz_from']
        if 'cert_expired_date' in d:
            o.cert_expired_date = d['cert_expired_date']
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'city' in d:
            o.city = d['city']
        if 'country' in d:
            o.country = d['country']
        if 'face_url' in d:
            o.face_url = d['face_url']
        if 'mobile' in d:
            o.mobile = d['mobile']
        if 'province' in d:
            o.province = d['province']
        if 'sex' in d:
            o.sex = d['sex']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'user_name' in d:
            o.user_name = d['user_name']
        if 'verso_url' in d:
            o.verso_url = d['verso_url']
        return o


