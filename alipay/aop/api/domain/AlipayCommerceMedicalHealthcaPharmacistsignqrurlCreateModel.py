#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalHealthcaPharmacistsignqrurlCreateModel(object):

    def __init__(self):
        self._id_card_no = None
        self._name = None
        self._name_style = None
        self._pharmacist_code = None
        self._request_id = None

    @property
    def id_card_no(self):
        return self._id_card_no

    @id_card_no.setter
    def id_card_no(self, value):
        self._id_card_no = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def name_style(self):
        return self._name_style

    @name_style.setter
    def name_style(self, value):
        self._name_style = value
    @property
    def pharmacist_code(self):
        return self._pharmacist_code

    @pharmacist_code.setter
    def pharmacist_code(self, value):
        self._pharmacist_code = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.id_card_no:
            if hasattr(self.id_card_no, 'to_alipay_dict'):
                params['id_card_no'] = self.id_card_no.to_alipay_dict()
            else:
                params['id_card_no'] = self.id_card_no
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.name_style:
            if hasattr(self.name_style, 'to_alipay_dict'):
                params['name_style'] = self.name_style.to_alipay_dict()
            else:
                params['name_style'] = self.name_style
        if self.pharmacist_code:
            if hasattr(self.pharmacist_code, 'to_alipay_dict'):
                params['pharmacist_code'] = self.pharmacist_code.to_alipay_dict()
            else:
                params['pharmacist_code'] = self.pharmacist_code
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalHealthcaPharmacistsignqrurlCreateModel()
        if 'id_card_no' in d:
            o.id_card_no = d['id_card_no']
        if 'name' in d:
            o.name = d['name']
        if 'name_style' in d:
            o.name_style = d['name_style']
        if 'pharmacist_code' in d:
            o.pharmacist_code = d['pharmacist_code']
        if 'request_id' in d:
            o.request_id = d['request_id']
        return o


