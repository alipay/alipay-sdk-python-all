#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EbppOrderItem(object):

    def __init__(self):
        self._alipay_item_id = None
        self._biz_amount = None
        self._biz_prod_id = None
        self._extend_field = None
        self._inst_item_id = None
        self._linked_bill_no = None
        self._status = None

    @property
    def alipay_item_id(self):
        return self._alipay_item_id

    @alipay_item_id.setter
    def alipay_item_id(self, value):
        self._alipay_item_id = value
    @property
    def biz_amount(self):
        return self._biz_amount

    @biz_amount.setter
    def biz_amount(self, value):
        self._biz_amount = value
    @property
    def biz_prod_id(self):
        return self._biz_prod_id

    @biz_prod_id.setter
    def biz_prod_id(self, value):
        self._biz_prod_id = value
    @property
    def extend_field(self):
        return self._extend_field

    @extend_field.setter
    def extend_field(self, value):
        self._extend_field = value
    @property
    def inst_item_id(self):
        return self._inst_item_id

    @inst_item_id.setter
    def inst_item_id(self, value):
        self._inst_item_id = value
    @property
    def linked_bill_no(self):
        return self._linked_bill_no

    @linked_bill_no.setter
    def linked_bill_no(self, value):
        self._linked_bill_no = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_item_id:
            if hasattr(self.alipay_item_id, 'to_alipay_dict'):
                params['alipay_item_id'] = self.alipay_item_id.to_alipay_dict()
            else:
                params['alipay_item_id'] = self.alipay_item_id
        if self.biz_amount:
            if hasattr(self.biz_amount, 'to_alipay_dict'):
                params['biz_amount'] = self.biz_amount.to_alipay_dict()
            else:
                params['biz_amount'] = self.biz_amount
        if self.biz_prod_id:
            if hasattr(self.biz_prod_id, 'to_alipay_dict'):
                params['biz_prod_id'] = self.biz_prod_id.to_alipay_dict()
            else:
                params['biz_prod_id'] = self.biz_prod_id
        if self.extend_field:
            if hasattr(self.extend_field, 'to_alipay_dict'):
                params['extend_field'] = self.extend_field.to_alipay_dict()
            else:
                params['extend_field'] = self.extend_field
        if self.inst_item_id:
            if hasattr(self.inst_item_id, 'to_alipay_dict'):
                params['inst_item_id'] = self.inst_item_id.to_alipay_dict()
            else:
                params['inst_item_id'] = self.inst_item_id
        if self.linked_bill_no:
            if hasattr(self.linked_bill_no, 'to_alipay_dict'):
                params['linked_bill_no'] = self.linked_bill_no.to_alipay_dict()
            else:
                params['linked_bill_no'] = self.linked_bill_no
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
        o = EbppOrderItem()
        if 'alipay_item_id' in d:
            o.alipay_item_id = d['alipay_item_id']
        if 'biz_amount' in d:
            o.biz_amount = d['biz_amount']
        if 'biz_prod_id' in d:
            o.biz_prod_id = d['biz_prod_id']
        if 'extend_field' in d:
            o.extend_field = d['extend_field']
        if 'inst_item_id' in d:
            o.inst_item_id = d['inst_item_id']
        if 'linked_bill_no' in d:
            o.linked_bill_no = d['linked_bill_no']
        if 'status' in d:
            o.status = d['status']
        return o


