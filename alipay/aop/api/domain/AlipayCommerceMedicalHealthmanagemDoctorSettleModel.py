#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalHealthmanagemDoctorSettleModel(object):

    def __init__(self):
        self._bill_amount = None
        self._finance_detail_no = None
        self._gmt_service = None
        self._item_id = None
        self._item_order_no = None
        self._package_order_no = None

    @property
    def bill_amount(self):
        return self._bill_amount

    @bill_amount.setter
    def bill_amount(self, value):
        self._bill_amount = value
    @property
    def finance_detail_no(self):
        return self._finance_detail_no

    @finance_detail_no.setter
    def finance_detail_no(self, value):
        self._finance_detail_no = value
    @property
    def gmt_service(self):
        return self._gmt_service

    @gmt_service.setter
    def gmt_service(self, value):
        self._gmt_service = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def item_order_no(self):
        return self._item_order_no

    @item_order_no.setter
    def item_order_no(self, value):
        self._item_order_no = value
    @property
    def package_order_no(self):
        return self._package_order_no

    @package_order_no.setter
    def package_order_no(self, value):
        self._package_order_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.bill_amount:
            if hasattr(self.bill_amount, 'to_alipay_dict'):
                params['bill_amount'] = self.bill_amount.to_alipay_dict()
            else:
                params['bill_amount'] = self.bill_amount
        if self.finance_detail_no:
            if hasattr(self.finance_detail_no, 'to_alipay_dict'):
                params['finance_detail_no'] = self.finance_detail_no.to_alipay_dict()
            else:
                params['finance_detail_no'] = self.finance_detail_no
        if self.gmt_service:
            if hasattr(self.gmt_service, 'to_alipay_dict'):
                params['gmt_service'] = self.gmt_service.to_alipay_dict()
            else:
                params['gmt_service'] = self.gmt_service
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.item_order_no:
            if hasattr(self.item_order_no, 'to_alipay_dict'):
                params['item_order_no'] = self.item_order_no.to_alipay_dict()
            else:
                params['item_order_no'] = self.item_order_no
        if self.package_order_no:
            if hasattr(self.package_order_no, 'to_alipay_dict'):
                params['package_order_no'] = self.package_order_no.to_alipay_dict()
            else:
                params['package_order_no'] = self.package_order_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalHealthmanagemDoctorSettleModel()
        if 'bill_amount' in d:
            o.bill_amount = d['bill_amount']
        if 'finance_detail_no' in d:
            o.finance_detail_no = d['finance_detail_no']
        if 'gmt_service' in d:
            o.gmt_service = d['gmt_service']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'item_order_no' in d:
            o.item_order_no = d['item_order_no']
        if 'package_order_no' in d:
            o.package_order_no = d['package_order_no']
        return o


