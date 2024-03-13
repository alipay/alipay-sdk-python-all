#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ForwardFeedbackOrderRequest import ForwardFeedbackOrderRequest


class AlipayIserviceItaskOutorderForwardFinishModel(object):

    def __init__(self):
        self._forward_feedback_order_request = None

    @property
    def forward_feedback_order_request(self):
        return self._forward_feedback_order_request

    @forward_feedback_order_request.setter
    def forward_feedback_order_request(self, value):
        if isinstance(value, ForwardFeedbackOrderRequest):
            self._forward_feedback_order_request = value
        else:
            self._forward_feedback_order_request = ForwardFeedbackOrderRequest.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.forward_feedback_order_request:
            if hasattr(self.forward_feedback_order_request, 'to_alipay_dict'):
                params['forward_feedback_order_request'] = self.forward_feedback_order_request.to_alipay_dict()
            else:
                params['forward_feedback_order_request'] = self.forward_feedback_order_request
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayIserviceItaskOutorderForwardFinishModel()
        if 'forward_feedback_order_request' in d:
            o.forward_feedback_order_request = d['forward_feedback_order_request']
        return o


