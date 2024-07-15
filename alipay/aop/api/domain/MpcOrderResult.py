#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MpcOrderLineResult import MpcOrderLineResult


class MpcOrderResult(object):

    def __init__(self):
        self._create_date = None
        self._logistics_status = None
        self._order_amount = None
        self._order_id = None
        self._order_line_list = None
        self._order_status = None

    @property
    def create_date(self):
        return self._create_date

    @create_date.setter
    def create_date(self, value):
        self._create_date = value
    @property
    def logistics_status(self):
        return self._logistics_status

    @logistics_status.setter
    def logistics_status(self, value):
        self._logistics_status = value
    @property
    def order_amount(self):
        return self._order_amount

    @order_amount.setter
    def order_amount(self, value):
        self._order_amount = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def order_line_list(self):
        return self._order_line_list

    @order_line_list.setter
    def order_line_list(self, value):
        if isinstance(value, list):
            self._order_line_list = list()
            for i in value:
                if isinstance(i, MpcOrderLineResult):
                    self._order_line_list.append(i)
                else:
                    self._order_line_list.append(MpcOrderLineResult.from_alipay_dict(i))
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.create_date:
            if hasattr(self.create_date, 'to_alipay_dict'):
                params['create_date'] = self.create_date.to_alipay_dict()
            else:
                params['create_date'] = self.create_date
        if self.logistics_status:
            if hasattr(self.logistics_status, 'to_alipay_dict'):
                params['logistics_status'] = self.logistics_status.to_alipay_dict()
            else:
                params['logistics_status'] = self.logistics_status
        if self.order_amount:
            if hasattr(self.order_amount, 'to_alipay_dict'):
                params['order_amount'] = self.order_amount.to_alipay_dict()
            else:
                params['order_amount'] = self.order_amount
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.order_line_list:
            if isinstance(self.order_line_list, list):
                for i in range(0, len(self.order_line_list)):
                    element = self.order_line_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.order_line_list[i] = element.to_alipay_dict()
            if hasattr(self.order_line_list, 'to_alipay_dict'):
                params['order_line_list'] = self.order_line_list.to_alipay_dict()
            else:
                params['order_line_list'] = self.order_line_list
        if self.order_status:
            if hasattr(self.order_status, 'to_alipay_dict'):
                params['order_status'] = self.order_status.to_alipay_dict()
            else:
                params['order_status'] = self.order_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MpcOrderResult()
        if 'create_date' in d:
            o.create_date = d['create_date']
        if 'logistics_status' in d:
            o.logistics_status = d['logistics_status']
        if 'order_amount' in d:
            o.order_amount = d['order_amount']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'order_line_list' in d:
            o.order_line_list = d['order_line_list']
        if 'order_status' in d:
            o.order_status = d['order_status']
        return o


