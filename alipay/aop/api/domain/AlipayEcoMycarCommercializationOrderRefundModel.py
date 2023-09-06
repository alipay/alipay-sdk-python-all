#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CommercializationCertificateInfo import CommercializationCertificateInfo


class AlipayEcoMycarCommercializationOrderRefundModel(object):

    def __init__(self):
        self._open_id = None
        self._out_order_id = None
        self._out_refund_no = None
        self._refund_certificate_list = None
        self._refund_reason = None
        self._user_id = None

    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def out_order_id(self):
        return self._out_order_id

    @out_order_id.setter
    def out_order_id(self, value):
        self._out_order_id = value
    @property
    def out_refund_no(self):
        return self._out_refund_no

    @out_refund_no.setter
    def out_refund_no(self, value):
        self._out_refund_no = value
    @property
    def refund_certificate_list(self):
        return self._refund_certificate_list

    @refund_certificate_list.setter
    def refund_certificate_list(self, value):
        if isinstance(value, list):
            self._refund_certificate_list = list()
            for i in value:
                if isinstance(i, CommercializationCertificateInfo):
                    self._refund_certificate_list.append(i)
                else:
                    self._refund_certificate_list.append(CommercializationCertificateInfo.from_alipay_dict(i))
    @property
    def refund_reason(self):
        return self._refund_reason

    @refund_reason.setter
    def refund_reason(self, value):
        self._refund_reason = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.out_order_id:
            if hasattr(self.out_order_id, 'to_alipay_dict'):
                params['out_order_id'] = self.out_order_id.to_alipay_dict()
            else:
                params['out_order_id'] = self.out_order_id
        if self.out_refund_no:
            if hasattr(self.out_refund_no, 'to_alipay_dict'):
                params['out_refund_no'] = self.out_refund_no.to_alipay_dict()
            else:
                params['out_refund_no'] = self.out_refund_no
        if self.refund_certificate_list:
            if isinstance(self.refund_certificate_list, list):
                for i in range(0, len(self.refund_certificate_list)):
                    element = self.refund_certificate_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.refund_certificate_list[i] = element.to_alipay_dict()
            if hasattr(self.refund_certificate_list, 'to_alipay_dict'):
                params['refund_certificate_list'] = self.refund_certificate_list.to_alipay_dict()
            else:
                params['refund_certificate_list'] = self.refund_certificate_list
        if self.refund_reason:
            if hasattr(self.refund_reason, 'to_alipay_dict'):
                params['refund_reason'] = self.refund_reason.to_alipay_dict()
            else:
                params['refund_reason'] = self.refund_reason
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoMycarCommercializationOrderRefundModel()
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'out_order_id' in d:
            o.out_order_id = d['out_order_id']
        if 'out_refund_no' in d:
            o.out_refund_no = d['out_refund_no']
        if 'refund_certificate_list' in d:
            o.refund_certificate_list = d['refund_certificate_list']
        if 'refund_reason' in d:
            o.refund_reason = d['refund_reason']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


