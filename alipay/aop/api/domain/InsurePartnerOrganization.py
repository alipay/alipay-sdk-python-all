#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InsurePartnerOrganization(object):

    def __init__(self):
        self._alipay_account_type = None
        self._alipay_id = None
        self._alipay_open_id = None
        self._cert_name = None
        self._cert_no = None
        self._cert_type = None
        self._partner_org_id = None

    @property
    def alipay_account_type(self):
        return self._alipay_account_type

    @alipay_account_type.setter
    def alipay_account_type(self, value):
        self._alipay_account_type = value
    @property
    def alipay_id(self):
        return self._alipay_id

    @alipay_id.setter
    def alipay_id(self, value):
        self._alipay_id = value
    @property
    def alipay_open_id(self):
        return self._alipay_open_id

    @alipay_open_id.setter
    def alipay_open_id(self, value):
        self._alipay_open_id = value
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
    def cert_type(self):
        return self._cert_type

    @cert_type.setter
    def cert_type(self, value):
        self._cert_type = value
    @property
    def partner_org_id(self):
        return self._partner_org_id

    @partner_org_id.setter
    def partner_org_id(self, value):
        self._partner_org_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_account_type:
            if hasattr(self.alipay_account_type, 'to_alipay_dict'):
                params['alipay_account_type'] = self.alipay_account_type.to_alipay_dict()
            else:
                params['alipay_account_type'] = self.alipay_account_type
        if self.alipay_id:
            if hasattr(self.alipay_id, 'to_alipay_dict'):
                params['alipay_id'] = self.alipay_id.to_alipay_dict()
            else:
                params['alipay_id'] = self.alipay_id
        if self.alipay_open_id:
            if hasattr(self.alipay_open_id, 'to_alipay_dict'):
                params['alipay_open_id'] = self.alipay_open_id.to_alipay_dict()
            else:
                params['alipay_open_id'] = self.alipay_open_id
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
        if self.cert_type:
            if hasattr(self.cert_type, 'to_alipay_dict'):
                params['cert_type'] = self.cert_type.to_alipay_dict()
            else:
                params['cert_type'] = self.cert_type
        if self.partner_org_id:
            if hasattr(self.partner_org_id, 'to_alipay_dict'):
                params['partner_org_id'] = self.partner_org_id.to_alipay_dict()
            else:
                params['partner_org_id'] = self.partner_org_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InsurePartnerOrganization()
        if 'alipay_account_type' in d:
            o.alipay_account_type = d['alipay_account_type']
        if 'alipay_id' in d:
            o.alipay_id = d['alipay_id']
        if 'alipay_open_id' in d:
            o.alipay_open_id = d['alipay_open_id']
        if 'cert_name' in d:
            o.cert_name = d['cert_name']
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'cert_type' in d:
            o.cert_type = d['cert_type']
        if 'partner_org_id' in d:
            o.partner_org_id = d['partner_org_id']
        return o


