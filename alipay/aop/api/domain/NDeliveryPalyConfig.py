#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.NDeliveryContentInfo import NDeliveryContentInfo


class NDeliveryPalyConfig(object):

    def __init__(self):
        self._n_delivery_content_info = None
        self._n_delivery_send_mode = None

    @property
    def n_delivery_content_info(self):
        return self._n_delivery_content_info

    @n_delivery_content_info.setter
    def n_delivery_content_info(self, value):
        if isinstance(value, NDeliveryContentInfo):
            self._n_delivery_content_info = value
        else:
            self._n_delivery_content_info = NDeliveryContentInfo.from_alipay_dict(value)
    @property
    def n_delivery_send_mode(self):
        return self._n_delivery_send_mode

    @n_delivery_send_mode.setter
    def n_delivery_send_mode(self, value):
        self._n_delivery_send_mode = value


    def to_alipay_dict(self):
        params = dict()
        if self.n_delivery_content_info:
            if hasattr(self.n_delivery_content_info, 'to_alipay_dict'):
                params['n_delivery_content_info'] = self.n_delivery_content_info.to_alipay_dict()
            else:
                params['n_delivery_content_info'] = self.n_delivery_content_info
        if self.n_delivery_send_mode:
            if hasattr(self.n_delivery_send_mode, 'to_alipay_dict'):
                params['n_delivery_send_mode'] = self.n_delivery_send_mode.to_alipay_dict()
            else:
                params['n_delivery_send_mode'] = self.n_delivery_send_mode
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = NDeliveryPalyConfig()
        if 'n_delivery_content_info' in d:
            o.n_delivery_content_info = d['n_delivery_content_info']
        if 'n_delivery_send_mode' in d:
            o.n_delivery_send_mode = d['n_delivery_send_mode']
        return o


