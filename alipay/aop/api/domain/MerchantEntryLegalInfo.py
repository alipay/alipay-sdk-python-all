#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MerchantEntryLegalInfo(object):

    def __init__(self):
        self._expired_date_is_long_term = None
        self._legal_cert_image = None
        self._legal_cert_image_back = None
        self._legal_cert_no = None
        self._legal_cert_type = None
        self._legal_expired_date = None
        self._legal_name = None

    @property
    def expired_date_is_long_term(self):
        return self._expired_date_is_long_term

    @expired_date_is_long_term.setter
    def expired_date_is_long_term(self, value):
        self._expired_date_is_long_term = value
    @property
    def legal_cert_image(self):
        return self._legal_cert_image

    @legal_cert_image.setter
    def legal_cert_image(self, value):
        self._legal_cert_image = value
    @property
    def legal_cert_image_back(self):
        return self._legal_cert_image_back

    @legal_cert_image_back.setter
    def legal_cert_image_back(self, value):
        self._legal_cert_image_back = value
    @property
    def legal_cert_no(self):
        return self._legal_cert_no

    @legal_cert_no.setter
    def legal_cert_no(self, value):
        self._legal_cert_no = value
    @property
    def legal_cert_type(self):
        return self._legal_cert_type

    @legal_cert_type.setter
    def legal_cert_type(self, value):
        self._legal_cert_type = value
    @property
    def legal_expired_date(self):
        return self._legal_expired_date

    @legal_expired_date.setter
    def legal_expired_date(self, value):
        self._legal_expired_date = value
    @property
    def legal_name(self):
        return self._legal_name

    @legal_name.setter
    def legal_name(self, value):
        self._legal_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.expired_date_is_long_term:
            if hasattr(self.expired_date_is_long_term, 'to_alipay_dict'):
                params['expired_date_is_long_term'] = self.expired_date_is_long_term.to_alipay_dict()
            else:
                params['expired_date_is_long_term'] = self.expired_date_is_long_term
        if self.legal_cert_image:
            if hasattr(self.legal_cert_image, 'to_alipay_dict'):
                params['legal_cert_image'] = self.legal_cert_image.to_alipay_dict()
            else:
                params['legal_cert_image'] = self.legal_cert_image
        if self.legal_cert_image_back:
            if hasattr(self.legal_cert_image_back, 'to_alipay_dict'):
                params['legal_cert_image_back'] = self.legal_cert_image_back.to_alipay_dict()
            else:
                params['legal_cert_image_back'] = self.legal_cert_image_back
        if self.legal_cert_no:
            if hasattr(self.legal_cert_no, 'to_alipay_dict'):
                params['legal_cert_no'] = self.legal_cert_no.to_alipay_dict()
            else:
                params['legal_cert_no'] = self.legal_cert_no
        if self.legal_cert_type:
            if hasattr(self.legal_cert_type, 'to_alipay_dict'):
                params['legal_cert_type'] = self.legal_cert_type.to_alipay_dict()
            else:
                params['legal_cert_type'] = self.legal_cert_type
        if self.legal_expired_date:
            if hasattr(self.legal_expired_date, 'to_alipay_dict'):
                params['legal_expired_date'] = self.legal_expired_date.to_alipay_dict()
            else:
                params['legal_expired_date'] = self.legal_expired_date
        if self.legal_name:
            if hasattr(self.legal_name, 'to_alipay_dict'):
                params['legal_name'] = self.legal_name.to_alipay_dict()
            else:
                params['legal_name'] = self.legal_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MerchantEntryLegalInfo()
        if 'expired_date_is_long_term' in d:
            o.expired_date_is_long_term = d['expired_date_is_long_term']
        if 'legal_cert_image' in d:
            o.legal_cert_image = d['legal_cert_image']
        if 'legal_cert_image_back' in d:
            o.legal_cert_image_back = d['legal_cert_image_back']
        if 'legal_cert_no' in d:
            o.legal_cert_no = d['legal_cert_no']
        if 'legal_cert_type' in d:
            o.legal_cert_type = d['legal_cert_type']
        if 'legal_expired_date' in d:
            o.legal_expired_date = d['legal_expired_date']
        if 'legal_name' in d:
            o.legal_name = d['legal_name']
        return o


