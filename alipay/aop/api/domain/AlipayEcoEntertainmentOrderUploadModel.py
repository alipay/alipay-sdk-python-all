#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EntertainmentOrderInfo import EntertainmentOrderInfo


class AlipayEcoEntertainmentOrderUploadModel(object):

    def __init__(self):
        self._entertainment_order_info = None

    @property
    def entertainment_order_info(self):
        return self._entertainment_order_info

    @entertainment_order_info.setter
    def entertainment_order_info(self, value):
        if isinstance(value, EntertainmentOrderInfo):
            self._entertainment_order_info = value
        else:
            self._entertainment_order_info = EntertainmentOrderInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.entertainment_order_info:
            if hasattr(self.entertainment_order_info, 'to_alipay_dict'):
                params['entertainment_order_info'] = self.entertainment_order_info.to_alipay_dict()
            else:
                params['entertainment_order_info'] = self.entertainment_order_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoEntertainmentOrderUploadModel()
        if 'entertainment_order_info' in d:
            o.entertainment_order_info = d['entertainment_order_info']
        return o


