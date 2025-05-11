#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceEcRecyclinginvoiceCompanyclerkCreateModel(object):

    def __init__(self):
        self._clerk_name = None
        self._clerk_no = None
        self._clerk_permit_list = None
        self._clerk_phone = None
        self._clerk_role = None
        self._out_clerk_id = None
        self._tax_no = None

    @property
    def clerk_name(self):
        return self._clerk_name

    @clerk_name.setter
    def clerk_name(self, value):
        self._clerk_name = value
    @property
    def clerk_no(self):
        return self._clerk_no

    @clerk_no.setter
    def clerk_no(self, value):
        self._clerk_no = value
    @property
    def clerk_permit_list(self):
        return self._clerk_permit_list

    @clerk_permit_list.setter
    def clerk_permit_list(self, value):
        if isinstance(value, list):
            self._clerk_permit_list = list()
            for i in value:
                self._clerk_permit_list.append(i)
    @property
    def clerk_phone(self):
        return self._clerk_phone

    @clerk_phone.setter
    def clerk_phone(self, value):
        self._clerk_phone = value
    @property
    def clerk_role(self):
        return self._clerk_role

    @clerk_role.setter
    def clerk_role(self, value):
        self._clerk_role = value
    @property
    def out_clerk_id(self):
        return self._out_clerk_id

    @out_clerk_id.setter
    def out_clerk_id(self, value):
        self._out_clerk_id = value
    @property
    def tax_no(self):
        return self._tax_no

    @tax_no.setter
    def tax_no(self, value):
        self._tax_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.clerk_name:
            if hasattr(self.clerk_name, 'to_alipay_dict'):
                params['clerk_name'] = self.clerk_name.to_alipay_dict()
            else:
                params['clerk_name'] = self.clerk_name
        if self.clerk_no:
            if hasattr(self.clerk_no, 'to_alipay_dict'):
                params['clerk_no'] = self.clerk_no.to_alipay_dict()
            else:
                params['clerk_no'] = self.clerk_no
        if self.clerk_permit_list:
            if isinstance(self.clerk_permit_list, list):
                for i in range(0, len(self.clerk_permit_list)):
                    element = self.clerk_permit_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.clerk_permit_list[i] = element.to_alipay_dict()
            if hasattr(self.clerk_permit_list, 'to_alipay_dict'):
                params['clerk_permit_list'] = self.clerk_permit_list.to_alipay_dict()
            else:
                params['clerk_permit_list'] = self.clerk_permit_list
        if self.clerk_phone:
            if hasattr(self.clerk_phone, 'to_alipay_dict'):
                params['clerk_phone'] = self.clerk_phone.to_alipay_dict()
            else:
                params['clerk_phone'] = self.clerk_phone
        if self.clerk_role:
            if hasattr(self.clerk_role, 'to_alipay_dict'):
                params['clerk_role'] = self.clerk_role.to_alipay_dict()
            else:
                params['clerk_role'] = self.clerk_role
        if self.out_clerk_id:
            if hasattr(self.out_clerk_id, 'to_alipay_dict'):
                params['out_clerk_id'] = self.out_clerk_id.to_alipay_dict()
            else:
                params['out_clerk_id'] = self.out_clerk_id
        if self.tax_no:
            if hasattr(self.tax_no, 'to_alipay_dict'):
                params['tax_no'] = self.tax_no.to_alipay_dict()
            else:
                params['tax_no'] = self.tax_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceEcRecyclinginvoiceCompanyclerkCreateModel()
        if 'clerk_name' in d:
            o.clerk_name = d['clerk_name']
        if 'clerk_no' in d:
            o.clerk_no = d['clerk_no']
        if 'clerk_permit_list' in d:
            o.clerk_permit_list = d['clerk_permit_list']
        if 'clerk_phone' in d:
            o.clerk_phone = d['clerk_phone']
        if 'clerk_role' in d:
            o.clerk_role = d['clerk_role']
        if 'out_clerk_id' in d:
            o.out_clerk_id = d['out_clerk_id']
        if 'tax_no' in d:
            o.tax_no = d['tax_no']
        return o


