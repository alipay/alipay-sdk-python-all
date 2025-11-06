#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InquiryEventInfo import InquiryEventInfo


class AlipayCommerceMedicalOuterorderEventNotifyModel(object):

    def __init__(self):
        self._consult_business = None
        self._event_business = None
        self._fulfillment_order_id = None
        self._partner_order_id = None
        self._vedio_event_info = None

    @property
    def consult_business(self):
        return self._consult_business

    @consult_business.setter
    def consult_business(self, value):
        self._consult_business = value
    @property
    def event_business(self):
        return self._event_business

    @event_business.setter
    def event_business(self, value):
        self._event_business = value
    @property
    def fulfillment_order_id(self):
        return self._fulfillment_order_id

    @fulfillment_order_id.setter
    def fulfillment_order_id(self, value):
        self._fulfillment_order_id = value
    @property
    def partner_order_id(self):
        return self._partner_order_id

    @partner_order_id.setter
    def partner_order_id(self, value):
        self._partner_order_id = value
    @property
    def vedio_event_info(self):
        return self._vedio_event_info

    @vedio_event_info.setter
    def vedio_event_info(self, value):
        if isinstance(value, InquiryEventInfo):
            self._vedio_event_info = value
        else:
            self._vedio_event_info = InquiryEventInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.consult_business:
            if hasattr(self.consult_business, 'to_alipay_dict'):
                params['consult_business'] = self.consult_business.to_alipay_dict()
            else:
                params['consult_business'] = self.consult_business
        if self.event_business:
            if hasattr(self.event_business, 'to_alipay_dict'):
                params['event_business'] = self.event_business.to_alipay_dict()
            else:
                params['event_business'] = self.event_business
        if self.fulfillment_order_id:
            if hasattr(self.fulfillment_order_id, 'to_alipay_dict'):
                params['fulfillment_order_id'] = self.fulfillment_order_id.to_alipay_dict()
            else:
                params['fulfillment_order_id'] = self.fulfillment_order_id
        if self.partner_order_id:
            if hasattr(self.partner_order_id, 'to_alipay_dict'):
                params['partner_order_id'] = self.partner_order_id.to_alipay_dict()
            else:
                params['partner_order_id'] = self.partner_order_id
        if self.vedio_event_info:
            if hasattr(self.vedio_event_info, 'to_alipay_dict'):
                params['vedio_event_info'] = self.vedio_event_info.to_alipay_dict()
            else:
                params['vedio_event_info'] = self.vedio_event_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalOuterorderEventNotifyModel()
        if 'consult_business' in d:
            o.consult_business = d['consult_business']
        if 'event_business' in d:
            o.event_business = d['event_business']
        if 'fulfillment_order_id' in d:
            o.fulfillment_order_id = d['fulfillment_order_id']
        if 'partner_order_id' in d:
            o.partner_order_id = d['partner_order_id']
        if 'vedio_event_info' in d:
            o.vedio_event_info = d['vedio_event_info']
        return o


