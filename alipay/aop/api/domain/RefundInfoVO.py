#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RefundRecordVO import RefundRecordVO


class RefundInfoVO(object):

    def __init__(self):
        self._refund_list = None

    @property
    def refund_list(self):
        return self._refund_list

    @refund_list.setter
    def refund_list(self, value):
        if isinstance(value, list):
            self._refund_list = list()
            for i in value:
                if isinstance(i, RefundRecordVO):
                    self._refund_list.append(i)
                else:
                    self._refund_list.append(RefundRecordVO.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.refund_list:
            if isinstance(self.refund_list, list):
                for i in range(0, len(self.refund_list)):
                    element = self.refund_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.refund_list[i] = element.to_alipay_dict()
            if hasattr(self.refund_list, 'to_alipay_dict'):
                params['refund_list'] = self.refund_list.to_alipay_dict()
            else:
                params['refund_list'] = self.refund_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RefundInfoVO()
        if 'refund_list' in d:
            o.refund_list = d['refund_list']
        return o


