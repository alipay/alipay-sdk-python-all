#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class BasicBizOrderLineDTO(object):

    def __init__(self):
        self._ar_no = None
        self._audit_memo = None
        self._fulfil_product_code = None
        self._order_line_state = None
        self._pd_open_no = None
        self._permission_set_code = None
        self._permission_set_open_no = None
        self._purchaser = None
        self._purchaser_type = None
        self._sales_product_code = None

    @property
    def ar_no(self):
        return self._ar_no

    @ar_no.setter
    def ar_no(self, value):
        self._ar_no = value
    @property
    def audit_memo(self):
        return self._audit_memo

    @audit_memo.setter
    def audit_memo(self, value):
        self._audit_memo = value
    @property
    def fulfil_product_code(self):
        return self._fulfil_product_code

    @fulfil_product_code.setter
    def fulfil_product_code(self, value):
        self._fulfil_product_code = value
    @property
    def order_line_state(self):
        return self._order_line_state

    @order_line_state.setter
    def order_line_state(self, value):
        self._order_line_state = value
    @property
    def pd_open_no(self):
        return self._pd_open_no

    @pd_open_no.setter
    def pd_open_no(self, value):
        self._pd_open_no = value
    @property
    def permission_set_code(self):
        return self._permission_set_code

    @permission_set_code.setter
    def permission_set_code(self, value):
        self._permission_set_code = value
    @property
    def permission_set_open_no(self):
        return self._permission_set_open_no

    @permission_set_open_no.setter
    def permission_set_open_no(self, value):
        self._permission_set_open_no = value
    @property
    def purchaser(self):
        return self._purchaser

    @purchaser.setter
    def purchaser(self, value):
        if isinstance(value, list):
            self._purchaser = list()
            for i in value:
                self._purchaser.append(i)
    @property
    def purchaser_type(self):
        return self._purchaser_type

    @purchaser_type.setter
    def purchaser_type(self, value):
        self._purchaser_type = value
    @property
    def sales_product_code(self):
        return self._sales_product_code

    @sales_product_code.setter
    def sales_product_code(self, value):
        self._sales_product_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.ar_no:
            if hasattr(self.ar_no, 'to_alipay_dict'):
                params['ar_no'] = self.ar_no.to_alipay_dict()
            else:
                params['ar_no'] = self.ar_no
        if self.audit_memo:
            if hasattr(self.audit_memo, 'to_alipay_dict'):
                params['audit_memo'] = self.audit_memo.to_alipay_dict()
            else:
                params['audit_memo'] = self.audit_memo
        if self.fulfil_product_code:
            if hasattr(self.fulfil_product_code, 'to_alipay_dict'):
                params['fulfil_product_code'] = self.fulfil_product_code.to_alipay_dict()
            else:
                params['fulfil_product_code'] = self.fulfil_product_code
        if self.order_line_state:
            if hasattr(self.order_line_state, 'to_alipay_dict'):
                params['order_line_state'] = self.order_line_state.to_alipay_dict()
            else:
                params['order_line_state'] = self.order_line_state
        if self.pd_open_no:
            if hasattr(self.pd_open_no, 'to_alipay_dict'):
                params['pd_open_no'] = self.pd_open_no.to_alipay_dict()
            else:
                params['pd_open_no'] = self.pd_open_no
        if self.permission_set_code:
            if hasattr(self.permission_set_code, 'to_alipay_dict'):
                params['permission_set_code'] = self.permission_set_code.to_alipay_dict()
            else:
                params['permission_set_code'] = self.permission_set_code
        if self.permission_set_open_no:
            if hasattr(self.permission_set_open_no, 'to_alipay_dict'):
                params['permission_set_open_no'] = self.permission_set_open_no.to_alipay_dict()
            else:
                params['permission_set_open_no'] = self.permission_set_open_no
        if self.purchaser:
            if isinstance(self.purchaser, list):
                for i in range(0, len(self.purchaser)):
                    element = self.purchaser[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.purchaser[i] = element.to_alipay_dict()
            if hasattr(self.purchaser, 'to_alipay_dict'):
                params['purchaser'] = self.purchaser.to_alipay_dict()
            else:
                params['purchaser'] = self.purchaser
        if self.purchaser_type:
            if hasattr(self.purchaser_type, 'to_alipay_dict'):
                params['purchaser_type'] = self.purchaser_type.to_alipay_dict()
            else:
                params['purchaser_type'] = self.purchaser_type
        if self.sales_product_code:
            if hasattr(self.sales_product_code, 'to_alipay_dict'):
                params['sales_product_code'] = self.sales_product_code.to_alipay_dict()
            else:
                params['sales_product_code'] = self.sales_product_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = BasicBizOrderLineDTO()
        if 'ar_no' in d:
            o.ar_no = d['ar_no']
        if 'audit_memo' in d:
            o.audit_memo = d['audit_memo']
        if 'fulfil_product_code' in d:
            o.fulfil_product_code = d['fulfil_product_code']
        if 'order_line_state' in d:
            o.order_line_state = d['order_line_state']
        if 'pd_open_no' in d:
            o.pd_open_no = d['pd_open_no']
        if 'permission_set_code' in d:
            o.permission_set_code = d['permission_set_code']
        if 'permission_set_open_no' in d:
            o.permission_set_open_no = d['permission_set_open_no']
        if 'purchaser' in d:
            o.purchaser = d['purchaser']
        if 'purchaser_type' in d:
            o.purchaser_type = d['purchaser_type']
        if 'sales_product_code' in d:
            o.sales_product_code = d['sales_product_code']
        return o


