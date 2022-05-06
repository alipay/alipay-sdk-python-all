#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InvoiceLineInfoOrder import InvoiceLineInfoOrder
from alipay.aop.api.domain.UserInvoiceInfoOrder import UserInvoiceInfoOrder


class AlipayBossFncGfsettleprodNobillinvoiceApplyModel(object):

    def __init__(self):
        self._audit_staff = None
        self._biz_id = None
        self._biz_no = None
        self._can_link = None
        self._inst_id = None
        self._invoice_line_list = None
        self._invoice_material = None
        self._invoice_note = None
        self._invoice_type = None
        self._memo = None
        self._operator = None
        self._operator_domain_name = None
        self._order_way = None
        self._user_invoice_info = None

    @property
    def audit_staff(self):
        return self._audit_staff

    @audit_staff.setter
    def audit_staff(self, value):
        self._audit_staff = value
    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def can_link(self):
        return self._can_link

    @can_link.setter
    def can_link(self, value):
        self._can_link = value
    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def invoice_line_list(self):
        return self._invoice_line_list

    @invoice_line_list.setter
    def invoice_line_list(self, value):
        if isinstance(value, list):
            self._invoice_line_list = list()
            for i in value:
                if isinstance(i, InvoiceLineInfoOrder):
                    self._invoice_line_list.append(i)
                else:
                    self._invoice_line_list.append(InvoiceLineInfoOrder.from_alipay_dict(i))
    @property
    def invoice_material(self):
        return self._invoice_material

    @invoice_material.setter
    def invoice_material(self, value):
        self._invoice_material = value
    @property
    def invoice_note(self):
        return self._invoice_note

    @invoice_note.setter
    def invoice_note(self, value):
        self._invoice_note = value
    @property
    def invoice_type(self):
        return self._invoice_type

    @invoice_type.setter
    def invoice_type(self, value):
        self._invoice_type = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        self._operator = value
    @property
    def operator_domain_name(self):
        return self._operator_domain_name

    @operator_domain_name.setter
    def operator_domain_name(self, value):
        self._operator_domain_name = value
    @property
    def order_way(self):
        return self._order_way

    @order_way.setter
    def order_way(self, value):
        self._order_way = value
    @property
    def user_invoice_info(self):
        return self._user_invoice_info

    @user_invoice_info.setter
    def user_invoice_info(self, value):
        if isinstance(value, UserInvoiceInfoOrder):
            self._user_invoice_info = value
        else:
            self._user_invoice_info = UserInvoiceInfoOrder.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.audit_staff:
            if hasattr(self.audit_staff, 'to_alipay_dict'):
                params['audit_staff'] = self.audit_staff.to_alipay_dict()
            else:
                params['audit_staff'] = self.audit_staff
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.biz_no:
            if hasattr(self.biz_no, 'to_alipay_dict'):
                params['biz_no'] = self.biz_no.to_alipay_dict()
            else:
                params['biz_no'] = self.biz_no
        if self.can_link:
            if hasattr(self.can_link, 'to_alipay_dict'):
                params['can_link'] = self.can_link.to_alipay_dict()
            else:
                params['can_link'] = self.can_link
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.invoice_line_list:
            if isinstance(self.invoice_line_list, list):
                for i in range(0, len(self.invoice_line_list)):
                    element = self.invoice_line_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.invoice_line_list[i] = element.to_alipay_dict()
            if hasattr(self.invoice_line_list, 'to_alipay_dict'):
                params['invoice_line_list'] = self.invoice_line_list.to_alipay_dict()
            else:
                params['invoice_line_list'] = self.invoice_line_list
        if self.invoice_material:
            if hasattr(self.invoice_material, 'to_alipay_dict'):
                params['invoice_material'] = self.invoice_material.to_alipay_dict()
            else:
                params['invoice_material'] = self.invoice_material
        if self.invoice_note:
            if hasattr(self.invoice_note, 'to_alipay_dict'):
                params['invoice_note'] = self.invoice_note.to_alipay_dict()
            else:
                params['invoice_note'] = self.invoice_note
        if self.invoice_type:
            if hasattr(self.invoice_type, 'to_alipay_dict'):
                params['invoice_type'] = self.invoice_type.to_alipay_dict()
            else:
                params['invoice_type'] = self.invoice_type
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.operator:
            if hasattr(self.operator, 'to_alipay_dict'):
                params['operator'] = self.operator.to_alipay_dict()
            else:
                params['operator'] = self.operator
        if self.operator_domain_name:
            if hasattr(self.operator_domain_name, 'to_alipay_dict'):
                params['operator_domain_name'] = self.operator_domain_name.to_alipay_dict()
            else:
                params['operator_domain_name'] = self.operator_domain_name
        if self.order_way:
            if hasattr(self.order_way, 'to_alipay_dict'):
                params['order_way'] = self.order_way.to_alipay_dict()
            else:
                params['order_way'] = self.order_way
        if self.user_invoice_info:
            if hasattr(self.user_invoice_info, 'to_alipay_dict'):
                params['user_invoice_info'] = self.user_invoice_info.to_alipay_dict()
            else:
                params['user_invoice_info'] = self.user_invoice_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossFncGfsettleprodNobillinvoiceApplyModel()
        if 'audit_staff' in d:
            o.audit_staff = d['audit_staff']
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'can_link' in d:
            o.can_link = d['can_link']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'invoice_line_list' in d:
            o.invoice_line_list = d['invoice_line_list']
        if 'invoice_material' in d:
            o.invoice_material = d['invoice_material']
        if 'invoice_note' in d:
            o.invoice_note = d['invoice_note']
        if 'invoice_type' in d:
            o.invoice_type = d['invoice_type']
        if 'memo' in d:
            o.memo = d['memo']
        if 'operator' in d:
            o.operator = d['operator']
        if 'operator_domain_name' in d:
            o.operator_domain_name = d['operator_domain_name']
        if 'order_way' in d:
            o.order_way = d['order_way']
        if 'user_invoice_info' in d:
            o.user_invoice_info = d['user_invoice_info']
        return o


