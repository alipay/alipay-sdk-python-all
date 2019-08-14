#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiSalesKbassetStuffFeedbackstockorderSyncModel(object):

    def __init__(self):
        self._erp_order = None
        self._ext_info = None
        self._feedback_type = None

    @property
    def erp_order(self):
        return self._erp_order

    @erp_order.setter
    def erp_order(self, value):
        self._erp_order = value
    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def feedback_type(self):
        return self._feedback_type

    @feedback_type.setter
    def feedback_type(self, value):
        self._feedback_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.erp_order:
            if hasattr(self.erp_order, 'to_alipay_dict'):
                params['erp_order'] = self.erp_order.to_alipay_dict()
            else:
                params['erp_order'] = self.erp_order
        if self.ext_info:
            if hasattr(self.ext_info, 'to_alipay_dict'):
                params['ext_info'] = self.ext_info.to_alipay_dict()
            else:
                params['ext_info'] = self.ext_info
        if self.feedback_type:
            if hasattr(self.feedback_type, 'to_alipay_dict'):
                params['feedback_type'] = self.feedback_type.to_alipay_dict()
            else:
                params['feedback_type'] = self.feedback_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiSalesKbassetStuffFeedbackstockorderSyncModel()
        if 'erp_order' in d:
            o.erp_order = d['erp_order']
        if 'ext_info' in d:
            o.ext_info = d['ext_info']
        if 'feedback_type' in d:
            o.feedback_type = d['feedback_type']
        return o


