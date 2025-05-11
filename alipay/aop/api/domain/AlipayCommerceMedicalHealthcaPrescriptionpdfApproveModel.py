#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalHealthcaPrescriptionpdfApproveModel(object):

    def __init__(self):
        self._id_card_no = None
        self._name = None
        self._name_style = None
        self._pdf_file_id = None
        self._pharmacist_code = None
        self._request_id = None
        self._sign_name_height = None
        self._sign_name_width = None
        self._sign_name_x = None
        self._sign_name_y = None

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
    def pdf_file_id(self):
        return self._pdf_file_id

    @pdf_file_id.setter
    def pdf_file_id(self, value):
        self._pdf_file_id = value
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
    @property
    def sign_name_height(self):
        return self._sign_name_height

    @sign_name_height.setter
    def sign_name_height(self, value):
        self._sign_name_height = value
    @property
    def sign_name_width(self):
        return self._sign_name_width

    @sign_name_width.setter
    def sign_name_width(self, value):
        self._sign_name_width = value
    @property
    def sign_name_x(self):
        return self._sign_name_x

    @sign_name_x.setter
    def sign_name_x(self, value):
        self._sign_name_x = value
    @property
    def sign_name_y(self):
        return self._sign_name_y

    @sign_name_y.setter
    def sign_name_y(self, value):
        self._sign_name_y = value


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
        if self.pdf_file_id:
            if hasattr(self.pdf_file_id, 'to_alipay_dict'):
                params['pdf_file_id'] = self.pdf_file_id.to_alipay_dict()
            else:
                params['pdf_file_id'] = self.pdf_file_id
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
        if self.sign_name_height:
            if hasattr(self.sign_name_height, 'to_alipay_dict'):
                params['sign_name_height'] = self.sign_name_height.to_alipay_dict()
            else:
                params['sign_name_height'] = self.sign_name_height
        if self.sign_name_width:
            if hasattr(self.sign_name_width, 'to_alipay_dict'):
                params['sign_name_width'] = self.sign_name_width.to_alipay_dict()
            else:
                params['sign_name_width'] = self.sign_name_width
        if self.sign_name_x:
            if hasattr(self.sign_name_x, 'to_alipay_dict'):
                params['sign_name_x'] = self.sign_name_x.to_alipay_dict()
            else:
                params['sign_name_x'] = self.sign_name_x
        if self.sign_name_y:
            if hasattr(self.sign_name_y, 'to_alipay_dict'):
                params['sign_name_y'] = self.sign_name_y.to_alipay_dict()
            else:
                params['sign_name_y'] = self.sign_name_y
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalHealthcaPrescriptionpdfApproveModel()
        if 'id_card_no' in d:
            o.id_card_no = d['id_card_no']
        if 'name' in d:
            o.name = d['name']
        if 'name_style' in d:
            o.name_style = d['name_style']
        if 'pdf_file_id' in d:
            o.pdf_file_id = d['pdf_file_id']
        if 'pharmacist_code' in d:
            o.pharmacist_code = d['pharmacist_code']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'sign_name_height' in d:
            o.sign_name_height = d['sign_name_height']
        if 'sign_name_width' in d:
            o.sign_name_width = d['sign_name_width']
        if 'sign_name_x' in d:
            o.sign_name_x = d['sign_name_x']
        if 'sign_name_y' in d:
            o.sign_name_y = d['sign_name_y']
        return o


