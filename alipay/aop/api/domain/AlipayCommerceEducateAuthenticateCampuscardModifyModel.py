#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEducateAuthenticateCampuscardModifyModel(object):

    def __init__(self):
        self._campus = None
        self._campus_no = None
        self._card_no = None
        self._card_status = None
        self._card_type = None
        self._cert_no = None
        self._cert_type = None
        self._chip_no = None
        self._email = None
        self._expire_at = None
        self._ext_info = None
        self._gender = None
        self._image_base_64 = None
        self._image_date = None
        self._isv_short_code = None
        self._mobile_no = None
        self._name = None
        self._organization = None
        self._school_name = None
        self._school_stdcode = None
        self._short_code = None

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
    def card_no(self):
        return self._card_no

    @card_no.setter
    def card_no(self, value):
        self._card_no = value
    @property
    def card_status(self):
        return self._card_status

    @card_status.setter
    def card_status(self, value):
        self._card_status = value
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
    def chip_no(self):
        return self._chip_no

    @chip_no.setter
    def chip_no(self, value):
        self._chip_no = value
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value
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
    def image_base_64(self):
        return self._image_base_64

    @image_base_64.setter
    def image_base_64(self, value):
        self._image_base_64 = value
    @property
    def image_date(self):
        return self._image_date

    @image_date.setter
    def image_date(self, value):
        self._image_date = value
    @property
    def isv_short_code(self):
        return self._isv_short_code

    @isv_short_code.setter
    def isv_short_code(self, value):
        self._isv_short_code = value
    @property
    def mobile_no(self):
        return self._mobile_no

    @mobile_no.setter
    def mobile_no(self, value):
        self._mobile_no = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
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
    def short_code(self):
        return self._short_code

    @short_code.setter
    def short_code(self, value):
        self._short_code = value


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
        if self.card_no:
            if hasattr(self.card_no, 'to_alipay_dict'):
                params['card_no'] = self.card_no.to_alipay_dict()
            else:
                params['card_no'] = self.card_no
        if self.card_status:
            if hasattr(self.card_status, 'to_alipay_dict'):
                params['card_status'] = self.card_status.to_alipay_dict()
            else:
                params['card_status'] = self.card_status
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
        if self.chip_no:
            if hasattr(self.chip_no, 'to_alipay_dict'):
                params['chip_no'] = self.chip_no.to_alipay_dict()
            else:
                params['chip_no'] = self.chip_no
        if self.email:
            if hasattr(self.email, 'to_alipay_dict'):
                params['email'] = self.email.to_alipay_dict()
            else:
                params['email'] = self.email
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
        if self.image_base_64:
            if hasattr(self.image_base_64, 'to_alipay_dict'):
                params['image_base_64'] = self.image_base_64.to_alipay_dict()
            else:
                params['image_base_64'] = self.image_base_64
        if self.image_date:
            if hasattr(self.image_date, 'to_alipay_dict'):
                params['image_date'] = self.image_date.to_alipay_dict()
            else:
                params['image_date'] = self.image_date
        if self.isv_short_code:
            if hasattr(self.isv_short_code, 'to_alipay_dict'):
                params['isv_short_code'] = self.isv_short_code.to_alipay_dict()
            else:
                params['isv_short_code'] = self.isv_short_code
        if self.mobile_no:
            if hasattr(self.mobile_no, 'to_alipay_dict'):
                params['mobile_no'] = self.mobile_no.to_alipay_dict()
            else:
                params['mobile_no'] = self.mobile_no
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
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
        if self.short_code:
            if hasattr(self.short_code, 'to_alipay_dict'):
                params['short_code'] = self.short_code.to_alipay_dict()
            else:
                params['short_code'] = self.short_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEducateAuthenticateCampuscardModifyModel()
        if 'campus' in d:
            o.campus = d['campus']
        if 'campus_no' in d:
            o.campus_no = d['campus_no']
        if 'card_no' in d:
            o.card_no = d['card_no']
        if 'card_status' in d:
            o.card_status = d['card_status']
        if 'card_type' in d:
            o.card_type = d['card_type']
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'chip_no' in d:
            o.chip_no = d['chip_no']
        if 'email' in d:
            o.email = d['email']
        if 'expire_at' in d:
            o.expire_at = d['expire_at']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'gender' in d:
            o.gender = d['gender']
        if 'image_base_64' in d:
            o.image_base_64 = d['image_base_64']
        if 'image_date' in d:
            o.image_date = d['image_date']
        if 'isv_short_code' in d:
            o.isv_short_code = d['isv_short_code']
        if 'mobile_no' in d:
            o.mobile_no = d['mobile_no']
        if 'name' in d:
            o.name = d['name']
        if 'organization' in d:
            o.organization = d['organization']
        if 'school_name' in d:
            o.school_name = d['school_name']
        if 'school_stdcode' in d:
            o.school_stdcode = d['school_stdcode']
        if 'short_code' in d:
            o.short_code = d['short_code']
        return o


