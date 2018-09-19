#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ExtendMedicalCard(object):

    def __init__(self):
        self._card_org_name = None
        self._card_org_no = None
        self._city = None
        self._extend_params = None
        self._gmt_sign = None
        self._medical_card_id = None
        self._medical_card_no = None
        self._medical_card_type = None
        self._out_user_card_no = None
        self._out_user_name = None
        self._sign_status = None

    @property
    def card_org_name(self):
        return self._card_org_name

    @card_org_name.setter
    def card_org_name(self, value):
        self._card_org_name = value
    @property
    def card_org_no(self):
        return self._card_org_no

    @card_org_no.setter
    def card_org_no(self, value):
        self._card_org_no = value
    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value
    @property
    def extend_params(self):
        return self._extend_params

    @extend_params.setter
    def extend_params(self, value):
        self._extend_params = value
    @property
    def gmt_sign(self):
        return self._gmt_sign

    @gmt_sign.setter
    def gmt_sign(self, value):
        self._gmt_sign = value
    @property
    def medical_card_id(self):
        return self._medical_card_id

    @medical_card_id.setter
    def medical_card_id(self, value):
        self._medical_card_id = value
    @property
    def medical_card_no(self):
        return self._medical_card_no

    @medical_card_no.setter
    def medical_card_no(self, value):
        self._medical_card_no = value
    @property
    def medical_card_type(self):
        return self._medical_card_type

    @medical_card_type.setter
    def medical_card_type(self, value):
        self._medical_card_type = value
    @property
    def out_user_card_no(self):
        return self._out_user_card_no

    @out_user_card_no.setter
    def out_user_card_no(self, value):
        self._out_user_card_no = value
    @property
    def out_user_name(self):
        return self._out_user_name

    @out_user_name.setter
    def out_user_name(self, value):
        self._out_user_name = value
    @property
    def sign_status(self):
        return self._sign_status

    @sign_status.setter
    def sign_status(self, value):
        self._sign_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.card_org_name:
            if hasattr(self.card_org_name, 'to_alipay_dict'):
                params['card_org_name'] = self.card_org_name.to_alipay_dict()
            else:
                params['card_org_name'] = self.card_org_name
        if self.card_org_no:
            if hasattr(self.card_org_no, 'to_alipay_dict'):
                params['card_org_no'] = self.card_org_no.to_alipay_dict()
            else:
                params['card_org_no'] = self.card_org_no
        if self.city:
            if hasattr(self.city, 'to_alipay_dict'):
                params['city'] = self.city.to_alipay_dict()
            else:
                params['city'] = self.city
        if self.extend_params:
            if hasattr(self.extend_params, 'to_alipay_dict'):
                params['extend_params'] = self.extend_params.to_alipay_dict()
            else:
                params['extend_params'] = self.extend_params
        if self.gmt_sign:
            if hasattr(self.gmt_sign, 'to_alipay_dict'):
                params['gmt_sign'] = self.gmt_sign.to_alipay_dict()
            else:
                params['gmt_sign'] = self.gmt_sign
        if self.medical_card_id:
            if hasattr(self.medical_card_id, 'to_alipay_dict'):
                params['medical_card_id'] = self.medical_card_id.to_alipay_dict()
            else:
                params['medical_card_id'] = self.medical_card_id
        if self.medical_card_no:
            if hasattr(self.medical_card_no, 'to_alipay_dict'):
                params['medical_card_no'] = self.medical_card_no.to_alipay_dict()
            else:
                params['medical_card_no'] = self.medical_card_no
        if self.medical_card_type:
            if hasattr(self.medical_card_type, 'to_alipay_dict'):
                params['medical_card_type'] = self.medical_card_type.to_alipay_dict()
            else:
                params['medical_card_type'] = self.medical_card_type
        if self.out_user_card_no:
            if hasattr(self.out_user_card_no, 'to_alipay_dict'):
                params['out_user_card_no'] = self.out_user_card_no.to_alipay_dict()
            else:
                params['out_user_card_no'] = self.out_user_card_no
        if self.out_user_name:
            if hasattr(self.out_user_name, 'to_alipay_dict'):
                params['out_user_name'] = self.out_user_name.to_alipay_dict()
            else:
                params['out_user_name'] = self.out_user_name
        if self.sign_status:
            if hasattr(self.sign_status, 'to_alipay_dict'):
                params['sign_status'] = self.sign_status.to_alipay_dict()
            else:
                params['sign_status'] = self.sign_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ExtendMedicalCard()
        if 'card_org_name' in d:
            o.card_org_name = d['card_org_name']
        if 'card_org_no' in d:
            o.card_org_no = d['card_org_no']
        if 'city' in d:
            o.city = d['city']
        if 'extend_params' in d:
            o.extend_params = d['extend_params']
        if 'gmt_sign' in d:
            o.gmt_sign = d['gmt_sign']
        if 'medical_card_id' in d:
            o.medical_card_id = d['medical_card_id']
        if 'medical_card_no' in d:
            o.medical_card_no = d['medical_card_no']
        if 'medical_card_type' in d:
            o.medical_card_type = d['medical_card_type']
        if 'out_user_card_no' in d:
            o.out_user_card_no = d['out_user_card_no']
        if 'out_user_name' in d:
            o.out_user_name = d['out_user_name']
        if 'sign_status' in d:
            o.sign_status = d['sign_status']
        return o


