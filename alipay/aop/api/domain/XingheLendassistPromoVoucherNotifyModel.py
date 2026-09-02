#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class XingheLendassistPromoVoucherNotifyModel(object):

    def __init__(self):
        self._apply_no = None
        self._cust_name = None
        self._id_card = None
        self._inst_code = None
        self._inst_voucher_info = None
        self._notify_type = None
        self._request_id = None

    @property
    def apply_no(self):
        return self._apply_no

    @apply_no.setter
    def apply_no(self, value):
        self._apply_no = value
    @property
    def cust_name(self):
        return self._cust_name

    @cust_name.setter
    def cust_name(self, value):
        self._cust_name = value
    @property
    def id_card(self):
        return self._id_card

    @id_card.setter
    def id_card(self, value):
        self._id_card = value
    @property
    def inst_code(self):
        return self._inst_code

    @inst_code.setter
    def inst_code(self, value):
        self._inst_code = value
    @property
    def inst_voucher_info(self):
        return self._inst_voucher_info

    @inst_voucher_info.setter
    def inst_voucher_info(self, value):
        self._inst_voucher_info = value
    @property
    def notify_type(self):
        return self._notify_type

    @notify_type.setter
    def notify_type(self, value):
        self._notify_type = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_no:
            if hasattr(self.apply_no, 'to_alipay_dict'):
                params['apply_no'] = self.apply_no.to_alipay_dict()
            else:
                params['apply_no'] = self.apply_no
        if self.cust_name:
            if hasattr(self.cust_name, 'to_alipay_dict'):
                params['cust_name'] = self.cust_name.to_alipay_dict()
            else:
                params['cust_name'] = self.cust_name
        if self.id_card:
            if hasattr(self.id_card, 'to_alipay_dict'):
                params['id_card'] = self.id_card.to_alipay_dict()
            else:
                params['id_card'] = self.id_card
        if self.inst_code:
            if hasattr(self.inst_code, 'to_alipay_dict'):
                params['inst_code'] = self.inst_code.to_alipay_dict()
            else:
                params['inst_code'] = self.inst_code
        if self.inst_voucher_info:
            if hasattr(self.inst_voucher_info, 'to_alipay_dict'):
                params['inst_voucher_info'] = self.inst_voucher_info.to_alipay_dict()
            else:
                params['inst_voucher_info'] = self.inst_voucher_info
        if self.notify_type:
            if hasattr(self.notify_type, 'to_alipay_dict'):
                params['notify_type'] = self.notify_type.to_alipay_dict()
            else:
                params['notify_type'] = self.notify_type
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = XingheLendassistPromoVoucherNotifyModel()
        if 'apply_no' in d:
            o.apply_no = d['apply_no']
        if 'cust_name' in d:
            o.cust_name = d['cust_name']
        if 'id_card' in d:
            o.id_card = d['id_card']
        if 'inst_code' in d:
            o.inst_code = d['inst_code']
        if 'inst_voucher_info' in d:
            o.inst_voucher_info = d['inst_voucher_info']
        if 'notify_type' in d:
            o.notify_type = d['notify_type']
        if 'request_id' in d:
            o.request_id = d['request_id']
        return o


