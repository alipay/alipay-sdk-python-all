#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class LsqBusinessLicenseInfo(object):

    def __init__(self):
        self._bl_image_oss = None
        self._bl_image_url = None
        self._bl_legal_person_name = None
        self._bl_license_name = None
        self._bl_license_no = None
        self._bl_valid_end_date = None
        self._bl_valid_start_date = None

    @property
    def bl_image_oss(self):
        return self._bl_image_oss

    @bl_image_oss.setter
    def bl_image_oss(self, value):
        self._bl_image_oss = value
    @property
    def bl_image_url(self):
        return self._bl_image_url

    @bl_image_url.setter
    def bl_image_url(self, value):
        self._bl_image_url = value
    @property
    def bl_legal_person_name(self):
        return self._bl_legal_person_name

    @bl_legal_person_name.setter
    def bl_legal_person_name(self, value):
        self._bl_legal_person_name = value
    @property
    def bl_license_name(self):
        return self._bl_license_name

    @bl_license_name.setter
    def bl_license_name(self, value):
        self._bl_license_name = value
    @property
    def bl_license_no(self):
        return self._bl_license_no

    @bl_license_no.setter
    def bl_license_no(self, value):
        self._bl_license_no = value
    @property
    def bl_valid_end_date(self):
        return self._bl_valid_end_date

    @bl_valid_end_date.setter
    def bl_valid_end_date(self, value):
        self._bl_valid_end_date = value
    @property
    def bl_valid_start_date(self):
        return self._bl_valid_start_date

    @bl_valid_start_date.setter
    def bl_valid_start_date(self, value):
        self._bl_valid_start_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.bl_image_oss:
            if hasattr(self.bl_image_oss, 'to_alipay_dict'):
                params['bl_image_oss'] = self.bl_image_oss.to_alipay_dict()
            else:
                params['bl_image_oss'] = self.bl_image_oss
        if self.bl_image_url:
            if hasattr(self.bl_image_url, 'to_alipay_dict'):
                params['bl_image_url'] = self.bl_image_url.to_alipay_dict()
            else:
                params['bl_image_url'] = self.bl_image_url
        if self.bl_legal_person_name:
            if hasattr(self.bl_legal_person_name, 'to_alipay_dict'):
                params['bl_legal_person_name'] = self.bl_legal_person_name.to_alipay_dict()
            else:
                params['bl_legal_person_name'] = self.bl_legal_person_name
        if self.bl_license_name:
            if hasattr(self.bl_license_name, 'to_alipay_dict'):
                params['bl_license_name'] = self.bl_license_name.to_alipay_dict()
            else:
                params['bl_license_name'] = self.bl_license_name
        if self.bl_license_no:
            if hasattr(self.bl_license_no, 'to_alipay_dict'):
                params['bl_license_no'] = self.bl_license_no.to_alipay_dict()
            else:
                params['bl_license_no'] = self.bl_license_no
        if self.bl_valid_end_date:
            if hasattr(self.bl_valid_end_date, 'to_alipay_dict'):
                params['bl_valid_end_date'] = self.bl_valid_end_date.to_alipay_dict()
            else:
                params['bl_valid_end_date'] = self.bl_valid_end_date
        if self.bl_valid_start_date:
            if hasattr(self.bl_valid_start_date, 'to_alipay_dict'):
                params['bl_valid_start_date'] = self.bl_valid_start_date.to_alipay_dict()
            else:
                params['bl_valid_start_date'] = self.bl_valid_start_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LsqBusinessLicenseInfo()
        if 'bl_image_oss' in d:
            o.bl_image_oss = d['bl_image_oss']
        if 'bl_image_url' in d:
            o.bl_image_url = d['bl_image_url']
        if 'bl_legal_person_name' in d:
            o.bl_legal_person_name = d['bl_legal_person_name']
        if 'bl_license_name' in d:
            o.bl_license_name = d['bl_license_name']
        if 'bl_license_no' in d:
            o.bl_license_no = d['bl_license_no']
        if 'bl_valid_end_date' in d:
            o.bl_valid_end_date = d['bl_valid_end_date']
        if 'bl_valid_start_date' in d:
            o.bl_valid_start_date = d['bl_valid_start_date']
        return o


