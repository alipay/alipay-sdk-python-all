#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class QueryDetailAopResult(object):

    def __init__(self):
        self._batch_no = None
        self._detail_no = None
        self._ext_param = None
        self._fail_message = None
        self._last_modified = None
        self._order_no = None
        self._pay_amount = None
        self._payee_id = None
        self._payer_id = None
        self._service_charge = None
        self._status = None

    @property
    def batch_no(self):
        return self._batch_no

    @batch_no.setter
    def batch_no(self, value):
        self._batch_no = value
    @property
    def detail_no(self):
        return self._detail_no

    @detail_no.setter
    def detail_no(self, value):
        self._detail_no = value
    @property
    def ext_param(self):
        return self._ext_param

    @ext_param.setter
    def ext_param(self, value):
        self._ext_param = value
    @property
    def fail_message(self):
        return self._fail_message

    @fail_message.setter
    def fail_message(self, value):
        self._fail_message = value
    @property
    def last_modified(self):
        return self._last_modified

    @last_modified.setter
    def last_modified(self, value):
        self._last_modified = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def pay_amount(self):
        return self._pay_amount

    @pay_amount.setter
    def pay_amount(self, value):
        self._pay_amount = value
    @property
    def payee_id(self):
        return self._payee_id

    @payee_id.setter
    def payee_id(self, value):
        self._payee_id = value
    @property
    def payer_id(self):
        return self._payer_id

    @payer_id.setter
    def payer_id(self, value):
        self._payer_id = value
    @property
    def service_charge(self):
        return self._service_charge

    @service_charge.setter
    def service_charge(self, value):
        self._service_charge = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.batch_no:
            if hasattr(self.batch_no, 'to_alipay_dict'):
                params['batch_no'] = self.batch_no.to_alipay_dict()
            else:
                params['batch_no'] = self.batch_no
        if self.detail_no:
            if hasattr(self.detail_no, 'to_alipay_dict'):
                params['detail_no'] = self.detail_no.to_alipay_dict()
            else:
                params['detail_no'] = self.detail_no
        if self.ext_param:
            if hasattr(self.ext_param, 'to_alipay_dict'):
                params['ext_param'] = self.ext_param.to_alipay_dict()
            else:
                params['ext_param'] = self.ext_param
        if self.fail_message:
            if hasattr(self.fail_message, 'to_alipay_dict'):
                params['fail_message'] = self.fail_message.to_alipay_dict()
            else:
                params['fail_message'] = self.fail_message
        if self.last_modified:
            if hasattr(self.last_modified, 'to_alipay_dict'):
                params['last_modified'] = self.last_modified.to_alipay_dict()
            else:
                params['last_modified'] = self.last_modified
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        if self.pay_amount:
            if hasattr(self.pay_amount, 'to_alipay_dict'):
                params['pay_amount'] = self.pay_amount.to_alipay_dict()
            else:
                params['pay_amount'] = self.pay_amount
        if self.payee_id:
            if hasattr(self.payee_id, 'to_alipay_dict'):
                params['payee_id'] = self.payee_id.to_alipay_dict()
            else:
                params['payee_id'] = self.payee_id
        if self.payer_id:
            if hasattr(self.payer_id, 'to_alipay_dict'):
                params['payer_id'] = self.payer_id.to_alipay_dict()
            else:
                params['payer_id'] = self.payer_id
        if self.service_charge:
            if hasattr(self.service_charge, 'to_alipay_dict'):
                params['service_charge'] = self.service_charge.to_alipay_dict()
            else:
                params['service_charge'] = self.service_charge
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
        o = QueryDetailAopResult()
        if 'batch_no' in d:
            o.batch_no = d['batch_no']
        if 'detail_no' in d:
            o.detail_no = d['detail_no']
        if 'ext_param' in d:
            o.ext_param = d['ext_param']
        if 'fail_message' in d:
            o.fail_message = d['fail_message']
        if 'last_modified' in d:
            o.last_modified = d['last_modified']
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'pay_amount' in d:
            o.pay_amount = d['pay_amount']
        if 'payee_id' in d:
            o.payee_id = d['payee_id']
        if 'payer_id' in d:
            o.payer_id = d['payer_id']
        if 'service_charge' in d:
            o.service_charge = d['service_charge']
        if 'status' in d:
            o.status = d['status']
        return o


