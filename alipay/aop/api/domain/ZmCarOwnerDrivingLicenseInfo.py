#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZmCarOwnerDrivingLicenseInfo(object):

    def __init__(self):
        self._license_expired_date = None
        self._license_img = None
        self._license_level = None
        self._license_no = None
        self._license_state = None
        self._verification_level = None

    @property
    def license_expired_date(self):
        return self._license_expired_date

    @license_expired_date.setter
    def license_expired_date(self, value):
        self._license_expired_date = value
    @property
    def license_img(self):
        return self._license_img

    @license_img.setter
    def license_img(self, value):
        if isinstance(value, list):
            self._license_img = list()
            for i in value:
                self._license_img.append(i)
    @property
    def license_level(self):
        return self._license_level

    @license_level.setter
    def license_level(self, value):
        self._license_level = value
    @property
    def license_no(self):
        return self._license_no

    @license_no.setter
    def license_no(self, value):
        self._license_no = value
    @property
    def license_state(self):
        return self._license_state

    @license_state.setter
    def license_state(self, value):
        self._license_state = value
    @property
    def verification_level(self):
        return self._verification_level

    @verification_level.setter
    def verification_level(self, value):
        self._verification_level = value


    def to_alipay_dict(self):
        params = dict()
        if self.license_expired_date:
            if hasattr(self.license_expired_date, 'to_alipay_dict'):
                params['license_expired_date'] = self.license_expired_date.to_alipay_dict()
            else:
                params['license_expired_date'] = self.license_expired_date
        if self.license_img:
            if isinstance(self.license_img, list):
                for i in range(0, len(self.license_img)):
                    element = self.license_img[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.license_img[i] = element.to_alipay_dict()
            if hasattr(self.license_img, 'to_alipay_dict'):
                params['license_img'] = self.license_img.to_alipay_dict()
            else:
                params['license_img'] = self.license_img
        if self.license_level:
            if hasattr(self.license_level, 'to_alipay_dict'):
                params['license_level'] = self.license_level.to_alipay_dict()
            else:
                params['license_level'] = self.license_level
        if self.license_no:
            if hasattr(self.license_no, 'to_alipay_dict'):
                params['license_no'] = self.license_no.to_alipay_dict()
            else:
                params['license_no'] = self.license_no
        if self.license_state:
            if hasattr(self.license_state, 'to_alipay_dict'):
                params['license_state'] = self.license_state.to_alipay_dict()
            else:
                params['license_state'] = self.license_state
        if self.verification_level:
            if hasattr(self.verification_level, 'to_alipay_dict'):
                params['verification_level'] = self.verification_level.to_alipay_dict()
            else:
                params['verification_level'] = self.verification_level
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZmCarOwnerDrivingLicenseInfo()
        if 'license_expired_date' in d:
            o.license_expired_date = d['license_expired_date']
        if 'license_img' in d:
            o.license_img = d['license_img']
        if 'license_level' in d:
            o.license_level = d['license_level']
        if 'license_no' in d:
            o.license_no = d['license_no']
        if 'license_state' in d:
            o.license_state = d['license_state']
        if 'verification_level' in d:
            o.verification_level = d['verification_level']
        return o


