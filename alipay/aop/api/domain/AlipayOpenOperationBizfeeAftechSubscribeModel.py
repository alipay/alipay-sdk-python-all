#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenOperationBizfeeAftechSubscribeModel(object):

    def __init__(self):
        self._app_name = None
        self._ar_no = None
        self._customer = None
        self._fee_amount = None
        self._fee_currency = None
        self._gmt_begin = None
        self._gmt_end = None
        self._gmt_service = None
        self._inst_code = None
        self._out_biz_no = None
        self._pkg_type = None
        self._product_code = None
        self._properties = None
        self._rel_order_no = None
        self._service_amount = None
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
    def gmt_begin(self):
        return self._gmt_begin

    @gmt_begin.setter
    def gmt_begin(self, value):
        self._gmt_begin = value
    @property
    def gmt_end(self):
        return self._gmt_end

    @gmt_end.setter
    def gmt_end(self, value):
        self._gmt_end = value
    @property
    def gmt_service(self):
        return self._gmt_service

    @gmt_service.setter
    def gmt_service(self, value):
        self._gmt_service = value
    @property
    def inst_code(self):
        return self._inst_code

    @inst_code.setter
    def inst_code(self, value):
        self._inst_code = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def pkg_type(self):
        return self._pkg_type

    @pkg_type.setter
    def pkg_type(self, value):
        self._pkg_type = value
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
    def rel_order_no(self):
        return self._rel_order_no

    @rel_order_no.setter
    def rel_order_no(self, value):
        self._rel_order_no = value
    @property
    def service_amount(self):
        return self._service_amount

    @service_amount.setter
    def service_amount(self, value):
        self._service_amount = value
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
        if self.gmt_begin:
            if hasattr(self.gmt_begin, 'to_alipay_dict'):
                params['gmt_begin'] = self.gmt_begin.to_alipay_dict()
            else:
                params['gmt_begin'] = self.gmt_begin
        if self.gmt_end:
            if hasattr(self.gmt_end, 'to_alipay_dict'):
                params['gmt_end'] = self.gmt_end.to_alipay_dict()
            else:
                params['gmt_end'] = self.gmt_end
        if self.gmt_service:
            if hasattr(self.gmt_service, 'to_alipay_dict'):
                params['gmt_service'] = self.gmt_service.to_alipay_dict()
            else:
                params['gmt_service'] = self.gmt_service
        if self.inst_code:
            if hasattr(self.inst_code, 'to_alipay_dict'):
                params['inst_code'] = self.inst_code.to_alipay_dict()
            else:
                params['inst_code'] = self.inst_code
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.pkg_type:
            if hasattr(self.pkg_type, 'to_alipay_dict'):
                params['pkg_type'] = self.pkg_type.to_alipay_dict()
            else:
                params['pkg_type'] = self.pkg_type
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
        if self.rel_order_no:
            if hasattr(self.rel_order_no, 'to_alipay_dict'):
                params['rel_order_no'] = self.rel_order_no.to_alipay_dict()
            else:
                params['rel_order_no'] = self.rel_order_no
        if self.service_amount:
            if hasattr(self.service_amount, 'to_alipay_dict'):
                params['service_amount'] = self.service_amount.to_alipay_dict()
            else:
                params['service_amount'] = self.service_amount
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
        o = AlipayOpenOperationBizfeeAftechSubscribeModel()
        if 'app_name' in d:
            o.app_name = d['app_name']
        if 'ar_no' in d:
            o.ar_no = d['ar_no']
        if 'customer' in d:
            o.customer = d['customer']
        if 'fee_amount' in d:
            o.fee_amount = d['fee_amount']
        if 'fee_currency' in d:
            o.fee_currency = d['fee_currency']
        if 'gmt_begin' in d:
            o.gmt_begin = d['gmt_begin']
        if 'gmt_end' in d:
            o.gmt_end = d['gmt_end']
        if 'gmt_service' in d:
            o.gmt_service = d['gmt_service']
        if 'inst_code' in d:
            o.inst_code = d['inst_code']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'pkg_type' in d:
            o.pkg_type = d['pkg_type']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'properties' in d:
            o.properties = d['properties']
        if 'rel_order_no' in d:
            o.rel_order_no = d['rel_order_no']
        if 'service_amount' in d:
            o.service_amount = d['service_amount']
        if 'tnt_inst_id' in d:
            o.tnt_inst_id = d['tnt_inst_id']
        return o


