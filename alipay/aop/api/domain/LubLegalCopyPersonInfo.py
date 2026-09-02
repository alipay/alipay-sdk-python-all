#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class LubLegalCopyPersonInfo(object):

    def __init__(self):
        self._id_image_url_back = None
        self._id_image_url_front = None
        self._id_legal_person_name = None
        self._id_license_no = None
        self._id_valid_end_date = None
        self._id_valid_start_date = None

    @property
    def id_image_url_back(self):
        return self._id_image_url_back

    @id_image_url_back.setter
    def id_image_url_back(self, value):
        self._id_image_url_back = value
    @property
    def id_image_url_front(self):
        return self._id_image_url_front

    @id_image_url_front.setter
    def id_image_url_front(self, value):
        self._id_image_url_front = value
    @property
    def id_legal_person_name(self):
        return self._id_legal_person_name

    @id_legal_person_name.setter
    def id_legal_person_name(self, value):
        self._id_legal_person_name = value
    @property
    def id_license_no(self):
        return self._id_license_no

    @id_license_no.setter
    def id_license_no(self, value):
        self._id_license_no = value
    @property
    def id_valid_end_date(self):
        return self._id_valid_end_date

    @id_valid_end_date.setter
    def id_valid_end_date(self, value):
        self._id_valid_end_date = value
    @property
    def id_valid_start_date(self):
        return self._id_valid_start_date

    @id_valid_start_date.setter
    def id_valid_start_date(self, value):
        self._id_valid_start_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.id_image_url_back:
            if hasattr(self.id_image_url_back, 'to_alipay_dict'):
                params['id_image_url_back'] = self.id_image_url_back.to_alipay_dict()
            else:
                params['id_image_url_back'] = self.id_image_url_back
        if self.id_image_url_front:
            if hasattr(self.id_image_url_front, 'to_alipay_dict'):
                params['id_image_url_front'] = self.id_image_url_front.to_alipay_dict()
            else:
                params['id_image_url_front'] = self.id_image_url_front
        if self.id_legal_person_name:
            if hasattr(self.id_legal_person_name, 'to_alipay_dict'):
                params['id_legal_person_name'] = self.id_legal_person_name.to_alipay_dict()
            else:
                params['id_legal_person_name'] = self.id_legal_person_name
        if self.id_license_no:
            if hasattr(self.id_license_no, 'to_alipay_dict'):
                params['id_license_no'] = self.id_license_no.to_alipay_dict()
            else:
                params['id_license_no'] = self.id_license_no
        if self.id_valid_end_date:
            if hasattr(self.id_valid_end_date, 'to_alipay_dict'):
                params['id_valid_end_date'] = self.id_valid_end_date.to_alipay_dict()
            else:
                params['id_valid_end_date'] = self.id_valid_end_date
        if self.id_valid_start_date:
            if hasattr(self.id_valid_start_date, 'to_alipay_dict'):
                params['id_valid_start_date'] = self.id_valid_start_date.to_alipay_dict()
            else:
                params['id_valid_start_date'] = self.id_valid_start_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LubLegalCopyPersonInfo()
        if 'id_image_url_back' in d:
            o.id_image_url_back = d['id_image_url_back']
        if 'id_image_url_front' in d:
            o.id_image_url_front = d['id_image_url_front']
        if 'id_legal_person_name' in d:
            o.id_legal_person_name = d['id_legal_person_name']
        if 'id_license_no' in d:
            o.id_license_no = d['id_license_no']
        if 'id_valid_end_date' in d:
            o.id_valid_end_date = d['id_valid_end_date']
        if 'id_valid_start_date' in d:
            o.id_valid_start_date = d['id_valid_start_date']
        return o


