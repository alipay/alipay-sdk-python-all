#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SelfItemOrderBillDetailResponse(object):

    def __init__(self):
        self._certificate_id = None
        self._certificate_price = None
        self._certificate_status = None
        self._fee_category = None
        self._isv_alloc_amount = None
        self._isv_name = None
        self._item_id = None
        self._item_type = None
        self._merchant_discount_amount = None
        self._merchant_verification_no = None
        self._mini_app_id = None
        self._order_id = None
        self._order_scene = None
        self._original_price = None
        self._pay_commission = None
        self._pay_discounted_price = None
        self._platform_discount_amount = None
        self._platform_service = None
        self._platform_service_refund = None
        self._pre_cps_amount = None
        self._pre_isv_alloc_amount = None
        self._pre_merchant_discount_amount = None
        self._pre_pay_commission = None
        self._pre_platform_discount_amount = None
        self._pre_public_alloc_amount = None
        self._pre_saas_alloc_amount = None
        self._pre_user_fund_amount = None
        self._predict_settle_time = None
        self._public_alloc_amount = None
        self._public_name = None
        self._real_receipt_amount = None
        self._refund_fee = None
        self._refund_isv_alloc_amount = None
        self._refund_merchant_discount_amount = None
        self._refund_pay_commission = None
        self._refund_platform_discount_amount = None
        self._refund_public_alloc_amount = None
        self._refund_saas_alloc_amount = None
        self._refund_service_amount = None
        self._saas_alloc_amount = None
        self._saas_name = None
        self._self_shop_name = None
        self._serial_no = None
        self._service_amount = None
        self._settle_account_no = None
        self._settle_account_type = None
        self._settle_amount = None
        self._settle_batch_id = None
        self._settle_rel_shop_id = None
        self._settle_status = None
        self._settle_time = None
        self._trade_no = None
        self._use_user_name = None
        self._user_fund_amount = None
        self._verification_shop_id = None
        self._verification_shop_name = None
        self._verification_time = None
        self._verification_trade_no = None

    @property
    def certificate_id(self):
        return self._certificate_id

    @certificate_id.setter
    def certificate_id(self, value):
        self._certificate_id = value
    @property
    def certificate_price(self):
        return self._certificate_price

    @certificate_price.setter
    def certificate_price(self, value):
        self._certificate_price = value
    @property
    def certificate_status(self):
        return self._certificate_status

    @certificate_status.setter
    def certificate_status(self, value):
        self._certificate_status = value
    @property
    def fee_category(self):
        return self._fee_category

    @fee_category.setter
    def fee_category(self, value):
        self._fee_category = value
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
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def item_type(self):
        return self._item_type

    @item_type.setter
    def item_type(self, value):
        self._item_type = value
    @property
    def merchant_discount_amount(self):
        return self._merchant_discount_amount

    @merchant_discount_amount.setter
    def merchant_discount_amount(self, value):
        self._merchant_discount_amount = value
    @property
    def merchant_verification_no(self):
        return self._merchant_verification_no

    @merchant_verification_no.setter
    def merchant_verification_no(self, value):
        self._merchant_verification_no = value
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
    def order_scene(self):
        return self._order_scene

    @order_scene.setter
    def order_scene(self, value):
        self._order_scene = value
    @property
    def original_price(self):
        return self._original_price

    @original_price.setter
    def original_price(self, value):
        self._original_price = value
    @property
    def pay_commission(self):
        return self._pay_commission

    @pay_commission.setter
    def pay_commission(self, value):
        self._pay_commission = value
    @property
    def pay_discounted_price(self):
        return self._pay_discounted_price

    @pay_discounted_price.setter
    def pay_discounted_price(self, value):
        self._pay_discounted_price = value
    @property
    def platform_discount_amount(self):
        return self._platform_discount_amount

    @platform_discount_amount.setter
    def platform_discount_amount(self, value):
        self._platform_discount_amount = value
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
    def pre_cps_amount(self):
        return self._pre_cps_amount

    @pre_cps_amount.setter
    def pre_cps_amount(self, value):
        self._pre_cps_amount = value
    @property
    def pre_isv_alloc_amount(self):
        return self._pre_isv_alloc_amount

    @pre_isv_alloc_amount.setter
    def pre_isv_alloc_amount(self, value):
        self._pre_isv_alloc_amount = value
    @property
    def pre_merchant_discount_amount(self):
        return self._pre_merchant_discount_amount

    @pre_merchant_discount_amount.setter
    def pre_merchant_discount_amount(self, value):
        self._pre_merchant_discount_amount = value
    @property
    def pre_pay_commission(self):
        return self._pre_pay_commission

    @pre_pay_commission.setter
    def pre_pay_commission(self, value):
        self._pre_pay_commission = value
    @property
    def pre_platform_discount_amount(self):
        return self._pre_platform_discount_amount

    @pre_platform_discount_amount.setter
    def pre_platform_discount_amount(self, value):
        self._pre_platform_discount_amount = value
    @property
    def pre_public_alloc_amount(self):
        return self._pre_public_alloc_amount

    @pre_public_alloc_amount.setter
    def pre_public_alloc_amount(self, value):
        self._pre_public_alloc_amount = value
    @property
    def pre_saas_alloc_amount(self):
        return self._pre_saas_alloc_amount

    @pre_saas_alloc_amount.setter
    def pre_saas_alloc_amount(self, value):
        self._pre_saas_alloc_amount = value
    @property
    def pre_user_fund_amount(self):
        return self._pre_user_fund_amount

    @pre_user_fund_amount.setter
    def pre_user_fund_amount(self, value):
        self._pre_user_fund_amount = value
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
    def real_receipt_amount(self):
        return self._real_receipt_amount

    @real_receipt_amount.setter
    def real_receipt_amount(self, value):
        self._real_receipt_amount = value
    @property
    def refund_fee(self):
        return self._refund_fee

    @refund_fee.setter
    def refund_fee(self, value):
        self._refund_fee = value
    @property
    def refund_isv_alloc_amount(self):
        return self._refund_isv_alloc_amount

    @refund_isv_alloc_amount.setter
    def refund_isv_alloc_amount(self, value):
        self._refund_isv_alloc_amount = value
    @property
    def refund_merchant_discount_amount(self):
        return self._refund_merchant_discount_amount

    @refund_merchant_discount_amount.setter
    def refund_merchant_discount_amount(self, value):
        self._refund_merchant_discount_amount = value
    @property
    def refund_pay_commission(self):
        return self._refund_pay_commission

    @refund_pay_commission.setter
    def refund_pay_commission(self, value):
        self._refund_pay_commission = value
    @property
    def refund_platform_discount_amount(self):
        return self._refund_platform_discount_amount

    @refund_platform_discount_amount.setter
    def refund_platform_discount_amount(self, value):
        self._refund_platform_discount_amount = value
    @property
    def refund_public_alloc_amount(self):
        return self._refund_public_alloc_amount

    @refund_public_alloc_amount.setter
    def refund_public_alloc_amount(self, value):
        self._refund_public_alloc_amount = value
    @property
    def refund_saas_alloc_amount(self):
        return self._refund_saas_alloc_amount

    @refund_saas_alloc_amount.setter
    def refund_saas_alloc_amount(self, value):
        self._refund_saas_alloc_amount = value
    @property
    def refund_service_amount(self):
        return self._refund_service_amount

    @refund_service_amount.setter
    def refund_service_amount(self, value):
        self._refund_service_amount = value
    @property
    def saas_alloc_amount(self):
        return self._saas_alloc_amount

    @saas_alloc_amount.setter
    def saas_alloc_amount(self, value):
        self._saas_alloc_amount = value
    @property
    def saas_name(self):
        return self._saas_name

    @saas_name.setter
    def saas_name(self, value):
        self._saas_name = value
    @property
    def self_shop_name(self):
        return self._self_shop_name

    @self_shop_name.setter
    def self_shop_name(self, value):
        self._self_shop_name = value
    @property
    def serial_no(self):
        return self._serial_no

    @serial_no.setter
    def serial_no(self, value):
        self._serial_no = value
    @property
    def service_amount(self):
        return self._service_amount

    @service_amount.setter
    def service_amount(self, value):
        self._service_amount = value
    @property
    def settle_account_no(self):
        return self._settle_account_no

    @settle_account_no.setter
    def settle_account_no(self, value):
        self._settle_account_no = value
    @property
    def settle_account_type(self):
        return self._settle_account_type

    @settle_account_type.setter
    def settle_account_type(self, value):
        self._settle_account_type = value
    @property
    def settle_amount(self):
        return self._settle_amount

    @settle_amount.setter
    def settle_amount(self, value):
        self._settle_amount = value
    @property
    def settle_batch_id(self):
        return self._settle_batch_id

    @settle_batch_id.setter
    def settle_batch_id(self, value):
        self._settle_batch_id = value
    @property
    def settle_rel_shop_id(self):
        return self._settle_rel_shop_id

    @settle_rel_shop_id.setter
    def settle_rel_shop_id(self, value):
        self._settle_rel_shop_id = value
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
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value
    @property
    def use_user_name(self):
        return self._use_user_name

    @use_user_name.setter
    def use_user_name(self, value):
        self._use_user_name = value
    @property
    def user_fund_amount(self):
        return self._user_fund_amount

    @user_fund_amount.setter
    def user_fund_amount(self, value):
        self._user_fund_amount = value
    @property
    def verification_shop_id(self):
        return self._verification_shop_id

    @verification_shop_id.setter
    def verification_shop_id(self, value):
        self._verification_shop_id = value
    @property
    def verification_shop_name(self):
        return self._verification_shop_name

    @verification_shop_name.setter
    def verification_shop_name(self, value):
        self._verification_shop_name = value
    @property
    def verification_time(self):
        return self._verification_time

    @verification_time.setter
    def verification_time(self, value):
        self._verification_time = value
    @property
    def verification_trade_no(self):
        return self._verification_trade_no

    @verification_trade_no.setter
    def verification_trade_no(self, value):
        self._verification_trade_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.certificate_id:
            if hasattr(self.certificate_id, 'to_alipay_dict'):
                params['certificate_id'] = self.certificate_id.to_alipay_dict()
            else:
                params['certificate_id'] = self.certificate_id
        if self.certificate_price:
            if hasattr(self.certificate_price, 'to_alipay_dict'):
                params['certificate_price'] = self.certificate_price.to_alipay_dict()
            else:
                params['certificate_price'] = self.certificate_price
        if self.certificate_status:
            if hasattr(self.certificate_status, 'to_alipay_dict'):
                params['certificate_status'] = self.certificate_status.to_alipay_dict()
            else:
                params['certificate_status'] = self.certificate_status
        if self.fee_category:
            if hasattr(self.fee_category, 'to_alipay_dict'):
                params['fee_category'] = self.fee_category.to_alipay_dict()
            else:
                params['fee_category'] = self.fee_category
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
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.item_type:
            if hasattr(self.item_type, 'to_alipay_dict'):
                params['item_type'] = self.item_type.to_alipay_dict()
            else:
                params['item_type'] = self.item_type
        if self.merchant_discount_amount:
            if hasattr(self.merchant_discount_amount, 'to_alipay_dict'):
                params['merchant_discount_amount'] = self.merchant_discount_amount.to_alipay_dict()
            else:
                params['merchant_discount_amount'] = self.merchant_discount_amount
        if self.merchant_verification_no:
            if hasattr(self.merchant_verification_no, 'to_alipay_dict'):
                params['merchant_verification_no'] = self.merchant_verification_no.to_alipay_dict()
            else:
                params['merchant_verification_no'] = self.merchant_verification_no
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
        if self.order_scene:
            if hasattr(self.order_scene, 'to_alipay_dict'):
                params['order_scene'] = self.order_scene.to_alipay_dict()
            else:
                params['order_scene'] = self.order_scene
        if self.original_price:
            if hasattr(self.original_price, 'to_alipay_dict'):
                params['original_price'] = self.original_price.to_alipay_dict()
            else:
                params['original_price'] = self.original_price
        if self.pay_commission:
            if hasattr(self.pay_commission, 'to_alipay_dict'):
                params['pay_commission'] = self.pay_commission.to_alipay_dict()
            else:
                params['pay_commission'] = self.pay_commission
        if self.pay_discounted_price:
            if hasattr(self.pay_discounted_price, 'to_alipay_dict'):
                params['pay_discounted_price'] = self.pay_discounted_price.to_alipay_dict()
            else:
                params['pay_discounted_price'] = self.pay_discounted_price
        if self.platform_discount_amount:
            if hasattr(self.platform_discount_amount, 'to_alipay_dict'):
                params['platform_discount_amount'] = self.platform_discount_amount.to_alipay_dict()
            else:
                params['platform_discount_amount'] = self.platform_discount_amount
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
        if self.pre_cps_amount:
            if hasattr(self.pre_cps_amount, 'to_alipay_dict'):
                params['pre_cps_amount'] = self.pre_cps_amount.to_alipay_dict()
            else:
                params['pre_cps_amount'] = self.pre_cps_amount
        if self.pre_isv_alloc_amount:
            if hasattr(self.pre_isv_alloc_amount, 'to_alipay_dict'):
                params['pre_isv_alloc_amount'] = self.pre_isv_alloc_amount.to_alipay_dict()
            else:
                params['pre_isv_alloc_amount'] = self.pre_isv_alloc_amount
        if self.pre_merchant_discount_amount:
            if hasattr(self.pre_merchant_discount_amount, 'to_alipay_dict'):
                params['pre_merchant_discount_amount'] = self.pre_merchant_discount_amount.to_alipay_dict()
            else:
                params['pre_merchant_discount_amount'] = self.pre_merchant_discount_amount
        if self.pre_pay_commission:
            if hasattr(self.pre_pay_commission, 'to_alipay_dict'):
                params['pre_pay_commission'] = self.pre_pay_commission.to_alipay_dict()
            else:
                params['pre_pay_commission'] = self.pre_pay_commission
        if self.pre_platform_discount_amount:
            if hasattr(self.pre_platform_discount_amount, 'to_alipay_dict'):
                params['pre_platform_discount_amount'] = self.pre_platform_discount_amount.to_alipay_dict()
            else:
                params['pre_platform_discount_amount'] = self.pre_platform_discount_amount
        if self.pre_public_alloc_amount:
            if hasattr(self.pre_public_alloc_amount, 'to_alipay_dict'):
                params['pre_public_alloc_amount'] = self.pre_public_alloc_amount.to_alipay_dict()
            else:
                params['pre_public_alloc_amount'] = self.pre_public_alloc_amount
        if self.pre_saas_alloc_amount:
            if hasattr(self.pre_saas_alloc_amount, 'to_alipay_dict'):
                params['pre_saas_alloc_amount'] = self.pre_saas_alloc_amount.to_alipay_dict()
            else:
                params['pre_saas_alloc_amount'] = self.pre_saas_alloc_amount
        if self.pre_user_fund_amount:
            if hasattr(self.pre_user_fund_amount, 'to_alipay_dict'):
                params['pre_user_fund_amount'] = self.pre_user_fund_amount.to_alipay_dict()
            else:
                params['pre_user_fund_amount'] = self.pre_user_fund_amount
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
        if self.real_receipt_amount:
            if hasattr(self.real_receipt_amount, 'to_alipay_dict'):
                params['real_receipt_amount'] = self.real_receipt_amount.to_alipay_dict()
            else:
                params['real_receipt_amount'] = self.real_receipt_amount
        if self.refund_fee:
            if hasattr(self.refund_fee, 'to_alipay_dict'):
                params['refund_fee'] = self.refund_fee.to_alipay_dict()
            else:
                params['refund_fee'] = self.refund_fee
        if self.refund_isv_alloc_amount:
            if hasattr(self.refund_isv_alloc_amount, 'to_alipay_dict'):
                params['refund_isv_alloc_amount'] = self.refund_isv_alloc_amount.to_alipay_dict()
            else:
                params['refund_isv_alloc_amount'] = self.refund_isv_alloc_amount
        if self.refund_merchant_discount_amount:
            if hasattr(self.refund_merchant_discount_amount, 'to_alipay_dict'):
                params['refund_merchant_discount_amount'] = self.refund_merchant_discount_amount.to_alipay_dict()
            else:
                params['refund_merchant_discount_amount'] = self.refund_merchant_discount_amount
        if self.refund_pay_commission:
            if hasattr(self.refund_pay_commission, 'to_alipay_dict'):
                params['refund_pay_commission'] = self.refund_pay_commission.to_alipay_dict()
            else:
                params['refund_pay_commission'] = self.refund_pay_commission
        if self.refund_platform_discount_amount:
            if hasattr(self.refund_platform_discount_amount, 'to_alipay_dict'):
                params['refund_platform_discount_amount'] = self.refund_platform_discount_amount.to_alipay_dict()
            else:
                params['refund_platform_discount_amount'] = self.refund_platform_discount_amount
        if self.refund_public_alloc_amount:
            if hasattr(self.refund_public_alloc_amount, 'to_alipay_dict'):
                params['refund_public_alloc_amount'] = self.refund_public_alloc_amount.to_alipay_dict()
            else:
                params['refund_public_alloc_amount'] = self.refund_public_alloc_amount
        if self.refund_saas_alloc_amount:
            if hasattr(self.refund_saas_alloc_amount, 'to_alipay_dict'):
                params['refund_saas_alloc_amount'] = self.refund_saas_alloc_amount.to_alipay_dict()
            else:
                params['refund_saas_alloc_amount'] = self.refund_saas_alloc_amount
        if self.refund_service_amount:
            if hasattr(self.refund_service_amount, 'to_alipay_dict'):
                params['refund_service_amount'] = self.refund_service_amount.to_alipay_dict()
            else:
                params['refund_service_amount'] = self.refund_service_amount
        if self.saas_alloc_amount:
            if hasattr(self.saas_alloc_amount, 'to_alipay_dict'):
                params['saas_alloc_amount'] = self.saas_alloc_amount.to_alipay_dict()
            else:
                params['saas_alloc_amount'] = self.saas_alloc_amount
        if self.saas_name:
            if hasattr(self.saas_name, 'to_alipay_dict'):
                params['saas_name'] = self.saas_name.to_alipay_dict()
            else:
                params['saas_name'] = self.saas_name
        if self.self_shop_name:
            if hasattr(self.self_shop_name, 'to_alipay_dict'):
                params['self_shop_name'] = self.self_shop_name.to_alipay_dict()
            else:
                params['self_shop_name'] = self.self_shop_name
        if self.serial_no:
            if hasattr(self.serial_no, 'to_alipay_dict'):
                params['serial_no'] = self.serial_no.to_alipay_dict()
            else:
                params['serial_no'] = self.serial_no
        if self.service_amount:
            if hasattr(self.service_amount, 'to_alipay_dict'):
                params['service_amount'] = self.service_amount.to_alipay_dict()
            else:
                params['service_amount'] = self.service_amount
        if self.settle_account_no:
            if hasattr(self.settle_account_no, 'to_alipay_dict'):
                params['settle_account_no'] = self.settle_account_no.to_alipay_dict()
            else:
                params['settle_account_no'] = self.settle_account_no
        if self.settle_account_type:
            if hasattr(self.settle_account_type, 'to_alipay_dict'):
                params['settle_account_type'] = self.settle_account_type.to_alipay_dict()
            else:
                params['settle_account_type'] = self.settle_account_type
        if self.settle_amount:
            if hasattr(self.settle_amount, 'to_alipay_dict'):
                params['settle_amount'] = self.settle_amount.to_alipay_dict()
            else:
                params['settle_amount'] = self.settle_amount
        if self.settle_batch_id:
            if hasattr(self.settle_batch_id, 'to_alipay_dict'):
                params['settle_batch_id'] = self.settle_batch_id.to_alipay_dict()
            else:
                params['settle_batch_id'] = self.settle_batch_id
        if self.settle_rel_shop_id:
            if hasattr(self.settle_rel_shop_id, 'to_alipay_dict'):
                params['settle_rel_shop_id'] = self.settle_rel_shop_id.to_alipay_dict()
            else:
                params['settle_rel_shop_id'] = self.settle_rel_shop_id
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
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        if self.use_user_name:
            if hasattr(self.use_user_name, 'to_alipay_dict'):
                params['use_user_name'] = self.use_user_name.to_alipay_dict()
            else:
                params['use_user_name'] = self.use_user_name
        if self.user_fund_amount:
            if hasattr(self.user_fund_amount, 'to_alipay_dict'):
                params['user_fund_amount'] = self.user_fund_amount.to_alipay_dict()
            else:
                params['user_fund_amount'] = self.user_fund_amount
        if self.verification_shop_id:
            if hasattr(self.verification_shop_id, 'to_alipay_dict'):
                params['verification_shop_id'] = self.verification_shop_id.to_alipay_dict()
            else:
                params['verification_shop_id'] = self.verification_shop_id
        if self.verification_shop_name:
            if hasattr(self.verification_shop_name, 'to_alipay_dict'):
                params['verification_shop_name'] = self.verification_shop_name.to_alipay_dict()
            else:
                params['verification_shop_name'] = self.verification_shop_name
        if self.verification_time:
            if hasattr(self.verification_time, 'to_alipay_dict'):
                params['verification_time'] = self.verification_time.to_alipay_dict()
            else:
                params['verification_time'] = self.verification_time
        if self.verification_trade_no:
            if hasattr(self.verification_trade_no, 'to_alipay_dict'):
                params['verification_trade_no'] = self.verification_trade_no.to_alipay_dict()
            else:
                params['verification_trade_no'] = self.verification_trade_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SelfItemOrderBillDetailResponse()
        if 'certificate_id' in d:
            o.certificate_id = d['certificate_id']
        if 'certificate_price' in d:
            o.certificate_price = d['certificate_price']
        if 'certificate_status' in d:
            o.certificate_status = d['certificate_status']
        if 'fee_category' in d:
            o.fee_category = d['fee_category']
        if 'isv_alloc_amount' in d:
            o.isv_alloc_amount = d['isv_alloc_amount']
        if 'isv_name' in d:
            o.isv_name = d['isv_name']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'item_type' in d:
            o.item_type = d['item_type']
        if 'merchant_discount_amount' in d:
            o.merchant_discount_amount = d['merchant_discount_amount']
        if 'merchant_verification_no' in d:
            o.merchant_verification_no = d['merchant_verification_no']
        if 'mini_app_id' in d:
            o.mini_app_id = d['mini_app_id']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'order_scene' in d:
            o.order_scene = d['order_scene']
        if 'original_price' in d:
            o.original_price = d['original_price']
        if 'pay_commission' in d:
            o.pay_commission = d['pay_commission']
        if 'pay_discounted_price' in d:
            o.pay_discounted_price = d['pay_discounted_price']
        if 'platform_discount_amount' in d:
            o.platform_discount_amount = d['platform_discount_amount']
        if 'platform_service' in d:
            o.platform_service = d['platform_service']
        if 'platform_service_refund' in d:
            o.platform_service_refund = d['platform_service_refund']
        if 'pre_cps_amount' in d:
            o.pre_cps_amount = d['pre_cps_amount']
        if 'pre_isv_alloc_amount' in d:
            o.pre_isv_alloc_amount = d['pre_isv_alloc_amount']
        if 'pre_merchant_discount_amount' in d:
            o.pre_merchant_discount_amount = d['pre_merchant_discount_amount']
        if 'pre_pay_commission' in d:
            o.pre_pay_commission = d['pre_pay_commission']
        if 'pre_platform_discount_amount' in d:
            o.pre_platform_discount_amount = d['pre_platform_discount_amount']
        if 'pre_public_alloc_amount' in d:
            o.pre_public_alloc_amount = d['pre_public_alloc_amount']
        if 'pre_saas_alloc_amount' in d:
            o.pre_saas_alloc_amount = d['pre_saas_alloc_amount']
        if 'pre_user_fund_amount' in d:
            o.pre_user_fund_amount = d['pre_user_fund_amount']
        if 'predict_settle_time' in d:
            o.predict_settle_time = d['predict_settle_time']
        if 'public_alloc_amount' in d:
            o.public_alloc_amount = d['public_alloc_amount']
        if 'public_name' in d:
            o.public_name = d['public_name']
        if 'real_receipt_amount' in d:
            o.real_receipt_amount = d['real_receipt_amount']
        if 'refund_fee' in d:
            o.refund_fee = d['refund_fee']
        if 'refund_isv_alloc_amount' in d:
            o.refund_isv_alloc_amount = d['refund_isv_alloc_amount']
        if 'refund_merchant_discount_amount' in d:
            o.refund_merchant_discount_amount = d['refund_merchant_discount_amount']
        if 'refund_pay_commission' in d:
            o.refund_pay_commission = d['refund_pay_commission']
        if 'refund_platform_discount_amount' in d:
            o.refund_platform_discount_amount = d['refund_platform_discount_amount']
        if 'refund_public_alloc_amount' in d:
            o.refund_public_alloc_amount = d['refund_public_alloc_amount']
        if 'refund_saas_alloc_amount' in d:
            o.refund_saas_alloc_amount = d['refund_saas_alloc_amount']
        if 'refund_service_amount' in d:
            o.refund_service_amount = d['refund_service_amount']
        if 'saas_alloc_amount' in d:
            o.saas_alloc_amount = d['saas_alloc_amount']
        if 'saas_name' in d:
            o.saas_name = d['saas_name']
        if 'self_shop_name' in d:
            o.self_shop_name = d['self_shop_name']
        if 'serial_no' in d:
            o.serial_no = d['serial_no']
        if 'service_amount' in d:
            o.service_amount = d['service_amount']
        if 'settle_account_no' in d:
            o.settle_account_no = d['settle_account_no']
        if 'settle_account_type' in d:
            o.settle_account_type = d['settle_account_type']
        if 'settle_amount' in d:
            o.settle_amount = d['settle_amount']
        if 'settle_batch_id' in d:
            o.settle_batch_id = d['settle_batch_id']
        if 'settle_rel_shop_id' in d:
            o.settle_rel_shop_id = d['settle_rel_shop_id']
        if 'settle_status' in d:
            o.settle_status = d['settle_status']
        if 'settle_time' in d:
            o.settle_time = d['settle_time']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        if 'use_user_name' in d:
            o.use_user_name = d['use_user_name']
        if 'user_fund_amount' in d:
            o.user_fund_amount = d['user_fund_amount']
        if 'verification_shop_id' in d:
            o.verification_shop_id = d['verification_shop_id']
        if 'verification_shop_name' in d:
            o.verification_shop_name = d['verification_shop_name']
        if 'verification_time' in d:
            o.verification_time = d['verification_time']
        if 'verification_trade_no' in d:
            o.verification_trade_no = d['verification_trade_no']
        return o


