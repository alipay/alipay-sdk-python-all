#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ServiceContactSimpleVO(object):

    def __init__(self):
        self._contact_email = None
        self._contact_name = None
        self._contact_tele = None

    @property
    def contact_email(self):
        return self._contact_email

    @contact_email.setter
    def contact_email(self, value):
        self._contact_email = value
    @property
    def contact_name(self):
        return self._contact_name

    @contact_name.setter
    def contact_name(self, value):
        self._contact_name = value
    @property
    def contact_tele(self):
        return self._contact_tele

    @contact_tele.setter
    def contact_tele(self, value):
        self._contact_tele = value


    def to_alipay_dict(self):
        params = dict()
        if self.contact_email:
            if hasattr(self.contact_email, 'to_alipay_dict'):
                params['contact_email'] = self.contact_email.to_alipay_dict()
            else:
                params['contact_email'] = self.contact_email
        if self.contact_name:
            if hasattr(self.contact_name, 'to_alipay_dict'):
                params['contact_name'] = self.contact_name.to_alipay_dict()
            else:
                params['contact_name'] = self.contact_name
        if self.contact_tele:
            if hasattr(self.contact_tele, 'to_alipay_dict'):
                params['contact_tele'] = self.contact_tele.to_alipay_dict()
            else:
                params['contact_tele'] = self.contact_tele
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ServiceContactSimpleVO()
        if 'contact_email' in d:
            o.contact_email = d['contact_email']
        if 'contact_name' in d:
            o.contact_name = d['contact_name']
        if 'contact_tele' in d:
            o.contact_tele = d['contact_tele']
        return o


