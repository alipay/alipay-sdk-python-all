#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ContactWayItem(object):

    def __init__(self):
        self._contact_value = None
        self._contect_type = None

    @property
    def contact_value(self):
        return self._contact_value

    @contact_value.setter
    def contact_value(self, value):
        self._contact_value = value
    @property
    def contect_type(self):
        return self._contect_type

    @contect_type.setter
    def contect_type(self, value):
        self._contect_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.contact_value:
            if hasattr(self.contact_value, 'to_alipay_dict'):
                params['contact_value'] = self.contact_value.to_alipay_dict()
            else:
                params['contact_value'] = self.contact_value
        if self.contect_type:
            if hasattr(self.contect_type, 'to_alipay_dict'):
                params['contect_type'] = self.contect_type.to_alipay_dict()
            else:
                params['contect_type'] = self.contect_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ContactWayItem()
        if 'contact_value' in d:
            o.contact_value = d['contact_value']
        if 'contect_type' in d:
            o.contect_type = d['contect_type']
        return o


