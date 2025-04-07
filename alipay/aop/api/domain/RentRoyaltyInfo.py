#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RentPlan import RentPlan
from alipay.aop.api.domain.RentRoyalty import RentRoyalty


class RentRoyaltyInfo(object):

    def __init__(self):
        self._buyer_id = None
        self._buyer_open_id = None
        self._invest_app_id = None
        self._invest_pid = None
        self._order_id = None
        self._out_order_id = None
        self._plan_list = None
        self._royalty_list = None
        self._status = None

    @property
    def buyer_id(self):
        return self._buyer_id

    @buyer_id.setter
    def buyer_id(self, value):
        self._buyer_id = value
    @property
    def buyer_open_id(self):
        return self._buyer_open_id

    @buyer_open_id.setter
    def buyer_open_id(self, value):
        self._buyer_open_id = value
    @property
    def invest_app_id(self):
        return self._invest_app_id

    @invest_app_id.setter
    def invest_app_id(self, value):
        self._invest_app_id = value
    @property
    def invest_pid(self):
        return self._invest_pid

    @invest_pid.setter
    def invest_pid(self, value):
        self._invest_pid = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def out_order_id(self):
        return self._out_order_id

    @out_order_id.setter
    def out_order_id(self, value):
        self._out_order_id = value
    @property
    def plan_list(self):
        return self._plan_list

    @plan_list.setter
    def plan_list(self, value):
        if isinstance(value, list):
            self._plan_list = list()
            for i in value:
                if isinstance(i, RentPlan):
                    self._plan_list.append(i)
                else:
                    self._plan_list.append(RentPlan.from_alipay_dict(i))
    @property
    def royalty_list(self):
        return self._royalty_list

    @royalty_list.setter
    def royalty_list(self, value):
        if isinstance(value, list):
            self._royalty_list = list()
            for i in value:
                if isinstance(i, RentRoyalty):
                    self._royalty_list.append(i)
                else:
                    self._royalty_list.append(RentRoyalty.from_alipay_dict(i))
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.buyer_id:
            if hasattr(self.buyer_id, 'to_alipay_dict'):
                params['buyer_id'] = self.buyer_id.to_alipay_dict()
            else:
                params['buyer_id'] = self.buyer_id
        if self.buyer_open_id:
            if hasattr(self.buyer_open_id, 'to_alipay_dict'):
                params['buyer_open_id'] = self.buyer_open_id.to_alipay_dict()
            else:
                params['buyer_open_id'] = self.buyer_open_id
        if self.invest_app_id:
            if hasattr(self.invest_app_id, 'to_alipay_dict'):
                params['invest_app_id'] = self.invest_app_id.to_alipay_dict()
            else:
                params['invest_app_id'] = self.invest_app_id
        if self.invest_pid:
            if hasattr(self.invest_pid, 'to_alipay_dict'):
                params['invest_pid'] = self.invest_pid.to_alipay_dict()
            else:
                params['invest_pid'] = self.invest_pid
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.out_order_id:
            if hasattr(self.out_order_id, 'to_alipay_dict'):
                params['out_order_id'] = self.out_order_id.to_alipay_dict()
            else:
                params['out_order_id'] = self.out_order_id
        if self.plan_list:
            if isinstance(self.plan_list, list):
                for i in range(0, len(self.plan_list)):
                    element = self.plan_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.plan_list[i] = element.to_alipay_dict()
            if hasattr(self.plan_list, 'to_alipay_dict'):
                params['plan_list'] = self.plan_list.to_alipay_dict()
            else:
                params['plan_list'] = self.plan_list
        if self.royalty_list:
            if isinstance(self.royalty_list, list):
                for i in range(0, len(self.royalty_list)):
                    element = self.royalty_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.royalty_list[i] = element.to_alipay_dict()
            if hasattr(self.royalty_list, 'to_alipay_dict'):
                params['royalty_list'] = self.royalty_list.to_alipay_dict()
            else:
                params['royalty_list'] = self.royalty_list
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
        o = RentRoyaltyInfo()
        if 'buyer_id' in d:
            o.buyer_id = d['buyer_id']
        if 'buyer_open_id' in d:
            o.buyer_open_id = d['buyer_open_id']
        if 'invest_app_id' in d:
            o.invest_app_id = d['invest_app_id']
        if 'invest_pid' in d:
            o.invest_pid = d['invest_pid']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'out_order_id' in d:
            o.out_order_id = d['out_order_id']
        if 'plan_list' in d:
            o.plan_list = d['plan_list']
        if 'royalty_list' in d:
            o.royalty_list = d['royalty_list']
        if 'status' in d:
            o.status = d['status']
        return o


