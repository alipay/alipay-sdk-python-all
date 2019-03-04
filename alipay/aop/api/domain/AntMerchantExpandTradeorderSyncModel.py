#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OrderExtInfo import OrderExtInfo
from alipay.aop.api.domain.ItemOrder import ItemOrder
from alipay.aop.api.domain.OutDiscountInfo import OutDiscountInfo


class AntMerchantExpandTradeorderSyncModel(object):

    def __init__(self):
        self._amount = None
        self._buyer_id = None
        self._ext_info = None
        self._item_order_list = None
        self._memo = None
        self._merchant_subsidy_amount = None
        self._out_biz_no = None
        self._out_biz_type = None
        self._out_discount_infos = None
        self._partner_id = None
        self._partner_subsidy_amount = None
        self._real_amount = None
        self._seller_id = None
        self._shop_id = None
        self._trade_no = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def buyer_id(self):
        return self._buyer_id

    @buyer_id.setter
    def buyer_id(self, value):
        self._buyer_id = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        if isinstance(value, list):
            self._ext_info = list()
            for i in value:
                if isinstance(i, OrderExtInfo):
                    self._ext_info.append(i)
                else:
                    self._ext_info.append(OrderExtInfo.from_alipay_dict(i))
    @property
    def item_order_list(self):
        return self._item_order_list

    @item_order_list.setter
    def item_order_list(self, value):
        if isinstance(value, list):
            self._item_order_list = list()
            for i in value:
                if isinstance(i, ItemOrder):
                    self._item_order_list.append(i)
                else:
                    self._item_order_list.append(ItemOrder.from_alipay_dict(i))
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def merchant_subsidy_amount(self):
        return self._merchant_subsidy_amount

    @merchant_subsidy_amount.setter
    def merchant_subsidy_amount(self, value):
        self._merchant_subsidy_amount = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def out_biz_type(self):
        return self._out_biz_type

    @out_biz_type.setter
    def out_biz_type(self, value):
        self._out_biz_type = value
    @property
    def out_discount_infos(self):
        return self._out_discount_infos

    @out_discount_infos.setter
    def out_discount_infos(self, value):
        if isinstance(value, list):
            self._out_discount_infos = list()
            for i in value:
                if isinstance(i, OutDiscountInfo):
                    self._out_discount_infos.append(i)
                else:
                    self._out_discount_infos.append(OutDiscountInfo.from_alipay_dict(i))
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def partner_subsidy_amount(self):
        return self._partner_subsidy_amount

    @partner_subsidy_amount.setter
    def partner_subsidy_amount(self, value):
        self._partner_subsidy_amount = value
    @property
    def real_amount(self):
        return self._real_amount

    @real_amount.setter
    def real_amount(self, value):
        self._real_amount = value
    @property
    def seller_id(self):
        return self._seller_id

    @seller_id.setter
    def seller_id(self, value):
        self._seller_id = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.buyer_id:
            if hasattr(self.buyer_id, 'to_alipay_dict'):
                params['buyer_id'] = self.buyer_id.to_alipay_dict()
            else:
                params['buyer_id'] = self.buyer_id
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
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.merchant_subsidy_amount:
            if hasattr(self.merchant_subsidy_amount, 'to_alipay_dict'):
                params['merchant_subsidy_amount'] = self.merchant_subsidy_amount.to_alipay_dict()
            else:
                params['merchant_subsidy_amount'] = self.merchant_subsidy_amount
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.out_biz_type:
            if hasattr(self.out_biz_type, 'to_alipay_dict'):
                params['out_biz_type'] = self.out_biz_type.to_alipay_dict()
            else:
                params['out_biz_type'] = self.out_biz_type
        if self.out_discount_infos:
            if isinstance(self.out_discount_infos, list):
                for i in range(0, len(self.out_discount_infos)):
                    element = self.out_discount_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.out_discount_infos[i] = element.to_alipay_dict()
            if hasattr(self.out_discount_infos, 'to_alipay_dict'):
                params['out_discount_infos'] = self.out_discount_infos.to_alipay_dict()
            else:
                params['out_discount_infos'] = self.out_discount_infos
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        if self.partner_subsidy_amount:
            if hasattr(self.partner_subsidy_amount, 'to_alipay_dict'):
                params['partner_subsidy_amount'] = self.partner_subsidy_amount.to_alipay_dict()
            else:
                params['partner_subsidy_amount'] = self.partner_subsidy_amount
        if self.real_amount:
            if hasattr(self.real_amount, 'to_alipay_dict'):
                params['real_amount'] = self.real_amount.to_alipay_dict()
            else:
                params['real_amount'] = self.real_amount
        if self.seller_id:
            if hasattr(self.seller_id, 'to_alipay_dict'):
                params['seller_id'] = self.seller_id.to_alipay_dict()
            else:
                params['seller_id'] = self.seller_id
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
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
        o = AntMerchantExpandTradeorderSyncModel()
        if 'amount' in d:
            o.amount = d['amount']
        if 'buyer_id' in d:
            o.buyer_id = d['buyer_id']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'item_order_list' in d:
            o.item_order_list = d['item_order_list']
        if 'memo' in d:
            o.memo = d['memo']
        if 'merchant_subsidy_amount' in d:
            o.merchant_subsidy_amount = d['merchant_subsidy_amount']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'out_biz_type' in d:
            o.out_biz_type = d['out_biz_type']
        if 'out_discount_infos' in d:
            o.out_discount_infos = d['out_discount_infos']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'partner_subsidy_amount' in d:
            o.partner_subsidy_amount = d['partner_subsidy_amount']
        if 'real_amount' in d:
            o.real_amount = d['real_amount']
        if 'seller_id' in d:
            o.seller_id = d['seller_id']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        return o


