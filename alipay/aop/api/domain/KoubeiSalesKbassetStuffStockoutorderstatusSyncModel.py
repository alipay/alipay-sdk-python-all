#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.StockShippingStepInfo import StockShippingStepInfo


class KoubeiSalesKbassetStuffStockoutorderstatusSyncModel(object):

    def __init__(self):
        self._erp_order = None
        self._erp_order_type = None
        self._ext_info = None
        self._steps = None
        self._warehouse_code = None
        self._way_bill_no = None

    @property
    def erp_order(self):
        return self._erp_order

    @erp_order.setter
    def erp_order(self, value):
        self._erp_order = value
    @property
    def erp_order_type(self):
        return self._erp_order_type

    @erp_order_type.setter
    def erp_order_type(self, value):
        self._erp_order_type = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def steps(self):
        return self._steps

    @steps.setter
    def steps(self, value):
        if isinstance(value, list):
            self._steps = list()
            for i in value:
                if isinstance(i, StockShippingStepInfo):
                    self._steps.append(i)
                else:
                    self._steps.append(StockShippingStepInfo.from_alipay_dict(i))
    @property
    def warehouse_code(self):
        return self._warehouse_code

    @warehouse_code.setter
    def warehouse_code(self, value):
        self._warehouse_code = value
    @property
    def way_bill_no(self):
        return self._way_bill_no

    @way_bill_no.setter
    def way_bill_no(self, value):
        self._way_bill_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.erp_order:
            if hasattr(self.erp_order, 'to_alipay_dict'):
                params['erp_order'] = self.erp_order.to_alipay_dict()
            else:
                params['erp_order'] = self.erp_order
        if self.erp_order_type:
            if hasattr(self.erp_order_type, 'to_alipay_dict'):
                params['erp_order_type'] = self.erp_order_type.to_alipay_dict()
            else:
                params['erp_order_type'] = self.erp_order_type
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.steps:
            if isinstance(self.steps, list):
                for i in range(0, len(self.steps)):
                    element = self.steps[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.steps[i] = element.to_alipay_dict()
            if hasattr(self.steps, 'to_alipay_dict'):
                params['steps'] = self.steps.to_alipay_dict()
            else:
                params['steps'] = self.steps
        if self.warehouse_code:
            if hasattr(self.warehouse_code, 'to_alipay_dict'):
                params['warehouse_code'] = self.warehouse_code.to_alipay_dict()
            else:
                params['warehouse_code'] = self.warehouse_code
        if self.way_bill_no:
            if hasattr(self.way_bill_no, 'to_alipay_dict'):
                params['way_bill_no'] = self.way_bill_no.to_alipay_dict()
            else:
                params['way_bill_no'] = self.way_bill_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiSalesKbassetStuffStockoutorderstatusSyncModel()
        if 'erp_order' in d:
            o.erp_order = d['erp_order']
        if 'erp_order_type' in d:
            o.erp_order_type = d['erp_order_type']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'steps' in d:
            o.steps = d['steps']
        if 'warehouse_code' in d:
            o.warehouse_code = d['warehouse_code']
        if 'way_bill_no' in d:
            o.way_bill_no = d['way_bill_no']
        return o


