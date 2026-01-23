#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportEtcenterpriseInvoiceApplyModel(object):

    def __init__(self):
        self._apply_ids = None
        self._corp_id = None
        self._invoice_mail = None
        self._open_id = None
        self._user_id = None

    @property
    def apply_ids(self):
        return self._apply_ids

    @apply_ids.setter
    def apply_ids(self, value):
        if isinstance(value, list):
            self._apply_ids = list()
            for i in value:
                self._apply_ids.append(i)
    @property
    def corp_id(self):
        return self._corp_id

    @corp_id.setter
    def corp_id(self, value):
        self._corp_id = value
    @property
    def invoice_mail(self):
        return self._invoice_mail

    @invoice_mail.setter
    def invoice_mail(self, value):
        self._invoice_mail = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_ids:
            if isinstance(self.apply_ids, list):
                for i in range(0, len(self.apply_ids)):
                    element = self.apply_ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.apply_ids[i] = element.to_alipay_dict()
            if hasattr(self.apply_ids, 'to_alipay_dict'):
                params['apply_ids'] = self.apply_ids.to_alipay_dict()
            else:
                params['apply_ids'] = self.apply_ids
        if self.corp_id:
            if hasattr(self.corp_id, 'to_alipay_dict'):
                params['corp_id'] = self.corp_id.to_alipay_dict()
            else:
                params['corp_id'] = self.corp_id
        if self.invoice_mail:
            if hasattr(self.invoice_mail, 'to_alipay_dict'):
                params['invoice_mail'] = self.invoice_mail.to_alipay_dict()
            else:
                params['invoice_mail'] = self.invoice_mail
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportEtcenterpriseInvoiceApplyModel()
        if 'apply_ids' in d:
            o.apply_ids = d['apply_ids']
        if 'corp_id' in d:
            o.corp_id = d['corp_id']
        if 'invoice_mail' in d:
            o.invoice_mail = d['invoice_mail']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


