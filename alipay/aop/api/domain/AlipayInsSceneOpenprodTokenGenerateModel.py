#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayInsSceneOpenprodTokenGenerateModel(object):

    def __init__(self):
        self._id_card_no = None
        self._outbound_source = None
        self._phone = None
        self._real_name = None

    @property
    def id_card_no(self):
        return self._id_card_no

    @id_card_no.setter
    def id_card_no(self, value):
        self._id_card_no = value
    @property
    def outbound_source(self):
        return self._outbound_source

    @outbound_source.setter
    def outbound_source(self, value):
        self._outbound_source = value
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


    def to_alipay_dict(self):
        params = dict()
        if self.id_card_no:
            if hasattr(self.id_card_no, 'to_alipay_dict'):
                params['id_card_no'] = self.id_card_no.to_alipay_dict()
            else:
                params['id_card_no'] = self.id_card_no
        if self.outbound_source:
            if hasattr(self.outbound_source, 'to_alipay_dict'):
                params['outbound_source'] = self.outbound_source.to_alipay_dict()
            else:
                params['outbound_source'] = self.outbound_source
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
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayInsSceneOpenprodTokenGenerateModel()
        if 'id_card_no' in d:
            o.id_card_no = d['id_card_no']
        if 'outbound_source' in d:
            o.outbound_source = d['outbound_source']
        if 'phone' in d:
            o.phone = d['phone']
        if 'real_name' in d:
            o.real_name = d['real_name']
        return o


