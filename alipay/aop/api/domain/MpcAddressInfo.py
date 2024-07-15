#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MpcAddressInfo(object):

    def __init__(self):
        self._address_detail = None
        self._address_id = None
        self._division_code = None
        self._receiver = None
        self._receiver_phone = None
        self._town_division_code = None

    @property
    def address_detail(self):
        return self._address_detail

    @address_detail.setter
    def address_detail(self, value):
        self._address_detail = value
    @property
    def address_id(self):
        return self._address_id

    @address_id.setter
    def address_id(self, value):
        self._address_id = value
    @property
    def division_code(self):
        return self._division_code

    @division_code.setter
    def division_code(self, value):
        self._division_code = value
    @property
    def receiver(self):
        return self._receiver

    @receiver.setter
    def receiver(self, value):
        self._receiver = value
    @property
    def receiver_phone(self):
        return self._receiver_phone

    @receiver_phone.setter
    def receiver_phone(self, value):
        self._receiver_phone = value
    @property
    def town_division_code(self):
        return self._town_division_code

    @town_division_code.setter
    def town_division_code(self, value):
        self._town_division_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.address_detail:
            if hasattr(self.address_detail, 'to_alipay_dict'):
                params['address_detail'] = self.address_detail.to_alipay_dict()
            else:
                params['address_detail'] = self.address_detail
        if self.address_id:
            if hasattr(self.address_id, 'to_alipay_dict'):
                params['address_id'] = self.address_id.to_alipay_dict()
            else:
                params['address_id'] = self.address_id
        if self.division_code:
            if hasattr(self.division_code, 'to_alipay_dict'):
                params['division_code'] = self.division_code.to_alipay_dict()
            else:
                params['division_code'] = self.division_code
        if self.receiver:
            if hasattr(self.receiver, 'to_alipay_dict'):
                params['receiver'] = self.receiver.to_alipay_dict()
            else:
                params['receiver'] = self.receiver
        if self.receiver_phone:
            if hasattr(self.receiver_phone, 'to_alipay_dict'):
                params['receiver_phone'] = self.receiver_phone.to_alipay_dict()
            else:
                params['receiver_phone'] = self.receiver_phone
        if self.town_division_code:
            if hasattr(self.town_division_code, 'to_alipay_dict'):
                params['town_division_code'] = self.town_division_code.to_alipay_dict()
            else:
                params['town_division_code'] = self.town_division_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MpcAddressInfo()
        if 'address_detail' in d:
            o.address_detail = d['address_detail']
        if 'address_id' in d:
            o.address_id = d['address_id']
        if 'division_code' in d:
            o.division_code = d['division_code']
        if 'receiver' in d:
            o.receiver = d['receiver']
        if 'receiver_phone' in d:
            o.receiver_phone = d['receiver_phone']
        if 'town_division_code' in d:
            o.town_division_code = d['town_division_code']
        return o


