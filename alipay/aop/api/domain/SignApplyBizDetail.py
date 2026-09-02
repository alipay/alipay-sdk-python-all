#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SignApplyBizDetail(object):

    def __init__(self):
        self._back_addr = None
        self._custtype = None
        self._freeze_amount = None
        self._goods_name = None
        self._id_number = None
        self._mobile_no = None
        self._pack_id = None
        self._pack_name = None
        self._pack_price = None
        self._principal = None
        self._province = None
        self._repayments = None
        self._request_no = None
        self._social_credit_code = None
        self._store_address = None
        self._store_id = None
        self._store_name = None
        self._user_name = None

    @property
    def back_addr(self):
        return self._back_addr

    @back_addr.setter
    def back_addr(self, value):
        self._back_addr = value
    @property
    def custtype(self):
        return self._custtype

    @custtype.setter
    def custtype(self, value):
        self._custtype = value
    @property
    def freeze_amount(self):
        return self._freeze_amount

    @freeze_amount.setter
    def freeze_amount(self, value):
        self._freeze_amount = value
    @property
    def goods_name(self):
        return self._goods_name

    @goods_name.setter
    def goods_name(self, value):
        self._goods_name = value
    @property
    def id_number(self):
        return self._id_number

    @id_number.setter
    def id_number(self, value):
        self._id_number = value
    @property
    def mobile_no(self):
        return self._mobile_no

    @mobile_no.setter
    def mobile_no(self, value):
        self._mobile_no = value
    @property
    def pack_id(self):
        return self._pack_id

    @pack_id.setter
    def pack_id(self, value):
        self._pack_id = value
    @property
    def pack_name(self):
        return self._pack_name

    @pack_name.setter
    def pack_name(self, value):
        self._pack_name = value
    @property
    def pack_price(self):
        return self._pack_price

    @pack_price.setter
    def pack_price(self, value):
        self._pack_price = value
    @property
    def principal(self):
        return self._principal

    @principal.setter
    def principal(self, value):
        self._principal = value
    @property
    def province(self):
        return self._province

    @province.setter
    def province(self, value):
        self._province = value
    @property
    def repayments(self):
        return self._repayments

    @repayments.setter
    def repayments(self, value):
        self._repayments = value
    @property
    def request_no(self):
        return self._request_no

    @request_no.setter
    def request_no(self, value):
        self._request_no = value
    @property
    def social_credit_code(self):
        return self._social_credit_code

    @social_credit_code.setter
    def social_credit_code(self, value):
        self._social_credit_code = value
    @property
    def store_address(self):
        return self._store_address

    @store_address.setter
    def store_address(self, value):
        self._store_address = value
    @property
    def store_id(self):
        return self._store_id

    @store_id.setter
    def store_id(self, value):
        self._store_id = value
    @property
    def store_name(self):
        return self._store_name

    @store_name.setter
    def store_name(self, value):
        self._store_name = value
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.back_addr:
            if hasattr(self.back_addr, 'to_alipay_dict'):
                params['back_addr'] = self.back_addr.to_alipay_dict()
            else:
                params['back_addr'] = self.back_addr
        if self.custtype:
            if hasattr(self.custtype, 'to_alipay_dict'):
                params['custtype'] = self.custtype.to_alipay_dict()
            else:
                params['custtype'] = self.custtype
        if self.freeze_amount:
            if hasattr(self.freeze_amount, 'to_alipay_dict'):
                params['freeze_amount'] = self.freeze_amount.to_alipay_dict()
            else:
                params['freeze_amount'] = self.freeze_amount
        if self.goods_name:
            if hasattr(self.goods_name, 'to_alipay_dict'):
                params['goods_name'] = self.goods_name.to_alipay_dict()
            else:
                params['goods_name'] = self.goods_name
        if self.id_number:
            if hasattr(self.id_number, 'to_alipay_dict'):
                params['id_number'] = self.id_number.to_alipay_dict()
            else:
                params['id_number'] = self.id_number
        if self.mobile_no:
            if hasattr(self.mobile_no, 'to_alipay_dict'):
                params['mobile_no'] = self.mobile_no.to_alipay_dict()
            else:
                params['mobile_no'] = self.mobile_no
        if self.pack_id:
            if hasattr(self.pack_id, 'to_alipay_dict'):
                params['pack_id'] = self.pack_id.to_alipay_dict()
            else:
                params['pack_id'] = self.pack_id
        if self.pack_name:
            if hasattr(self.pack_name, 'to_alipay_dict'):
                params['pack_name'] = self.pack_name.to_alipay_dict()
            else:
                params['pack_name'] = self.pack_name
        if self.pack_price:
            if hasattr(self.pack_price, 'to_alipay_dict'):
                params['pack_price'] = self.pack_price.to_alipay_dict()
            else:
                params['pack_price'] = self.pack_price
        if self.principal:
            if hasattr(self.principal, 'to_alipay_dict'):
                params['principal'] = self.principal.to_alipay_dict()
            else:
                params['principal'] = self.principal
        if self.province:
            if hasattr(self.province, 'to_alipay_dict'):
                params['province'] = self.province.to_alipay_dict()
            else:
                params['province'] = self.province
        if self.repayments:
            if hasattr(self.repayments, 'to_alipay_dict'):
                params['repayments'] = self.repayments.to_alipay_dict()
            else:
                params['repayments'] = self.repayments
        if self.request_no:
            if hasattr(self.request_no, 'to_alipay_dict'):
                params['request_no'] = self.request_no.to_alipay_dict()
            else:
                params['request_no'] = self.request_no
        if self.social_credit_code:
            if hasattr(self.social_credit_code, 'to_alipay_dict'):
                params['social_credit_code'] = self.social_credit_code.to_alipay_dict()
            else:
                params['social_credit_code'] = self.social_credit_code
        if self.store_address:
            if hasattr(self.store_address, 'to_alipay_dict'):
                params['store_address'] = self.store_address.to_alipay_dict()
            else:
                params['store_address'] = self.store_address
        if self.store_id:
            if hasattr(self.store_id, 'to_alipay_dict'):
                params['store_id'] = self.store_id.to_alipay_dict()
            else:
                params['store_id'] = self.store_id
        if self.store_name:
            if hasattr(self.store_name, 'to_alipay_dict'):
                params['store_name'] = self.store_name.to_alipay_dict()
            else:
                params['store_name'] = self.store_name
        if self.user_name:
            if hasattr(self.user_name, 'to_alipay_dict'):
                params['user_name'] = self.user_name.to_alipay_dict()
            else:
                params['user_name'] = self.user_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SignApplyBizDetail()
        if 'back_addr' in d:
            o.back_addr = d['back_addr']
        if 'custtype' in d:
            o.custtype = d['custtype']
        if 'freeze_amount' in d:
            o.freeze_amount = d['freeze_amount']
        if 'goods_name' in d:
            o.goods_name = d['goods_name']
        if 'id_number' in d:
            o.id_number = d['id_number']
        if 'mobile_no' in d:
            o.mobile_no = d['mobile_no']
        if 'pack_id' in d:
            o.pack_id = d['pack_id']
        if 'pack_name' in d:
            o.pack_name = d['pack_name']
        if 'pack_price' in d:
            o.pack_price = d['pack_price']
        if 'principal' in d:
            o.principal = d['principal']
        if 'province' in d:
            o.province = d['province']
        if 'repayments' in d:
            o.repayments = d['repayments']
        if 'request_no' in d:
            o.request_no = d['request_no']
        if 'social_credit_code' in d:
            o.social_credit_code = d['social_credit_code']
        if 'store_address' in d:
            o.store_address = d['store_address']
        if 'store_id' in d:
            o.store_id = d['store_id']
        if 'store_name' in d:
            o.store_name = d['store_name']
        if 'user_name' in d:
            o.user_name = d['user_name']
        return o


