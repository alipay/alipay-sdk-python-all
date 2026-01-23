#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SubsidyMoney import SubsidyMoney
from alipay.aop.api.domain.SubsidyMoney import SubsidyMoney


class SubsidySimpleRequest(object):

    def __init__(self):
        self._acquire_mode = None
        self._asset_type_code = None
        self._biz_identity = None
        self._buyer_user_id = None
        self._good_item_id = None
        self._install_nums = None
        self._installment_biz_info = None
        self._investor_id = None
        self._ipay_secmerchant = None
        self._merge_pay = None
        self._mshop_id = None
        self._order_amount = None
        self._original_mid = None
        self._original_seller_id = None
        self._out_order_no = None
        self._partner_id = None
        self._platform = None
        self._platform_type = None
        self._sales_product_code = None
        self._scene = None
        self._secondary_merchant_id = None
        self._seller_id = None
        self._store_id = None
        self._sub_platform_type = None
        self._subsidy_biz_code = None
        self._total_amount = None
        self._trade_no = None
        self._user_id = None

    @property
    def acquire_mode(self):
        return self._acquire_mode

    @acquire_mode.setter
    def acquire_mode(self, value):
        self._acquire_mode = value
    @property
    def asset_type_code(self):
        return self._asset_type_code

    @asset_type_code.setter
    def asset_type_code(self, value):
        self._asset_type_code = value
    @property
    def biz_identity(self):
        return self._biz_identity

    @biz_identity.setter
    def biz_identity(self, value):
        self._biz_identity = value
    @property
    def buyer_user_id(self):
        return self._buyer_user_id

    @buyer_user_id.setter
    def buyer_user_id(self, value):
        self._buyer_user_id = value
    @property
    def good_item_id(self):
        return self._good_item_id

    @good_item_id.setter
    def good_item_id(self, value):
        self._good_item_id = value
    @property
    def install_nums(self):
        return self._install_nums

    @install_nums.setter
    def install_nums(self, value):
        if isinstance(value, list):
            self._install_nums = list()
            for i in value:
                self._install_nums.append(i)
    @property
    def installment_biz_info(self):
        return self._installment_biz_info

    @installment_biz_info.setter
    def installment_biz_info(self, value):
        self._installment_biz_info = value
    @property
    def investor_id(self):
        return self._investor_id

    @investor_id.setter
    def investor_id(self, value):
        self._investor_id = value
    @property
    def ipay_secmerchant(self):
        return self._ipay_secmerchant

    @ipay_secmerchant.setter
    def ipay_secmerchant(self, value):
        self._ipay_secmerchant = value
    @property
    def merge_pay(self):
        return self._merge_pay

    @merge_pay.setter
    def merge_pay(self, value):
        self._merge_pay = value
    @property
    def mshop_id(self):
        return self._mshop_id

    @mshop_id.setter
    def mshop_id(self, value):
        self._mshop_id = value
    @property
    def order_amount(self):
        return self._order_amount

    @order_amount.setter
    def order_amount(self, value):
        if isinstance(value, SubsidyMoney):
            self._order_amount = value
        else:
            self._order_amount = SubsidyMoney.from_alipay_dict(value)
    @property
    def original_mid(self):
        return self._original_mid

    @original_mid.setter
    def original_mid(self, value):
        self._original_mid = value
    @property
    def original_seller_id(self):
        return self._original_seller_id

    @original_seller_id.setter
    def original_seller_id(self, value):
        self._original_seller_id = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def platform(self):
        return self._platform

    @platform.setter
    def platform(self, value):
        self._platform = value
    @property
    def platform_type(self):
        return self._platform_type

    @platform_type.setter
    def platform_type(self, value):
        self._platform_type = value
    @property
    def sales_product_code(self):
        return self._sales_product_code

    @sales_product_code.setter
    def sales_product_code(self, value):
        self._sales_product_code = value
    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value
    @property
    def secondary_merchant_id(self):
        return self._secondary_merchant_id

    @secondary_merchant_id.setter
    def secondary_merchant_id(self, value):
        self._secondary_merchant_id = value
    @property
    def seller_id(self):
        return self._seller_id

    @seller_id.setter
    def seller_id(self, value):
        self._seller_id = value
    @property
    def store_id(self):
        return self._store_id

    @store_id.setter
    def store_id(self, value):
        self._store_id = value
    @property
    def sub_platform_type(self):
        return self._sub_platform_type

    @sub_platform_type.setter
    def sub_platform_type(self, value):
        self._sub_platform_type = value
    @property
    def subsidy_biz_code(self):
        return self._subsidy_biz_code

    @subsidy_biz_code.setter
    def subsidy_biz_code(self, value):
        self._subsidy_biz_code = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        if isinstance(value, SubsidyMoney):
            self._total_amount = value
        else:
            self._total_amount = SubsidyMoney.from_alipay_dict(value)
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.acquire_mode:
            if hasattr(self.acquire_mode, 'to_alipay_dict'):
                params['acquire_mode'] = self.acquire_mode.to_alipay_dict()
            else:
                params['acquire_mode'] = self.acquire_mode
        if self.asset_type_code:
            if hasattr(self.asset_type_code, 'to_alipay_dict'):
                params['asset_type_code'] = self.asset_type_code.to_alipay_dict()
            else:
                params['asset_type_code'] = self.asset_type_code
        if self.biz_identity:
            if hasattr(self.biz_identity, 'to_alipay_dict'):
                params['biz_identity'] = self.biz_identity.to_alipay_dict()
            else:
                params['biz_identity'] = self.biz_identity
        if self.buyer_user_id:
            if hasattr(self.buyer_user_id, 'to_alipay_dict'):
                params['buyer_user_id'] = self.buyer_user_id.to_alipay_dict()
            else:
                params['buyer_user_id'] = self.buyer_user_id
        if self.good_item_id:
            if hasattr(self.good_item_id, 'to_alipay_dict'):
                params['good_item_id'] = self.good_item_id.to_alipay_dict()
            else:
                params['good_item_id'] = self.good_item_id
        if self.install_nums:
            if isinstance(self.install_nums, list):
                for i in range(0, len(self.install_nums)):
                    element = self.install_nums[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.install_nums[i] = element.to_alipay_dict()
            if hasattr(self.install_nums, 'to_alipay_dict'):
                params['install_nums'] = self.install_nums.to_alipay_dict()
            else:
                params['install_nums'] = self.install_nums
        if self.installment_biz_info:
            if hasattr(self.installment_biz_info, 'to_alipay_dict'):
                params['installment_biz_info'] = self.installment_biz_info.to_alipay_dict()
            else:
                params['installment_biz_info'] = self.installment_biz_info
        if self.investor_id:
            if hasattr(self.investor_id, 'to_alipay_dict'):
                params['investor_id'] = self.investor_id.to_alipay_dict()
            else:
                params['investor_id'] = self.investor_id
        if self.ipay_secmerchant:
            if hasattr(self.ipay_secmerchant, 'to_alipay_dict'):
                params['ipay_secmerchant'] = self.ipay_secmerchant.to_alipay_dict()
            else:
                params['ipay_secmerchant'] = self.ipay_secmerchant
        if self.merge_pay:
            if hasattr(self.merge_pay, 'to_alipay_dict'):
                params['merge_pay'] = self.merge_pay.to_alipay_dict()
            else:
                params['merge_pay'] = self.merge_pay
        if self.mshop_id:
            if hasattr(self.mshop_id, 'to_alipay_dict'):
                params['mshop_id'] = self.mshop_id.to_alipay_dict()
            else:
                params['mshop_id'] = self.mshop_id
        if self.order_amount:
            if hasattr(self.order_amount, 'to_alipay_dict'):
                params['order_amount'] = self.order_amount.to_alipay_dict()
            else:
                params['order_amount'] = self.order_amount
        if self.original_mid:
            if hasattr(self.original_mid, 'to_alipay_dict'):
                params['original_mid'] = self.original_mid.to_alipay_dict()
            else:
                params['original_mid'] = self.original_mid
        if self.original_seller_id:
            if hasattr(self.original_seller_id, 'to_alipay_dict'):
                params['original_seller_id'] = self.original_seller_id.to_alipay_dict()
            else:
                params['original_seller_id'] = self.original_seller_id
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        if self.platform:
            if hasattr(self.platform, 'to_alipay_dict'):
                params['platform'] = self.platform.to_alipay_dict()
            else:
                params['platform'] = self.platform
        if self.platform_type:
            if hasattr(self.platform_type, 'to_alipay_dict'):
                params['platform_type'] = self.platform_type.to_alipay_dict()
            else:
                params['platform_type'] = self.platform_type
        if self.sales_product_code:
            if hasattr(self.sales_product_code, 'to_alipay_dict'):
                params['sales_product_code'] = self.sales_product_code.to_alipay_dict()
            else:
                params['sales_product_code'] = self.sales_product_code
        if self.scene:
            if hasattr(self.scene, 'to_alipay_dict'):
                params['scene'] = self.scene.to_alipay_dict()
            else:
                params['scene'] = self.scene
        if self.secondary_merchant_id:
            if hasattr(self.secondary_merchant_id, 'to_alipay_dict'):
                params['secondary_merchant_id'] = self.secondary_merchant_id.to_alipay_dict()
            else:
                params['secondary_merchant_id'] = self.secondary_merchant_id
        if self.seller_id:
            if hasattr(self.seller_id, 'to_alipay_dict'):
                params['seller_id'] = self.seller_id.to_alipay_dict()
            else:
                params['seller_id'] = self.seller_id
        if self.store_id:
            if hasattr(self.store_id, 'to_alipay_dict'):
                params['store_id'] = self.store_id.to_alipay_dict()
            else:
                params['store_id'] = self.store_id
        if self.sub_platform_type:
            if hasattr(self.sub_platform_type, 'to_alipay_dict'):
                params['sub_platform_type'] = self.sub_platform_type.to_alipay_dict()
            else:
                params['sub_platform_type'] = self.sub_platform_type
        if self.subsidy_biz_code:
            if hasattr(self.subsidy_biz_code, 'to_alipay_dict'):
                params['subsidy_biz_code'] = self.subsidy_biz_code.to_alipay_dict()
            else:
                params['subsidy_biz_code'] = self.subsidy_biz_code
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
        o = SubsidySimpleRequest()
        if 'acquire_mode' in d:
            o.acquire_mode = d['acquire_mode']
        if 'asset_type_code' in d:
            o.asset_type_code = d['asset_type_code']
        if 'biz_identity' in d:
            o.biz_identity = d['biz_identity']
        if 'buyer_user_id' in d:
            o.buyer_user_id = d['buyer_user_id']
        if 'good_item_id' in d:
            o.good_item_id = d['good_item_id']
        if 'install_nums' in d:
            o.install_nums = d['install_nums']
        if 'installment_biz_info' in d:
            o.installment_biz_info = d['installment_biz_info']
        if 'investor_id' in d:
            o.investor_id = d['investor_id']
        if 'ipay_secmerchant' in d:
            o.ipay_secmerchant = d['ipay_secmerchant']
        if 'merge_pay' in d:
            o.merge_pay = d['merge_pay']
        if 'mshop_id' in d:
            o.mshop_id = d['mshop_id']
        if 'order_amount' in d:
            o.order_amount = d['order_amount']
        if 'original_mid' in d:
            o.original_mid = d['original_mid']
        if 'original_seller_id' in d:
            o.original_seller_id = d['original_seller_id']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'platform' in d:
            o.platform = d['platform']
        if 'platform_type' in d:
            o.platform_type = d['platform_type']
        if 'sales_product_code' in d:
            o.sales_product_code = d['sales_product_code']
        if 'scene' in d:
            o.scene = d['scene']
        if 'secondary_merchant_id' in d:
            o.secondary_merchant_id = d['secondary_merchant_id']
        if 'seller_id' in d:
            o.seller_id = d['seller_id']
        if 'store_id' in d:
            o.store_id = d['store_id']
        if 'sub_platform_type' in d:
            o.sub_platform_type = d['sub_platform_type']
        if 'subsidy_biz_code' in d:
            o.subsidy_biz_code = d['subsidy_biz_code']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


