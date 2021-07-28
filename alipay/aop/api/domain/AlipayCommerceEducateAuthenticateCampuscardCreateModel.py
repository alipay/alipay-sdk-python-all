#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEducateAuthenticateCampuscardCreateModel(object):

    def __init__(self):
        self._campus = None
        self._campus_no = None
        self._card_type = None
        self._cert_no = None
        self._cert_type = None
        self._expire_at = None
        self._ext_info = None
        self._gender = None
        self._isv_short_code = None
        self._organization = None
        self._school_name = None
        self._school_stdcode = None
        self._user_name = None

    @property
    def campus(self):
        return self._campus

    @campus.setter
    def campus(self, value):
        self._campus = value
    @property
    def campus_no(self):
        return self._campus_no

    @campus_no.setter
    def campus_no(self, value):
        self._campus_no = value
    @property
    def card_type(self):
        return self._card_type

    @card_type.setter
    def card_type(self, value):
        self._card_type = value
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
    def expire_at(self):
        return self._expire_at

    @expire_at.setter
    def expire_at(self, value):
        self._expire_at = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        self._gender = value
    @property
    def isv_short_code(self):
        return self._isv_short_code

    @isv_short_code.setter
    def isv_short_code(self, value):
        self._isv_short_code = value
    @property
    def organization(self):
        return self._organization

    @organization.setter
    def organization(self, value):
        self._organization = value
    @property
    def school_name(self):
        return self._school_name

    @school_name.setter
    def school_name(self, value):
        self._school_name = value
    @property
    def school_stdcode(self):
        return self._school_stdcode

    @school_stdcode.setter
    def school_stdcode(self, value):
        self._school_stdcode = value
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.campus:
            if hasattr(self.campus, 'to_alipay_dict'):
                params['campus'] = self.campus.to_alipay_dict()
            else:
                params['campus'] = self.campus
        if self.campus_no:
            if hasattr(self.campus_no, 'to_alipay_dict'):
                params['campus_no'] = self.campus_no.to_alipay_dict()
            else:
                params['campus_no'] = self.campus_no
        if self.card_type:
            if hasattr(self.card_type, 'to_alipay_dict'):
                params['card_type'] = self.card_type.to_alipay_dict()
            else:
                params['card_type'] = self.card_type
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
        if self.expire_at:
            if hasattr(self.expire_at, 'to_alipay_dict'):
                params['expire_at'] = self.expire_at.to_alipay_dict()
            else:
                params['expire_at'] = self.expire_at
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.gender:
            if hasattr(self.gender, 'to_alipay_dict'):
                params['gender'] = self.gender.to_alipay_dict()
            else:
                params['gender'] = self.gender
        if self.isv_short_code:
            if hasattr(self.isv_short_code, 'to_alipay_dict'):
                params['isv_short_code'] = self.isv_short_code.to_alipay_dict()
            else:
                params['isv_short_code'] = self.isv_short_code
        if self.organization:
            if hasattr(self.organization, 'to_alipay_dict'):
                params['organization'] = self.organization.to_alipay_dict()
            else:
                params['organization'] = self.organization
        if self.school_name:
            if hasattr(self.school_name, 'to_alipay_dict'):
                params['school_name'] = self.school_name.to_alipay_dict()
            else:
                params['school_name'] = self.school_name
        if self.school_stdcode:
            if hasattr(self.school_stdcode, 'to_alipay_dict'):
                params['school_stdcode'] = self.school_stdcode.to_alipay_dict()
            else:
                params['school_stdcode'] = self.school_stdcode
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
        o = AlipayCommerceEducateAuthenticateCampuscardCreateModel()
        if 'campus' in d:
            o.campus = d['campus']
        if 'campus_no' in d:
            o.campus_no = d['campus_no']
        if 'card_type' in d:
            o.card_type = d['card_type']
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'expire_at' in d:
            o.expire_at = d['expire_at']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'gender' in d:
            o.gender = d['gender']
        if 'isv_short_code' in d:
            o.isv_short_code = d['isv_short_code']
        if 'organization' in d:
            o.organization = d['organization']
        if 'school_name' in d:
            o.school_name = d['school_name']
        if 'school_stdcode' in d:
            o.school_stdcode = d['school_stdcode']
        if 'user_name' in d:
            o.user_name = d['user_name']
        return o


