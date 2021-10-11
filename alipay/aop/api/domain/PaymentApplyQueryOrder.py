#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PaymentApplyQueryOrder(object):

    def __init__(self):
        self._apply_relative_id_list = None
        self._arrangement_no = None
        self._bill_no = None
        self._inv_accept_status = None
        self._invoice_id = None
        self._ip_role_id = None
        self._settle_status_list = None
        self._type = None

    @property
    def apply_relative_id_list(self):
        return self._apply_relative_id_list

    @apply_relative_id_list.setter
    def apply_relative_id_list(self, value):
        if isinstance(value, list):
            self._apply_relative_id_list = list()
            for i in value:
                self._apply_relative_id_list.append(i)
    @property
    def arrangement_no(self):
        return self._arrangement_no

    @arrangement_no.setter
    def arrangement_no(self, value):
        self._arrangement_no = value
    @property
    def bill_no(self):
        return self._bill_no

    @bill_no.setter
    def bill_no(self, value):
        self._bill_no = value
    @property
    def inv_accept_status(self):
        return self._inv_accept_status

    @inv_accept_status.setter
    def inv_accept_status(self, value):
        self._inv_accept_status = value
    @property
    def invoice_id(self):
        return self._invoice_id

    @invoice_id.setter
    def invoice_id(self, value):
        self._invoice_id = value
    @property
    def ip_role_id(self):
        return self._ip_role_id

    @ip_role_id.setter
    def ip_role_id(self, value):
        self._ip_role_id = value
    @property
    def settle_status_list(self):
        return self._settle_status_list

    @settle_status_list.setter
    def settle_status_list(self, value):
        if isinstance(value, list):
            self._settle_status_list = list()
            for i in value:
                self._settle_status_list.append(i)
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_relative_id_list:
            if isinstance(self.apply_relative_id_list, list):
                for i in range(0, len(self.apply_relative_id_list)):
                    element = self.apply_relative_id_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.apply_relative_id_list[i] = element.to_alipay_dict()
            if hasattr(self.apply_relative_id_list, 'to_alipay_dict'):
                params['apply_relative_id_list'] = self.apply_relative_id_list.to_alipay_dict()
            else:
                params['apply_relative_id_list'] = self.apply_relative_id_list
        if self.arrangement_no:
            if hasattr(self.arrangement_no, 'to_alipay_dict'):
                params['arrangement_no'] = self.arrangement_no.to_alipay_dict()
            else:
                params['arrangement_no'] = self.arrangement_no
        if self.bill_no:
            if hasattr(self.bill_no, 'to_alipay_dict'):
                params['bill_no'] = self.bill_no.to_alipay_dict()
            else:
                params['bill_no'] = self.bill_no
        if self.inv_accept_status:
            if hasattr(self.inv_accept_status, 'to_alipay_dict'):
                params['inv_accept_status'] = self.inv_accept_status.to_alipay_dict()
            else:
                params['inv_accept_status'] = self.inv_accept_status
        if self.invoice_id:
            if hasattr(self.invoice_id, 'to_alipay_dict'):
                params['invoice_id'] = self.invoice_id.to_alipay_dict()
            else:
                params['invoice_id'] = self.invoice_id
        if self.ip_role_id:
            if hasattr(self.ip_role_id, 'to_alipay_dict'):
                params['ip_role_id'] = self.ip_role_id.to_alipay_dict()
            else:
                params['ip_role_id'] = self.ip_role_id
        if self.settle_status_list:
            if isinstance(self.settle_status_list, list):
                for i in range(0, len(self.settle_status_list)):
                    element = self.settle_status_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.settle_status_list[i] = element.to_alipay_dict()
            if hasattr(self.settle_status_list, 'to_alipay_dict'):
                params['settle_status_list'] = self.settle_status_list.to_alipay_dict()
            else:
                params['settle_status_list'] = self.settle_status_list
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PaymentApplyQueryOrder()
        if 'apply_relative_id_list' in d:
            o.apply_relative_id_list = d['apply_relative_id_list']
        if 'arrangement_no' in d:
            o.arrangement_no = d['arrangement_no']
        if 'bill_no' in d:
            o.bill_no = d['bill_no']
        if 'inv_accept_status' in d:
            o.inv_accept_status = d['inv_accept_status']
        if 'invoice_id' in d:
            o.invoice_id = d['invoice_id']
        if 'ip_role_id' in d:
            o.ip_role_id = d['ip_role_id']
        if 'settle_status_list' in d:
            o.settle_status_list = d['settle_status_list']
        if 'type' in d:
            o.type = d['type']
        return o


