#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayUserCertDocIDCard(object):

    def __init__(self):
        self._encoded_img_emblem = None
        self._encoded_img_identity = None
        self._expire_date = None
        self._name = None
        self._number = None

    @property
    def encoded_img_emblem(self):
        return self._encoded_img_emblem

    @encoded_img_emblem.setter
    def encoded_img_emblem(self, value):
        self._encoded_img_emblem = value
    @property
    def encoded_img_identity(self):
        return self._encoded_img_identity

    @encoded_img_identity.setter
    def encoded_img_identity(self, value):
        self._encoded_img_identity = value
    @property
    def expire_date(self):
        return self._expire_date

    @expire_date.setter
    def expire_date(self, value):
        self._expire_date = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        self._number = value


    def to_alipay_dict(self):
        params = dict()
        if self.encoded_img_emblem:
            if hasattr(self.encoded_img_emblem, 'to_alipay_dict'):
                params['encoded_img_emblem'] = self.encoded_img_emblem.to_alipay_dict()
            else:
                params['encoded_img_emblem'] = self.encoded_img_emblem
        if self.encoded_img_identity:
            if hasattr(self.encoded_img_identity, 'to_alipay_dict'):
                params['encoded_img_identity'] = self.encoded_img_identity.to_alipay_dict()
            else:
                params['encoded_img_identity'] = self.encoded_img_identity
        if self.expire_date:
            if hasattr(self.expire_date, 'to_alipay_dict'):
                params['expire_date'] = self.expire_date.to_alipay_dict()
            else:
                params['expire_date'] = self.expire_date
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.number:
            if hasattr(self.number, 'to_alipay_dict'):
                params['number'] = self.number.to_alipay_dict()
            else:
                params['number'] = self.number
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayUserCertDocIDCard()
        if 'encoded_img_emblem' in d:
            o.encoded_img_emblem = d['encoded_img_emblem']
        if 'encoded_img_identity' in d:
            o.encoded_img_identity = d['encoded_img_identity']
        if 'expire_date' in d:
            o.expire_date = d['expire_date']
        if 'name' in d:
            o.name = d['name']
        if 'number' in d:
            o.number = d['number']
        return o


