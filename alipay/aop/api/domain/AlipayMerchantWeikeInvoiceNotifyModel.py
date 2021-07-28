#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.IsvLogisticsInfo import IsvLogisticsInfo


class AlipayMerchantWeikeInvoiceNotifyModel(object):

    def __init__(self):
        self._apply_id = None
        self._feedback_code = None
        self._feedback_msg = None
        self._feedback_result = None
        self._invoice_kind = None
        self._logistics_info = None

    @property
    def apply_id(self):
        return self._apply_id

    @apply_id.setter
    def apply_id(self, value):
        self._apply_id = value
    @property
    def feedback_code(self):
        return self._feedback_code

    @feedback_code.setter
    def feedback_code(self, value):
        self._feedback_code = value
    @property
    def feedback_msg(self):
        return self._feedback_msg

    @feedback_msg.setter
    def feedback_msg(self, value):
        self._feedback_msg = value
    @property
    def feedback_result(self):
        return self._feedback_result

    @feedback_result.setter
    def feedback_result(self, value):
        self._feedback_result = value
    @property
    def invoice_kind(self):
        return self._invoice_kind

    @invoice_kind.setter
    def invoice_kind(self, value):
        self._invoice_kind = value
    @property
    def logistics_info(self):
        return self._logistics_info

    @logistics_info.setter
    def logistics_info(self, value):
        if isinstance(value, list):
            self._logistics_info = list()
            for i in value:
                if isinstance(i, IsvLogisticsInfo):
                    self._logistics_info.append(i)
                else:
                    self._logistics_info.append(IsvLogisticsInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.apply_id:
            if hasattr(self.apply_id, 'to_alipay_dict'):
                params['apply_id'] = self.apply_id.to_alipay_dict()
            else:
                params['apply_id'] = self.apply_id
        if self.feedback_code:
            if hasattr(self.feedback_code, 'to_alipay_dict'):
                params['feedback_code'] = self.feedback_code.to_alipay_dict()
            else:
                params['feedback_code'] = self.feedback_code
        if self.feedback_msg:
            if hasattr(self.feedback_msg, 'to_alipay_dict'):
                params['feedback_msg'] = self.feedback_msg.to_alipay_dict()
            else:
                params['feedback_msg'] = self.feedback_msg
        if self.feedback_result:
            if hasattr(self.feedback_result, 'to_alipay_dict'):
                params['feedback_result'] = self.feedback_result.to_alipay_dict()
            else:
                params['feedback_result'] = self.feedback_result
        if self.invoice_kind:
            if hasattr(self.invoice_kind, 'to_alipay_dict'):
                params['invoice_kind'] = self.invoice_kind.to_alipay_dict()
            else:
                params['invoice_kind'] = self.invoice_kind
        if self.logistics_info:
            if isinstance(self.logistics_info, list):
                for i in range(0, len(self.logistics_info)):
                    element = self.logistics_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.logistics_info[i] = element.to_alipay_dict()
            if hasattr(self.logistics_info, 'to_alipay_dict'):
                params['logistics_info'] = self.logistics_info.to_alipay_dict()
            else:
                params['logistics_info'] = self.logistics_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMerchantWeikeInvoiceNotifyModel()
        if 'apply_id' in d:
            o.apply_id = d['apply_id']
        if 'feedback_code' in d:
            o.feedback_code = d['feedback_code']
        if 'feedback_msg' in d:
            o.feedback_msg = d['feedback_msg']
        if 'feedback_result' in d:
            o.feedback_result = d['feedback_result']
        if 'invoice_kind' in d:
            o.invoice_kind = d['invoice_kind']
        if 'logistics_info' in d:
            o.logistics_info = d['logistics_info']
        return o


