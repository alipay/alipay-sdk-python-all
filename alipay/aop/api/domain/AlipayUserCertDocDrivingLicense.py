#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserCertDocDrivingLicense(object):

    def __init__(self):
        self._clazz = None
        self._driving_license_no = None
        self._encoded_img_main = None
        self._encoded_img_vice = None
        self._expire_date = None
        self._file_no = None
        self._name = None
        self._valide_date = None

    @property
    def clazz(self):
        return self._clazz

    @clazz.setter
    def clazz(self, value):
        self._clazz = value
    @property
    def driving_license_no(self):
        return self._driving_license_no

    @driving_license_no.setter
    def driving_license_no(self, value):
        self._driving_license_no = value
    @property
    def encoded_img_main(self):
        return self._encoded_img_main

    @encoded_img_main.setter
    def encoded_img_main(self, value):
        self._encoded_img_main = value
    @property
    def encoded_img_vice(self):
        return self._encoded_img_vice

    @encoded_img_vice.setter
    def encoded_img_vice(self, value):
        self._encoded_img_vice = value
    @property
    def expire_date(self):
        return self._expire_date

    @expire_date.setter
    def expire_date(self, value):
        self._expire_date = value
    @property
    def file_no(self):
        return self._file_no

    @file_no.setter
    def file_no(self, value):
        self._file_no = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def valide_date(self):
        return self._valide_date

    @valide_date.setter
    def valide_date(self, value):
        self._valide_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.clazz:
            if hasattr(self.clazz, 'to_alipay_dict'):
                params['clazz'] = self.clazz.to_alipay_dict()
            else:
                params['clazz'] = self.clazz
        if self.driving_license_no:
            if hasattr(self.driving_license_no, 'to_alipay_dict'):
                params['driving_license_no'] = self.driving_license_no.to_alipay_dict()
            else:
                params['driving_license_no'] = self.driving_license_no
        if self.encoded_img_main:
            if hasattr(self.encoded_img_main, 'to_alipay_dict'):
                params['encoded_img_main'] = self.encoded_img_main.to_alipay_dict()
            else:
                params['encoded_img_main'] = self.encoded_img_main
        if self.encoded_img_vice:
            if hasattr(self.encoded_img_vice, 'to_alipay_dict'):
                params['encoded_img_vice'] = self.encoded_img_vice.to_alipay_dict()
            else:
                params['encoded_img_vice'] = self.encoded_img_vice
        if self.expire_date:
            if hasattr(self.expire_date, 'to_alipay_dict'):
                params['expire_date'] = self.expire_date.to_alipay_dict()
            else:
                params['expire_date'] = self.expire_date
        if self.file_no:
            if hasattr(self.file_no, 'to_alipay_dict'):
                params['file_no'] = self.file_no.to_alipay_dict()
            else:
                params['file_no'] = self.file_no
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.valide_date:
            if hasattr(self.valide_date, 'to_alipay_dict'):
                params['valide_date'] = self.valide_date.to_alipay_dict()
            else:
                params['valide_date'] = self.valide_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserCertDocDrivingLicense()
        if 'clazz' in d:
            o.clazz = d['clazz']
        if 'driving_license_no' in d:
            o.driving_license_no = d['driving_license_no']
        if 'encoded_img_main' in d:
            o.encoded_img_main = d['encoded_img_main']
        if 'encoded_img_vice' in d:
            o.encoded_img_vice = d['encoded_img_vice']
        if 'expire_date' in d:
            o.expire_date = d['expire_date']
        if 'file_no' in d:
            o.file_no = d['file_no']
        if 'name' in d:
            o.name = d['name']
        if 'valide_date' in d:
            o.valide_date = d['valide_date']
        return o


