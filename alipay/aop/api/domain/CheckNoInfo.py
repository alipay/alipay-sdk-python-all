#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CheckItem import CheckItem


class CheckNoInfo(object):

    def __init__(self):
        self._check_item_list = None
        self._check_no = None
        self._create_time = None
        self._fulfillment_id = None
        self._status = None
        self._status_desc = None
        self._trade_order_id = None
        self._validity_end_time = None
        self._validity_period_desc = None

    @property
    def check_item_list(self):
        return self._check_item_list

    @check_item_list.setter
    def check_item_list(self, value):
        if isinstance(value, list):
            self._check_item_list = list()
            for i in value:
                if isinstance(i, CheckItem):
                    self._check_item_list.append(i)
                else:
                    self._check_item_list.append(CheckItem.from_alipay_dict(i))
    @property
    def check_no(self):
        return self._check_no

    @check_no.setter
    def check_no(self, value):
        self._check_no = value
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def fulfillment_id(self):
        return self._fulfillment_id

    @fulfillment_id.setter
    def fulfillment_id(self, value):
        self._fulfillment_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def status_desc(self):
        return self._status_desc

    @status_desc.setter
    def status_desc(self, value):
        self._status_desc = value
    @property
    def trade_order_id(self):
        return self._trade_order_id

    @trade_order_id.setter
    def trade_order_id(self, value):
        self._trade_order_id = value
    @property
    def validity_end_time(self):
        return self._validity_end_time

    @validity_end_time.setter
    def validity_end_time(self, value):
        self._validity_end_time = value
    @property
    def validity_period_desc(self):
        return self._validity_period_desc

    @validity_period_desc.setter
    def validity_period_desc(self, value):
        self._validity_period_desc = value


    def to_alipay_dict(self):
        params = dict()
        if self.check_item_list:
            if isinstance(self.check_item_list, list):
                for i in range(0, len(self.check_item_list)):
                    element = self.check_item_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.check_item_list[i] = element.to_alipay_dict()
            if hasattr(self.check_item_list, 'to_alipay_dict'):
                params['check_item_list'] = self.check_item_list.to_alipay_dict()
            else:
                params['check_item_list'] = self.check_item_list
        if self.check_no:
            if hasattr(self.check_no, 'to_alipay_dict'):
                params['check_no'] = self.check_no.to_alipay_dict()
            else:
                params['check_no'] = self.check_no
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.fulfillment_id:
            if hasattr(self.fulfillment_id, 'to_alipay_dict'):
                params['fulfillment_id'] = self.fulfillment_id.to_alipay_dict()
            else:
                params['fulfillment_id'] = self.fulfillment_id
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.status_desc:
            if hasattr(self.status_desc, 'to_alipay_dict'):
                params['status_desc'] = self.status_desc.to_alipay_dict()
            else:
                params['status_desc'] = self.status_desc
        if self.trade_order_id:
            if hasattr(self.trade_order_id, 'to_alipay_dict'):
                params['trade_order_id'] = self.trade_order_id.to_alipay_dict()
            else:
                params['trade_order_id'] = self.trade_order_id
        if self.validity_end_time:
            if hasattr(self.validity_end_time, 'to_alipay_dict'):
                params['validity_end_time'] = self.validity_end_time.to_alipay_dict()
            else:
                params['validity_end_time'] = self.validity_end_time
        if self.validity_period_desc:
            if hasattr(self.validity_period_desc, 'to_alipay_dict'):
                params['validity_period_desc'] = self.validity_period_desc.to_alipay_dict()
            else:
                params['validity_period_desc'] = self.validity_period_desc
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CheckNoInfo()
        if 'check_item_list' in d:
            o.check_item_list = d['check_item_list']
        if 'check_no' in d:
            o.check_no = d['check_no']
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'fulfillment_id' in d:
            o.fulfillment_id = d['fulfillment_id']
        if 'status' in d:
            o.status = d['status']
        if 'status_desc' in d:
            o.status_desc = d['status_desc']
        if 'trade_order_id' in d:
            o.trade_order_id = d['trade_order_id']
        if 'validity_end_time' in d:
            o.validity_end_time = d['validity_end_time']
        if 'validity_period_desc' in d:
            o.validity_period_desc = d['validity_period_desc']
        return o


