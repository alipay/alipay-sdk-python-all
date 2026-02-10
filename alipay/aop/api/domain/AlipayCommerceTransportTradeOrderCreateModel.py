#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.WithholdingDetail import WithholdingDetail


class AlipayCommerceTransportTradeOrderCreateModel(object):

    def __init__(self):
        self._describe = None
        self._discountable_amount = None
        self._goods_name = None
        self._merchant_biz_type = None
        self._notify = None
        self._open_id = None
        self._out_biz_no = None
        self._out_sub_biz_no = None
        self._partner_unique_code = None
        self._portable = None
        self._price = None
        self._quantity = None
        self._smid = None
        self._sub_merchant_name = None
        self._sub_merchant_service_description = None
        self._sub_merchant_service_name = None
        self._subject = None
        self._total_amount = None
        self._undiscountable_amount = None
        self._user_id = None
        self._withholding_agreement_no = None
        self._withholding_detail = None

    @property
    def describe(self):
        return self._describe

    @describe.setter
    def describe(self, value):
        self._describe = value
    @property
    def discountable_amount(self):
        return self._discountable_amount

    @discountable_amount.setter
    def discountable_amount(self, value):
        self._discountable_amount = value
    @property
    def goods_name(self):
        return self._goods_name

    @goods_name.setter
    def goods_name(self, value):
        self._goods_name = value
    @property
    def merchant_biz_type(self):
        return self._merchant_biz_type

    @merchant_biz_type.setter
    def merchant_biz_type(self, value):
        self._merchant_biz_type = value
    @property
    def notify(self):
        return self._notify

    @notify.setter
    def notify(self, value):
        self._notify = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def out_sub_biz_no(self):
        return self._out_sub_biz_no

    @out_sub_biz_no.setter
    def out_sub_biz_no(self, value):
        self._out_sub_biz_no = value
    @property
    def partner_unique_code(self):
        return self._partner_unique_code

    @partner_unique_code.setter
    def partner_unique_code(self, value):
        self._partner_unique_code = value
    @property
    def portable(self):
        return self._portable

    @portable.setter
    def portable(self, value):
        self._portable = value
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value
    @property
    def smid(self):
        return self._smid

    @smid.setter
    def smid(self, value):
        self._smid = value
    @property
    def sub_merchant_name(self):
        return self._sub_merchant_name

    @sub_merchant_name.setter
    def sub_merchant_name(self, value):
        self._sub_merchant_name = value
    @property
    def sub_merchant_service_description(self):
        return self._sub_merchant_service_description

    @sub_merchant_service_description.setter
    def sub_merchant_service_description(self, value):
        self._sub_merchant_service_description = value
    @property
    def sub_merchant_service_name(self):
        return self._sub_merchant_service_name

    @sub_merchant_service_name.setter
    def sub_merchant_service_name(self, value):
        self._sub_merchant_service_name = value
    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, value):
        self._subject = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value
    @property
    def undiscountable_amount(self):
        return self._undiscountable_amount

    @undiscountable_amount.setter
    def undiscountable_amount(self, value):
        self._undiscountable_amount = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
    @property
    def withholding_agreement_no(self):
        return self._withholding_agreement_no

    @withholding_agreement_no.setter
    def withholding_agreement_no(self, value):
        self._withholding_agreement_no = value
    @property
    def withholding_detail(self):
        return self._withholding_detail

    @withholding_detail.setter
    def withholding_detail(self, value):
        if isinstance(value, WithholdingDetail):
            self._withholding_detail = value
        else:
            self._withholding_detail = WithholdingDetail.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.describe:
            if hasattr(self.describe, 'to_alipay_dict'):
                params['describe'] = self.describe.to_alipay_dict()
            else:
                params['describe'] = self.describe
        if self.discountable_amount:
            if hasattr(self.discountable_amount, 'to_alipay_dict'):
                params['discountable_amount'] = self.discountable_amount.to_alipay_dict()
            else:
                params['discountable_amount'] = self.discountable_amount
        if self.goods_name:
            if hasattr(self.goods_name, 'to_alipay_dict'):
                params['goods_name'] = self.goods_name.to_alipay_dict()
            else:
                params['goods_name'] = self.goods_name
        if self.merchant_biz_type:
            if hasattr(self.merchant_biz_type, 'to_alipay_dict'):
                params['merchant_biz_type'] = self.merchant_biz_type.to_alipay_dict()
            else:
                params['merchant_biz_type'] = self.merchant_biz_type
        if self.notify:
            if hasattr(self.notify, 'to_alipay_dict'):
                params['notify'] = self.notify.to_alipay_dict()
            else:
                params['notify'] = self.notify
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.out_sub_biz_no:
            if hasattr(self.out_sub_biz_no, 'to_alipay_dict'):
                params['out_sub_biz_no'] = self.out_sub_biz_no.to_alipay_dict()
            else:
                params['out_sub_biz_no'] = self.out_sub_biz_no
        if self.partner_unique_code:
            if hasattr(self.partner_unique_code, 'to_alipay_dict'):
                params['partner_unique_code'] = self.partner_unique_code.to_alipay_dict()
            else:
                params['partner_unique_code'] = self.partner_unique_code
        if self.portable:
            if hasattr(self.portable, 'to_alipay_dict'):
                params['portable'] = self.portable.to_alipay_dict()
            else:
                params['portable'] = self.portable
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
        if self.quantity:
            if hasattr(self.quantity, 'to_alipay_dict'):
                params['quantity'] = self.quantity.to_alipay_dict()
            else:
                params['quantity'] = self.quantity
        if self.smid:
            if hasattr(self.smid, 'to_alipay_dict'):
                params['smid'] = self.smid.to_alipay_dict()
            else:
                params['smid'] = self.smid
        if self.sub_merchant_name:
            if hasattr(self.sub_merchant_name, 'to_alipay_dict'):
                params['sub_merchant_name'] = self.sub_merchant_name.to_alipay_dict()
            else:
                params['sub_merchant_name'] = self.sub_merchant_name
        if self.sub_merchant_service_description:
            if hasattr(self.sub_merchant_service_description, 'to_alipay_dict'):
                params['sub_merchant_service_description'] = self.sub_merchant_service_description.to_alipay_dict()
            else:
                params['sub_merchant_service_description'] = self.sub_merchant_service_description
        if self.sub_merchant_service_name:
            if hasattr(self.sub_merchant_service_name, 'to_alipay_dict'):
                params['sub_merchant_service_name'] = self.sub_merchant_service_name.to_alipay_dict()
            else:
                params['sub_merchant_service_name'] = self.sub_merchant_service_name
        if self.subject:
            if hasattr(self.subject, 'to_alipay_dict'):
                params['subject'] = self.subject.to_alipay_dict()
            else:
                params['subject'] = self.subject
        if self.total_amount:
            if hasattr(self.total_amount, 'to_alipay_dict'):
                params['total_amount'] = self.total_amount.to_alipay_dict()
            else:
                params['total_amount'] = self.total_amount
        if self.undiscountable_amount:
            if hasattr(self.undiscountable_amount, 'to_alipay_dict'):
                params['undiscountable_amount'] = self.undiscountable_amount.to_alipay_dict()
            else:
                params['undiscountable_amount'] = self.undiscountable_amount
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        if self.withholding_agreement_no:
            if hasattr(self.withholding_agreement_no, 'to_alipay_dict'):
                params['withholding_agreement_no'] = self.withholding_agreement_no.to_alipay_dict()
            else:
                params['withholding_agreement_no'] = self.withholding_agreement_no
        if self.withholding_detail:
            if hasattr(self.withholding_detail, 'to_alipay_dict'):
                params['withholding_detail'] = self.withholding_detail.to_alipay_dict()
            else:
                params['withholding_detail'] = self.withholding_detail
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportTradeOrderCreateModel()
        if 'describe' in d:
            o.describe = d['describe']
        if 'discountable_amount' in d:
            o.discountable_amount = d['discountable_amount']
        if 'goods_name' in d:
            o.goods_name = d['goods_name']
        if 'merchant_biz_type' in d:
            o.merchant_biz_type = d['merchant_biz_type']
        if 'notify' in d:
            o.notify = d['notify']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'out_sub_biz_no' in d:
            o.out_sub_biz_no = d['out_sub_biz_no']
        if 'partner_unique_code' in d:
            o.partner_unique_code = d['partner_unique_code']
        if 'portable' in d:
            o.portable = d['portable']
        if 'price' in d:
            o.price = d['price']
        if 'quantity' in d:
            o.quantity = d['quantity']
        if 'smid' in d:
            o.smid = d['smid']
        if 'sub_merchant_name' in d:
            o.sub_merchant_name = d['sub_merchant_name']
        if 'sub_merchant_service_description' in d:
            o.sub_merchant_service_description = d['sub_merchant_service_description']
        if 'sub_merchant_service_name' in d:
            o.sub_merchant_service_name = d['sub_merchant_service_name']
        if 'subject' in d:
            o.subject = d['subject']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        if 'undiscountable_amount' in d:
            o.undiscountable_amount = d['undiscountable_amount']
        if 'user_id' in d:
            o.user_id = d['user_id']
        if 'withholding_agreement_no' in d:
            o.withholding_agreement_no = d['withholding_agreement_no']
        if 'withholding_detail' in d:
            o.withholding_detail = d['withholding_detail']
        return o


