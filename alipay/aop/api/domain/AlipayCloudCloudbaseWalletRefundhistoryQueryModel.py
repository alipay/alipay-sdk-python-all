#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCloudCloudbaseWalletRefundhistoryQueryModel(object):

    def __init__(self):
        self._biz_app_id = None
        self._refund_date = None

    @property
    def biz_app_id(self):
        return self._biz_app_id

    @biz_app_id.setter
    def biz_app_id(self, value):
        self._biz_app_id = value
    @property
    def refund_date(self):
        return self._refund_date

    @refund_date.setter
    def refund_date(self, value):
        self._refund_date = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_app_id:
            if hasattr(self.biz_app_id, 'to_alipay_dict'):
                params['biz_app_id'] = self.biz_app_id.to_alipay_dict()
            else:
                params['biz_app_id'] = self.biz_app_id
        if self.refund_date:
            if hasattr(self.refund_date, 'to_alipay_dict'):
                params['refund_date'] = self.refund_date.to_alipay_dict()
            else:
                params['refund_date'] = self.refund_date
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudCloudbaseWalletRefundhistoryQueryModel()
        if 'biz_app_id' in d:
            o.biz_app_id = d['biz_app_id']
        if 'refund_date' in d:
            o.refund_date = d['refund_date']
        return o


