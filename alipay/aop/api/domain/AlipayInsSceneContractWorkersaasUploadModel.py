#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayInsSceneContractWorkersaasUploadModel(object):

    def __init__(self):
        self._files = None
        self._id_card = None
        self._payload = None
        self._phone = None
        self._real_name = None
        self._sign_order_no = None
        self._sign_time = None

    @property
    def files(self):
        return self._files

    @files.setter
    def files(self, value):
        self._files = value
    @property
    def id_card(self):
        return self._id_card

    @id_card.setter
    def id_card(self, value):
        self._id_card = value
    @property
    def payload(self):
        return self._payload

    @payload.setter
    def payload(self, value):
        self._payload = value
    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value
    @property
    def real_name(self):
        return self._real_name

    @real_name.setter
    def real_name(self, value):
        self._real_name = value
    @property
    def sign_order_no(self):
        return self._sign_order_no

    @sign_order_no.setter
    def sign_order_no(self, value):
        self._sign_order_no = value
    @property
    def sign_time(self):
        return self._sign_time

    @sign_time.setter
    def sign_time(self, value):
        self._sign_time = value


    def to_alipay_dict(self):
        params = dict()
        if self.files:
            if hasattr(self.files, 'to_alipay_dict'):
                params['files'] = self.files.to_alipay_dict()
            else:
                params['files'] = self.files
        if self.id_card:
            if hasattr(self.id_card, 'to_alipay_dict'):
                params['id_card'] = self.id_card.to_alipay_dict()
            else:
                params['id_card'] = self.id_card
        if self.payload:
            if hasattr(self.payload, 'to_alipay_dict'):
                params['payload'] = self.payload.to_alipay_dict()
            else:
                params['payload'] = self.payload
        if self.phone:
            if hasattr(self.phone, 'to_alipay_dict'):
                params['phone'] = self.phone.to_alipay_dict()
            else:
                params['phone'] = self.phone
        if self.real_name:
            if hasattr(self.real_name, 'to_alipay_dict'):
                params['real_name'] = self.real_name.to_alipay_dict()
            else:
                params['real_name'] = self.real_name
        if self.sign_order_no:
            if hasattr(self.sign_order_no, 'to_alipay_dict'):
                params['sign_order_no'] = self.sign_order_no.to_alipay_dict()
            else:
                params['sign_order_no'] = self.sign_order_no
        if self.sign_time:
            if hasattr(self.sign_time, 'to_alipay_dict'):
                params['sign_time'] = self.sign_time.to_alipay_dict()
            else:
                params['sign_time'] = self.sign_time
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsSceneContractWorkersaasUploadModel()
        if 'files' in d:
            o.files = d['files']
        if 'id_card' in d:
            o.id_card = d['id_card']
        if 'payload' in d:
            o.payload = d['payload']
        if 'phone' in d:
            o.phone = d['phone']
        if 'real_name' in d:
            o.real_name = d['real_name']
        if 'sign_order_no' in d:
            o.sign_order_no = d['sign_order_no']
        if 'sign_time' in d:
            o.sign_time = d['sign_time']
        return o


