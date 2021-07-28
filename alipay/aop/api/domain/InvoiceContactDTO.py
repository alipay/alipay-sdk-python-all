#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InvoiceContactDTO(object):

    def __init__(self):
        self._contact_addr = None
        self._contact_mail = None
        self._contact_mobile = None
        self._contact_name = None

    @property
    def contact_addr(self):
        return self._contact_addr

    @contact_addr.setter
    def contact_addr(self, value):
        self._contact_addr = value
    @property
    def contact_mail(self):
        return self._contact_mail

    @contact_mail.setter
    def contact_mail(self, value):
        self._contact_mail = value
    @property
    def contact_mobile(self):
        return self._contact_mobile

    @contact_mobile.setter
    def contact_mobile(self, value):
        self._contact_mobile = value
    @property
    def contact_name(self):
        return self._contact_name

    @contact_name.setter
    def contact_name(self, value):
        self._contact_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.contact_addr:
            if hasattr(self.contact_addr, 'to_alipay_dict'):
                params['contact_addr'] = self.contact_addr.to_alipay_dict()
            else:
                params['contact_addr'] = self.contact_addr
        if self.contact_mail:
            if hasattr(self.contact_mail, 'to_alipay_dict'):
                params['contact_mail'] = self.contact_mail.to_alipay_dict()
            else:
                params['contact_mail'] = self.contact_mail
        if self.contact_mobile:
            if hasattr(self.contact_mobile, 'to_alipay_dict'):
                params['contact_mobile'] = self.contact_mobile.to_alipay_dict()
            else:
                params['contact_mobile'] = self.contact_mobile
        if self.contact_name:
            if hasattr(self.contact_name, 'to_alipay_dict'):
                params['contact_name'] = self.contact_name.to_alipay_dict()
            else:
                params['contact_name'] = self.contact_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InvoiceContactDTO()
        if 'contact_addr' in d:
            o.contact_addr = d['contact_addr']
        if 'contact_mail' in d:
            o.contact_mail = d['contact_mail']
        if 'contact_mobile' in d:
            o.contact_mobile = d['contact_mobile']
        if 'contact_name' in d:
            o.contact_name = d['contact_name']
        return o


