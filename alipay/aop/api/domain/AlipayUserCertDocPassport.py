#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserCertDocPassport(object):

    def __init__(self):
        self._encoded_img = None
        self._expire_date = None
        self._family_name = None
        self._given_name = None
        self._number = None

    @property
    def encoded_img(self):
        return self._encoded_img

    @encoded_img.setter
    def encoded_img(self, value):
        self._encoded_img = value
    @property
    def expire_date(self):
        return self._expire_date

    @expire_date.setter
    def expire_date(self, value):
        self._expire_date = value
    @property
    def family_name(self):
        return self._family_name

    @family_name.setter
    def family_name(self, value):
        self._family_name = value
    @property
    def given_name(self):
        return self._given_name

    @given_name.setter
    def given_name(self, value):
        self._given_name = value
    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        self._number = value


    def to_alipay_dict(self):
        params = dict()
        if self.encoded_img:
            if hasattr(self.encoded_img, 'to_alipay_dict'):
                params['encoded_img'] = self.encoded_img.to_alipay_dict()
            else:
                params['encoded_img'] = self.encoded_img
        if self.expire_date:
            if hasattr(self.expire_date, 'to_alipay_dict'):
                params['expire_date'] = self.expire_date.to_alipay_dict()
            else:
                params['expire_date'] = self.expire_date
        if self.family_name:
            if hasattr(self.family_name, 'to_alipay_dict'):
                params['family_name'] = self.family_name.to_alipay_dict()
            else:
                params['family_name'] = self.family_name
        if self.given_name:
            if hasattr(self.given_name, 'to_alipay_dict'):
                params['given_name'] = self.given_name.to_alipay_dict()
            else:
                params['given_name'] = self.given_name
        if self.number:
            if hasattr(self.number, 'to_alipay_dict'):
                params['number'] = self.number.to_alipay_dict()
            else:
                params['number'] = self.number
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserCertDocPassport()
        if 'encoded_img' in d:
            o.encoded_img = d['encoded_img']
        if 'expire_date' in d:
            o.expire_date = d['expire_date']
        if 'family_name' in d:
            o.family_name = d['family_name']
        if 'given_name' in d:
            o.given_name = d['given_name']
        if 'number' in d:
            o.number = d['number']
        return o


