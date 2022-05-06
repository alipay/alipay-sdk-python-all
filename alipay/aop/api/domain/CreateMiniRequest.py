#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CreateMiniRequest(object):

    def __init__(self):
        self._alipay_account = None
        self._app_name = None
        self._cert_name = None
        self._cert_no = None
        self._contact_name = None
        self._contact_phone = None
        self._is_individual = None
        self._legal_personal_name = None
        self._out_order_no = None

    @property
    def alipay_account(self):
        return self._alipay_account

    @alipay_account.setter
    def alipay_account(self, value):
        self._alipay_account = value
    @property
    def app_name(self):
        return self._app_name

    @app_name.setter
    def app_name(self, value):
        self._app_name = value
    @property
    def cert_name(self):
        return self._cert_name

    @cert_name.setter
    def cert_name(self, value):
        self._cert_name = value
    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def contact_name(self):
        return self._contact_name

    @contact_name.setter
    def contact_name(self, value):
        self._contact_name = value
    @property
    def contact_phone(self):
        return self._contact_phone

    @contact_phone.setter
    def contact_phone(self, value):
        self._contact_phone = value
    @property
    def is_individual(self):
        return self._is_individual

    @is_individual.setter
    def is_individual(self, value):
        self._is_individual = value
    @property
    def legal_personal_name(self):
        return self._legal_personal_name

    @legal_personal_name.setter
    def legal_personal_name(self, value):
        self._legal_personal_name = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_account:
            if hasattr(self.alipay_account, 'to_alipay_dict'):
                params['alipay_account'] = self.alipay_account.to_alipay_dict()
            else:
                params['alipay_account'] = self.alipay_account
        if self.app_name:
            if hasattr(self.app_name, 'to_alipay_dict'):
                params['app_name'] = self.app_name.to_alipay_dict()
            else:
                params['app_name'] = self.app_name
        if self.cert_name:
            if hasattr(self.cert_name, 'to_alipay_dict'):
                params['cert_name'] = self.cert_name.to_alipay_dict()
            else:
                params['cert_name'] = self.cert_name
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.contact_name:
            if hasattr(self.contact_name, 'to_alipay_dict'):
                params['contact_name'] = self.contact_name.to_alipay_dict()
            else:
                params['contact_name'] = self.contact_name
        if self.contact_phone:
            if hasattr(self.contact_phone, 'to_alipay_dict'):
                params['contact_phone'] = self.contact_phone.to_alipay_dict()
            else:
                params['contact_phone'] = self.contact_phone
        if self.is_individual:
            if hasattr(self.is_individual, 'to_alipay_dict'):
                params['is_individual'] = self.is_individual.to_alipay_dict()
            else:
                params['is_individual'] = self.is_individual
        if self.legal_personal_name:
            if hasattr(self.legal_personal_name, 'to_alipay_dict'):
                params['legal_personal_name'] = self.legal_personal_name.to_alipay_dict()
            else:
                params['legal_personal_name'] = self.legal_personal_name
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CreateMiniRequest()
        if 'alipay_account' in d:
            o.alipay_account = d['alipay_account']
        if 'app_name' in d:
            o.app_name = d['app_name']
        if 'cert_name' in d:
            o.cert_name = d['cert_name']
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'contact_name' in d:
            o.contact_name = d['contact_name']
        if 'contact_phone' in d:
            o.contact_phone = d['contact_phone']
        if 'is_individual' in d:
            o.is_individual = d['is_individual']
        if 'legal_personal_name' in d:
            o.legal_personal_name = d['legal_personal_name']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        return o


