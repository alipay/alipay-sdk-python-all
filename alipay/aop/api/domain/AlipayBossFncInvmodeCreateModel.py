#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayBossFncInvmodeCreateModel(object):

    def __init__(self):
        self._ar_no = None
        self._inst_id = None
        self._invoice_mode = None
        self._ip_role_id = None

    @property
    def ar_no(self):
        return self._ar_no

    @ar_no.setter
    def ar_no(self, value):
        self._ar_no = value
    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def invoice_mode(self):
        return self._invoice_mode

    @invoice_mode.setter
    def invoice_mode(self, value):
        self._invoice_mode = value
    @property
    def ip_role_id(self):
        return self._ip_role_id

    @ip_role_id.setter
    def ip_role_id(self, value):
        self._ip_role_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.ar_no:
            if hasattr(self.ar_no, 'to_alipay_dict'):
                params['ar_no'] = self.ar_no.to_alipay_dict()
            else:
                params['ar_no'] = self.ar_no
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.invoice_mode:
            if hasattr(self.invoice_mode, 'to_alipay_dict'):
                params['invoice_mode'] = self.invoice_mode.to_alipay_dict()
            else:
                params['invoice_mode'] = self.invoice_mode
        if self.ip_role_id:
            if hasattr(self.ip_role_id, 'to_alipay_dict'):
                params['ip_role_id'] = self.ip_role_id.to_alipay_dict()
            else:
                params['ip_role_id'] = self.ip_role_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossFncInvmodeCreateModel()
        if 'ar_no' in d:
            o.ar_no = d['ar_no']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'invoice_mode' in d:
            o.invoice_mode = d['invoice_mode']
        if 'ip_role_id' in d:
            o.ip_role_id = d['ip_role_id']
        return o


