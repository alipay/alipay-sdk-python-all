#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiRetailWmsDeliveryorderprocessQueryModel(object):

    def __init__(self):
        self._notice_order_id = None

    @property
    def notice_order_id(self):
        return self._notice_order_id

    @notice_order_id.setter
    def notice_order_id(self, value):
        self._notice_order_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.notice_order_id:
            if hasattr(self.notice_order_id, 'to_alipay_dict'):
                params['notice_order_id'] = self.notice_order_id.to_alipay_dict()
            else:
                params['notice_order_id'] = self.notice_order_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiRetailWmsDeliveryorderprocessQueryModel()
        if 'notice_order_id' in d:
            o.notice_order_id = d['notice_order_id']
        return o


