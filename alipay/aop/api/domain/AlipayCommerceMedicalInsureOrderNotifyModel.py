#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalInsureOrderNotifyModel(object):

    def __init__(self):
        self._certificate_number = None
        self._claims_status = None
        self._institution_code = None
        self._insurant_user_name = None
        self._open_id = None
        self._product_name = None
        self._status = None
        self._vas_services_status = None

    @property
    def certificate_number(self):
        return self._certificate_number

    @certificate_number.setter
    def certificate_number(self, value):
        self._certificate_number = value
    @property
    def claims_status(self):
        return self._claims_status

    @claims_status.setter
    def claims_status(self, value):
        self._claims_status = value
    @property
    def institution_code(self):
        return self._institution_code

    @institution_code.setter
    def institution_code(self, value):
        self._institution_code = value
    @property
    def insurant_user_name(self):
        return self._insurant_user_name

    @insurant_user_name.setter
    def insurant_user_name(self, value):
        self._insurant_user_name = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def product_name(self):
        return self._product_name

    @product_name.setter
    def product_name(self, value):
        self._product_name = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def vas_services_status(self):
        return self._vas_services_status

    @vas_services_status.setter
    def vas_services_status(self, value):
        self._vas_services_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.certificate_number:
            if hasattr(self.certificate_number, 'to_alipay_dict'):
                params['certificate_number'] = self.certificate_number.to_alipay_dict()
            else:
                params['certificate_number'] = self.certificate_number
        if self.claims_status:
            if hasattr(self.claims_status, 'to_alipay_dict'):
                params['claims_status'] = self.claims_status.to_alipay_dict()
            else:
                params['claims_status'] = self.claims_status
        if self.institution_code:
            if hasattr(self.institution_code, 'to_alipay_dict'):
                params['institution_code'] = self.institution_code.to_alipay_dict()
            else:
                params['institution_code'] = self.institution_code
        if self.insurant_user_name:
            if hasattr(self.insurant_user_name, 'to_alipay_dict'):
                params['insurant_user_name'] = self.insurant_user_name.to_alipay_dict()
            else:
                params['insurant_user_name'] = self.insurant_user_name
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.product_name:
            if hasattr(self.product_name, 'to_alipay_dict'):
                params['product_name'] = self.product_name.to_alipay_dict()
            else:
                params['product_name'] = self.product_name
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.vas_services_status:
            if hasattr(self.vas_services_status, 'to_alipay_dict'):
                params['vas_services_status'] = self.vas_services_status.to_alipay_dict()
            else:
                params['vas_services_status'] = self.vas_services_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalInsureOrderNotifyModel()
        if 'certificate_number' in d:
            o.certificate_number = d['certificate_number']
        if 'claims_status' in d:
            o.claims_status = d['claims_status']
        if 'institution_code' in d:
            o.institution_code = d['institution_code']
        if 'insurant_user_name' in d:
            o.insurant_user_name = d['insurant_user_name']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'product_name' in d:
            o.product_name = d['product_name']
        if 'status' in d:
            o.status = d['status']
        if 'vas_services_status' in d:
            o.vas_services_status = d['vas_services_status']
        return o


