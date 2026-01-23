#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceLogisticsFreightflowCloudfundrefundApplyModel(object):

    def __init__(self):
        self._biz_no = None
        self._cloud_fund_biz_no = None
        self._cloud_fund_order_no = None
        self._currency = None
        self._logistics_code = None
        self._mode = None
        self._mybank_app_id = None
        self._participant_id = None
        self._participant_type = None
        self._partner_id = None
        self._refund_amount = None
        self._refund_reason = None

    @property
    def biz_no(self):
        return self._biz_no

    @biz_no.setter
    def biz_no(self, value):
        self._biz_no = value
    @property
    def cloud_fund_biz_no(self):
        return self._cloud_fund_biz_no

    @cloud_fund_biz_no.setter
    def cloud_fund_biz_no(self, value):
        self._cloud_fund_biz_no = value
    @property
    def cloud_fund_order_no(self):
        return self._cloud_fund_order_no

    @cloud_fund_order_no.setter
    def cloud_fund_order_no(self, value):
        self._cloud_fund_order_no = value
    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        self._currency = value
    @property
    def logistics_code(self):
        return self._logistics_code

    @logistics_code.setter
    def logistics_code(self, value):
        self._logistics_code = value
    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, value):
        self._mode = value
    @property
    def mybank_app_id(self):
        return self._mybank_app_id

    @mybank_app_id.setter
    def mybank_app_id(self, value):
        self._mybank_app_id = value
    @property
    def participant_id(self):
        return self._participant_id

    @participant_id.setter
    def participant_id(self, value):
        self._participant_id = value
    @property
    def participant_type(self):
        return self._participant_type

    @participant_type.setter
    def participant_type(self, value):
        self._participant_type = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def refund_amount(self):
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        self._refund_amount = value
    @property
    def refund_reason(self):
        return self._refund_reason

    @refund_reason.setter
    def refund_reason(self, value):
        self._refund_reason = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_no:
            if hasattr(self.biz_no, 'to_alipay_dict'):
                params['biz_no'] = self.biz_no.to_alipay_dict()
            else:
                params['biz_no'] = self.biz_no
        if self.cloud_fund_biz_no:
            if hasattr(self.cloud_fund_biz_no, 'to_alipay_dict'):
                params['cloud_fund_biz_no'] = self.cloud_fund_biz_no.to_alipay_dict()
            else:
                params['cloud_fund_biz_no'] = self.cloud_fund_biz_no
        if self.cloud_fund_order_no:
            if hasattr(self.cloud_fund_order_no, 'to_alipay_dict'):
                params['cloud_fund_order_no'] = self.cloud_fund_order_no.to_alipay_dict()
            else:
                params['cloud_fund_order_no'] = self.cloud_fund_order_no
        if self.currency:
            if hasattr(self.currency, 'to_alipay_dict'):
                params['currency'] = self.currency.to_alipay_dict()
            else:
                params['currency'] = self.currency
        if self.logistics_code:
            if hasattr(self.logistics_code, 'to_alipay_dict'):
                params['logistics_code'] = self.logistics_code.to_alipay_dict()
            else:
                params['logistics_code'] = self.logistics_code
        if self.mode:
            if hasattr(self.mode, 'to_alipay_dict'):
                params['mode'] = self.mode.to_alipay_dict()
            else:
                params['mode'] = self.mode
        if self.mybank_app_id:
            if hasattr(self.mybank_app_id, 'to_alipay_dict'):
                params['mybank_app_id'] = self.mybank_app_id.to_alipay_dict()
            else:
                params['mybank_app_id'] = self.mybank_app_id
        if self.participant_id:
            if hasattr(self.participant_id, 'to_alipay_dict'):
                params['participant_id'] = self.participant_id.to_alipay_dict()
            else:
                params['participant_id'] = self.participant_id
        if self.participant_type:
            if hasattr(self.participant_type, 'to_alipay_dict'):
                params['participant_type'] = self.participant_type.to_alipay_dict()
            else:
                params['participant_type'] = self.participant_type
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        if self.refund_amount:
            if hasattr(self.refund_amount, 'to_alipay_dict'):
                params['refund_amount'] = self.refund_amount.to_alipay_dict()
            else:
                params['refund_amount'] = self.refund_amount
        if self.refund_reason:
            if hasattr(self.refund_reason, 'to_alipay_dict'):
                params['refund_reason'] = self.refund_reason.to_alipay_dict()
            else:
                params['refund_reason'] = self.refund_reason
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceLogisticsFreightflowCloudfundrefundApplyModel()
        if 'biz_no' in d:
            o.biz_no = d['biz_no']
        if 'cloud_fund_biz_no' in d:
            o.cloud_fund_biz_no = d['cloud_fund_biz_no']
        if 'cloud_fund_order_no' in d:
            o.cloud_fund_order_no = d['cloud_fund_order_no']
        if 'currency' in d:
            o.currency = d['currency']
        if 'logistics_code' in d:
            o.logistics_code = d['logistics_code']
        if 'mode' in d:
            o.mode = d['mode']
        if 'mybank_app_id' in d:
            o.mybank_app_id = d['mybank_app_id']
        if 'participant_id' in d:
            o.participant_id = d['participant_id']
        if 'participant_type' in d:
            o.participant_type = d['participant_type']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'refund_amount' in d:
            o.refund_amount = d['refund_amount']
        if 'refund_reason' in d:
            o.refund_reason = d['refund_reason']
        return o


