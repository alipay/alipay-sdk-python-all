#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MultiStepTransferParticipant import MultiStepTransferParticipant
from alipay.aop.api.domain.MultiStepTransferParticipant import MultiStepTransferParticipant


class MultiStepTransOrderDetailResponse(object):

    def __init__(self):
        self._amount = None
        self._gmt_pay = None
        self._open_id = None
        self._order_id = None
        self._order_seq = None
        self._order_title = None
        self._out_biz_no = None
        self._payee_info = None
        self._payer_info = None
        self._remark = None
        self._request_user_id = None
        self._status = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def gmt_pay(self):
        return self._gmt_pay

    @gmt_pay.setter
    def gmt_pay(self, value):
        self._gmt_pay = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def order_seq(self):
        return self._order_seq

    @order_seq.setter
    def order_seq(self, value):
        self._order_seq = value
    @property
    def order_title(self):
        return self._order_title

    @order_title.setter
    def order_title(self, value):
        self._order_title = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def payee_info(self):
        return self._payee_info

    @payee_info.setter
    def payee_info(self, value):
        if isinstance(value, MultiStepTransferParticipant):
            self._payee_info = value
        else:
            self._payee_info = MultiStepTransferParticipant.from_alipay_dict(value)
    @property
    def payer_info(self):
        return self._payer_info

    @payer_info.setter
    def payer_info(self, value):
        if isinstance(value, MultiStepTransferParticipant):
            self._payer_info = value
        else:
            self._payer_info = MultiStepTransferParticipant.from_alipay_dict(value)
    @property
    def remark(self):
        return self._remark

    @remark.setter
    def remark(self, value):
        self._remark = value
    @property
    def request_user_id(self):
        return self._request_user_id

    @request_user_id.setter
    def request_user_id(self, value):
        self._request_user_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount:
            if hasattr(self.amount, 'to_alipay_dict'):
                params['amount'] = self.amount.to_alipay_dict()
            else:
                params['amount'] = self.amount
        if self.gmt_pay:
            if hasattr(self.gmt_pay, 'to_alipay_dict'):
                params['gmt_pay'] = self.gmt_pay.to_alipay_dict()
            else:
                params['gmt_pay'] = self.gmt_pay
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.order_seq:
            if hasattr(self.order_seq, 'to_alipay_dict'):
                params['order_seq'] = self.order_seq.to_alipay_dict()
            else:
                params['order_seq'] = self.order_seq
        if self.order_title:
            if hasattr(self.order_title, 'to_alipay_dict'):
                params['order_title'] = self.order_title.to_alipay_dict()
            else:
                params['order_title'] = self.order_title
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.payee_info:
            if hasattr(self.payee_info, 'to_alipay_dict'):
                params['payee_info'] = self.payee_info.to_alipay_dict()
            else:
                params['payee_info'] = self.payee_info
        if self.payer_info:
            if hasattr(self.payer_info, 'to_alipay_dict'):
                params['payer_info'] = self.payer_info.to_alipay_dict()
            else:
                params['payer_info'] = self.payer_info
        if self.remark:
            if hasattr(self.remark, 'to_alipay_dict'):
                params['remark'] = self.remark.to_alipay_dict()
            else:
                params['remark'] = self.remark
        if self.request_user_id:
            if hasattr(self.request_user_id, 'to_alipay_dict'):
                params['request_user_id'] = self.request_user_id.to_alipay_dict()
            else:
                params['request_user_id'] = self.request_user_id
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MultiStepTransOrderDetailResponse()
        if 'amount' in d:
            o.amount = d['amount']
        if 'gmt_pay' in d:
            o.gmt_pay = d['gmt_pay']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'order_seq' in d:
            o.order_seq = d['order_seq']
        if 'order_title' in d:
            o.order_title = d['order_title']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'payee_info' in d:
            o.payee_info = d['payee_info']
        if 'payer_info' in d:
            o.payer_info = d['payer_info']
        if 'remark' in d:
            o.remark = d['remark']
        if 'request_user_id' in d:
            o.request_user_id = d['request_user_id']
        if 'status' in d:
            o.status = d['status']
        return o


