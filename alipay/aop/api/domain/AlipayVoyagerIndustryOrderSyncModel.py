#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Buyer import Buyer
from alipay.aop.api.domain.AmountDTO import AmountDTO
from alipay.aop.api.domain.TravelItemInfo import TravelItemInfo
from alipay.aop.api.domain.TravelerLogisticsInfo import TravelerLogisticsInfo
from alipay.aop.api.domain.AmountDTO import AmountDTO
from alipay.aop.api.domain.AmountDTO import AmountDTO


class AlipayVoyagerIndustryOrderSyncModel(object):

    def __init__(self):
        self._buyer_info = None
        self._discount_amount = None
        self._ext_info = None
        self._industry_code = None
        self._item_order_list = None
        self._logistics_info_list = None
        self._open_id = None
        self._order_amount = None
        self._order_create_time = None
        self._order_modified_time = None
        self._order_pay_time = None
        self._out_biz_no = None
        self._pay_amount = None
        self._payment_no = None
        self._source_app = None
        self._user_id = None

    @property
    def buyer_info(self):
        return self._buyer_info

    @buyer_info.setter
    def buyer_info(self, value):
        if isinstance(value, Buyer):
            self._buyer_info = value
        else:
            self._buyer_info = Buyer.from_alipay_dict(value)
    @property
    def discount_amount(self):
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, value):
        if isinstance(value, AmountDTO):
            self._discount_amount = value
        else:
            self._discount_amount = AmountDTO.from_alipay_dict(value)
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        if isinstance(value, list):
            self._ext_info = list()
            for i in value:
                self._ext_info.append(i)
    @property
    def industry_code(self):
        return self._industry_code

    @industry_code.setter
    def industry_code(self, value):
        self._industry_code = value
    @property
    def item_order_list(self):
        return self._item_order_list

    @item_order_list.setter
    def item_order_list(self, value):
        if isinstance(value, list):
            self._item_order_list = list()
            for i in value:
                if isinstance(i, TravelItemInfo):
                    self._item_order_list.append(i)
                else:
                    self._item_order_list.append(TravelItemInfo.from_alipay_dict(i))
    @property
    def logistics_info_list(self):
        return self._logistics_info_list

    @logistics_info_list.setter
    def logistics_info_list(self, value):
        if isinstance(value, list):
            self._logistics_info_list = list()
            for i in value:
                if isinstance(i, TravelerLogisticsInfo):
                    self._logistics_info_list.append(i)
                else:
                    self._logistics_info_list.append(TravelerLogisticsInfo.from_alipay_dict(i))
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def order_amount(self):
        return self._order_amount

    @order_amount.setter
    def order_amount(self, value):
        if isinstance(value, AmountDTO):
            self._order_amount = value
        else:
            self._order_amount = AmountDTO.from_alipay_dict(value)
    @property
    def order_create_time(self):
        return self._order_create_time

    @order_create_time.setter
    def order_create_time(self, value):
        self._order_create_time = value
    @property
    def order_modified_time(self):
        return self._order_modified_time

    @order_modified_time.setter
    def order_modified_time(self, value):
        self._order_modified_time = value
    @property
    def order_pay_time(self):
        return self._order_pay_time

    @order_pay_time.setter
    def order_pay_time(self, value):
        self._order_pay_time = value
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
        if isinstance(value, AmountDTO):
            self._pay_amount = value
        else:
            self._pay_amount = AmountDTO.from_alipay_dict(value)
    @property
    def payment_no(self):
        return self._payment_no

    @payment_no.setter
    def payment_no(self, value):
        self._payment_no = value
    @property
    def source_app(self):
        return self._source_app

    @source_app.setter
    def source_app(self, value):
        self._source_app = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.buyer_info:
            if hasattr(self.buyer_info, 'to_alipay_dict'):
                params['buyer_info'] = self.buyer_info.to_alipay_dict()
            else:
                params['buyer_info'] = self.buyer_info
        if self.discount_amount:
            if hasattr(self.discount_amount, 'to_alipay_dict'):
                params['discount_amount'] = self.discount_amount.to_alipay_dict()
            else:
                params['discount_amount'] = self.discount_amount
        if self.ext_info:
            if isinstance(self.ext_info, list):
                for i in range(0, len(self.ext_info)):
                    element = self.ext_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ext_info[i] = element.to_alipay_dict()
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.industry_code:
            if hasattr(self.industry_code, 'to_alipay_dict'):
                params['industry_code'] = self.industry_code.to_alipay_dict()
            else:
                params['industry_code'] = self.industry_code
        if self.item_order_list:
            if isinstance(self.item_order_list, list):
                for i in range(0, len(self.item_order_list)):
                    element = self.item_order_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.item_order_list[i] = element.to_alipay_dict()
            if hasattr(self.item_order_list, 'to_alipay_dict'):
                params['item_order_list'] = self.item_order_list.to_alipay_dict()
            else:
                params['item_order_list'] = self.item_order_list
        if self.logistics_info_list:
            if isinstance(self.logistics_info_list, list):
                for i in range(0, len(self.logistics_info_list)):
                    element = self.logistics_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.logistics_info_list[i] = element.to_alipay_dict()
            if hasattr(self.logistics_info_list, 'to_alipay_dict'):
                params['logistics_info_list'] = self.logistics_info_list.to_alipay_dict()
            else:
                params['logistics_info_list'] = self.logistics_info_list
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.order_amount:
            if hasattr(self.order_amount, 'to_alipay_dict'):
                params['order_amount'] = self.order_amount.to_alipay_dict()
            else:
                params['order_amount'] = self.order_amount
        if self.order_create_time:
            if hasattr(self.order_create_time, 'to_alipay_dict'):
                params['order_create_time'] = self.order_create_time.to_alipay_dict()
            else:
                params['order_create_time'] = self.order_create_time
        if self.order_modified_time:
            if hasattr(self.order_modified_time, 'to_alipay_dict'):
                params['order_modified_time'] = self.order_modified_time.to_alipay_dict()
            else:
                params['order_modified_time'] = self.order_modified_time
        if self.order_pay_time:
            if hasattr(self.order_pay_time, 'to_alipay_dict'):
                params['order_pay_time'] = self.order_pay_time.to_alipay_dict()
            else:
                params['order_pay_time'] = self.order_pay_time
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
        if self.payment_no:
            if hasattr(self.payment_no, 'to_alipay_dict'):
                params['payment_no'] = self.payment_no.to_alipay_dict()
            else:
                params['payment_no'] = self.payment_no
        if self.source_app:
            if hasattr(self.source_app, 'to_alipay_dict'):
                params['source_app'] = self.source_app.to_alipay_dict()
            else:
                params['source_app'] = self.source_app
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
        o = AlipayVoyagerIndustryOrderSyncModel()
        if 'buyer_info' in d:
            o.buyer_info = d['buyer_info']
        if 'discount_amount' in d:
            o.discount_amount = d['discount_amount']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'industry_code' in d:
            o.industry_code = d['industry_code']
        if 'item_order_list' in d:
            o.item_order_list = d['item_order_list']
        if 'logistics_info_list' in d:
            o.logistics_info_list = d['logistics_info_list']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'order_amount' in d:
            o.order_amount = d['order_amount']
        if 'order_create_time' in d:
            o.order_create_time = d['order_create_time']
        if 'order_modified_time' in d:
            o.order_modified_time = d['order_modified_time']
        if 'order_pay_time' in d:
            o.order_pay_time = d['order_pay_time']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'pay_amount' in d:
            o.pay_amount = d['pay_amount']
        if 'payment_no' in d:
            o.payment_no = d['payment_no']
        if 'source_app' in d:
            o.source_app = d['source_app']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


