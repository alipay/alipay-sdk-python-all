#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DiscountInfos import DiscountInfos
from alipay.aop.api.domain.DishList import DishList
from alipay.aop.api.domain.OtherAmountInfos import OtherAmountInfos
from alipay.aop.api.domain.PaymentList import PaymentList
from alipay.aop.api.domain.RefundList import RefundList


class KoubeiCateringOrderSyncModel(object):

    def __init__(self):
        self._adjust_amount = None
        self._amount = None
        self._biz_product = None
        self._business_type = None
        self._dinner_type = None
        self._discount_amount = None
        self._discount_infos = None
        self._dish_amount = None
        self._dish_list = None
        self._ext_infos = None
        self._koubei_payment_amount = None
        self._offline_payment_amount = None
        self._order_id = None
        self._order_style = None
        self._order_time = None
        self._other_amount_discountable = None
        self._other_amount_infos = None
        self._other_amount_undiscountable = None
        self._out_biz_no = None
        self._partner_id = None
        self._pay_style = None
        self._payment_list = None
        self._people_num = None
        self._pos_version = None
        self._receivable_amount = None
        self._refund_list = None
        self._shop_id = None
        self._status = None
        self._table_no = None
        self._total_paymented_amount = None
        self._use_online_promotion_flag = None

    @property
    def adjust_amount(self):
        return self._adjust_amount

    @adjust_amount.setter
    def adjust_amount(self, value):
        self._adjust_amount = value
    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def biz_product(self):
        return self._biz_product

    @biz_product.setter
    def biz_product(self, value):
        self._biz_product = value
    @property
    def business_type(self):
        return self._business_type

    @business_type.setter
    def business_type(self, value):
        self._business_type = value
    @property
    def dinner_type(self):
        return self._dinner_type

    @dinner_type.setter
    def dinner_type(self, value):
        self._dinner_type = value
    @property
    def discount_amount(self):
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, value):
        self._discount_amount = value
    @property
    def discount_infos(self):
        return self._discount_infos

    @discount_infos.setter
    def discount_infos(self, value):
        if isinstance(value, list):
            self._discount_infos = list()
            for i in value:
                if isinstance(i, DiscountInfos):
                    self._discount_infos.append(i)
                else:
                    self._discount_infos.append(DiscountInfos.from_alipay_dict(i))
    @property
    def dish_amount(self):
        return self._dish_amount

    @dish_amount.setter
    def dish_amount(self, value):
        self._dish_amount = value
    @property
    def dish_list(self):
        return self._dish_list

    @dish_list.setter
    def dish_list(self, value):
        if isinstance(value, list):
            self._dish_list = list()
            for i in value:
                if isinstance(i, DishList):
                    self._dish_list.append(i)
                else:
                    self._dish_list.append(DishList.from_alipay_dict(i))
    @property
    def ext_infos(self):
        return self._ext_infos

    @ext_infos.setter
    def ext_infos(self, value):
        self._ext_infos = value
    @property
    def koubei_payment_amount(self):
        return self._koubei_payment_amount

    @koubei_payment_amount.setter
    def koubei_payment_amount(self, value):
        self._koubei_payment_amount = value
    @property
    def offline_payment_amount(self):
        return self._offline_payment_amount

    @offline_payment_amount.setter
    def offline_payment_amount(self, value):
        self._offline_payment_amount = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def order_style(self):
        return self._order_style

    @order_style.setter
    def order_style(self, value):
        self._order_style = value
    @property
    def order_time(self):
        return self._order_time

    @order_time.setter
    def order_time(self, value):
        self._order_time = value
    @property
    def other_amount_discountable(self):
        return self._other_amount_discountable

    @other_amount_discountable.setter
    def other_amount_discountable(self, value):
        self._other_amount_discountable = value
    @property
    def other_amount_infos(self):
        return self._other_amount_infos

    @other_amount_infos.setter
    def other_amount_infos(self, value):
        if isinstance(value, list):
            self._other_amount_infos = list()
            for i in value:
                if isinstance(i, OtherAmountInfos):
                    self._other_amount_infos.append(i)
                else:
                    self._other_amount_infos.append(OtherAmountInfos.from_alipay_dict(i))
    @property
    def other_amount_undiscountable(self):
        return self._other_amount_undiscountable

    @other_amount_undiscountable.setter
    def other_amount_undiscountable(self, value):
        self._other_amount_undiscountable = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def pay_style(self):
        return self._pay_style

    @pay_style.setter
    def pay_style(self, value):
        self._pay_style = value
    @property
    def payment_list(self):
        return self._payment_list

    @payment_list.setter
    def payment_list(self, value):
        if isinstance(value, list):
            self._payment_list = list()
            for i in value:
                if isinstance(i, PaymentList):
                    self._payment_list.append(i)
                else:
                    self._payment_list.append(PaymentList.from_alipay_dict(i))
    @property
    def people_num(self):
        return self._people_num

    @people_num.setter
    def people_num(self, value):
        self._people_num = value
    @property
    def pos_version(self):
        return self._pos_version

    @pos_version.setter
    def pos_version(self, value):
        self._pos_version = value
    @property
    def receivable_amount(self):
        return self._receivable_amount

    @receivable_amount.setter
    def receivable_amount(self, value):
        self._receivable_amount = value
    @property
    def refund_list(self):
        return self._refund_list

    @refund_list.setter
    def refund_list(self, value):
        if isinstance(value, list):
            self._refund_list = list()
            for i in value:
                if isinstance(i, RefundList):
                    self._refund_list.append(i)
                else:
                    self._refund_list.append(RefundList.from_alipay_dict(i))
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def table_no(self):
        return self._table_no

    @table_no.setter
    def table_no(self, value):
        self._table_no = value
    @property
    def total_paymented_amount(self):
        return self._total_paymented_amount

    @total_paymented_amount.setter
    def total_paymented_amount(self, value):
        self._total_paymented_amount = value
    @property
    def use_online_promotion_flag(self):
        return self._use_online_promotion_flag

    @use_online_promotion_flag.setter
    def use_online_promotion_flag(self, value):
        self._use_online_promotion_flag = value


    def to_alipay_dict(self):
        params = dict()
        if self.adjust_amount:
            if hasattr(self.adjust_amount, 'to_alipay_dict'):
                params['adjust_amount'] = self.adjust_amount.to_alipay_dict()
            else:
                params['adjust_amount'] = self.adjust_amount
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.biz_product:
            if hasattr(self.biz_product, 'to_alipay_dict'):
                params['biz_product'] = self.biz_product.to_alipay_dict()
            else:
                params['biz_product'] = self.biz_product
        if self.business_type:
            if hasattr(self.business_type, 'to_alipay_dict'):
                params['business_type'] = self.business_type.to_alipay_dict()
            else:
                params['business_type'] = self.business_type
        if self.dinner_type:
            if hasattr(self.dinner_type, 'to_alipay_dict'):
                params['dinner_type'] = self.dinner_type.to_alipay_dict()
            else:
                params['dinner_type'] = self.dinner_type
        if self.discount_amount:
            if hasattr(self.discount_amount, 'to_alipay_dict'):
                params['discount_amount'] = self.discount_amount.to_alipay_dict()
            else:
                params['discount_amount'] = self.discount_amount
        if self.discount_infos:
            if isinstance(self.discount_infos, list):
                for i in range(0, len(self.discount_infos)):
                    element = self.discount_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.discount_infos[i] = element.to_alipay_dict()
            if hasattr(self.discount_infos, 'to_alipay_dict'):
                params['discount_infos'] = self.discount_infos.to_alipay_dict()
            else:
                params['discount_infos'] = self.discount_infos
        if self.dish_amount:
            if hasattr(self.dish_amount, 'to_alipay_dict'):
                params['dish_amount'] = self.dish_amount.to_alipay_dict()
            else:
                params['dish_amount'] = self.dish_amount
        if self.dish_list:
            if isinstance(self.dish_list, list):
                for i in range(0, len(self.dish_list)):
                    element = self.dish_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.dish_list[i] = element.to_alipay_dict()
            if hasattr(self.dish_list, 'to_alipay_dict'):
                params['dish_list'] = self.dish_list.to_alipay_dict()
            else:
                params['dish_list'] = self.dish_list
        if self.ext_infos:
            if hasattr(self.ext_infos, 'to_alipay_dict'):
                params['ext_infos'] = self.ext_infos.to_alipay_dict()
            else:
                params['ext_infos'] = self.ext_infos
        if self.koubei_payment_amount:
            if hasattr(self.koubei_payment_amount, 'to_alipay_dict'):
                params['koubei_payment_amount'] = self.koubei_payment_amount.to_alipay_dict()
            else:
                params['koubei_payment_amount'] = self.koubei_payment_amount
        if self.offline_payment_amount:
            if hasattr(self.offline_payment_amount, 'to_alipay_dict'):
                params['offline_payment_amount'] = self.offline_payment_amount.to_alipay_dict()
            else:
                params['offline_payment_amount'] = self.offline_payment_amount
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.order_style:
            if hasattr(self.order_style, 'to_alipay_dict'):
                params['order_style'] = self.order_style.to_alipay_dict()
            else:
                params['order_style'] = self.order_style
        if self.order_time:
            if hasattr(self.order_time, 'to_alipay_dict'):
                params['order_time'] = self.order_time.to_alipay_dict()
            else:
                params['order_time'] = self.order_time
        if self.other_amount_discountable:
            if hasattr(self.other_amount_discountable, 'to_alipay_dict'):
                params['other_amount_discountable'] = self.other_amount_discountable.to_alipay_dict()
            else:
                params['other_amount_discountable'] = self.other_amount_discountable
        if self.other_amount_infos:
            if isinstance(self.other_amount_infos, list):
                for i in range(0, len(self.other_amount_infos)):
                    element = self.other_amount_infos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.other_amount_infos[i] = element.to_alipay_dict()
            if hasattr(self.other_amount_infos, 'to_alipay_dict'):
                params['other_amount_infos'] = self.other_amount_infos.to_alipay_dict()
            else:
                params['other_amount_infos'] = self.other_amount_infos
        if self.other_amount_undiscountable:
            if hasattr(self.other_amount_undiscountable, 'to_alipay_dict'):
                params['other_amount_undiscountable'] = self.other_amount_undiscountable.to_alipay_dict()
            else:
                params['other_amount_undiscountable'] = self.other_amount_undiscountable
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        if self.pay_style:
            if hasattr(self.pay_style, 'to_alipay_dict'):
                params['pay_style'] = self.pay_style.to_alipay_dict()
            else:
                params['pay_style'] = self.pay_style
        if self.payment_list:
            if isinstance(self.payment_list, list):
                for i in range(0, len(self.payment_list)):
                    element = self.payment_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.payment_list[i] = element.to_alipay_dict()
            if hasattr(self.payment_list, 'to_alipay_dict'):
                params['payment_list'] = self.payment_list.to_alipay_dict()
            else:
                params['payment_list'] = self.payment_list
        if self.people_num:
            if hasattr(self.people_num, 'to_alipay_dict'):
                params['people_num'] = self.people_num.to_alipay_dict()
            else:
                params['people_num'] = self.people_num
        if self.pos_version:
            if hasattr(self.pos_version, 'to_alipay_dict'):
                params['pos_version'] = self.pos_version.to_alipay_dict()
            else:
                params['pos_version'] = self.pos_version
        if self.receivable_amount:
            if hasattr(self.receivable_amount, 'to_alipay_dict'):
                params['receivable_amount'] = self.receivable_amount.to_alipay_dict()
            else:
                params['receivable_amount'] = self.receivable_amount
        if self.refund_list:
            if isinstance(self.refund_list, list):
                for i in range(0, len(self.refund_list)):
                    element = self.refund_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.refund_list[i] = element.to_alipay_dict()
            if hasattr(self.refund_list, 'to_alipay_dict'):
                params['refund_list'] = self.refund_list.to_alipay_dict()
            else:
                params['refund_list'] = self.refund_list
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.table_no:
            if hasattr(self.table_no, 'to_alipay_dict'):
                params['table_no'] = self.table_no.to_alipay_dict()
            else:
                params['table_no'] = self.table_no
        if self.total_paymented_amount:
            if hasattr(self.total_paymented_amount, 'to_alipay_dict'):
                params['total_paymented_amount'] = self.total_paymented_amount.to_alipay_dict()
            else:
                params['total_paymented_amount'] = self.total_paymented_amount
        if self.use_online_promotion_flag:
            if hasattr(self.use_online_promotion_flag, 'to_alipay_dict'):
                params['use_online_promotion_flag'] = self.use_online_promotion_flag.to_alipay_dict()
            else:
                params['use_online_promotion_flag'] = self.use_online_promotion_flag
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiCateringOrderSyncModel()
        if 'adjust_amount' in d:
            o.adjust_amount = d['adjust_amount']
        if 'amount' in d:
            o.amount = d['amount']
        if 'biz_product' in d:
            o.biz_product = d['biz_product']
        if 'business_type' in d:
            o.business_type = d['business_type']
        if 'dinner_type' in d:
            o.dinner_type = d['dinner_type']
        if 'discount_amount' in d:
            o.discount_amount = d['discount_amount']
        if 'discount_infos' in d:
            o.discount_infos = d['discount_infos']
        if 'dish_amount' in d:
            o.dish_amount = d['dish_amount']
        if 'dish_list' in d:
            o.dish_list = d['dish_list']
        if 'ext_infos' in d:
            o.ext_infos = d['ext_infos']
        if 'koubei_payment_amount' in d:
            o.koubei_payment_amount = d['koubei_payment_amount']
        if 'offline_payment_amount' in d:
            o.offline_payment_amount = d['offline_payment_amount']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'order_style' in d:
            o.order_style = d['order_style']
        if 'order_time' in d:
            o.order_time = d['order_time']
        if 'other_amount_discountable' in d:
            o.other_amount_discountable = d['other_amount_discountable']
        if 'other_amount_infos' in d:
            o.other_amount_infos = d['other_amount_infos']
        if 'other_amount_undiscountable' in d:
            o.other_amount_undiscountable = d['other_amount_undiscountable']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'pay_style' in d:
            o.pay_style = d['pay_style']
        if 'payment_list' in d:
            o.payment_list = d['payment_list']
        if 'people_num' in d:
            o.people_num = d['people_num']
        if 'pos_version' in d:
            o.pos_version = d['pos_version']
        if 'receivable_amount' in d:
            o.receivable_amount = d['receivable_amount']
        if 'refund_list' in d:
            o.refund_list = d['refund_list']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'status' in d:
            o.status = d['status']
        if 'table_no' in d:
            o.table_no = d['table_no']
        if 'total_paymented_amount' in d:
            o.total_paymented_amount = d['total_paymented_amount']
        if 'use_online_promotion_flag' in d:
            o.use_online_promotion_flag = d['use_online_promotion_flag']
        return o


