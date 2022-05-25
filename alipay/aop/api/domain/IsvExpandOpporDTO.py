#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class IsvExpandOpporDTO(object):

    def __init__(self):
        self._address = None
        self._leads_id = None
        self._name = None
        self._oppor_id = None
        self._out_biz_no = None
        self._phone = None
        self._status = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def leads_id(self):
        return self._leads_id

    @leads_id.setter
    def leads_id(self, value):
        self._leads_id = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def oppor_id(self):
        return self._oppor_id

    @oppor_id.setter
    def oppor_id(self, value):
        self._oppor_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.leads_id:
            if hasattr(self.leads_id, 'to_alipay_dict'):
                params['leads_id'] = self.leads_id.to_alipay_dict()
            else:
                params['leads_id'] = self.leads_id
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.oppor_id:
            if hasattr(self.oppor_id, 'to_alipay_dict'):
                params['oppor_id'] = self.oppor_id.to_alipay_dict()
            else:
                params['oppor_id'] = self.oppor_id
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.phone:
            if hasattr(self.phone, 'to_alipay_dict'):
                params['phone'] = self.phone.to_alipay_dict()
            else:
                params['phone'] = self.phone
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IsvExpandOpporDTO()
        if 'address' in d:
            o.address = d['address']
        if 'leads_id' in d:
            o.leads_id = d['leads_id']
        if 'name' in d:
            o.name = d['name']
        if 'oppor_id' in d:
            o.oppor_id = d['oppor_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'phone' in d:
            o.phone = d['phone']
        if 'status' in d:
            o.status = d['status']
        return o


