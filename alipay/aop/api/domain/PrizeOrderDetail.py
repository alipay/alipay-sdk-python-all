#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PrizeOrderDetail(object):

    def __init__(self):
        self._budget_type = None
        self._camp_id = None
        self._camp_order_id = None
        self._gmt_create = None
        self._gmt_modified = None
        self._out_biz_no = None
        self._out_prize_id = None
        self._parent_order_id = None
        self._price = None
        self._prize_id = None
        self._prize_name = None
        self._prize_sub_type = None
        self._prize_type = None
        self._send_order_id = None
        self._send_status = None

    @property
    def budget_type(self):
        return self._budget_type

    @budget_type.setter
    def budget_type(self, value):
        self._budget_type = value
    @property
    def camp_id(self):
        return self._camp_id

    @camp_id.setter
    def camp_id(self, value):
        self._camp_id = value
    @property
    def camp_order_id(self):
        return self._camp_order_id

    @camp_order_id.setter
    def camp_order_id(self, value):
        self._camp_order_id = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def out_prize_id(self):
        return self._out_prize_id

    @out_prize_id.setter
    def out_prize_id(self, value):
        self._out_prize_id = value
    @property
    def parent_order_id(self):
        return self._parent_order_id

    @parent_order_id.setter
    def parent_order_id(self, value):
        self._parent_order_id = value
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
    @property
    def prize_id(self):
        return self._prize_id

    @prize_id.setter
    def prize_id(self, value):
        self._prize_id = value
    @property
    def prize_name(self):
        return self._prize_name

    @prize_name.setter
    def prize_name(self, value):
        self._prize_name = value
    @property
    def prize_sub_type(self):
        return self._prize_sub_type

    @prize_sub_type.setter
    def prize_sub_type(self, value):
        self._prize_sub_type = value
    @property
    def prize_type(self):
        return self._prize_type

    @prize_type.setter
    def prize_type(self, value):
        self._prize_type = value
    @property
    def send_order_id(self):
        return self._send_order_id

    @send_order_id.setter
    def send_order_id(self, value):
        self._send_order_id = value
    @property
    def send_status(self):
        return self._send_status

    @send_status.setter
    def send_status(self, value):
        self._send_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.budget_type:
            if hasattr(self.budget_type, 'to_alipay_dict'):
                params['budget_type'] = self.budget_type.to_alipay_dict()
            else:
                params['budget_type'] = self.budget_type
        if self.camp_id:
            if hasattr(self.camp_id, 'to_alipay_dict'):
                params['camp_id'] = self.camp_id.to_alipay_dict()
            else:
                params['camp_id'] = self.camp_id
        if self.camp_order_id:
            if hasattr(self.camp_order_id, 'to_alipay_dict'):
                params['camp_order_id'] = self.camp_order_id.to_alipay_dict()
            else:
                params['camp_order_id'] = self.camp_order_id
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.gmt_modified:
            if hasattr(self.gmt_modified, 'to_alipay_dict'):
                params['gmt_modified'] = self.gmt_modified.to_alipay_dict()
            else:
                params['gmt_modified'] = self.gmt_modified
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.out_prize_id:
            if hasattr(self.out_prize_id, 'to_alipay_dict'):
                params['out_prize_id'] = self.out_prize_id.to_alipay_dict()
            else:
                params['out_prize_id'] = self.out_prize_id
        if self.parent_order_id:
            if hasattr(self.parent_order_id, 'to_alipay_dict'):
                params['parent_order_id'] = self.parent_order_id.to_alipay_dict()
            else:
                params['parent_order_id'] = self.parent_order_id
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
        if self.prize_id:
            if hasattr(self.prize_id, 'to_alipay_dict'):
                params['prize_id'] = self.prize_id.to_alipay_dict()
            else:
                params['prize_id'] = self.prize_id
        if self.prize_name:
            if hasattr(self.prize_name, 'to_alipay_dict'):
                params['prize_name'] = self.prize_name.to_alipay_dict()
            else:
                params['prize_name'] = self.prize_name
        if self.prize_sub_type:
            if hasattr(self.prize_sub_type, 'to_alipay_dict'):
                params['prize_sub_type'] = self.prize_sub_type.to_alipay_dict()
            else:
                params['prize_sub_type'] = self.prize_sub_type
        if self.prize_type:
            if hasattr(self.prize_type, 'to_alipay_dict'):
                params['prize_type'] = self.prize_type.to_alipay_dict()
            else:
                params['prize_type'] = self.prize_type
        if self.send_order_id:
            if hasattr(self.send_order_id, 'to_alipay_dict'):
                params['send_order_id'] = self.send_order_id.to_alipay_dict()
            else:
                params['send_order_id'] = self.send_order_id
        if self.send_status:
            if hasattr(self.send_status, 'to_alipay_dict'):
                params['send_status'] = self.send_status.to_alipay_dict()
            else:
                params['send_status'] = self.send_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PrizeOrderDetail()
        if 'budget_type' in d:
            o.budget_type = d['budget_type']
        if 'camp_id' in d:
            o.camp_id = d['camp_id']
        if 'camp_order_id' in d:
            o.camp_order_id = d['camp_order_id']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'out_prize_id' in d:
            o.out_prize_id = d['out_prize_id']
        if 'parent_order_id' in d:
            o.parent_order_id = d['parent_order_id']
        if 'price' in d:
            o.price = d['price']
        if 'prize_id' in d:
            o.prize_id = d['prize_id']
        if 'prize_name' in d:
            o.prize_name = d['prize_name']
        if 'prize_sub_type' in d:
            o.prize_sub_type = d['prize_sub_type']
        if 'prize_type' in d:
            o.prize_type = d['prize_type']
        if 'send_order_id' in d:
            o.send_order_id = d['send_order_id']
        if 'send_status' in d:
            o.send_status = d['send_status']
        return o


