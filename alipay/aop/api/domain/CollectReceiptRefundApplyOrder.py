#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AttachmentFile import AttachmentFile
from alipay.aop.api.domain.MultiCurrencyMoneyOpenApi import MultiCurrencyMoneyOpenApi
from alipay.aop.api.domain.MapTypeParam import MapTypeParam


class CollectReceiptRefundApplyOrder(object):

    def __init__(self):
        self._attachment_file_list = None
        self._business_scene = None
        self._channel = None
        self._idempotent_no = None
        self._memo = None
        self._need_audit = None
        self._operator = None
        self._operator_id = None
        self._operator_staff_no = None
        self._receipt_no = None
        self._refund_amount = None
        self._refund_payee_account_name = None
        self._refund_payee_account_no = None
        self._refund_payee_ext_inf = None

    @property
    def attachment_file_list(self):
        return self._attachment_file_list

    @attachment_file_list.setter
    def attachment_file_list(self, value):
        if isinstance(value, list):
            self._attachment_file_list = list()
            for i in value:
                if isinstance(i, AttachmentFile):
                    self._attachment_file_list.append(i)
                else:
                    self._attachment_file_list.append(AttachmentFile.from_alipay_dict(i))
    @property
    def business_scene(self):
        return self._business_scene

    @business_scene.setter
    def business_scene(self, value):
        self._business_scene = value
    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def idempotent_no(self):
        return self._idempotent_no

    @idempotent_no.setter
    def idempotent_no(self, value):
        self._idempotent_no = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def need_audit(self):
        return self._need_audit

    @need_audit.setter
    def need_audit(self, value):
        self._need_audit = value
    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        self._operator = value
    @property
    def operator_id(self):
        return self._operator_id

    @operator_id.setter
    def operator_id(self, value):
        self._operator_id = value
    @property
    def operator_staff_no(self):
        return self._operator_staff_no

    @operator_staff_no.setter
    def operator_staff_no(self, value):
        self._operator_staff_no = value
    @property
    def receipt_no(self):
        return self._receipt_no

    @receipt_no.setter
    def receipt_no(self, value):
        self._receipt_no = value
    @property
    def refund_amount(self):
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        if isinstance(value, MultiCurrencyMoneyOpenApi):
            self._refund_amount = value
        else:
            self._refund_amount = MultiCurrencyMoneyOpenApi.from_alipay_dict(value)
    @property
    def refund_payee_account_name(self):
        return self._refund_payee_account_name

    @refund_payee_account_name.setter
    def refund_payee_account_name(self, value):
        self._refund_payee_account_name = value
    @property
    def refund_payee_account_no(self):
        return self._refund_payee_account_no

    @refund_payee_account_no.setter
    def refund_payee_account_no(self, value):
        self._refund_payee_account_no = value
    @property
    def refund_payee_ext_inf(self):
        return self._refund_payee_ext_inf

    @refund_payee_ext_inf.setter
    def refund_payee_ext_inf(self, value):
        if isinstance(value, MapTypeParam):
            self._refund_payee_ext_inf = value
        else:
            self._refund_payee_ext_inf = MapTypeParam.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.attachment_file_list:
            if isinstance(self.attachment_file_list, list):
                for i in range(0, len(self.attachment_file_list)):
                    element = self.attachment_file_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.attachment_file_list[i] = element.to_alipay_dict()
            if hasattr(self.attachment_file_list, 'to_alipay_dict'):
                params['attachment_file_list'] = self.attachment_file_list.to_alipay_dict()
            else:
                params['attachment_file_list'] = self.attachment_file_list
        if self.business_scene:
            if hasattr(self.business_scene, 'to_alipay_dict'):
                params['business_scene'] = self.business_scene.to_alipay_dict()
            else:
                params['business_scene'] = self.business_scene
        if self.channel:
            if hasattr(self.channel, 'to_alipay_dict'):
                params['channel'] = self.channel.to_alipay_dict()
            else:
                params['channel'] = self.channel
        if self.idempotent_no:
            if hasattr(self.idempotent_no, 'to_alipay_dict'):
                params['idempotent_no'] = self.idempotent_no.to_alipay_dict()
            else:
                params['idempotent_no'] = self.idempotent_no
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.need_audit:
            if hasattr(self.need_audit, 'to_alipay_dict'):
                params['need_audit'] = self.need_audit.to_alipay_dict()
            else:
                params['need_audit'] = self.need_audit
        if self.operator:
            if hasattr(self.operator, 'to_alipay_dict'):
                params['operator'] = self.operator.to_alipay_dict()
            else:
                params['operator'] = self.operator
        if self.operator_id:
            if hasattr(self.operator_id, 'to_alipay_dict'):
                params['operator_id'] = self.operator_id.to_alipay_dict()
            else:
                params['operator_id'] = self.operator_id
        if self.operator_staff_no:
            if hasattr(self.operator_staff_no, 'to_alipay_dict'):
                params['operator_staff_no'] = self.operator_staff_no.to_alipay_dict()
            else:
                params['operator_staff_no'] = self.operator_staff_no
        if self.receipt_no:
            if hasattr(self.receipt_no, 'to_alipay_dict'):
                params['receipt_no'] = self.receipt_no.to_alipay_dict()
            else:
                params['receipt_no'] = self.receipt_no
        if self.refund_amount:
            if hasattr(self.refund_amount, 'to_alipay_dict'):
                params['refund_amount'] = self.refund_amount.to_alipay_dict()
            else:
                params['refund_amount'] = self.refund_amount
        if self.refund_payee_account_name:
            if hasattr(self.refund_payee_account_name, 'to_alipay_dict'):
                params['refund_payee_account_name'] = self.refund_payee_account_name.to_alipay_dict()
            else:
                params['refund_payee_account_name'] = self.refund_payee_account_name
        if self.refund_payee_account_no:
            if hasattr(self.refund_payee_account_no, 'to_alipay_dict'):
                params['refund_payee_account_no'] = self.refund_payee_account_no.to_alipay_dict()
            else:
                params['refund_payee_account_no'] = self.refund_payee_account_no
        if self.refund_payee_ext_inf:
            if hasattr(self.refund_payee_ext_inf, 'to_alipay_dict'):
                params['refund_payee_ext_inf'] = self.refund_payee_ext_inf.to_alipay_dict()
            else:
                params['refund_payee_ext_inf'] = self.refund_payee_ext_inf
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CollectReceiptRefundApplyOrder()
        if 'attachment_file_list' in d:
            o.attachment_file_list = d['attachment_file_list']
        if 'business_scene' in d:
            o.business_scene = d['business_scene']
        if 'channel' in d:
            o.channel = d['channel']
        if 'idempotent_no' in d:
            o.idempotent_no = d['idempotent_no']
        if 'memo' in d:
            o.memo = d['memo']
        if 'need_audit' in d:
            o.need_audit = d['need_audit']
        if 'operator' in d:
            o.operator = d['operator']
        if 'operator_id' in d:
            o.operator_id = d['operator_id']
        if 'operator_staff_no' in d:
            o.operator_staff_no = d['operator_staff_no']
        if 'receipt_no' in d:
            o.receipt_no = d['receipt_no']
        if 'refund_amount' in d:
            o.refund_amount = d['refund_amount']
        if 'refund_payee_account_name' in d:
            o.refund_payee_account_name = d['refund_payee_account_name']
        if 'refund_payee_account_no' in d:
            o.refund_payee_account_no = d['refund_payee_account_no']
        if 'refund_payee_ext_inf' in d:
            o.refund_payee_ext_inf = d['refund_payee_ext_inf']
        return o


