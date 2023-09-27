#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PrizeReceiveDetail(object):

    def __init__(self):
        self._send_order_id = None
        self._voucher_gmt_create = None
        self._voucher_gmt_expired = None
        self._voucher_gmt_modified = None
        self._voucher_id = None
        self._voucher_status = None
        self._voucher_template_id = None

    @property
    def send_order_id(self):
        return self._send_order_id

    @send_order_id.setter
    def send_order_id(self, value):
        self._send_order_id = value
    @property
    def voucher_gmt_create(self):
        return self._voucher_gmt_create

    @voucher_gmt_create.setter
    def voucher_gmt_create(self, value):
        self._voucher_gmt_create = value
    @property
    def voucher_gmt_expired(self):
        return self._voucher_gmt_expired

    @voucher_gmt_expired.setter
    def voucher_gmt_expired(self, value):
        self._voucher_gmt_expired = value
    @property
    def voucher_gmt_modified(self):
        return self._voucher_gmt_modified

    @voucher_gmt_modified.setter
    def voucher_gmt_modified(self, value):
        self._voucher_gmt_modified = value
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
    @property
    def voucher_template_id(self):
        return self._voucher_template_id

    @voucher_template_id.setter
    def voucher_template_id(self, value):
        self._voucher_template_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.send_order_id:
            if hasattr(self.send_order_id, 'to_alipay_dict'):
                params['send_order_id'] = self.send_order_id.to_alipay_dict()
            else:
                params['send_order_id'] = self.send_order_id
        if self.voucher_gmt_create:
            if hasattr(self.voucher_gmt_create, 'to_alipay_dict'):
                params['voucher_gmt_create'] = self.voucher_gmt_create.to_alipay_dict()
            else:
                params['voucher_gmt_create'] = self.voucher_gmt_create
        if self.voucher_gmt_expired:
            if hasattr(self.voucher_gmt_expired, 'to_alipay_dict'):
                params['voucher_gmt_expired'] = self.voucher_gmt_expired.to_alipay_dict()
            else:
                params['voucher_gmt_expired'] = self.voucher_gmt_expired
        if self.voucher_gmt_modified:
            if hasattr(self.voucher_gmt_modified, 'to_alipay_dict'):
                params['voucher_gmt_modified'] = self.voucher_gmt_modified.to_alipay_dict()
            else:
                params['voucher_gmt_modified'] = self.voucher_gmt_modified
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
        if self.voucher_template_id:
            if hasattr(self.voucher_template_id, 'to_alipay_dict'):
                params['voucher_template_id'] = self.voucher_template_id.to_alipay_dict()
            else:
                params['voucher_template_id'] = self.voucher_template_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PrizeReceiveDetail()
        if 'send_order_id' in d:
            o.send_order_id = d['send_order_id']
        if 'voucher_gmt_create' in d:
            o.voucher_gmt_create = d['voucher_gmt_create']
        if 'voucher_gmt_expired' in d:
            o.voucher_gmt_expired = d['voucher_gmt_expired']
        if 'voucher_gmt_modified' in d:
            o.voucher_gmt_modified = d['voucher_gmt_modified']
        if 'voucher_id' in d:
            o.voucher_id = d['voucher_id']
        if 'voucher_status' in d:
            o.voucher_status = d['voucher_status']
        if 'voucher_template_id' in d:
            o.voucher_template_id = d['voucher_template_id']
        return o


