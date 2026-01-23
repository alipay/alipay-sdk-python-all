#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InteOpBusinessLicenseInfo(object):

    def __init__(self):
        self._business_license_mobile = None
        self._business_license_no = None
        self._business_license_pic = None
        self._date_limitation = None
        self._long_term = None

    @property
    def business_license_mobile(self):
        return self._business_license_mobile

    @business_license_mobile.setter
    def business_license_mobile(self, value):
        self._business_license_mobile = value
    @property
    def business_license_no(self):
        return self._business_license_no

    @business_license_no.setter
    def business_license_no(self, value):
        self._business_license_no = value
    @property
    def business_license_pic(self):
        return self._business_license_pic

    @business_license_pic.setter
    def business_license_pic(self, value):
        self._business_license_pic = value
    @property
    def date_limitation(self):
        return self._date_limitation

    @date_limitation.setter
    def date_limitation(self, value):
        self._date_limitation = value
    @property
    def long_term(self):
        return self._long_term

    @long_term.setter
    def long_term(self, value):
        self._long_term = value


    def to_alipay_dict(self):
        params = dict()
        if self.business_license_mobile:
            if hasattr(self.business_license_mobile, 'to_alipay_dict'):
                params['business_license_mobile'] = self.business_license_mobile.to_alipay_dict()
            else:
                params['business_license_mobile'] = self.business_license_mobile
        if self.business_license_no:
            if hasattr(self.business_license_no, 'to_alipay_dict'):
                params['business_license_no'] = self.business_license_no.to_alipay_dict()
            else:
                params['business_license_no'] = self.business_license_no
        if self.business_license_pic:
            if hasattr(self.business_license_pic, 'to_alipay_dict'):
                params['business_license_pic'] = self.business_license_pic.to_alipay_dict()
            else:
                params['business_license_pic'] = self.business_license_pic
        if self.date_limitation:
            if hasattr(self.date_limitation, 'to_alipay_dict'):
                params['date_limitation'] = self.date_limitation.to_alipay_dict()
            else:
                params['date_limitation'] = self.date_limitation
        if self.long_term:
            if hasattr(self.long_term, 'to_alipay_dict'):
                params['long_term'] = self.long_term.to_alipay_dict()
            else:
                params['long_term'] = self.long_term
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InteOpBusinessLicenseInfo()
        if 'business_license_mobile' in d:
            o.business_license_mobile = d['business_license_mobile']
        if 'business_license_no' in d:
            o.business_license_no = d['business_license_no']
        if 'business_license_pic' in d:
            o.business_license_pic = d['business_license_pic']
        if 'date_limitation' in d:
            o.date_limitation = d['date_limitation']
        if 'long_term' in d:
            o.long_term = d['long_term']
        return o


