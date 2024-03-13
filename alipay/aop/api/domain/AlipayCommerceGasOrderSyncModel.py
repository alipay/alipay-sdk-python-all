#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.GasDiscountInfo import GasDiscountInfo
from alipay.aop.api.domain.ExtensionMap import ExtensionMap
from alipay.aop.api.domain.GoodsInfoDetail import GoodsInfoDetail


class AlipayCommerceGasOrderSyncModel(object):

    def __init__(self):
        self._create_time = None
        self._discount_amount = None
        self._discount_list = None
        self._ext_info = None
        self._goods_info = None
        self._inst_code = None
        self._inst_pid = None
        self._modified_time = None
        self._order_status = None
        self._order_type = None
        self._out_biz_no = None
        self._pay_amount = None
        self._payment_time = None
        self._source_channel = None
        self._total_amount = None
        self._trade_no = None
        self._trade_type = None
        self._user_id = None

    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def discount_amount(self):
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, value):
        self._discount_amount = value
    @property
    def discount_list(self):
        return self._discount_list

    @discount_list.setter
    def discount_list(self, value):
        if isinstance(value, list):
            self._discount_list = list()
            for i in value:
                if isinstance(i, GasDiscountInfo):
                    self._discount_list.append(i)
                else:
                    self._discount_list.append(GasDiscountInfo.from_alipay_dict(i))
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        if isinstance(value, ExtensionMap):
            self._ext_info = value
        else:
            self._ext_info = ExtensionMap.from_alipay_dict(value)
    @property
    def goods_info(self):
        return self._goods_info

    @goods_info.setter
    def goods_info(self, value):
        if isinstance(value, list):
            self._goods_info = list()
            for i in value:
                if isinstance(i, GoodsInfoDetail):
                    self._goods_info.append(i)
                else:
                    self._goods_info.append(GoodsInfoDetail.from_alipay_dict(i))
    @property
    def inst_code(self):
        return self._inst_code

    @inst_code.setter
    def inst_code(self, value):
        self._inst_code = value
    @property
    def inst_pid(self):
        return self._inst_pid

    @inst_pid.setter
    def inst_pid(self, value):
        self._inst_pid = value
    @property
    def modified_time(self):
        return self._modified_time

    @modified_time.setter
    def modified_time(self, value):
        self._modified_time = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def order_type(self):
        return self._order_type

    @order_type.setter
    def order_type(self, value):
        self._order_type = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def pay_amount(self):
        return self._pay_amount

    @pay_amount.setter
    def pay_amount(self, value):
        self._pay_amount = value
    @property
    def payment_time(self):
        return self._payment_time

    @payment_time.setter
    def payment_time(self, value):
        self._payment_time = value
    @property
    def source_channel(self):
        return self._source_channel

    @source_channel.setter
    def source_channel(self, value):
        self._source_channel = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value
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
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.discount_amount:
            if hasattr(self.discount_amount, 'to_alipay_dict'):
                params['discount_amount'] = self.discount_amount.to_alipay_dict()
            else:
                params['discount_amount'] = self.discount_amount
        if self.discount_list:
            if isinstance(self.discount_list, list):
                for i in range(0, len(self.discount_list)):
                    element = self.discount_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.discount_list[i] = element.to_alipay_dict()
            if hasattr(self.discount_list, 'to_alipay_dict'):
                params['discount_list'] = self.discount_list.to_alipay_dict()
            else:
                params['discount_list'] = self.discount_list
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.goods_info:
            if isinstance(self.goods_info, list):
                for i in range(0, len(self.goods_info)):
                    element = self.goods_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.goods_info[i] = element.to_alipay_dict()
            if hasattr(self.goods_info, 'to_alipay_dict'):
                params['goods_info'] = self.goods_info.to_alipay_dict()
            else:
                params['goods_info'] = self.goods_info
        if self.inst_code:
            if hasattr(self.inst_code, 'to_alipay_dict'):
                params['inst_code'] = self.inst_code.to_alipay_dict()
            else:
                params['inst_code'] = self.inst_code
        if self.inst_pid:
            if hasattr(self.inst_pid, 'to_alipay_dict'):
                params['inst_pid'] = self.inst_pid.to_alipay_dict()
            else:
                params['inst_pid'] = self.inst_pid
        if self.modified_time:
            if hasattr(self.modified_time, 'to_alipay_dict'):
                params['modified_time'] = self.modified_time.to_alipay_dict()
            else:
                params['modified_time'] = self.modified_time
        if self.order_status:
            if hasattr(self.order_status, 'to_alipay_dict'):
                params['order_status'] = self.order_status.to_alipay_dict()
            else:
                params['order_status'] = self.order_status
        if self.order_type:
            if hasattr(self.order_type, 'to_alipay_dict'):
                params['order_type'] = self.order_type.to_alipay_dict()
            else:
                params['order_type'] = self.order_type
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.pay_amount:
            if hasattr(self.pay_amount, 'to_alipay_dict'):
                params['pay_amount'] = self.pay_amount.to_alipay_dict()
            else:
                params['pay_amount'] = self.pay_amount
        if self.payment_time:
            if hasattr(self.payment_time, 'to_alipay_dict'):
                params['payment_time'] = self.payment_time.to_alipay_dict()
            else:
                params['payment_time'] = self.payment_time
        if self.source_channel:
            if hasattr(self.source_channel, 'to_alipay_dict'):
                params['source_channel'] = self.source_channel.to_alipay_dict()
            else:
                params['source_channel'] = self.source_channel
        if self.total_amount:
            if hasattr(self.total_amount, 'to_alipay_dict'):
                params['total_amount'] = self.total_amount.to_alipay_dict()
            else:
                params['total_amount'] = self.total_amount
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
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
        o = AlipayCommerceGasOrderSyncModel()
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'discount_amount' in d:
            o.discount_amount = d['discount_amount']
        if 'discount_list' in d:
            o.discount_list = d['discount_list']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'goods_info' in d:
            o.goods_info = d['goods_info']
        if 'inst_code' in d:
            o.inst_code = d['inst_code']
        if 'inst_pid' in d:
            o.inst_pid = d['inst_pid']
        if 'modified_time' in d:
            o.modified_time = d['modified_time']
        if 'order_status' in d:
            o.order_status = d['order_status']
        if 'order_type' in d:
            o.order_type = d['order_type']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'pay_amount' in d:
            o.pay_amount = d['pay_amount']
        if 'payment_time' in d:
            o.payment_time = d['payment_time']
        if 'source_channel' in d:
            o.source_channel = d['source_channel']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        if 'trade_type' in d:
            o.trade_type = d['trade_type']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


