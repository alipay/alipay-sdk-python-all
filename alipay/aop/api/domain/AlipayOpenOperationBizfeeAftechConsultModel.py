#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenOperationBizfeeAftechConsultModel(object):

    def __init__(self):
        self._app_name = None
        self._biz_no = None
        self._customer = None
        self._event_codes = None
        self._gmt_charge = None
        self._out_biz_no = None
        self._product_code = None
        self._properties = None
        self._tnt_inst_id = None

    @property
    def app_name(self):
        return self._app_name

    @app_name.setter
    def app_name(self, value):
        self._app_name = value
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
    def event_codes(self):
        return self._event_codes

    @event_codes.setter
    def event_codes(self, value):
        self._event_codes = value
    @property
    def gmt_charge(self):
        return self._gmt_charge

    @gmt_charge.setter
    def gmt_charge(self, value):
        self._gmt_charge = value
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
        if self.event_codes:
            if hasattr(self.event_codes, 'to_alipay_dict'):
                params['event_codes'] = self.event_codes.to_alipay_dict()
            else:
                params['event_codes'] = self.event_codes
        if self.gmt_charge:
            if hasattr(self.gmt_charge, 'to_alipay_dict'):
                params['gmt_charge'] = self.gmt_charge.to_alipay_dict()
            else:
                params['gmt_charge'] = self.gmt_charge
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
        o = AlipayOpenOperationBizfeeAftechConsultModel()
        if 'app_name' in d:
            o.app_name = d['app_name']
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'customer' in d:
            o.customer = d['customer']
        if 'event_codes' in d:
            o.event_codes = d['event_codes']
        if 'gmt_charge' in d:
            o.gmt_charge = d['gmt_charge']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'product_code' in d:
            o.product_code = d['product_code']
        if 'properties' in d:
            o.properties = d['properties']
        if 'tnt_inst_id' in d:
            o.tnt_inst_id = d['tnt_inst_id']
        return o


