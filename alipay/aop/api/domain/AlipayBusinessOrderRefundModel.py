#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EnvInfo import EnvInfo
from alipay.aop.api.domain.PaytoolRefundRequestDetail import PaytoolRefundRequestDetail


class AlipayBusinessOrderRefundModel(object):

    def __init__(self):
        self._env_info = None
        self._order_no = None
        self._refund_paytool_list = None
        self._refund_reason = None
        self._refund_request_no = None

    @property
    def env_info(self):
        return self._env_info

    @env_info.setter
    def env_info(self, value):
        if isinstance(value, EnvInfo):
            self._env_info = value
        else:
            self._env_info = EnvInfo.from_alipay_dict(value)
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def refund_paytool_list(self):
        return self._refund_paytool_list

    @refund_paytool_list.setter
    def refund_paytool_list(self, value):
        if isinstance(value, list):
            self._refund_paytool_list = list()
            for i in value:
                if isinstance(i, PaytoolRefundRequestDetail):
                    self._refund_paytool_list.append(i)
                else:
                    self._refund_paytool_list.append(PaytoolRefundRequestDetail.from_alipay_dict(i))
    @property
    def refund_reason(self):
        return self._refund_reason

    @refund_reason.setter
    def refund_reason(self, value):
        self._refund_reason = value
    @property
    def refund_request_no(self):
        return self._refund_request_no

    @refund_request_no.setter
    def refund_request_no(self, value):
        self._refund_request_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.env_info:
            if hasattr(self.env_info, 'to_alipay_dict'):
                params['env_info'] = self.env_info.to_alipay_dict()
            else:
                params['env_info'] = self.env_info
        if self.order_no:
            if hasattr(self.order_no, 'to_alipay_dict'):
                params['order_no'] = self.order_no.to_alipay_dict()
            else:
                params['order_no'] = self.order_no
        if self.refund_paytool_list:
            if isinstance(self.refund_paytool_list, list):
                for i in range(0, len(self.refund_paytool_list)):
                    element = self.refund_paytool_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.refund_paytool_list[i] = element.to_alipay_dict()
            if hasattr(self.refund_paytool_list, 'to_alipay_dict'):
                params['refund_paytool_list'] = self.refund_paytool_list.to_alipay_dict()
            else:
                params['refund_paytool_list'] = self.refund_paytool_list
        if self.refund_reason:
            if hasattr(self.refund_reason, 'to_alipay_dict'):
                params['refund_reason'] = self.refund_reason.to_alipay_dict()
            else:
                params['refund_reason'] = self.refund_reason
        if self.refund_request_no:
            if hasattr(self.refund_request_no, 'to_alipay_dict'):
                params['refund_request_no'] = self.refund_request_no.to_alipay_dict()
            else:
                params['refund_request_no'] = self.refund_request_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBusinessOrderRefundModel()
        if 'env_info' in d:
            o.env_info = d['env_info']
        if 'order_no' in d:
            o.order_no = d['order_no']
        if 'refund_paytool_list' in d:
            o.refund_paytool_list = d['refund_paytool_list']
        if 'refund_reason' in d:
            o.refund_reason = d['refund_reason']
        if 'refund_request_no' in d:
            o.refund_request_no = d['refund_request_no']
        return o


