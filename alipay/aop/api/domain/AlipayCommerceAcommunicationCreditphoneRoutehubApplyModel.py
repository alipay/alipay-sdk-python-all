#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RefundApplyBizDetail import RefundApplyBizDetail
from alipay.aop.api.domain.RepaymentApplyBizDetail import RepaymentApplyBizDetail
from alipay.aop.api.domain.SignApplyBizDetail import SignApplyBizDetail
from alipay.aop.api.domain.TransferApplyBizDetail import TransferApplyBizDetail
from alipay.aop.api.domain.UnbindApplyBizDetail import UnbindApplyBizDetail


class AlipayCommerceAcommunicationCreditphoneRoutehubApplyModel(object):

    def __init__(self):
        self._inst_pid = None
        self._operation_type = None
        self._order_no = None
        self._refund_apply_biz_detail = None
        self._repayment_apply_biz_detail = None
        self._sign_apply_biz_detail = None
        self._transfer_apply_biz_detail = None
        self._unbind_apply_biz_detail = None

    @property
    def inst_pid(self):
        return self._inst_pid

    @inst_pid.setter
    def inst_pid(self, value):
        self._inst_pid = value
    @property
    def operation_type(self):
        return self._operation_type

    @operation_type.setter
    def operation_type(self, value):
        self._operation_type = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def refund_apply_biz_detail(self):
        return self._refund_apply_biz_detail

    @refund_apply_biz_detail.setter
    def refund_apply_biz_detail(self, value):
        if isinstance(value, RefundApplyBizDetail):
            self._refund_apply_biz_detail = value
        else:
            self._refund_apply_biz_detail = RefundApplyBizDetail.from_alipay_dict(value)
    @property
    def repayment_apply_biz_detail(self):
        return self._repayment_apply_biz_detail

    @repayment_apply_biz_detail.setter
    def repayment_apply_biz_detail(self, value):
        if isinstance(value, RepaymentApplyBizDetail):
            self._repayment_apply_biz_detail = value
        else:
            self._repayment_apply_biz_detail = RepaymentApplyBizDetail.from_alipay_dict(value)
    @property
    def sign_apply_biz_detail(self):
        return self._sign_apply_biz_detail

    @sign_apply_biz_detail.setter
    def sign_apply_biz_detail(self, value):
        if isinstance(value, SignApplyBizDetail):
            self._sign_apply_biz_detail = value
        else:
            self._sign_apply_biz_detail = SignApplyBizDetail.from_alipay_dict(value)
    @property
    def transfer_apply_biz_detail(self):
        return self._transfer_apply_biz_detail

    @transfer_apply_biz_detail.setter
    def transfer_apply_biz_detail(self, value):
        if isinstance(value, TransferApplyBizDetail):
            self._transfer_apply_biz_detail = value
        else:
            self._transfer_apply_biz_detail = TransferApplyBizDetail.from_alipay_dict(value)
    @property
    def unbind_apply_biz_detail(self):
        return self._unbind_apply_biz_detail

    @unbind_apply_biz_detail.setter
    def unbind_apply_biz_detail(self, value):
        if isinstance(value, UnbindApplyBizDetail):
            self._unbind_apply_biz_detail = value
        else:
            self._unbind_apply_biz_detail = UnbindApplyBizDetail.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.inst_pid:
            if hasattr(self.inst_pid, 'to_alipay_dict'):
                params['inst_pid'] = self.inst_pid.to_alipay_dict()
            else:
                params['inst_pid'] = self.inst_pid
        if self.operation_type:
            if hasattr(self.operation_type, 'to_alipay_dict'):
                params['operation_type'] = self.operation_type.to_alipay_dict()
            else:
                params['operation_type'] = self.operation_type
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        if self.refund_apply_biz_detail:
            if hasattr(self.refund_apply_biz_detail, 'to_alipay_dict'):
                params['refund_apply_biz_detail'] = self.refund_apply_biz_detail.to_alipay_dict()
            else:
                params['refund_apply_biz_detail'] = self.refund_apply_biz_detail
        if self.repayment_apply_biz_detail:
            if hasattr(self.repayment_apply_biz_detail, 'to_alipay_dict'):
                params['repayment_apply_biz_detail'] = self.repayment_apply_biz_detail.to_alipay_dict()
            else:
                params['repayment_apply_biz_detail'] = self.repayment_apply_biz_detail
        if self.sign_apply_biz_detail:
            if hasattr(self.sign_apply_biz_detail, 'to_alipay_dict'):
                params['sign_apply_biz_detail'] = self.sign_apply_biz_detail.to_alipay_dict()
            else:
                params['sign_apply_biz_detail'] = self.sign_apply_biz_detail
        if self.transfer_apply_biz_detail:
            if hasattr(self.transfer_apply_biz_detail, 'to_alipay_dict'):
                params['transfer_apply_biz_detail'] = self.transfer_apply_biz_detail.to_alipay_dict()
            else:
                params['transfer_apply_biz_detail'] = self.transfer_apply_biz_detail
        if self.unbind_apply_biz_detail:
            if hasattr(self.unbind_apply_biz_detail, 'to_alipay_dict'):
                params['unbind_apply_biz_detail'] = self.unbind_apply_biz_detail.to_alipay_dict()
            else:
                params['unbind_apply_biz_detail'] = self.unbind_apply_biz_detail
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceAcommunicationCreditphoneRoutehubApplyModel()
        if 'inst_pid' in d:
            o.inst_pid = d['inst_pid']
        if 'operation_type' in d:
            o.operation_type = d['operation_type']
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'refund_apply_biz_detail' in d:
            o.refund_apply_biz_detail = d['refund_apply_biz_detail']
        if 'repayment_apply_biz_detail' in d:
            o.repayment_apply_biz_detail = d['repayment_apply_biz_detail']
        if 'sign_apply_biz_detail' in d:
            o.sign_apply_biz_detail = d['sign_apply_biz_detail']
        if 'transfer_apply_biz_detail' in d:
            o.transfer_apply_biz_detail = d['transfer_apply_biz_detail']
        if 'unbind_apply_biz_detail' in d:
            o.unbind_apply_biz_detail = d['unbind_apply_biz_detail']
        return o


