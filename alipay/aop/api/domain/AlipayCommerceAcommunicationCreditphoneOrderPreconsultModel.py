#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceAcommunicationCreditphoneOrderPreconsultModel(object):

    def __init__(self):
        self._alipay_open_id = None
        self._alipay_user_id = None
        self._busi_level = None
        self._cert_no = None
        self._check_cert_no = None
        self._freeze_amount = None
        self._installment_numbers = None
        self._isp_abbr_cn = None
        self._item_name = None
        self._merchant_id = None
        self._merchant_name = None
        self._mobile = None
        self._province = None
        self._request_no = None
        self._spu_id = None
        self._user_name = None

    @property
    def alipay_open_id(self):
        return self._alipay_open_id

    @alipay_open_id.setter
    def alipay_open_id(self, value):
        self._alipay_open_id = value
    @property
    def alipay_user_id(self):
        return self._alipay_user_id

    @alipay_user_id.setter
    def alipay_user_id(self, value):
        self._alipay_user_id = value
    @property
    def busi_level(self):
        return self._busi_level

    @busi_level.setter
    def busi_level(self, value):
        self._busi_level = value
    @property
    def cert_no(self):
        return self._cert_no

    @cert_no.setter
    def cert_no(self, value):
        self._cert_no = value
    @property
    def check_cert_no(self):
        return self._check_cert_no

    @check_cert_no.setter
    def check_cert_no(self, value):
        self._check_cert_no = value
    @property
    def freeze_amount(self):
        return self._freeze_amount

    @freeze_amount.setter
    def freeze_amount(self, value):
        self._freeze_amount = value
    @property
    def installment_numbers(self):
        return self._installment_numbers

    @installment_numbers.setter
    def installment_numbers(self, value):
        self._installment_numbers = value
    @property
    def isp_abbr_cn(self):
        return self._isp_abbr_cn

    @isp_abbr_cn.setter
    def isp_abbr_cn(self, value):
        self._isp_abbr_cn = value
    @property
    def item_name(self):
        return self._item_name

    @item_name.setter
    def item_name(self, value):
        self._item_name = value
    @property
    def merchant_id(self):
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, value):
        self._merchant_id = value
    @property
    def merchant_name(self):
        return self._merchant_name

    @merchant_name.setter
    def merchant_name(self, value):
        self._merchant_name = value
    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, value):
        self._mobile = value
    @property
    def province(self):
        return self._province

    @province.setter
    def province(self, value):
        self._province = value
    @property
    def request_no(self):
        return self._request_no

    @request_no.setter
    def request_no(self, value):
        self._request_no = value
    @property
    def spu_id(self):
        return self._spu_id

    @spu_id.setter
    def spu_id(self, value):
        self._spu_id = value
    @property
    def user_name(self):
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        self._user_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.alipay_open_id:
            if hasattr(self.alipay_open_id, 'to_alipay_dict'):
                params['alipay_open_id'] = self.alipay_open_id.to_alipay_dict()
            else:
                params['alipay_open_id'] = self.alipay_open_id
        if self.alipay_user_id:
            if hasattr(self.alipay_user_id, 'to_alipay_dict'):
                params['alipay_user_id'] = self.alipay_user_id.to_alipay_dict()
            else:
                params['alipay_user_id'] = self.alipay_user_id
        if self.busi_level:
            if hasattr(self.busi_level, 'to_alipay_dict'):
                params['busi_level'] = self.busi_level.to_alipay_dict()
            else:
                params['busi_level'] = self.busi_level
        if self.cert_no:
            if hasattr(self.cert_no, 'to_alipay_dict'):
                params['cert_no'] = self.cert_no.to_alipay_dict()
            else:
                params['cert_no'] = self.cert_no
        if self.check_cert_no:
            if hasattr(self.check_cert_no, 'to_alipay_dict'):
                params['check_cert_no'] = self.check_cert_no.to_alipay_dict()
            else:
                params['check_cert_no'] = self.check_cert_no
        if self.freeze_amount:
            if hasattr(self.freeze_amount, 'to_alipay_dict'):
                params['freeze_amount'] = self.freeze_amount.to_alipay_dict()
            else:
                params['freeze_amount'] = self.freeze_amount
        if self.installment_numbers:
            if hasattr(self.installment_numbers, 'to_alipay_dict'):
                params['installment_numbers'] = self.installment_numbers.to_alipay_dict()
            else:
                params['installment_numbers'] = self.installment_numbers
        if self.isp_abbr_cn:
            if hasattr(self.isp_abbr_cn, 'to_alipay_dict'):
                params['isp_abbr_cn'] = self.isp_abbr_cn.to_alipay_dict()
            else:
                params['isp_abbr_cn'] = self.isp_abbr_cn
        if self.item_name:
            if hasattr(self.item_name, 'to_alipay_dict'):
                params['item_name'] = self.item_name.to_alipay_dict()
            else:
                params['item_name'] = self.item_name
        if self.merchant_id:
            if hasattr(self.merchant_id, 'to_alipay_dict'):
                params['merchant_id'] = self.merchant_id.to_alipay_dict()
            else:
                params['merchant_id'] = self.merchant_id
        if self.merchant_name:
            if hasattr(self.merchant_name, 'to_alipay_dict'):
                params['merchant_name'] = self.merchant_name.to_alipay_dict()
            else:
                params['merchant_name'] = self.merchant_name
        if self.mobile:
            if hasattr(self.mobile, 'to_alipay_dict'):
                params['mobile'] = self.mobile.to_alipay_dict()
            else:
                params['mobile'] = self.mobile
        if self.province:
            if hasattr(self.province, 'to_alipay_dict'):
                params['province'] = self.province.to_alipay_dict()
            else:
                params['province'] = self.province
        if self.request_no:
            if hasattr(self.request_no, 'to_alipay_dict'):
                params['request_no'] = self.request_no.to_alipay_dict()
            else:
                params['request_no'] = self.request_no
        if self.spu_id:
            if hasattr(self.spu_id, 'to_alipay_dict'):
                params['spu_id'] = self.spu_id.to_alipay_dict()
            else:
                params['spu_id'] = self.spu_id
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
        o = AlipayCommerceAcommunicationCreditphoneOrderPreconsultModel()
        if 'alipay_open_id' in d:
            o.alipay_open_id = d['alipay_open_id']
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'busi_level' in d:
            o.busi_level = d['busi_level']
        if 'cert_no' in d:
            o.cert_no = d['cert_no']
        if 'check_cert_no' in d:
            o.check_cert_no = d['check_cert_no']
        if 'freeze_amount' in d:
            o.freeze_amount = d['freeze_amount']
        if 'installment_numbers' in d:
            o.installment_numbers = d['installment_numbers']
        if 'isp_abbr_cn' in d:
            o.isp_abbr_cn = d['isp_abbr_cn']
        if 'item_name' in d:
            o.item_name = d['item_name']
        if 'merchant_id' in d:
            o.merchant_id = d['merchant_id']
        if 'merchant_name' in d:
            o.merchant_name = d['merchant_name']
        if 'mobile' in d:
            o.mobile = d['mobile']
        if 'province' in d:
            o.province = d['province']
        if 'request_no' in d:
            o.request_no = d['request_no']
        if 'spu_id' in d:
            o.spu_id = d['spu_id']
        if 'user_name' in d:
            o.user_name = d['user_name']
        return o


