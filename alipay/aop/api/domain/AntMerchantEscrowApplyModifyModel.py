#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EscrowSettleCardInfo import EscrowSettleCardInfo


class AntMerchantEscrowApplyModifyModel(object):

    def __init__(self):
        self._ant_merchant_order_no = None
        self._card_info = None
        self._out_request_no = None
        self._platform_partner_id = None
        self._seller_user_id = None

    @property
    def ant_merchant_order_no(self):
        return self._ant_merchant_order_no

    @ant_merchant_order_no.setter
    def ant_merchant_order_no(self, value):
        self._ant_merchant_order_no = value
    @property
    def card_info(self):
        return self._card_info

    @card_info.setter
    def card_info(self, value):
        if isinstance(value, EscrowSettleCardInfo):
            self._card_info = value
        else:
            self._card_info = EscrowSettleCardInfo.from_alipay_dict(value)
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def platform_partner_id(self):
        return self._platform_partner_id

    @platform_partner_id.setter
    def platform_partner_id(self, value):
        self._platform_partner_id = value
    @property
    def seller_user_id(self):
        return self._seller_user_id

    @seller_user_id.setter
    def seller_user_id(self, value):
        self._seller_user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.ant_merchant_order_no:
            if hasattr(self.ant_merchant_order_no, 'to_alipay_dict'):
                params['ant_merchant_order_no'] = self.ant_merchant_order_no.to_alipay_dict()
            else:
                params['ant_merchant_order_no'] = self.ant_merchant_order_no
        if self.card_info:
            if hasattr(self.card_info, 'to_alipay_dict'):
                params['card_info'] = self.card_info.to_alipay_dict()
            else:
                params['card_info'] = self.card_info
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        if self.platform_partner_id:
            if hasattr(self.platform_partner_id, 'to_alipay_dict'):
                params['platform_partner_id'] = self.platform_partner_id.to_alipay_dict()
            else:
                params['platform_partner_id'] = self.platform_partner_id
        if self.seller_user_id:
            if hasattr(self.seller_user_id, 'to_alipay_dict'):
                params['seller_user_id'] = self.seller_user_id.to_alipay_dict()
            else:
                params['seller_user_id'] = self.seller_user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntMerchantEscrowApplyModifyModel()
        if 'ant_merchant_order_no' in d:
            o.ant_merchant_order_no = d['ant_merchant_order_no']
        if 'card_info' in d:
            o.card_info = d['card_info']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'platform_partner_id' in d:
            o.platform_partner_id = d['platform_partner_id']
        if 'seller_user_id' in d:
            o.seller_user_id = d['seller_user_id']
        return o


