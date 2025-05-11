#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalHealthcaPrescriptionpicApproveModel(object):

    def __init__(self):
        self._id_card_no = None
        self._name = None
        self._pharmacist_code = None
        self._pic_file_id = None
        self._sign_mark_text = None
        self._sign_name_file_id = None
        self._sign_name_size = None
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
    def pharmacist_code(self):
        return self._pharmacist_code

    @pharmacist_code.setter
    def pharmacist_code(self, value):
        self._pharmacist_code = value
    @property
    def pic_file_id(self):
        return self._pic_file_id

    @pic_file_id.setter
    def pic_file_id(self, value):
        self._pic_file_id = value
    @property
    def sign_mark_text(self):
        return self._sign_mark_text

    @sign_mark_text.setter
    def sign_mark_text(self, value):
        self._sign_mark_text = value
    @property
    def sign_name_file_id(self):
        return self._sign_name_file_id

    @sign_name_file_id.setter
    def sign_name_file_id(self, value):
        self._sign_name_file_id = value
    @property
    def sign_name_size(self):
        return self._sign_name_size

    @sign_name_size.setter
    def sign_name_size(self, value):
        self._sign_name_size = value
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
        if self.pharmacist_code:
            if hasattr(self.pharmacist_code, 'to_alipay_dict'):
                params['pharmacist_code'] = self.pharmacist_code.to_alipay_dict()
            else:
                params['pharmacist_code'] = self.pharmacist_code
        if self.pic_file_id:
            if hasattr(self.pic_file_id, 'to_alipay_dict'):
                params['pic_file_id'] = self.pic_file_id.to_alipay_dict()
            else:
                params['pic_file_id'] = self.pic_file_id
        if self.sign_mark_text:
            if hasattr(self.sign_mark_text, 'to_alipay_dict'):
                params['sign_mark_text'] = self.sign_mark_text.to_alipay_dict()
            else:
                params['sign_mark_text'] = self.sign_mark_text
        if self.sign_name_file_id:
            if hasattr(self.sign_name_file_id, 'to_alipay_dict'):
                params['sign_name_file_id'] = self.sign_name_file_id.to_alipay_dict()
            else:
                params['sign_name_file_id'] = self.sign_name_file_id
        if self.sign_name_size:
            if hasattr(self.sign_name_size, 'to_alipay_dict'):
                params['sign_name_size'] = self.sign_name_size.to_alipay_dict()
            else:
                params['sign_name_size'] = self.sign_name_size
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
        o = AlipayCommerceMedicalHealthcaPrescriptionpicApproveModel()
        if 'id_card_no' in d:
            o.id_card_no = d['id_card_no']
        if 'name' in d:
            o.name = d['name']
        if 'pharmacist_code' in d:
            o.pharmacist_code = d['pharmacist_code']
        if 'pic_file_id' in d:
            o.pic_file_id = d['pic_file_id']
        if 'sign_mark_text' in d:
            o.sign_mark_text = d['sign_mark_text']
        if 'sign_name_file_id' in d:
            o.sign_name_file_id = d['sign_name_file_id']
        if 'sign_name_size' in d:
            o.sign_name_size = d['sign_name_size']
        if 'sign_name_x' in d:
            o.sign_name_x = d['sign_name_x']
        if 'sign_name_y' in d:
            o.sign_name_y = d['sign_name_y']
        return o


