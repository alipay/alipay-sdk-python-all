#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BsContactPersonInfo(object):

    def __init__(self):
        self._contact_name = None
        self._contact_phone_no = None

    @property
    def contact_name(self):
        return self._contact_name

    @contact_name.setter
    def contact_name(self, value):
        self._contact_name = value
    @property
    def contact_phone_no(self):
        return self._contact_phone_no

    @contact_phone_no.setter
    def contact_phone_no(self, value):
        self._contact_phone_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.contact_name:
            if hasattr(self.contact_name, 'to_alipay_dict'):
                params['contact_name'] = self.contact_name.to_alipay_dict()
            else:
                params['contact_name'] = self.contact_name
        if self.contact_phone_no:
            if hasattr(self.contact_phone_no, 'to_alipay_dict'):
                params['contact_phone_no'] = self.contact_phone_no.to_alipay_dict()
            else:
                params['contact_phone_no'] = self.contact_phone_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BsContactPersonInfo()
        if 'contact_name' in d:
            o.contact_name = d['contact_name']
        if 'contact_phone_no' in d:
            o.contact_phone_no = d['contact_phone_no']
        return o


