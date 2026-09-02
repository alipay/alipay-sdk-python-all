#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RefundCallbackBizDetail import RefundCallbackBizDetail
from alipay.aop.api.domain.RepaymentCallbackBizDetail import RepaymentCallbackBizDetail
from alipay.aop.api.domain.SignCallbackBizDetail import SignCallbackBizDetail
from alipay.aop.api.domain.TransferCallbackBizDetail import TransferCallbackBizDetail
from alipay.aop.api.domain.UnbindCallbackBizDetail import UnbindCallbackBizDetail


class AlipayCommerceAcommunicationCreditphoneRoutehubCallbackModel(object):

    def __init__(self):
        self._event_type = None
        self._order_no = None
        self._refund_callback_biz_detail = None
        self._repayment_callback_biz_detail = None
        self._sign_callback_biz_detail = None
        self._transfer_callback_biz_detail = None
        self._unbind_callback_biz_detail = None

    @property
    def event_type(self):
        return self._event_type

    @event_type.setter
    def event_type(self, value):
        self._event_type = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def refund_callback_biz_detail(self):
        return self._refund_callback_biz_detail

    @refund_callback_biz_detail.setter
    def refund_callback_biz_detail(self, value):
        if isinstance(value, RefundCallbackBizDetail):
            self._refund_callback_biz_detail = value
        else:
            self._refund_callback_biz_detail = RefundCallbackBizDetail.from_alipay_dict(value)
    @property
    def repayment_callback_biz_detail(self):
        return self._repayment_callback_biz_detail

    @repayment_callback_biz_detail.setter
    def repayment_callback_biz_detail(self, value):
        if isinstance(value, RepaymentCallbackBizDetail):
            self._repayment_callback_biz_detail = value
        else:
            self._repayment_callback_biz_detail = RepaymentCallbackBizDetail.from_alipay_dict(value)
    @property
    def sign_callback_biz_detail(self):
        return self._sign_callback_biz_detail

    @sign_callback_biz_detail.setter
    def sign_callback_biz_detail(self, value):
        if isinstance(value, SignCallbackBizDetail):
            self._sign_callback_biz_detail = value
        else:
            self._sign_callback_biz_detail = SignCallbackBizDetail.from_alipay_dict(value)
    @property
    def transfer_callback_biz_detail(self):
        return self._transfer_callback_biz_detail

    @transfer_callback_biz_detail.setter
    def transfer_callback_biz_detail(self, value):
        if isinstance(value, TransferCallbackBizDetail):
            self._transfer_callback_biz_detail = value
        else:
            self._transfer_callback_biz_detail = TransferCallbackBizDetail.from_alipay_dict(value)
    @property
    def unbind_callback_biz_detail(self):
        return self._unbind_callback_biz_detail

    @unbind_callback_biz_detail.setter
    def unbind_callback_biz_detail(self, value):
        if isinstance(value, UnbindCallbackBizDetail):
            self._unbind_callback_biz_detail = value
        else:
            self._unbind_callback_biz_detail = UnbindCallbackBizDetail.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.event_type:
            if hasattr(self.event_type, 'to_alipay_dict'):
                params['event_type'] = self.event_type.to_alipay_dict()
            else:
                params['event_type'] = self.event_type
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        if self.refund_callback_biz_detail:
            if hasattr(self.refund_callback_biz_detail, 'to_alipay_dict'):
                params['refund_callback_biz_detail'] = self.refund_callback_biz_detail.to_alipay_dict()
            else:
                params['refund_callback_biz_detail'] = self.refund_callback_biz_detail
        if self.repayment_callback_biz_detail:
            if hasattr(self.repayment_callback_biz_detail, 'to_alipay_dict'):
                params['repayment_callback_biz_detail'] = self.repayment_callback_biz_detail.to_alipay_dict()
            else:
                params['repayment_callback_biz_detail'] = self.repayment_callback_biz_detail
        if self.sign_callback_biz_detail:
            if hasattr(self.sign_callback_biz_detail, 'to_alipay_dict'):
                params['sign_callback_biz_detail'] = self.sign_callback_biz_detail.to_alipay_dict()
            else:
                params['sign_callback_biz_detail'] = self.sign_callback_biz_detail
        if self.transfer_callback_biz_detail:
            if hasattr(self.transfer_callback_biz_detail, 'to_alipay_dict'):
                params['transfer_callback_biz_detail'] = self.transfer_callback_biz_detail.to_alipay_dict()
            else:
                params['transfer_callback_biz_detail'] = self.transfer_callback_biz_detail
        if self.unbind_callback_biz_detail:
            if hasattr(self.unbind_callback_biz_detail, 'to_alipay_dict'):
                params['unbind_callback_biz_detail'] = self.unbind_callback_biz_detail.to_alipay_dict()
            else:
                params['unbind_callback_biz_detail'] = self.unbind_callback_biz_detail
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceAcommunicationCreditphoneRoutehubCallbackModel()
        if 'event_type' in d:
            o.event_type = d['event_type']
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'refund_callback_biz_detail' in d:
            o.refund_callback_biz_detail = d['refund_callback_biz_detail']
        if 'repayment_callback_biz_detail' in d:
            o.repayment_callback_biz_detail = d['repayment_callback_biz_detail']
        if 'sign_callback_biz_detail' in d:
            o.sign_callback_biz_detail = d['sign_callback_biz_detail']
        if 'transfer_callback_biz_detail' in d:
            o.transfer_callback_biz_detail = d['transfer_callback_biz_detail']
        if 'unbind_callback_biz_detail' in d:
            o.unbind_callback_biz_detail = d['unbind_callback_biz_detail']
        return o


