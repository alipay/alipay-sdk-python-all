#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ItemOrderBillRefundResponse import ItemOrderBillRefundResponse


class ItemOrderBillDetailResponse(object):

    def __init__(self):
        self._create_time = None
        self._fee_categories = None
        self._huabei_technical_service_fee = None
        self._isv_alloc_amount = None
        self._isv_name = None
        self._mini_app_id = None
        self._order_id = None
        self._order_name = None
        self._order_price = None
        self._order_status = None
        self._out_trade_no = None
        self._pay_amount = None
        self._pay_commission = None
        self._platform_service = None
        self._platform_service_refund = None
        self._pre_promotion = None
        self._predict_settle_time = None
        self._public_alloc_amount = None
        self._public_name = None
        self._receipt_amount = None
        self._refund_fee = None
        self._refund_fee_list = None
        self._refund_isv_alloc_amount = None
        self._refund_pay_commission = None
        self._refund_public_alloc_amount = None
        self._remark = None
        self._rent_funder_commission_amount = None
        self._rent_funder_nick_name = None
        self._service_type = None
        self._settle_status = None
        self._settle_time = None
        self._settlement_amount = None
        self._sub_biz_no = None
        self._trade_no = None

    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, value):
        self._create_time = value
    @property
    def fee_categories(self):
        return self._fee_categories

    @fee_categories.setter
    def fee_categories(self, value):
        self._fee_categories = value
    @property
    def huabei_technical_service_fee(self):
        return self._huabei_technical_service_fee

    @huabei_technical_service_fee.setter
    def huabei_technical_service_fee(self, value):
        self._huabei_technical_service_fee = value
    @property
    def isv_alloc_amount(self):
        return self._isv_alloc_amount

    @isv_alloc_amount.setter
    def isv_alloc_amount(self, value):
        self._isv_alloc_amount = value
    @property
    def isv_name(self):
        return self._isv_name

    @isv_name.setter
    def isv_name(self, value):
        self._isv_name = value
    @property
    def mini_app_id(self):
        return self._mini_app_id

    @mini_app_id.setter
    def mini_app_id(self, value):
        self._mini_app_id = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def order_name(self):
        return self._order_name

    @order_name.setter
    def order_name(self, value):
        self._order_name = value
    @property
    def order_price(self):
        return self._order_price

    @order_price.setter
    def order_price(self, value):
        self._order_price = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def pay_amount(self):
        return self._pay_amount

    @pay_amount.setter
    def pay_amount(self, value):
        self._pay_amount = value
    @property
    def pay_commission(self):
        return self._pay_commission

    @pay_commission.setter
    def pay_commission(self, value):
        self._pay_commission = value
    @property
    def platform_service(self):
        return self._platform_service

    @platform_service.setter
    def platform_service(self, value):
        self._platform_service = value
    @property
    def platform_service_refund(self):
        return self._platform_service_refund

    @platform_service_refund.setter
    def platform_service_refund(self, value):
        self._platform_service_refund = value
    @property
    def pre_promotion(self):
        return self._pre_promotion

    @pre_promotion.setter
    def pre_promotion(self, value):
        self._pre_promotion = value
    @property
    def predict_settle_time(self):
        return self._predict_settle_time

    @predict_settle_time.setter
    def predict_settle_time(self, value):
        self._predict_settle_time = value
    @property
    def public_alloc_amount(self):
        return self._public_alloc_amount

    @public_alloc_amount.setter
    def public_alloc_amount(self, value):
        self._public_alloc_amount = value
    @property
    def public_name(self):
        return self._public_name

    @public_name.setter
    def public_name(self, value):
        self._public_name = value
    @property
    def receipt_amount(self):
        return self._receipt_amount

    @receipt_amount.setter
    def receipt_amount(self, value):
        self._receipt_amount = value
    @property
    def refund_fee(self):
        return self._refund_fee

    @refund_fee.setter
    def refund_fee(self, value):
        self._refund_fee = value
    @property
    def refund_fee_list(self):
        return self._refund_fee_list

    @refund_fee_list.setter
    def refund_fee_list(self, value):
        if isinstance(value, list):
            self._refund_fee_list = list()
            for i in value:
                if isinstance(i, ItemOrderBillRefundResponse):
                    self._refund_fee_list.append(i)
                else:
                    self._refund_fee_list.append(ItemOrderBillRefundResponse.from_alipay_dict(i))
    @property
    def refund_isv_alloc_amount(self):
        return self._refund_isv_alloc_amount

    @refund_isv_alloc_amount.setter
    def refund_isv_alloc_amount(self, value):
        self._refund_isv_alloc_amount = value
    @property
    def refund_pay_commission(self):
        return self._refund_pay_commission

    @refund_pay_commission.setter
    def refund_pay_commission(self, value):
        self._refund_pay_commission = value
    @property
    def refund_public_alloc_amount(self):
        return self._refund_public_alloc_amount

    @refund_public_alloc_amount.setter
    def refund_public_alloc_amount(self, value):
        self._refund_public_alloc_amount = value
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value
    @property
    def rent_funder_commission_amount(self):
        return self._rent_funder_commission_amount

    @rent_funder_commission_amount.setter
    def rent_funder_commission_amount(self, value):
        self._rent_funder_commission_amount = value
    @property
    def rent_funder_nick_name(self):
        return self._rent_funder_nick_name

    @rent_funder_nick_name.setter
    def rent_funder_nick_name(self, value):
        self._rent_funder_nick_name = value
    @property
    def service_type(self):
        return self._service_type

    @service_type.setter
    def service_type(self, value):
        self._service_type = value
    @property
    def settle_status(self):
        return self._settle_status

    @settle_status.setter
    def settle_status(self, value):
        self._settle_status = value
    @property
    def settle_time(self):
        return self._settle_time

    @settle_time.setter
    def settle_time(self, value):
        self._settle_time = value
    @property
    def settlement_amount(self):
        return self._settlement_amount

    @settlement_amount.setter
    def settlement_amount(self, value):
        self._settlement_amount = value
    @property
    def sub_biz_no(self):
        return self._sub_biz_no

    @sub_biz_no.setter
    def sub_biz_no(self, value):
        self._sub_biz_no = value
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
        if self.fee_categories:
            if hasattr(self.fee_categories, 'to_alipay_dict'):
                params['fee_categories'] = self.fee_categories.to_alipay_dict()
            else:
                params['fee_categories'] = self.fee_categories
        if self.huabei_technical_service_fee:
            if hasattr(self.huabei_technical_service_fee, 'to_alipay_dict'):
                params['huabei_technical_service_fee'] = self.huabei_technical_service_fee.to_alipay_dict()
            else:
                params['huabei_technical_service_fee'] = self.huabei_technical_service_fee
        if self.isv_alloc_amount:
            if hasattr(self.isv_alloc_amount, 'to_alipay_dict'):
                params['isv_alloc_amount'] = self.isv_alloc_amount.to_alipay_dict()
            else:
                params['isv_alloc_amount'] = self.isv_alloc_amount
        if self.isv_name:
            if hasattr(self.isv_name, 'to_alipay_dict'):
                params['isv_name'] = self.isv_name.to_alipay_dict()
            else:
                params['isv_name'] = self.isv_name
        if self.mini_app_id:
            if hasattr(self.mini_app_id, 'to_alipay_dict'):
                params['mini_app_id'] = self.mini_app_id.to_alipay_dict()
            else:
                params['mini_app_id'] = self.mini_app_id
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.order_name:
            if hasattr(self.order_name, 'to_alipay_dict'):
                params['order_name'] = self.order_name.to_alipay_dict()
            else:
                params['order_name'] = self.order_name
        if self.order_price:
            if hasattr(self.order_price, 'to_alipay_dict'):
                params['order_price'] = self.order_price.to_alipay_dict()
            else:
                params['order_price'] = self.order_price
        if self.order_status:
            if hasattr(self.order_status, 'to_alipay_dict'):
                params['order_status'] = self.order_status.to_alipay_dict()
            else:
                params['order_status'] = self.order_status
        if self.out_trade_no:
            if hasattr(self.out_trade_no, 'to_alipay_dict'):
                params['out_trade_no'] = self.out_trade_no.to_alipay_dict()
            else:
                params['out_trade_no'] = self.out_trade_no
        if self.pay_amount:
            if hasattr(self.pay_amount, 'to_alipay_dict'):
                params['pay_amount'] = self.pay_amount.to_alipay_dict()
            else:
                params['pay_amount'] = self.pay_amount
        if self.pay_commission:
            if hasattr(self.pay_commission, 'to_alipay_dict'):
                params['pay_commission'] = self.pay_commission.to_alipay_dict()
            else:
                params['pay_commission'] = self.pay_commission
        if self.platform_service:
            if hasattr(self.platform_service, 'to_alipay_dict'):
                params['platform_service'] = self.platform_service.to_alipay_dict()
            else:
                params['platform_service'] = self.platform_service
        if self.platform_service_refund:
            if hasattr(self.platform_service_refund, 'to_alipay_dict'):
                params['platform_service_refund'] = self.platform_service_refund.to_alipay_dict()
            else:
                params['platform_service_refund'] = self.platform_service_refund
        if self.pre_promotion:
            if hasattr(self.pre_promotion, 'to_alipay_dict'):
                params['pre_promotion'] = self.pre_promotion.to_alipay_dict()
            else:
                params['pre_promotion'] = self.pre_promotion
        if self.predict_settle_time:
            if hasattr(self.predict_settle_time, 'to_alipay_dict'):
                params['predict_settle_time'] = self.predict_settle_time.to_alipay_dict()
            else:
                params['predict_settle_time'] = self.predict_settle_time
        if self.public_alloc_amount:
            if hasattr(self.public_alloc_amount, 'to_alipay_dict'):
                params['public_alloc_amount'] = self.public_alloc_amount.to_alipay_dict()
            else:
                params['public_alloc_amount'] = self.public_alloc_amount
        if self.public_name:
            if hasattr(self.public_name, 'to_alipay_dict'):
                params['public_name'] = self.public_name.to_alipay_dict()
            else:
                params['public_name'] = self.public_name
        if self.receipt_amount:
            if hasattr(self.receipt_amount, 'to_alipay_dict'):
                params['receipt_amount'] = self.receipt_amount.to_alipay_dict()
            else:
                params['receipt_amount'] = self.receipt_amount
        if self.refund_fee:
            if hasattr(self.refund_fee, 'to_alipay_dict'):
                params['refund_fee'] = self.refund_fee.to_alipay_dict()
            else:
                params['refund_fee'] = self.refund_fee
        if self.refund_fee_list:
            if isinstance(self.refund_fee_list, list):
                for i in range(0, len(self.refund_fee_list)):
                    element = self.refund_fee_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.refund_fee_list[i] = element.to_alipay_dict()
            if hasattr(self.refund_fee_list, 'to_alipay_dict'):
                params['refund_fee_list'] = self.refund_fee_list.to_alipay_dict()
            else:
                params['refund_fee_list'] = self.refund_fee_list
        if self.refund_isv_alloc_amount:
            if hasattr(self.refund_isv_alloc_amount, 'to_alipay_dict'):
                params['refund_isv_alloc_amount'] = self.refund_isv_alloc_amount.to_alipay_dict()
            else:
                params['refund_isv_alloc_amount'] = self.refund_isv_alloc_amount
        if self.refund_pay_commission:
            if hasattr(self.refund_pay_commission, 'to_alipay_dict'):
                params['refund_pay_commission'] = self.refund_pay_commission.to_alipay_dict()
            else:
                params['refund_pay_commission'] = self.refund_pay_commission
        if self.refund_public_alloc_amount:
            if hasattr(self.refund_public_alloc_amount, 'to_alipay_dict'):
                params['refund_public_alloc_amount'] = self.refund_public_alloc_amount.to_alipay_dict()
            else:
                params['refund_public_alloc_amount'] = self.refund_public_alloc_amount
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
        if self.rent_funder_commission_amount:
            if hasattr(self.rent_funder_commission_amount, 'to_alipay_dict'):
                params['rent_funder_commission_amount'] = self.rent_funder_commission_amount.to_alipay_dict()
            else:
                params['rent_funder_commission_amount'] = self.rent_funder_commission_amount
        if self.rent_funder_nick_name:
            if hasattr(self.rent_funder_nick_name, 'to_alipay_dict'):
                params['rent_funder_nick_name'] = self.rent_funder_nick_name.to_alipay_dict()
            else:
                params['rent_funder_nick_name'] = self.rent_funder_nick_name
        if self.service_type:
            if hasattr(self.service_type, 'to_alipay_dict'):
                params['service_type'] = self.service_type.to_alipay_dict()
            else:
                params['service_type'] = self.service_type
        if self.settle_status:
            if hasattr(self.settle_status, 'to_alipay_dict'):
                params['settle_status'] = self.settle_status.to_alipay_dict()
            else:
                params['settle_status'] = self.settle_status
        if self.settle_time:
            if hasattr(self.settle_time, 'to_alipay_dict'):
                params['settle_time'] = self.settle_time.to_alipay_dict()
            else:
                params['settle_time'] = self.settle_time
        if self.settlement_amount:
            if hasattr(self.settlement_amount, 'to_alipay_dict'):
                params['settlement_amount'] = self.settlement_amount.to_alipay_dict()
            else:
                params['settlement_amount'] = self.settlement_amount
        if self.sub_biz_no:
            if hasattr(self.sub_biz_no, 'to_alipay_dict'):
                params['sub_biz_no'] = self.sub_biz_no.to_alipay_dict()
            else:
                params['sub_biz_no'] = self.sub_biz_no
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
        o = ItemOrderBillDetailResponse()
        if 'create_time' in d:
            o.create_time = d['create_time']
        if 'fee_categories' in d:
            o.fee_categories = d['fee_categories']
        if 'huabei_technical_service_fee' in d:
            o.huabei_technical_service_fee = d['huabei_technical_service_fee']
        if 'isv_alloc_amount' in d:
            o.isv_alloc_amount = d['isv_alloc_amount']
        if 'isv_name' in d:
            o.isv_name = d['isv_name']
        if 'mini_app_id' in d:
            o.mini_app_id = d['mini_app_id']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'order_name' in d:
            o.order_name = d['order_name']
        if 'order_price' in d:
            o.order_price = d['order_price']
        if 'order_status' in d:
            o.order_status = d['order_status']
        if 'out_trade_no' in d:
            o.out_trade_no = d['out_trade_no']
        if 'pay_amount' in d:
            o.pay_amount = d['pay_amount']
        if 'pay_commission' in d:
            o.pay_commission = d['pay_commission']
        if 'platform_service' in d:
            o.platform_service = d['platform_service']
        if 'platform_service_refund' in d:
            o.platform_service_refund = d['platform_service_refund']
        if 'pre_promotion' in d:
            o.pre_promotion = d['pre_promotion']
        if 'predict_settle_time' in d:
            o.predict_settle_time = d['predict_settle_time']
        if 'public_alloc_amount' in d:
            o.public_alloc_amount = d['public_alloc_amount']
        if 'public_name' in d:
            o.public_name = d['public_name']
        if 'receipt_amount' in d:
            o.receipt_amount = d['receipt_amount']
        if 'refund_fee' in d:
            o.refund_fee = d['refund_fee']
        if 'refund_fee_list' in d:
            o.refund_fee_list = d['refund_fee_list']
        if 'refund_isv_alloc_amount' in d:
            o.refund_isv_alloc_amount = d['refund_isv_alloc_amount']
        if 'refund_pay_commission' in d:
            o.refund_pay_commission = d['refund_pay_commission']
        if 'refund_public_alloc_amount' in d:
            o.refund_public_alloc_amount = d['refund_public_alloc_amount']
        if 'remark' in d:
            o.remark = d['remark']
        if 'rent_funder_commission_amount' in d:
            o.rent_funder_commission_amount = d['rent_funder_commission_amount']
        if 'rent_funder_nick_name' in d:
            o.rent_funder_nick_name = d['rent_funder_nick_name']
        if 'service_type' in d:
            o.service_type = d['service_type']
        if 'settle_status' in d:
            o.settle_status = d['settle_status']
        if 'settle_time' in d:
            o.settle_time = d['settle_time']
        if 'settlement_amount' in d:
            o.settlement_amount = d['settlement_amount']
        if 'sub_biz_no' in d:
            o.sub_biz_no = d['sub_biz_no']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        return o


