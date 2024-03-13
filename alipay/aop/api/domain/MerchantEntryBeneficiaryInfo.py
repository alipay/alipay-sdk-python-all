#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MerchantEntryBeneficiaryInfo(object):

    def __init__(self):
        self._beneficiary_cert_expired_date = None
        self._beneficiary_cert_image = None
        self._beneficiary_cert_image_back = None
        self._beneficiary_cert_no = None
        self._beneficiary_cert_type = None
        self._beneficiary_name = None
        self._expired_date_is_long_term = None

    @property
    def beneficiary_cert_expired_date(self):
        return self._beneficiary_cert_expired_date

    @beneficiary_cert_expired_date.setter
    def beneficiary_cert_expired_date(self, value):
        self._beneficiary_cert_expired_date = value
    @property
    def beneficiary_cert_image(self):
        return self._beneficiary_cert_image

    @beneficiary_cert_image.setter
    def beneficiary_cert_image(self, value):
        self._beneficiary_cert_image = value
    @property
    def beneficiary_cert_image_back(self):
        return self._beneficiary_cert_image_back

    @beneficiary_cert_image_back.setter
    def beneficiary_cert_image_back(self, value):
        self._beneficiary_cert_image_back = value
    @property
    def beneficiary_cert_no(self):
        return self._beneficiary_cert_no

    @beneficiary_cert_no.setter
    def beneficiary_cert_no(self, value):
        self._beneficiary_cert_no = value
    @property
    def beneficiary_cert_type(self):
        return self._beneficiary_cert_type

    @beneficiary_cert_type.setter
    def beneficiary_cert_type(self, value):
        self._beneficiary_cert_type = value
    @property
    def beneficiary_name(self):
        return self._beneficiary_name

    @beneficiary_name.setter
    def beneficiary_name(self, value):
        self._beneficiary_name = value
    @property
    def expired_date_is_long_term(self):
        return self._expired_date_is_long_term

    @expired_date_is_long_term.setter
    def expired_date_is_long_term(self, value):
        self._expired_date_is_long_term = value


    def to_alipay_dict(self):
        params = dict()
        if self.beneficiary_cert_expired_date:
            if hasattr(self.beneficiary_cert_expired_date, 'to_alipay_dict'):
                params['beneficiary_cert_expired_date'] = self.beneficiary_cert_expired_date.to_alipay_dict()
            else:
                params['beneficiary_cert_expired_date'] = self.beneficiary_cert_expired_date
        if self.beneficiary_cert_image:
            if hasattr(self.beneficiary_cert_image, 'to_alipay_dict'):
                params['beneficiary_cert_image'] = self.beneficiary_cert_image.to_alipay_dict()
            else:
                params['beneficiary_cert_image'] = self.beneficiary_cert_image
        if self.beneficiary_cert_image_back:
            if hasattr(self.beneficiary_cert_image_back, 'to_alipay_dict'):
                params['beneficiary_cert_image_back'] = self.beneficiary_cert_image_back.to_alipay_dict()
            else:
                params['beneficiary_cert_image_back'] = self.beneficiary_cert_image_back
        if self.beneficiary_cert_no:
            if hasattr(self.beneficiary_cert_no, 'to_alipay_dict'):
                params['beneficiary_cert_no'] = self.beneficiary_cert_no.to_alipay_dict()
            else:
                params['beneficiary_cert_no'] = self.beneficiary_cert_no
        if self.beneficiary_cert_type:
            if hasattr(self.beneficiary_cert_type, 'to_alipay_dict'):
                params['beneficiary_cert_type'] = self.beneficiary_cert_type.to_alipay_dict()
            else:
                params['beneficiary_cert_type'] = self.beneficiary_cert_type
        if self.beneficiary_name:
            if hasattr(self.beneficiary_name, 'to_alipay_dict'):
                params['beneficiary_name'] = self.beneficiary_name.to_alipay_dict()
            else:
                params['beneficiary_name'] = self.beneficiary_name
        if self.expired_date_is_long_term:
            if hasattr(self.expired_date_is_long_term, 'to_alipay_dict'):
                params['expired_date_is_long_term'] = self.expired_date_is_long_term.to_alipay_dict()
            else:
                params['expired_date_is_long_term'] = self.expired_date_is_long_term
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MerchantEntryBeneficiaryInfo()
        if 'beneficiary_cert_expired_date' in d:
            o.beneficiary_cert_expired_date = d['beneficiary_cert_expired_date']
        if 'beneficiary_cert_image' in d:
            o.beneficiary_cert_image = d['beneficiary_cert_image']
        if 'beneficiary_cert_image_back' in d:
            o.beneficiary_cert_image_back = d['beneficiary_cert_image_back']
        if 'beneficiary_cert_no' in d:
            o.beneficiary_cert_no = d['beneficiary_cert_no']
        if 'beneficiary_cert_type' in d:
            o.beneficiary_cert_type = d['beneficiary_cert_type']
        if 'beneficiary_name' in d:
            o.beneficiary_name = d['beneficiary_name']
        if 'expired_date_is_long_term' in d:
            o.expired_date_is_long_term = d['expired_date_is_long_term']
        return o


