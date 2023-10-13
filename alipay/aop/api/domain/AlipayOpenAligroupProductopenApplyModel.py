#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ApplyBusinessPropertyDTO import ApplyBusinessPropertyDTO
from alipay.aop.api.domain.ApplyOrderLineDTO import ApplyOrderLineDTO


class AlipayOpenAligroupProductopenApplyModel(object):

    def __init__(self):
        self._business_properties = None
        self._channel_code = None
        self._ctu_event_property = None
        self._order_lines = None
        self._out_biz_no = None
        self._out_request_no = None
        self._partner_id = None

    @property
    def business_properties(self):
        return self._business_properties

    @business_properties.setter
    def business_properties(self, value):
        if isinstance(value, ApplyBusinessPropertyDTO):
            self._business_properties = value
        else:
            self._business_properties = ApplyBusinessPropertyDTO.from_alipay_dict(value)
    @property
    def channel_code(self):
        return self._channel_code

    @channel_code.setter
    def channel_code(self, value):
        self._channel_code = value
    @property
    def ctu_event_property(self):
        return self._ctu_event_property

    @ctu_event_property.setter
    def ctu_event_property(self, value):
        self._ctu_event_property = value
    @property
    def order_lines(self):
        return self._order_lines

    @order_lines.setter
    def order_lines(self, value):
        if isinstance(value, list):
            self._order_lines = list()
            for i in value:
                if isinstance(i, ApplyOrderLineDTO):
                    self._order_lines.append(i)
                else:
                    self._order_lines.append(ApplyOrderLineDTO.from_alipay_dict(i))
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.business_properties:
            if hasattr(self.business_properties, 'to_alipay_dict'):
                params['business_properties'] = self.business_properties.to_alipay_dict()
            else:
                params['business_properties'] = self.business_properties
        if self.channel_code:
            if hasattr(self.channel_code, 'to_alipay_dict'):
                params['channel_code'] = self.channel_code.to_alipay_dict()
            else:
                params['channel_code'] = self.channel_code
        if self.ctu_event_property:
            if hasattr(self.ctu_event_property, 'to_alipay_dict'):
                params['ctu_event_property'] = self.ctu_event_property.to_alipay_dict()
            else:
                params['ctu_event_property'] = self.ctu_event_property
        if self.order_lines:
            if isinstance(self.order_lines, list):
                for i in range(0, len(self.order_lines)):
                    element = self.order_lines[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.order_lines[i] = element.to_alipay_dict()
            if hasattr(self.order_lines, 'to_alipay_dict'):
                params['order_lines'] = self.order_lines.to_alipay_dict()
            else:
                params['order_lines'] = self.order_lines
        if self.out_biz_no:
            if hasattr(self.out_biz_no, 'to_alipay_dict'):
                params['out_biz_no'] = self.out_biz_no.to_alipay_dict()
            else:
                params['out_biz_no'] = self.out_biz_no
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAligroupProductopenApplyModel()
        if 'business_properties' in d:
            o.business_properties = d['business_properties']
        if 'channel_code' in d:
            o.channel_code = d['channel_code']
        if 'ctu_event_property' in d:
            o.ctu_event_property = d['ctu_event_property']
        if 'order_lines' in d:
            o.order_lines = d['order_lines']
        if 'out_biz_no' in d:
            o.out_biz_no = d['out_biz_no']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        return o


