#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.IcInboundSeatEventModel import IcInboundSeatEventModel


class AlipayIserviceIcontrolSeateventUploadModel(object):

    def __init__(self):
        self._ic_inbound_seat_event_payload = None
        self._order_id = None
        self._order_type = None
        self._service_uniq_code = None

    @property
    def ic_inbound_seat_event_payload(self):
        return self._ic_inbound_seat_event_payload

    @ic_inbound_seat_event_payload.setter
    def ic_inbound_seat_event_payload(self, value):
        if isinstance(value, IcInboundSeatEventModel):
            self._ic_inbound_seat_event_payload = value
        else:
            self._ic_inbound_seat_event_payload = IcInboundSeatEventModel.from_alipay_dict(value)
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def order_type(self):
        return self._order_type

    @order_type.setter
    def order_type(self, value):
        self._order_type = value
    @property
    def service_uniq_code(self):
        return self._service_uniq_code

    @service_uniq_code.setter
    def service_uniq_code(self, value):
        self._service_uniq_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.ic_inbound_seat_event_payload:
            if hasattr(self.ic_inbound_seat_event_payload, 'to_alipay_dict'):
                params['ic_inbound_seat_event_payload'] = self.ic_inbound_seat_event_payload.to_alipay_dict()
            else:
                params['ic_inbound_seat_event_payload'] = self.ic_inbound_seat_event_payload
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.order_type:
            if hasattr(self.order_type, 'to_alipay_dict'):
                params['order_type'] = self.order_type.to_alipay_dict()
            else:
                params['order_type'] = self.order_type
        if self.service_uniq_code:
            if hasattr(self.service_uniq_code, 'to_alipay_dict'):
                params['service_uniq_code'] = self.service_uniq_code.to_alipay_dict()
            else:
                params['service_uniq_code'] = self.service_uniq_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayIserviceIcontrolSeateventUploadModel()
        if 'ic_inbound_seat_event_payload' in d:
            o.ic_inbound_seat_event_payload = d['ic_inbound_seat_event_payload']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'order_type' in d:
            o.order_type = d['order_type']
        if 'service_uniq_code' in d:
            o.service_uniq_code = d['service_uniq_code']
        return o


