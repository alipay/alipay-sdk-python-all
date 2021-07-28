#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenOperationBizfeeAftechApplyModel(object):

    def __init__(self):
        self._app_name = None
        self._ar_no = None
        self._biz_no = None
        self._customer = None
        self._fee_amount = None
        self._fee_currency = None
        self._gmt_charge = None
        self._gmt_receive = None
        self._gmt_service = None
        self._op_mode = None
        self._out_biz_no = None
        self._product_code = None
        self._properties = None
        self._service_amount = None
        self._settle_period = None
        self._settle_postponed_time = None
        self._settle_type = None
        self._tnt_inst_id = None

    @property
    def app_name(self):
        return self._app_name

    @app_name.setter
    def app_name(self, value):
        self._app_name = value
    @property
    def ar_no(self):
        return self._ar_no

    @ar_no.setter
    def ar_no(self, value):
        self._ar_no = value
    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, value):
        self._customer = value
    @property
    def fee_amount(self):
        return self._fee_amount

    @fee_amount.setter
    def fee_amount(self, value):
        self._fee_amount = value
    @property
    def fee_currency(self):
        return self._fee_currency

    @fee_currency.setter
    def fee_currency(self, value):
        self._fee_currency = value
    @property
    def gmt_charge(self):
        return self._gmt_charge

    @gmt_charge.setter
    def gmt_charge(self, value):
        self._gmt_charge = value
    @property
    def gmt_receive(self):
        return self._gmt_receive

    @gmt_receive.setter
    def gmt_receive(self, value):
        self._gmt_receive = value
    @property
    def gmt_service(self):
        return self._gmt_service

    @gmt_service.setter
    def gmt_service(self, value):
        self._gmt_service = value
    @property
    def op_mode(self):
        return self._op_mode

    @op_mode.setter
    def op_mode(self, value):
        self._op_mode = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def properties(self):
        return self._properties

    @properties.setter
    def properties(self, value):
        self._properties = value
    @property
    def service_amount(self):
        return self._service_amount

    @service_amount.setter
    def service_amount(self, value):
        self._service_amount = value
    @property
    def settle_period(self):
        return self._settle_period

    @settle_period.setter
    def settle_period(self, value):
        self._settle_period = value
    @property
    def settle_postponed_time(self):
        return self._settle_postponed_time

    @settle_postponed_time.setter
    def settle_postponed_time(self, value):
        self._settle_postponed_time = value
    @property
    def settle_type(self):
        return self._settle_type

    @settle_type.setter
    def settle_type(self, value):
        self._settle_type = value
    @property
    def tnt_inst_id(self):
        return self._tnt_inst_id

    @tnt_inst_id.setter
    def tnt_inst_id(self, value):
        self._tnt_inst_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_name:
            if hasattr(self.app_name, 'to_alipay_dict'):
                params['app_name'] = self.app_name.to_alipay_dict()
            else:
                params['app_name'] = self.app_name
        if self.ar_no:
            if hasattr(self.ar_no, 'to_alipay_dict'):
                params['ar_no'] = self.ar_no.to_alipay_dict()
            else:
                params['ar_no'] = self.ar_no
        if self.biz_no:
            if hasattr(self.biz_no, 'to_alipay_dict'):
                params['biz_no'] = self.biz_no.to_alipay_dict()
            else:
                params['biz_no'] = self.biz_no
        if self.customer:
            if hasattr(self.customer, 'to_alipay_dict'):
                params['customer'] = self.customer.to_alipay_dict()
            else:
                params['customer'] = self.customer
        if self.fee_amount:
            if hasattr(self.fee_amount, 'to_alipay_dict'):
                params['fee_amount'] = self.fee_amount.to_alipay_dict()
            else:
                params['fee_amount'] = self.fee_amount
        if self.fee_currency:
            if hasattr(self.fee_currency, 'to_alipay_dict'):
                params['fee_currency'] = self.fee_currency.to_alipay_dict()
            else:
                params['fee_currency'] = self.fee_currency
        if self.gmt_charge:
            if hasattr(self.gmt_charge, 'to_alipay_dict'):
                params['gmt_charge'] = self.gmt_charge.to_alipay_dict()
            else:
                params['gmt_charge'] = self.gmt_charge
        if self.gmt_receive:
            if hasattr(self.gmt_receive, 'to_alipay_dict'):
                params['gmt_receive'] = self.gmt_receive.to_alipay_dict()
            else:
                params['gmt_receive'] = self.gmt_receive
        if self.gmt_service:
            if hasattr(self.gmt_service, 'to_alipay_dict'):
                params['gmt_service'] = self.gmt_service.to_alipay_dict()
            else:
                params['gmt_service'] = self.gmt_service
        if self.op_mode:
            if hasattr(self.op_mode, 'to_alipay_dict'):
                params['op_mode'] = self.op_mode.to_alipay_dict()
            else:
                params['op_mode'] = self.op_mode
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.product_code:
            if hasattr(self.product_code, 'to_alipay_dict'):
                params['product_code'] = self.product_code.to_alipay_dict()
            else:
                params['product_code'] = self.product_code
        if self.properties:
            if hasattr(self.properties, 'to_alipay_dict'):
                params['properties'] = self.properties.to_alipay_dict()
            else:
                params['properties'] = self.properties
        if self.service_amount:
            if hasattr(self.service_amount, 'to_alipay_dict'):
                params['service_amount'] = self.service_amount.to_alipay_dict()
            else:
                params['service_amount'] = self.service_amount
        if self.settle_period:
            if hasattr(self.settle_period, 'to_alipay_dict'):
                params['settle_period'] = self.settle_period.to_alipay_dict()
            else:
                params['settle_period'] = self.settle_period
        if self.settle_postponed_time:
            if hasattr(self.settle_postponed_time, 'to_alipay_dict'):
                params['settle_postponed_time'] = self.settle_postponed_time.to_alipay_dict()
            else:
                params['settle_postponed_time'] = self.settle_postponed_time
        if self.settle_type:
            if hasattr(self.settle_type, 'to_alipay_dict'):
                params['settle_type'] = self.settle_type.to_alipay_dict()
            else:
                params['settle_type'] = self.settle_type
        if self.tnt_inst_id:
            if hasattr(self.tnt_inst_id, 'to_alipay_dict'):
                params['tnt_inst_id'] = self.tnt_inst_id.to_alipay_dict()
            else:
                params['tnt_inst_id'] = self.tnt_inst_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenOperationBizfeeAftechApplyModel()
        if 'app_name' in d:
            o.app_name = d['app_name']
        if 'ar_no' in d:
            o.ar_no = d['ar_no']
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'customer' in d:
            o.customer = d['customer']
        if 'fee_amount' in d:
            o.fee_amount = d['fee_amount']
        if 'fee_currency' in d:
            o.fee_currency = d['fee_currency']
        if 'gmt_charge' in d:
            o.gmt_charge = d['gmt_charge']
        if 'gmt_receive' in d:
            o.gmt_receive = d['gmt_receive']
        if 'gmt_service' in d:
            o.gmt_service = d['gmt_service']
        if 'op_mode' in d:
            o.op_mode = d['op_mode']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'properties' in d:
            o.properties = d['properties']
        if 'service_amount' in d:
            o.service_amount = d['service_amount']
        if 'settle_period' in d:
            o.settle_period = d['settle_period']
        if 'settle_postponed_time' in d:
            o.settle_postponed_time = d['settle_postponed_time']
        if 'settle_type' in d:
            o.settle_type = d['settle_type']
        if 'tnt_inst_id' in d:
            o.tnt_inst_id = d['tnt_inst_id']
        return o


