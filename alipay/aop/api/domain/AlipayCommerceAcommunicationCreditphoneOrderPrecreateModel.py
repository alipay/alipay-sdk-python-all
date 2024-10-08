#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CreditPhoneInfo import CreditPhoneInfo
from alipay.aop.api.domain.CreditPhoneRiskInfo import CreditPhoneRiskInfo


class AlipayCommerceAcommunicationCreditphoneOrderPrecreateModel(object):

    def __init__(self):
        self._alipay_open_id = None
        self._alipay_user_id = None
        self._biz_time = None
        self._credit_phone_info = None
        self._detail_url = None
        self._freeze_amount = None
        self._inst_sign_aisle_data = None
        self._out_order_no = None
        self._risk_info = None
        self._source_id = None

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
    def biz_time(self):
        return self._biz_time

    @biz_time.setter
    def biz_time(self, value):
        self._biz_time = value
    @property
    def credit_phone_info(self):
        return self._credit_phone_info

    @credit_phone_info.setter
    def credit_phone_info(self, value):
        if isinstance(value, CreditPhoneInfo):
            self._credit_phone_info = value
        else:
            self._credit_phone_info = CreditPhoneInfo.from_alipay_dict(value)
    @property
    def detail_url(self):
        return self._detail_url

    @detail_url.setter
    def detail_url(self, value):
        self._detail_url = value
    @property
    def freeze_amount(self):
        return self._freeze_amount

    @freeze_amount.setter
    def freeze_amount(self, value):
        self._freeze_amount = value
    @property
    def inst_sign_aisle_data(self):
        return self._inst_sign_aisle_data

    @inst_sign_aisle_data.setter
    def inst_sign_aisle_data(self, value):
        self._inst_sign_aisle_data = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def risk_info(self):
        return self._risk_info

    @risk_info.setter
    def risk_info(self, value):
        if isinstance(value, CreditPhoneRiskInfo):
            self._risk_info = value
        else:
            self._risk_info = CreditPhoneRiskInfo.from_alipay_dict(value)
    @property
    def source_id(self):
        return self._source_id

    @source_id.setter
    def source_id(self, value):
        self._source_id = value


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
        if self.biz_time:
            if hasattr(self.biz_time, 'to_alipay_dict'):
                params['biz_time'] = self.biz_time.to_alipay_dict()
            else:
                params['biz_time'] = self.biz_time
        if self.credit_phone_info:
            if hasattr(self.credit_phone_info, 'to_alipay_dict'):
                params['credit_phone_info'] = self.credit_phone_info.to_alipay_dict()
            else:
                params['credit_phone_info'] = self.credit_phone_info
        if self.detail_url:
            if hasattr(self.detail_url, 'to_alipay_dict'):
                params['detail_url'] = self.detail_url.to_alipay_dict()
            else:
                params['detail_url'] = self.detail_url
        if self.freeze_amount:
            if hasattr(self.freeze_amount, 'to_alipay_dict'):
                params['freeze_amount'] = self.freeze_amount.to_alipay_dict()
            else:
                params['freeze_amount'] = self.freeze_amount
        if self.inst_sign_aisle_data:
            if hasattr(self.inst_sign_aisle_data, 'to_alipay_dict'):
                params['inst_sign_aisle_data'] = self.inst_sign_aisle_data.to_alipay_dict()
            else:
                params['inst_sign_aisle_data'] = self.inst_sign_aisle_data
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
        if self.risk_info:
            if hasattr(self.risk_info, 'to_alipay_dict'):
                params['risk_info'] = self.risk_info.to_alipay_dict()
            else:
                params['risk_info'] = self.risk_info
        if self.source_id:
            if hasattr(self.source_id, 'to_alipay_dict'):
                params['source_id'] = self.source_id.to_alipay_dict()
            else:
                params['source_id'] = self.source_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceAcommunicationCreditphoneOrderPrecreateModel()
        if 'alipay_open_id' in d:
            o.alipay_open_id = d['alipay_open_id']
        if 'alipay_user_id' in d:
            o.alipay_user_id = d['alipay_user_id']
        if 'biz_time' in d:
            o.biz_time = d['biz_time']
        if 'credit_phone_info' in d:
            o.credit_phone_info = d['credit_phone_info']
        if 'detail_url' in d:
            o.detail_url = d['detail_url']
        if 'freeze_amount' in d:
            o.freeze_amount = d['freeze_amount']
        if 'inst_sign_aisle_data' in d:
            o.inst_sign_aisle_data = d['inst_sign_aisle_data']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'risk_info' in d:
            o.risk_info = d['risk_info']
        if 'source_id' in d:
            o.source_id = d['source_id']
        return o


