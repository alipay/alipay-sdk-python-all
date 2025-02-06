#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.VoyagerOrderRebookInfo import VoyagerOrderRebookInfo
from alipay.aop.api.domain.VoyagerSegmentOfPassengersCancelledInfo import VoyagerSegmentOfPassengersCancelledInfo
from alipay.aop.api.domain.VoyagerSegmentOfPassengersChangedInfo import VoyagerSegmentOfPassengersChangedInfo
from alipay.aop.api.domain.VoyagerSegmentOfPassengersCancelledInfo import VoyagerSegmentOfPassengersCancelledInfo


class AlipayVoyagerFlightSupplierNotifyModel(object):

    def __init__(self):
        self._event_type = None
        self._occurrence_time = None
        self._order_id = None
        self._rebook_info = None
        self._refund_id = None
        self._segment_of_passengers_cancelled = None
        self._segment_of_passengers_changed = None
        self._segment_of_passengers_refund_info = None

    @property
    def event_type(self):
        return self._event_type

    @event_type.setter
    def event_type(self, value):
        self._event_type = value
    @property
    def occurrence_time(self):
        return self._occurrence_time

    @occurrence_time.setter
    def occurrence_time(self, value):
        self._occurrence_time = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def rebook_info(self):
        return self._rebook_info

    @rebook_info.setter
    def rebook_info(self, value):
        if isinstance(value, VoyagerOrderRebookInfo):
            self._rebook_info = value
        else:
            self._rebook_info = VoyagerOrderRebookInfo.from_alipay_dict(value)
    @property
    def refund_id(self):
        return self._refund_id

    @refund_id.setter
    def refund_id(self, value):
        self._refund_id = value
    @property
    def segment_of_passengers_cancelled(self):
        return self._segment_of_passengers_cancelled

    @segment_of_passengers_cancelled.setter
    def segment_of_passengers_cancelled(self, value):
        if isinstance(value, list):
            self._segment_of_passengers_cancelled = list()
            for i in value:
                if isinstance(i, VoyagerSegmentOfPassengersCancelledInfo):
                    self._segment_of_passengers_cancelled.append(i)
                else:
                    self._segment_of_passengers_cancelled.append(VoyagerSegmentOfPassengersCancelledInfo.from_alipay_dict(i))
    @property
    def segment_of_passengers_changed(self):
        return self._segment_of_passengers_changed

    @segment_of_passengers_changed.setter
    def segment_of_passengers_changed(self, value):
        if isinstance(value, list):
            self._segment_of_passengers_changed = list()
            for i in value:
                if isinstance(i, VoyagerSegmentOfPassengersChangedInfo):
                    self._segment_of_passengers_changed.append(i)
                else:
                    self._segment_of_passengers_changed.append(VoyagerSegmentOfPassengersChangedInfo.from_alipay_dict(i))
    @property
    def segment_of_passengers_refund_info(self):
        return self._segment_of_passengers_refund_info

    @segment_of_passengers_refund_info.setter
    def segment_of_passengers_refund_info(self, value):
        if isinstance(value, list):
            self._segment_of_passengers_refund_info = list()
            for i in value:
                if isinstance(i, VoyagerSegmentOfPassengersCancelledInfo):
                    self._segment_of_passengers_refund_info.append(i)
                else:
                    self._segment_of_passengers_refund_info.append(VoyagerSegmentOfPassengersCancelledInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.event_type:
            if hasattr(self.event_type, 'to_alipay_dict'):
                params['event_type'] = self.event_type.to_alipay_dict()
            else:
                params['event_type'] = self.event_type
        if self.occurrence_time:
            if hasattr(self.occurrence_time, 'to_alipay_dict'):
                params['occurrence_time'] = self.occurrence_time.to_alipay_dict()
            else:
                params['occurrence_time'] = self.occurrence_time
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.rebook_info:
            if hasattr(self.rebook_info, 'to_alipay_dict'):
                params['rebook_info'] = self.rebook_info.to_alipay_dict()
            else:
                params['rebook_info'] = self.rebook_info
        if self.refund_id:
            if hasattr(self.refund_id, 'to_alipay_dict'):
                params['refund_id'] = self.refund_id.to_alipay_dict()
            else:
                params['refund_id'] = self.refund_id
        if self.segment_of_passengers_cancelled:
            if isinstance(self.segment_of_passengers_cancelled, list):
                for i in range(0, len(self.segment_of_passengers_cancelled)):
                    element = self.segment_of_passengers_cancelled[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.segment_of_passengers_cancelled[i] = element.to_alipay_dict()
            if hasattr(self.segment_of_passengers_cancelled, 'to_alipay_dict'):
                params['segment_of_passengers_cancelled'] = self.segment_of_passengers_cancelled.to_alipay_dict()
            else:
                params['segment_of_passengers_cancelled'] = self.segment_of_passengers_cancelled
        if self.segment_of_passengers_changed:
            if isinstance(self.segment_of_passengers_changed, list):
                for i in range(0, len(self.segment_of_passengers_changed)):
                    element = self.segment_of_passengers_changed[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.segment_of_passengers_changed[i] = element.to_alipay_dict()
            if hasattr(self.segment_of_passengers_changed, 'to_alipay_dict'):
                params['segment_of_passengers_changed'] = self.segment_of_passengers_changed.to_alipay_dict()
            else:
                params['segment_of_passengers_changed'] = self.segment_of_passengers_changed
        if self.segment_of_passengers_refund_info:
            if isinstance(self.segment_of_passengers_refund_info, list):
                for i in range(0, len(self.segment_of_passengers_refund_info)):
                    element = self.segment_of_passengers_refund_info[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.segment_of_passengers_refund_info[i] = element.to_alipay_dict()
            if hasattr(self.segment_of_passengers_refund_info, 'to_alipay_dict'):
                params['segment_of_passengers_refund_info'] = self.segment_of_passengers_refund_info.to_alipay_dict()
            else:
                params['segment_of_passengers_refund_info'] = self.segment_of_passengers_refund_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayVoyagerFlightSupplierNotifyModel()
        if 'event_type' in d:
            o.event_type = d['event_type']
        if 'occurrence_time' in d:
            o.occurrence_time = d['occurrence_time']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'rebook_info' in d:
            o.rebook_info = d['rebook_info']
        if 'refund_id' in d:
            o.refund_id = d['refund_id']
        if 'segment_of_passengers_cancelled' in d:
            o.segment_of_passengers_cancelled = d['segment_of_passengers_cancelled']
        if 'segment_of_passengers_changed' in d:
            o.segment_of_passengers_changed = d['segment_of_passengers_changed']
        if 'segment_of_passengers_refund_info' in d:
            o.segment_of_passengers_refund_info = d['segment_of_passengers_refund_info']
        return o


