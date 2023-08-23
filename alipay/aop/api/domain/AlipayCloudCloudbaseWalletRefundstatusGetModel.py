#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCloudCloudbaseWalletRefundstatusGetModel(object):

    def __init__(self):
        self._biz_app_id = None
        self._refund_order_no = None

    @property
    def biz_app_id(self):
        return self._biz_app_id

    @biz_app_id.setter
    def biz_app_id(self, value):
        self._biz_app_id = value
    @property
    def refund_order_no(self):
        return self._refund_order_no

    @refund_order_no.setter
    def refund_order_no(self, value):
        self._refund_order_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_app_id:
            if hasattr(self.biz_app_id, 'to_alipay_dict'):
                params['biz_app_id'] = self.biz_app_id.to_alipay_dict()
            else:
                params['biz_app_id'] = self.biz_app_id
        if self.refund_order_no:
            if hasattr(self.refund_order_no, 'to_alipay_dict'):
                params['refund_order_no'] = self.refund_order_no.to_alipay_dict()
            else:
                params['refund_order_no'] = self.refund_order_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudCloudbaseWalletRefundstatusGetModel()
        if 'biz_app_id' in d:
            o.biz_app_id = d['biz_app_id']
        if 'refund_order_no' in d:
            o.refund_order_no = d['refund_order_no']
        return o


