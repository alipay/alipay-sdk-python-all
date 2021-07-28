#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class VoucherInfoVO(object):

    def __init__(self):
        self._gmt_active = None
        self._gmt_create = None
        self._gmt_expired = None
        self._name = None
        self._template_id = None
        self._total_amount = None
        self._voucher_id = None
        self._voucher_status = None

    @property
    def gmt_active(self):
        return self._gmt_active

    @gmt_active.setter
    def gmt_active(self, value):
        self._gmt_active = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def gmt_expired(self):
        return self._gmt_expired

    @gmt_expired.setter
    def gmt_expired(self, value):
        self._gmt_expired = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def template_id(self):
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        self._template_id = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value
    @property
    def voucher_id(self):
        return self._voucher_id

    @voucher_id.setter
    def voucher_id(self, value):
        self._voucher_id = value
    @property
    def voucher_status(self):
        return self._voucher_status

    @voucher_status.setter
    def voucher_status(self, value):
        self._voucher_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.gmt_active:
            if hasattr(self.gmt_active, 'to_alipay_dict'):
                params['gmt_active'] = self.gmt_active.to_alipay_dict()
            else:
                params['gmt_active'] = self.gmt_active
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.gmt_expired:
            if hasattr(self.gmt_expired, 'to_alipay_dict'):
                params['gmt_expired'] = self.gmt_expired.to_alipay_dict()
            else:
                params['gmt_expired'] = self.gmt_expired
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.template_id:
            if hasattr(self.template_id, 'to_alipay_dict'):
                params['template_id'] = self.template_id.to_alipay_dict()
            else:
                params['template_id'] = self.template_id
        if self.total_amount:
            if hasattr(self.total_amount, 'to_alipay_dict'):
                params['total_amount'] = self.total_amount.to_alipay_dict()
            else:
                params['total_amount'] = self.total_amount
        if self.voucher_id:
            if hasattr(self.voucher_id, 'to_alipay_dict'):
                params['voucher_id'] = self.voucher_id.to_alipay_dict()
            else:
                params['voucher_id'] = self.voucher_id
        if self.voucher_status:
            if hasattr(self.voucher_status, 'to_alipay_dict'):
                params['voucher_status'] = self.voucher_status.to_alipay_dict()
            else:
                params['voucher_status'] = self.voucher_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VoucherInfoVO()
        if 'gmt_active' in d:
            o.gmt_active = d['gmt_active']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'gmt_expired' in d:
            o.gmt_expired = d['gmt_expired']
        if 'name' in d:
            o.name = d['name']
        if 'template_id' in d:
            o.template_id = d['template_id']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        if 'voucher_id' in d:
            o.voucher_id = d['voucher_id']
        if 'voucher_status' in d:
            o.voucher_status = d['voucher_status']
        return o


