#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ServiceDetailE import ServiceDetailE
from alipay.aop.api.domain.TradeDetailE import TradeDetailE


class AlipayCommerceRentHouseProcessSyncModel(object):

    def __init__(self):
        self._alipay_open_id = None
        self._biz_order_id = None
        self._dispatch_id = None
        self._item_id = None
        self._operation_type = None
        self._out_biz_no = None
        self._out_biz_title = None
        self._prev_process_id = None
        self._process_time = None
        self._rental_process = None
        self._service_detail = None
        self._trade_detail = None
        self._trade_type = None
        self._user_id = None

    @property
    def alipay_open_id(self):
        return self._alipay_open_id

    @alipay_open_id.setter
    def alipay_open_id(self, value):
        self._alipay_open_id = value
    @property
    def biz_order_id(self):
        return self._biz_order_id

    @biz_order_id.setter
    def biz_order_id(self, value):
        self._biz_order_id = value
    @property
    def dispatch_id(self):
        return self._dispatch_id

    @dispatch_id.setter
    def dispatch_id(self, value):
        self._dispatch_id = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def operation_type(self):
        return self._operation_type

    @operation_type.setter
    def operation_type(self, value):
        self._operation_type = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def out_biz_title(self):
        return self._out_biz_title

    @out_biz_title.setter
    def out_biz_title(self, value):
        self._out_biz_title = value
    @property
    def prev_process_id(self):
        return self._prev_process_id

    @prev_process_id.setter
    def prev_process_id(self, value):
        self._prev_process_id = value
    @property
    def process_time(self):
        return self._process_time

    @process_time.setter
    def process_time(self, value):
        self._process_time = value
    @property
    def rental_process(self):
        return self._rental_process

    @rental_process.setter
    def rental_process(self, value):
        self._rental_process = value
    @property
    def service_detail(self):
        return self._service_detail

    @service_detail.setter
    def service_detail(self, value):
        if isinstance(value, ServiceDetailE):
            self._service_detail = value
        else:
            self._service_detail = ServiceDetailE.from_alipay_dict(value)
    @property
    def trade_detail(self):
        return self._trade_detail

    @trade_detail.setter
    def trade_detail(self, value):
        if isinstance(value, TradeDetailE):
            self._trade_detail = value
        else:
            self._trade_detail = TradeDetailE.from_alipay_dict(value)
    @property
    def trade_type(self):
        return self._trade_type

    @trade_type.setter
    def trade_type(self, value):
        self._trade_type = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_open_id:
            if hasattr(self.alipay_open_id, 'to_alipay_dict'):
                params['alipay_open_id'] = self.alipay_open_id.to_alipay_dict()
            else:
                params['alipay_open_id'] = self.alipay_open_id
        if self.biz_order_id:
            if hasattr(self.biz_order_id, 'to_alipay_dict'):
                params['biz_order_id'] = self.biz_order_id.to_alipay_dict()
            else:
                params['biz_order_id'] = self.biz_order_id
        if self.dispatch_id:
            if hasattr(self.dispatch_id, 'to_alipay_dict'):
                params['dispatch_id'] = self.dispatch_id.to_alipay_dict()
            else:
                params['dispatch_id'] = self.dispatch_id
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.operation_type:
            if hasattr(self.operation_type, 'to_alipay_dict'):
                params['operation_type'] = self.operation_type.to_alipay_dict()
            else:
                params['operation_type'] = self.operation_type
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.out_biz_title:
            if hasattr(self.out_biz_title, 'to_alipay_dict'):
                params['out_biz_title'] = self.out_biz_title.to_alipay_dict()
            else:
                params['out_biz_title'] = self.out_biz_title
        if self.prev_process_id:
            if hasattr(self.prev_process_id, 'to_alipay_dict'):
                params['prev_process_id'] = self.prev_process_id.to_alipay_dict()
            else:
                params['prev_process_id'] = self.prev_process_id
        if self.process_time:
            if hasattr(self.process_time, 'to_alipay_dict'):
                params['process_time'] = self.process_time.to_alipay_dict()
            else:
                params['process_time'] = self.process_time
        if self.rental_process:
            if hasattr(self.rental_process, 'to_alipay_dict'):
                params['rental_process'] = self.rental_process.to_alipay_dict()
            else:
                params['rental_process'] = self.rental_process
        if self.service_detail:
            if hasattr(self.service_detail, 'to_alipay_dict'):
                params['service_detail'] = self.service_detail.to_alipay_dict()
            else:
                params['service_detail'] = self.service_detail
        if self.trade_detail:
            if hasattr(self.trade_detail, 'to_alipay_dict'):
                params['trade_detail'] = self.trade_detail.to_alipay_dict()
            else:
                params['trade_detail'] = self.trade_detail
        if self.trade_type:
            if hasattr(self.trade_type, 'to_alipay_dict'):
                params['trade_type'] = self.trade_type.to_alipay_dict()
            else:
                params['trade_type'] = self.trade_type
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceRentHouseProcessSyncModel()
        if 'alipay_open_id' in d:
            o.alipay_open_id = d['alipay_open_id']
        if 'biz_order_id' in d:
            o.biz_order_id = d['biz_order_id']
        if 'dispatch_id' in d:
            o.dispatch_id = d['dispatch_id']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'operation_type' in d:
            o.operation_type = d['operation_type']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'out_biz_title' in d:
            o.out_biz_title = d['out_biz_title']
        if 'prev_process_id' in d:
            o.prev_process_id = d['prev_process_id']
        if 'process_time' in d:
            o.process_time = d['process_time']
        if 'rental_process' in d:
            o.rental_process = d['rental_process']
        if 'service_detail' in d:
            o.service_detail = d['service_detail']
        if 'trade_detail' in d:
            o.trade_detail = d['trade_detail']
        if 'trade_type' in d:
            o.trade_type = d['trade_type']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


