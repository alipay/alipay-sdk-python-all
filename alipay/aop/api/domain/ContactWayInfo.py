#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ContactWayInfo(object):

    def __init__(self):
        self._contact_type = None
        self._contact_value = None

    @property
    def contact_type(self):
        return self._contact_type

    @contact_type.setter
    def contact_type(self, value):
        self._contact_type = value
    @property
    def contact_value(self):
        return self._contact_value

    @contact_value.setter
    def contact_value(self, value):
        self._contact_value = value


    def to_alipay_dict(self):
        params = dict()
        if self.contact_type:
            if hasattr(self.contact_type, 'to_alipay_dict'):
                params['contact_type'] = self.contact_type.to_alipay_dict()
            else:
                params['contact_type'] = self.contact_type
        if self.contact_value:
            if hasattr(self.contact_value, 'to_alipay_dict'):
                params['contact_value'] = self.contact_value.to_alipay_dict()
            else:
                params['contact_value'] = self.contact_value
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ContactWayInfo()
        if 'contact_type' in d:
            o.contact_type = d['contact_type']
        if 'contact_value' in d:
            o.contact_value = d['contact_value']
        return o


