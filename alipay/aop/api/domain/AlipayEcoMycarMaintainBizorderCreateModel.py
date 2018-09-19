#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MaintainBizOrder import MaintainBizOrder


class AlipayEcoMycarMaintainBizorderCreateModel(object):

    def __init__(self):
        self._appoint_affirm_time = None
        self._appoint_end_time = None
        self._appoint_start_time = None
        self._appoint_status = None
        self._arrive_time = None
        self._biz_status_txt = None
        self._biz_type = None
        self._car_id = None
        self._order_server_list = None
        self._order_status = None
        self._original_cost = None
        self._out_order_no = None
        self._out_shop_id = None
        self._pay_time = None
        self._real_cost = None
        self._shop_id = None
        self._user_id = None

    @property
    def appoint_affirm_time(self):
        return self._appoint_affirm_time

    @appoint_affirm_time.setter
    def appoint_affirm_time(self, value):
        self._appoint_affirm_time = value
    @property
    def appoint_end_time(self):
        return self._appoint_end_time

    @appoint_end_time.setter
    def appoint_end_time(self, value):
        self._appoint_end_time = value
    @property
    def appoint_start_time(self):
        return self._appoint_start_time

    @appoint_start_time.setter
    def appoint_start_time(self, value):
        self._appoint_start_time = value
    @property
    def appoint_status(self):
        return self._appoint_status

    @appoint_status.setter
    def appoint_status(self, value):
        self._appoint_status = value
    @property
    def arrive_time(self):
        return self._arrive_time

    @arrive_time.setter
    def arrive_time(self, value):
        self._arrive_time = value
    @property
    def biz_status_txt(self):
        return self._biz_status_txt

    @biz_status_txt.setter
    def biz_status_txt(self, value):
        self._biz_status_txt = value
    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def car_id(self):
        return self._car_id

    @car_id.setter
    def car_id(self, value):
        self._car_id = value
    @property
    def order_server_list(self):
        return self._order_server_list

    @order_server_list.setter
    def order_server_list(self, value):
        if isinstance(value, list):
            self._order_server_list = list()
            for i in value:
                if isinstance(i, MaintainBizOrder):
                    self._order_server_list.append(i)
                else:
                    self._order_server_list.append(MaintainBizOrder.from_alipay_dict(i))
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def original_cost(self):
        return self._original_cost

    @original_cost.setter
    def original_cost(self, value):
        self._original_cost = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def out_shop_id(self):
        return self._out_shop_id

    @out_shop_id.setter
    def out_shop_id(self, value):
        self._out_shop_id = value
    @property
    def pay_time(self):
        return self._pay_time

    @pay_time.setter
    def pay_time(self, value):
        self._pay_time = value
    @property
    def real_cost(self):
        return self._real_cost

    @real_cost.setter
    def real_cost(self, value):
        self._real_cost = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.appoint_affirm_time:
            if hasattr(self.appoint_affirm_time, 'to_alipay_dict'):
                params['appoint_affirm_time'] = self.appoint_affirm_time.to_alipay_dict()
            else:
                params['appoint_affirm_time'] = self.appoint_affirm_time
        if self.appoint_end_time:
            if hasattr(self.appoint_end_time, 'to_alipay_dict'):
                params['appoint_end_time'] = self.appoint_end_time.to_alipay_dict()
            else:
                params['appoint_end_time'] = self.appoint_end_time
        if self.appoint_start_time:
            if hasattr(self.appoint_start_time, 'to_alipay_dict'):
                params['appoint_start_time'] = self.appoint_start_time.to_alipay_dict()
            else:
                params['appoint_start_time'] = self.appoint_start_time
        if self.appoint_status:
            if hasattr(self.appoint_status, 'to_alipay_dict'):
                params['appoint_status'] = self.appoint_status.to_alipay_dict()
            else:
                params['appoint_status'] = self.appoint_status
        if self.arrive_time:
            if hasattr(self.arrive_time, 'to_alipay_dict'):
                params['arrive_time'] = self.arrive_time.to_alipay_dict()
            else:
                params['arrive_time'] = self.arrive_time
        if self.biz_status_txt:
            if hasattr(self.biz_status_txt, 'to_alipay_dict'):
                params['biz_status_txt'] = self.biz_status_txt.to_alipay_dict()
            else:
                params['biz_status_txt'] = self.biz_status_txt
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.car_id:
            if hasattr(self.car_id, 'to_alipay_dict'):
                params['car_id'] = self.car_id.to_alipay_dict()
            else:
                params['car_id'] = self.car_id
        if self.order_server_list:
            if isinstance(self.order_server_list, list):
                for i in range(0, len(self.order_server_list)):
                    element = self.order_server_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.order_server_list[i] = element.to_alipay_dict()
            if hasattr(self.order_server_list, 'to_alipay_dict'):
                params['order_server_list'] = self.order_server_list.to_alipay_dict()
            else:
                params['order_server_list'] = self.order_server_list
        if self.order_status:
            if hasattr(self.order_status, 'to_alipay_dict'):
                params['order_status'] = self.order_status.to_alipay_dict()
            else:
                params['order_status'] = self.order_status
        if self.original_cost:
            if hasattr(self.original_cost, 'to_alipay_dict'):
                params['original_cost'] = self.original_cost.to_alipay_dict()
            else:
                params['original_cost'] = self.original_cost
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
        if self.out_shop_id:
            if hasattr(self.out_shop_id, 'to_alipay_dict'):
                params['out_shop_id'] = self.out_shop_id.to_alipay_dict()
            else:
                params['out_shop_id'] = self.out_shop_id
        if self.pay_time:
            if hasattr(self.pay_time, 'to_alipay_dict'):
                params['pay_time'] = self.pay_time.to_alipay_dict()
            else:
                params['pay_time'] = self.pay_time
        if self.real_cost:
            if hasattr(self.real_cost, 'to_alipay_dict'):
                params['real_cost'] = self.real_cost.to_alipay_dict()
            else:
                params['real_cost'] = self.real_cost
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
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
        o = AlipayEcoMycarMaintainBizorderCreateModel()
        if 'appoint_affirm_time' in d:
            o.appoint_affirm_time = d['appoint_affirm_time']
        if 'appoint_end_time' in d:
            o.appoint_end_time = d['appoint_end_time']
        if 'appoint_start_time' in d:
            o.appoint_start_time = d['appoint_start_time']
        if 'appoint_status' in d:
            o.appoint_status = d['appoint_status']
        if 'arrive_time' in d:
            o.arrive_time = d['arrive_time']
        if 'biz_status_txt' in d:
            o.biz_status_txt = d['biz_status_txt']
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'car_id' in d:
            o.car_id = d['car_id']
        if 'order_server_list' in d:
            o.order_server_list = d['order_server_list']
        if 'order_status' in d:
            o.order_status = d['order_status']
        if 'original_cost' in d:
            o.original_cost = d['original_cost']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'out_shop_id' in d:
            o.out_shop_id = d['out_shop_id']
        if 'pay_time' in d:
            o.pay_time = d['pay_time']
        if 'real_cost' in d:
            o.real_cost = d['real_cost']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


