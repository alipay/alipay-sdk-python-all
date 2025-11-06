#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class YxContactInfo(object):

    def __init__(self):
        self._contact_name = None
        self._data_id = None
        self._default_contact = None
        self._mobile_phone = None
        self._position = None

    @property
    def contact_name(self):
        return self._contact_name

    @contact_name.setter
    def contact_name(self, value):
        self._contact_name = value
    @property
    def data_id(self):
        return self._data_id

    @data_id.setter
    def data_id(self, value):
        self._data_id = value
    @property
    def default_contact(self):
        return self._default_contact

    @default_contact.setter
    def default_contact(self, value):
        self._default_contact = value
    @property
    def mobile_phone(self):
        return self._mobile_phone

    @mobile_phone.setter
    def mobile_phone(self, value):
        self._mobile_phone = value
    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        self._position = value


    def to_alipay_dict(self):
        params = dict()
        if self.contact_name:
            if hasattr(self.contact_name, 'to_alipay_dict'):
                params['contact_name'] = self.contact_name.to_alipay_dict()
            else:
                params['contact_name'] = self.contact_name
        if self.data_id:
            if hasattr(self.data_id, 'to_alipay_dict'):
                params['data_id'] = self.data_id.to_alipay_dict()
            else:
                params['data_id'] = self.data_id
        if self.default_contact:
            if hasattr(self.default_contact, 'to_alipay_dict'):
                params['default_contact'] = self.default_contact.to_alipay_dict()
            else:
                params['default_contact'] = self.default_contact
        if self.mobile_phone:
            if hasattr(self.mobile_phone, 'to_alipay_dict'):
                params['mobile_phone'] = self.mobile_phone.to_alipay_dict()
            else:
                params['mobile_phone'] = self.mobile_phone
        if self.position:
            if hasattr(self.position, 'to_alipay_dict'):
                params['position'] = self.position.to_alipay_dict()
            else:
                params['position'] = self.position
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = YxContactInfo()
        if 'contact_name' in d:
            o.contact_name = d['contact_name']
        if 'data_id' in d:
            o.data_id = d['data_id']
        if 'default_contact' in d:
            o.default_contact = d['default_contact']
        if 'mobile_phone' in d:
            o.mobile_phone = d['mobile_phone']
        if 'position' in d:
            o.position = d['position']
        return o


