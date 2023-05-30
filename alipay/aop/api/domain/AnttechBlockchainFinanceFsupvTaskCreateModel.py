#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechBlockchainFinanceFsupvTaskCreateModel(object):

    def __init__(self):
        self._fund_supv_product_code = None
        self._obj_number = None
        self._obj_trade_end = None
        self._obj_trade_install_amount = None
        self._obj_trade_no = None
        self._obj_trade_settle_period_type = None
        self._obj_trade_start = None
        self._obj_trade_type = None
        self._obj_type = None
        self._request_no = None
        self._supervised_id_number = None
        self._supervised_id_type = None
        self._supervised_name = None
        self._supervisor_id_number = None
        self._supervisor_id_type = None
        self._supervisor_name = None

    @property
    def fund_supv_product_code(self):
        return self._fund_supv_product_code

    @fund_supv_product_code.setter
    def fund_supv_product_code(self, value):
        self._fund_supv_product_code = value
    @property
    def obj_number(self):
        return self._obj_number

    @obj_number.setter
    def obj_number(self, value):
        self._obj_number = value
    @property
    def obj_trade_end(self):
        return self._obj_trade_end

    @obj_trade_end.setter
    def obj_trade_end(self, value):
        self._obj_trade_end = value
    @property
    def obj_trade_install_amount(self):
        return self._obj_trade_install_amount

    @obj_trade_install_amount.setter
    def obj_trade_install_amount(self, value):
        self._obj_trade_install_amount = value
    @property
    def obj_trade_no(self):
        return self._obj_trade_no

    @obj_trade_no.setter
    def obj_trade_no(self, value):
        self._obj_trade_no = value
    @property
    def obj_trade_settle_period_type(self):
        return self._obj_trade_settle_period_type

    @obj_trade_settle_period_type.setter
    def obj_trade_settle_period_type(self, value):
        self._obj_trade_settle_period_type = value
    @property
    def obj_trade_start(self):
        return self._obj_trade_start

    @obj_trade_start.setter
    def obj_trade_start(self, value):
        self._obj_trade_start = value
    @property
    def obj_trade_type(self):
        return self._obj_trade_type

    @obj_trade_type.setter
    def obj_trade_type(self, value):
        self._obj_trade_type = value
    @property
    def obj_type(self):
        return self._obj_type

    @obj_type.setter
    def obj_type(self, value):
        self._obj_type = value
    @property
    def request_no(self):
        return self._request_no

    @request_no.setter
    def request_no(self, value):
        self._request_no = value
    @property
    def supervised_id_number(self):
        return self._supervised_id_number

    @supervised_id_number.setter
    def supervised_id_number(self, value):
        self._supervised_id_number = value
    @property
    def supervised_id_type(self):
        return self._supervised_id_type

    @supervised_id_type.setter
    def supervised_id_type(self, value):
        self._supervised_id_type = value
    @property
    def supervised_name(self):
        return self._supervised_name

    @supervised_name.setter
    def supervised_name(self, value):
        self._supervised_name = value
    @property
    def supervisor_id_number(self):
        return self._supervisor_id_number

    @supervisor_id_number.setter
    def supervisor_id_number(self, value):
        self._supervisor_id_number = value
    @property
    def supervisor_id_type(self):
        return self._supervisor_id_type

    @supervisor_id_type.setter
    def supervisor_id_type(self, value):
        self._supervisor_id_type = value
    @property
    def supervisor_name(self):
        return self._supervisor_name

    @supervisor_name.setter
    def supervisor_name(self, value):
        self._supervisor_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.fund_supv_product_code:
            if hasattr(self.fund_supv_product_code, 'to_alipay_dict'):
                params['fund_supv_product_code'] = self.fund_supv_product_code.to_alipay_dict()
            else:
                params['fund_supv_product_code'] = self.fund_supv_product_code
        if self.obj_number:
            if hasattr(self.obj_number, 'to_alipay_dict'):
                params['obj_number'] = self.obj_number.to_alipay_dict()
            else:
                params['obj_number'] = self.obj_number
        if self.obj_trade_end:
            if hasattr(self.obj_trade_end, 'to_alipay_dict'):
                params['obj_trade_end'] = self.obj_trade_end.to_alipay_dict()
            else:
                params['obj_trade_end'] = self.obj_trade_end
        if self.obj_trade_install_amount:
            if hasattr(self.obj_trade_install_amount, 'to_alipay_dict'):
                params['obj_trade_install_amount'] = self.obj_trade_install_amount.to_alipay_dict()
            else:
                params['obj_trade_install_amount'] = self.obj_trade_install_amount
        if self.obj_trade_no:
            if hasattr(self.obj_trade_no, 'to_alipay_dict'):
                params['obj_trade_no'] = self.obj_trade_no.to_alipay_dict()
            else:
                params['obj_trade_no'] = self.obj_trade_no
        if self.obj_trade_settle_period_type:
            if hasattr(self.obj_trade_settle_period_type, 'to_alipay_dict'):
                params['obj_trade_settle_period_type'] = self.obj_trade_settle_period_type.to_alipay_dict()
            else:
                params['obj_trade_settle_period_type'] = self.obj_trade_settle_period_type
        if self.obj_trade_start:
            if hasattr(self.obj_trade_start, 'to_alipay_dict'):
                params['obj_trade_start'] = self.obj_trade_start.to_alipay_dict()
            else:
                params['obj_trade_start'] = self.obj_trade_start
        if self.obj_trade_type:
            if hasattr(self.obj_trade_type, 'to_alipay_dict'):
                params['obj_trade_type'] = self.obj_trade_type.to_alipay_dict()
            else:
                params['obj_trade_type'] = self.obj_trade_type
        if self.obj_type:
            if hasattr(self.obj_type, 'to_alipay_dict'):
                params['obj_type'] = self.obj_type.to_alipay_dict()
            else:
                params['obj_type'] = self.obj_type
        if self.request_no:
            if hasattr(self.request_no, 'to_alipay_dict'):
                params['request_no'] = self.request_no.to_alipay_dict()
            else:
                params['request_no'] = self.request_no
        if self.supervised_id_number:
            if hasattr(self.supervised_id_number, 'to_alipay_dict'):
                params['supervised_id_number'] = self.supervised_id_number.to_alipay_dict()
            else:
                params['supervised_id_number'] = self.supervised_id_number
        if self.supervised_id_type:
            if hasattr(self.supervised_id_type, 'to_alipay_dict'):
                params['supervised_id_type'] = self.supervised_id_type.to_alipay_dict()
            else:
                params['supervised_id_type'] = self.supervised_id_type
        if self.supervised_name:
            if hasattr(self.supervised_name, 'to_alipay_dict'):
                params['supervised_name'] = self.supervised_name.to_alipay_dict()
            else:
                params['supervised_name'] = self.supervised_name
        if self.supervisor_id_number:
            if hasattr(self.supervisor_id_number, 'to_alipay_dict'):
                params['supervisor_id_number'] = self.supervisor_id_number.to_alipay_dict()
            else:
                params['supervisor_id_number'] = self.supervisor_id_number
        if self.supervisor_id_type:
            if hasattr(self.supervisor_id_type, 'to_alipay_dict'):
                params['supervisor_id_type'] = self.supervisor_id_type.to_alipay_dict()
            else:
                params['supervisor_id_type'] = self.supervisor_id_type
        if self.supervisor_name:
            if hasattr(self.supervisor_name, 'to_alipay_dict'):
                params['supervisor_name'] = self.supervisor_name.to_alipay_dict()
            else:
                params['supervisor_name'] = self.supervisor_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechBlockchainFinanceFsupvTaskCreateModel()
        if 'fund_supv_product_code' in d:
            o.fund_supv_product_code = d['fund_supv_product_code']
        if 'obj_number' in d:
            o.obj_number = d['obj_number']
        if 'obj_trade_end' in d:
            o.obj_trade_end = d['obj_trade_end']
        if 'obj_trade_install_amount' in d:
            o.obj_trade_install_amount = d['obj_trade_install_amount']
        if 'obj_trade_no' in d:
            o.obj_trade_no = d['obj_trade_no']
        if 'obj_trade_settle_period_type' in d:
            o.obj_trade_settle_period_type = d['obj_trade_settle_period_type']
        if 'obj_trade_start' in d:
            o.obj_trade_start = d['obj_trade_start']
        if 'obj_trade_type' in d:
            o.obj_trade_type = d['obj_trade_type']
        if 'obj_type' in d:
            o.obj_type = d['obj_type']
        if 'request_no' in d:
            o.request_no = d['request_no']
        if 'supervised_id_number' in d:
            o.supervised_id_number = d['supervised_id_number']
        if 'supervised_id_type' in d:
            o.supervised_id_type = d['supervised_id_type']
        if 'supervised_name' in d:
            o.supervised_name = d['supervised_name']
        if 'supervisor_id_number' in d:
            o.supervisor_id_number = d['supervisor_id_number']
        if 'supervisor_id_type' in d:
            o.supervisor_id_type = d['supervisor_id_type']
        if 'supervisor_name' in d:
            o.supervisor_name = d['supervisor_name']
        return o


