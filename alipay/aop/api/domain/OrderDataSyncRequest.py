#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DeductionPlanDataSyncRequest import DeductionPlanDataSyncRequest


class OrderDataSyncRequest(object):

    def __init__(self):
        self._biz_id = None
        self._cancel_type = None
        self._card_name = None
        self._card_version = None
        self._channel_type = None
        self._count_unit = None
        self._create_time = None
        self._deduction_plan_list = None
        self._detail_url = None
        self._env = None
        self._expired_end_time = None
        self._expired_start_time = None
        self._isv_pid = None
        self._item_code = None
        self._kabao_id = None
        self._merchant_name = None
        self._merchant_pid = None
        self._mini_app_id = None
        self._open_id = None
        self._order_no = None
        self._order_shop_id = None
        self._out_order_no = None
        self._refund_price = None
        self._refund_time = None
        self._remain_count = None
        self._solution_type = None
        self._status = None
        self._total_count = None
        self._total_original_price = None
        self._total_sale_price = None
        self._update_time = None
        self._user_id = None

    @property
    def biz_id(self):
        return self._biz_id

    @biz_id.setter
    def biz_id(self, value):
        self._biz_id = value
    @property
    def cancel_type(self):
        return self._cancel_type

    @cancel_type.setter
    def cancel_type(self, value):
        self._cancel_type = value
    @property
    def card_name(self):
        return self._card_name

    @card_name.setter
    def card_name(self, value):
        self._card_name = value
    @property
    def card_version(self):
        return self._card_version

    @card_version.setter
    def card_version(self, value):
        self._card_version = value
    @property
    def channel_type(self):
        return self._channel_type

    @channel_type.setter
    def channel_type(self, value):
        self._channel_type = value
    @property
    def count_unit(self):
        return self._count_unit

    @count_unit.setter
    def count_unit(self, value):
        self._count_unit = value
    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def deduction_plan_list(self):
        return self._deduction_plan_list

    @deduction_plan_list.setter
    def deduction_plan_list(self, value):
        if isinstance(value, list):
            self._deduction_plan_list = list()
            for i in value:
                if isinstance(i, DeductionPlanDataSyncRequest):
                    self._deduction_plan_list.append(i)
                else:
                    self._deduction_plan_list.append(DeductionPlanDataSyncRequest.from_alipay_dict(i))
    @property
    def detail_url(self):
        return self._detail_url

    @detail_url.setter
    def detail_url(self, value):
        self._detail_url = value
    @property
    def env(self):
        return self._env

    @env.setter
    def env(self, value):
        self._env = value
    @property
    def expired_end_time(self):
        return self._expired_end_time

    @expired_end_time.setter
    def expired_end_time(self, value):
        self._expired_end_time = value
    @property
    def expired_start_time(self):
        return self._expired_start_time

    @expired_start_time.setter
    def expired_start_time(self, value):
        self._expired_start_time = value
    @property
    def isv_pid(self):
        return self._isv_pid

    @isv_pid.setter
    def isv_pid(self, value):
        self._isv_pid = value
    @property
    def item_code(self):
        return self._item_code

    @item_code.setter
    def item_code(self, value):
        self._item_code = value
    @property
    def kabao_id(self):
        return self._kabao_id

    @kabao_id.setter
    def kabao_id(self, value):
        self._kabao_id = value
    @property
    def merchant_name(self):
        return self._merchant_name

    @merchant_name.setter
    def merchant_name(self, value):
        self._merchant_name = value
    @property
    def merchant_pid(self):
        return self._merchant_pid

    @merchant_pid.setter
    def merchant_pid(self, value):
        self._merchant_pid = value
    @property
    def mini_app_id(self):
        return self._mini_app_id

    @mini_app_id.setter
    def mini_app_id(self, value):
        self._mini_app_id = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def order_shop_id(self):
        return self._order_shop_id

    @order_shop_id.setter
    def order_shop_id(self, value):
        self._order_shop_id = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def refund_price(self):
        return self._refund_price

    @refund_price.setter
    def refund_price(self, value):
        self._refund_price = value
    @property
    def refund_time(self):
        return self._refund_time

    @refund_time.setter
    def refund_time(self, value):
        self._refund_time = value
    @property
    def remain_count(self):
        return self._remain_count

    @remain_count.setter
    def remain_count(self, value):
        self._remain_count = value
    @property
    def solution_type(self):
        return self._solution_type

    @solution_type.setter
    def solution_type(self, value):
        self._solution_type = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def total_count(self):
        return self._total_count

    @total_count.setter
    def total_count(self, value):
        self._total_count = value
    @property
    def total_original_price(self):
        return self._total_original_price

    @total_original_price.setter
    def total_original_price(self, value):
        self._total_original_price = value
    @property
    def total_sale_price(self):
        return self._total_sale_price

    @total_sale_price.setter
    def total_sale_price(self, value):
        self._total_sale_price = value
    @property
    def update_time(self):
        return self._update_time

    @update_time.setter
    def update_time(self, value):
        self._update_time = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_id:
            if hasattr(self.biz_id, 'to_alipay_dict'):
                params['biz_id'] = self.biz_id.to_alipay_dict()
            else:
                params['biz_id'] = self.biz_id
        if self.cancel_type:
            if hasattr(self.cancel_type, 'to_alipay_dict'):
                params['cancel_type'] = self.cancel_type.to_alipay_dict()
            else:
                params['cancel_type'] = self.cancel_type
        if self.card_name:
            if hasattr(self.card_name, 'to_alipay_dict'):
                params['card_name'] = self.card_name.to_alipay_dict()
            else:
                params['card_name'] = self.card_name
        if self.card_version:
            if hasattr(self.card_version, 'to_alipay_dict'):
                params['card_version'] = self.card_version.to_alipay_dict()
            else:
                params['card_version'] = self.card_version
        if self.channel_type:
            if hasattr(self.channel_type, 'to_alipay_dict'):
                params['channel_type'] = self.channel_type.to_alipay_dict()
            else:
                params['channel_type'] = self.channel_type
        if self.count_unit:
            if hasattr(self.count_unit, 'to_alipay_dict'):
                params['count_unit'] = self.count_unit.to_alipay_dict()
            else:
                params['count_unit'] = self.count_unit
        if self.create_time:
            if hasattr(self.create_time, 'to_alipay_dict'):
                params['create_time'] = self.create_time.to_alipay_dict()
            else:
                params['create_time'] = self.create_time
        if self.deduction_plan_list:
            if isinstance(self.deduction_plan_list, list):
                for i in range(0, len(self.deduction_plan_list)):
                    element = self.deduction_plan_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.deduction_plan_list[i] = element.to_alipay_dict()
            if hasattr(self.deduction_plan_list, 'to_alipay_dict'):
                params['deduction_plan_list'] = self.deduction_plan_list.to_alipay_dict()
            else:
                params['deduction_plan_list'] = self.deduction_plan_list
        if self.detail_url:
            if hasattr(self.detail_url, 'to_alipay_dict'):
                params['detail_url'] = self.detail_url.to_alipay_dict()
            else:
                params['detail_url'] = self.detail_url
        if self.env:
            if hasattr(self.env, 'to_alipay_dict'):
                params['env'] = self.env.to_alipay_dict()
            else:
                params['env'] = self.env
        if self.expired_end_time:
            if hasattr(self.expired_end_time, 'to_alipay_dict'):
                params['expired_end_time'] = self.expired_end_time.to_alipay_dict()
            else:
                params['expired_end_time'] = self.expired_end_time
        if self.expired_start_time:
            if hasattr(self.expired_start_time, 'to_alipay_dict'):
                params['expired_start_time'] = self.expired_start_time.to_alipay_dict()
            else:
                params['expired_start_time'] = self.expired_start_time
        if self.isv_pid:
            if hasattr(self.isv_pid, 'to_alipay_dict'):
                params['isv_pid'] = self.isv_pid.to_alipay_dict()
            else:
                params['isv_pid'] = self.isv_pid
        if self.item_code:
            if hasattr(self.item_code, 'to_alipay_dict'):
                params['item_code'] = self.item_code.to_alipay_dict()
            else:
                params['item_code'] = self.item_code
        if self.kabao_id:
            if hasattr(self.kabao_id, 'to_alipay_dict'):
                params['kabao_id'] = self.kabao_id.to_alipay_dict()
            else:
                params['kabao_id'] = self.kabao_id
        if self.merchant_name:
            if hasattr(self.merchant_name, 'to_alipay_dict'):
                params['merchant_name'] = self.merchant_name.to_alipay_dict()
            else:
                params['merchant_name'] = self.merchant_name
        if self.merchant_pid:
            if hasattr(self.merchant_pid, 'to_alipay_dict'):
                params['merchant_pid'] = self.merchant_pid.to_alipay_dict()
            else:
                params['merchant_pid'] = self.merchant_pid
        if self.mini_app_id:
            if hasattr(self.mini_app_id, 'to_alipay_dict'):
                params['mini_app_id'] = self.mini_app_id.to_alipay_dict()
            else:
                params['mini_app_id'] = self.mini_app_id
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        if self.order_shop_id:
            if hasattr(self.order_shop_id, 'to_alipay_dict'):
                params['order_shop_id'] = self.order_shop_id.to_alipay_dict()
            else:
                params['order_shop_id'] = self.order_shop_id
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
        if self.refund_price:
            if hasattr(self.refund_price, 'to_alipay_dict'):
                params['refund_price'] = self.refund_price.to_alipay_dict()
            else:
                params['refund_price'] = self.refund_price
        if self.refund_time:
            if hasattr(self.refund_time, 'to_alipay_dict'):
                params['refund_time'] = self.refund_time.to_alipay_dict()
            else:
                params['refund_time'] = self.refund_time
        if self.remain_count:
            if hasattr(self.remain_count, 'to_alipay_dict'):
                params['remain_count'] = self.remain_count.to_alipay_dict()
            else:
                params['remain_count'] = self.remain_count
        if self.solution_type:
            if hasattr(self.solution_type, 'to_alipay_dict'):
                params['solution_type'] = self.solution_type.to_alipay_dict()
            else:
                params['solution_type'] = self.solution_type
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.total_count:
            if hasattr(self.total_count, 'to_alipay_dict'):
                params['total_count'] = self.total_count.to_alipay_dict()
            else:
                params['total_count'] = self.total_count
        if self.total_original_price:
            if hasattr(self.total_original_price, 'to_alipay_dict'):
                params['total_original_price'] = self.total_original_price.to_alipay_dict()
            else:
                params['total_original_price'] = self.total_original_price
        if self.total_sale_price:
            if hasattr(self.total_sale_price, 'to_alipay_dict'):
                params['total_sale_price'] = self.total_sale_price.to_alipay_dict()
            else:
                params['total_sale_price'] = self.total_sale_price
        if self.update_time:
            if hasattr(self.update_time, 'to_alipay_dict'):
                params['update_time'] = self.update_time.to_alipay_dict()
            else:
                params['update_time'] = self.update_time
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
        o = OrderDataSyncRequest()
        if 'biz_id' in d:
            o.biz_id = d['biz_id']
        if 'cancel_type' in d:
            o.cancel_type = d['cancel_type']
        if 'card_name' in d:
            o.card_name = d['card_name']
        if 'card_version' in d:
            o.card_version = d['card_version']
        if 'channel_type' in d:
            o.channel_type = d['channel_type']
        if 'count_unit' in d:
            o.count_unit = d['count_unit']
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'deduction_plan_list' in d:
            o.deduction_plan_list = d['deduction_plan_list']
        if 'detail_url' in d:
            o.detail_url = d['detail_url']
        if 'env' in d:
            o.env = d['env']
        if 'expired_end_time' in d:
            o.expired_end_time = d['expired_end_time']
        if 'expired_start_time' in d:
            o.expired_start_time = d['expired_start_time']
        if 'isv_pid' in d:
            o.isv_pid = d['isv_pid']
        if 'item_code' in d:
            o.item_code = d['item_code']
        if 'kabao_id' in d:
            o.kabao_id = d['kabao_id']
        if 'merchant_name' in d:
            o.merchant_name = d['merchant_name']
        if 'merchant_pid' in d:
            o.merchant_pid = d['merchant_pid']
        if 'mini_app_id' in d:
            o.mini_app_id = d['mini_app_id']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'order_shop_id' in d:
            o.order_shop_id = d['order_shop_id']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'refund_price' in d:
            o.refund_price = d['refund_price']
        if 'refund_time' in d:
            o.refund_time = d['refund_time']
        if 'remain_count' in d:
            o.remain_count = d['remain_count']
        if 'solution_type' in d:
            o.solution_type = d['solution_type']
        if 'status' in d:
            o.status = d['status']
        if 'total_count' in d:
            o.total_count = d['total_count']
        if 'total_original_price' in d:
            o.total_original_price = d['total_original_price']
        if 'total_sale_price' in d:
            o.total_sale_price = d['total_sale_price']
        if 'update_time' in d:
            o.update_time = d['update_time']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


