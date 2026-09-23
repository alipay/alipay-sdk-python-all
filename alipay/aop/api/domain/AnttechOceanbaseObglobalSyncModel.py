#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechOceanbaseObglobalSyncModel(object):

    def __init__(self):
        self._delivery_sync_event_id = None
        self._delivery_time = None
        self._general_agency_order_no = None
        self._quotation_no = None

    @property
    def delivery_sync_event_id(self):
        return self._delivery_sync_event_id

    @delivery_sync_event_id.setter
    def delivery_sync_event_id(self, value):
        self._delivery_sync_event_id = value
    @property
    def delivery_time(self):
        return self._delivery_time

    @delivery_time.setter
    def delivery_time(self, value):
        self._delivery_time = value
    @property
    def general_agency_order_no(self):
        return self._general_agency_order_no

    @general_agency_order_no.setter
    def general_agency_order_no(self, value):
        self._general_agency_order_no = value
    @property
    def quotation_no(self):
        return self._quotation_no

    @quotation_no.setter
    def quotation_no(self, value):
        self._quotation_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.delivery_sync_event_id:
            if hasattr(self.delivery_sync_event_id, 'to_alipay_dict'):
                params['delivery_sync_event_id'] = self.delivery_sync_event_id.to_alipay_dict()
            else:
                params['delivery_sync_event_id'] = self.delivery_sync_event_id
        if self.delivery_time:
            if hasattr(self.delivery_time, 'to_alipay_dict'):
                params['delivery_time'] = self.delivery_time.to_alipay_dict()
            else:
                params['delivery_time'] = self.delivery_time
        if self.general_agency_order_no:
            if hasattr(self.general_agency_order_no, 'to_alipay_dict'):
                params['general_agency_order_no'] = self.general_agency_order_no.to_alipay_dict()
            else:
                params['general_agency_order_no'] = self.general_agency_order_no
        if self.quotation_no:
            if hasattr(self.quotation_no, 'to_alipay_dict'):
                params['quotation_no'] = self.quotation_no.to_alipay_dict()
            else:
                params['quotation_no'] = self.quotation_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechOceanbaseObglobalSyncModel()
        if 'delivery_sync_event_id' in d:
            o.delivery_sync_event_id = d['delivery_sync_event_id']
        if 'delivery_time' in d:
            o.delivery_time = d['delivery_time']
        if 'general_agency_order_no' in d:
            o.general_agency_order_no = d['general_agency_order_no']
        if 'quotation_no' in d:
            o.quotation_no = d['quotation_no']
        return o


