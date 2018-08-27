#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InsMerchant import InsMerchant


class InsApplicationQuery(object):

    def __init__(self):
        self._application_no = None
        self._application_status = None
        self._merchant = None
        self._operation_id = None
        self._out_biz_no = None
        self._prod_code = None
        self._trade_no = None

    @property
    def application_no(self):
        return self._application_no

    @application_no.setter
    def application_no(self, value):
        self._application_no = value
    @property
    def application_status(self):
        return self._application_status

    @application_status.setter
    def application_status(self, value):
        self._application_status = value
    @property
    def merchant(self):
        return self._merchant

    @merchant.setter
    def merchant(self, value):
        if isinstance(value, InsMerchant):
            self._merchant = value
        else:
            self._merchant = InsMerchant.from_alipay_dict(value)
    @property
    def operation_id(self):
        return self._operation_id

    @operation_id.setter
    def operation_id(self, value):
        self._operation_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def prod_code(self):
        return self._prod_code

    @prod_code.setter
    def prod_code(self, value):
        self._prod_code = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.application_no:
            if hasattr(self.application_no, 'to_alipay_dict'):
                params['application_no'] = self.application_no.to_alipay_dict()
            else:
                params['application_no'] = self.application_no
        if self.application_status:
            if hasattr(self.application_status, 'to_alipay_dict'):
                params['application_status'] = self.application_status.to_alipay_dict()
            else:
                params['application_status'] = self.application_status
        if self.merchant:
            if hasattr(self.merchant, 'to_alipay_dict'):
                params['merchant'] = self.merchant.to_alipay_dict()
            else:
                params['merchant'] = self.merchant
        if self.operation_id:
            if hasattr(self.operation_id, 'to_alipay_dict'):
                params['operation_id'] = self.operation_id.to_alipay_dict()
            else:
                params['operation_id'] = self.operation_id
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.prod_code:
            if hasattr(self.prod_code, 'to_alipay_dict'):
                params['prod_code'] = self.prod_code.to_alipay_dict()
            else:
                params['prod_code'] = self.prod_code
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InsApplicationQuery()
        if 'application_no' in d:
            o.application_no = d['application_no']
        if 'application_status' in d:
            o.application_status = d['application_status']
        if 'merchant' in d:
            o.merchant = d['merchant']
        if 'operation_id' in d:
            o.operation_id = d['operation_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'prod_code' in d:
            o.prod_code = d['prod_code']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        return o


