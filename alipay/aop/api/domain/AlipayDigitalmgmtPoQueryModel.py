#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDigitalmgmtPoQueryModel(object):

    def __init__(self):
        self._demander_purchase_org_id = None
        self._po_number_list = None
        self._po_view_control = None
        self._receiver = None
        self._status = None
        self._supplier_id = None

    @property
    def demander_purchase_org_id(self):
        return self._demander_purchase_org_id

    @demander_purchase_org_id.setter
    def demander_purchase_org_id(self, value):
        self._demander_purchase_org_id = value
    @property
    def po_number_list(self):
        return self._po_number_list

    @po_number_list.setter
    def po_number_list(self, value):
        if isinstance(value, list):
            self._po_number_list = list()
            for i in value:
                self._po_number_list.append(i)
    @property
    def po_view_control(self):
        return self._po_view_control

    @po_view_control.setter
    def po_view_control(self, value):
        self._po_view_control = value
    @property
    def receiver(self):
        return self._receiver

    @receiver.setter
    def receiver(self, value):
        self._receiver = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        if isinstance(value, list):
            self._status = list()
            for i in value:
                self._status.append(i)
    @property
    def supplier_id(self):
        return self._supplier_id

    @supplier_id.setter
    def supplier_id(self, value):
        self._supplier_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.demander_purchase_org_id:
            if hasattr(self.demander_purchase_org_id, 'to_alipay_dict'):
                params['demander_purchase_org_id'] = self.demander_purchase_org_id.to_alipay_dict()
            else:
                params['demander_purchase_org_id'] = self.demander_purchase_org_id
        if self.po_number_list:
            if isinstance(self.po_number_list, list):
                for i in range(0, len(self.po_number_list)):
                    element = self.po_number_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.po_number_list[i] = element.to_alipay_dict()
            if hasattr(self.po_number_list, 'to_alipay_dict'):
                params['po_number_list'] = self.po_number_list.to_alipay_dict()
            else:
                params['po_number_list'] = self.po_number_list
        if self.po_view_control:
            if hasattr(self.po_view_control, 'to_alipay_dict'):
                params['po_view_control'] = self.po_view_control.to_alipay_dict()
            else:
                params['po_view_control'] = self.po_view_control
        if self.receiver:
            if hasattr(self.receiver, 'to_alipay_dict'):
                params['receiver'] = self.receiver.to_alipay_dict()
            else:
                params['receiver'] = self.receiver
        if self.status:
            if isinstance(self.status, list):
                for i in range(0, len(self.status)):
                    element = self.status[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.status[i] = element.to_alipay_dict()
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.supplier_id:
            if hasattr(self.supplier_id, 'to_alipay_dict'):
                params['supplier_id'] = self.supplier_id.to_alipay_dict()
            else:
                params['supplier_id'] = self.supplier_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDigitalmgmtPoQueryModel()
        if 'demander_purchase_org_id' in d:
            o.demander_purchase_org_id = d['demander_purchase_org_id']
        if 'po_number_list' in d:
            o.po_number_list = d['po_number_list']
        if 'po_view_control' in d:
            o.po_view_control = d['po_view_control']
        if 'receiver' in d:
            o.receiver = d['receiver']
        if 'status' in d:
            o.status = d['status']
        if 'supplier_id' in d:
            o.supplier_id = d['supplier_id']
        return o


