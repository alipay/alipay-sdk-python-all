#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenMiniOrderItembillBatchqueryModel(object):

    def __init__(self):
        self._create_time = None
        self._mini_app_id = None
        self._order_status = None
        self._page_num = None
        self._page_size = None
        self._service_type_list = None
        self._settle_status = None
        self._settlement_date = None
        self._trade_no = None

    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def mini_app_id(self):
        return self._mini_app_id

    @mini_app_id.setter
    def mini_app_id(self, value):
        self._mini_app_id = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def page_num(self):
        return self._page_num

    @page_num.setter
    def page_num(self, value):
        self._page_num = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value
    @property
    def service_type_list(self):
        return self._service_type_list

    @service_type_list.setter
    def service_type_list(self, value):
        if isinstance(value, list):
            self._service_type_list = list()
            for i in value:
                self._service_type_list.append(i)
    @property
    def settle_status(self):
        return self._settle_status

    @settle_status.setter
    def settle_status(self, value):
        self._settle_status = value
    @property
    def settlement_date(self):
        return self._settlement_date

    @settlement_date.setter
    def settlement_date(self, value):
        self._settlement_date = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.mini_app_id:
            if hasattr(self.mini_app_id, 'to_alipay_dict'):
                params['mini_app_id'] = self.mini_app_id.to_alipay_dict()
            else:
                params['mini_app_id'] = self.mini_app_id
        if self.order_status:
            if hasattr(self.order_status, 'to_alipay_dict'):
                params['order_status'] = self.order_status.to_alipay_dict()
            else:
                params['order_status'] = self.order_status
        if self.page_num:
            if hasattr(self.page_num, 'to_alipay_dict'):
                params['page_num'] = self.page_num.to_alipay_dict()
            else:
                params['page_num'] = self.page_num
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        if self.service_type_list:
            if isinstance(self.service_type_list, list):
                for i in range(0, len(self.service_type_list)):
                    element = self.service_type_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.service_type_list[i] = element.to_alipay_dict()
            if hasattr(self.service_type_list, 'to_alipay_dict'):
                params['service_type_list'] = self.service_type_list.to_alipay_dict()
            else:
                params['service_type_list'] = self.service_type_list
        if self.settle_status:
            if hasattr(self.settle_status, 'to_alipay_dict'):
                params['settle_status'] = self.settle_status.to_alipay_dict()
            else:
                params['settle_status'] = self.settle_status
        if self.settlement_date:
            if hasattr(self.settlement_date, 'to_alipay_dict'):
                params['settlement_date'] = self.settlement_date.to_alipay_dict()
            else:
                params['settlement_date'] = self.settlement_date
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
        o = AlipayOpenMiniOrderItembillBatchqueryModel()
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'mini_app_id' in d:
            o.mini_app_id = d['mini_app_id']
        if 'order_status' in d:
            o.order_status = d['order_status']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        if 'service_type_list' in d:
            o.service_type_list = d['service_type_list']
        if 'settle_status' in d:
            o.settle_status = d['settle_status']
        if 'settlement_date' in d:
            o.settlement_date = d['settlement_date']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        return o


