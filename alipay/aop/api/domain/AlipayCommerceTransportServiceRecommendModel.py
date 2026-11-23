#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TransportServiceRecommendTravelLog import TransportServiceRecommendTravelLog


class AlipayCommerceTransportServiceRecommendModel(object):

    def __init__(self):
        self._card_no = None
        self._issue_id = None
        self._location_ciphertext = None
        self._location_key_id = None
        self._mtd_amount = None
        self._out_request_no = None
        self._station = None
        self._travel_log_list = None

    @property
    def card_no(self):
        return self._card_no

    @card_no.setter
    def card_no(self, value):
        self._card_no = value
    @property
    def issue_id(self):
        return self._issue_id

    @issue_id.setter
    def issue_id(self, value):
        self._issue_id = value
    @property
    def location_ciphertext(self):
        return self._location_ciphertext

    @location_ciphertext.setter
    def location_ciphertext(self, value):
        self._location_ciphertext = value
    @property
    def location_key_id(self):
        return self._location_key_id

    @location_key_id.setter
    def location_key_id(self, value):
        self._location_key_id = value
    @property
    def mtd_amount(self):
        return self._mtd_amount

    @mtd_amount.setter
    def mtd_amount(self, value):
        self._mtd_amount = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def station(self):
        return self._station

    @station.setter
    def station(self, value):
        self._station = value
    @property
    def travel_log_list(self):
        return self._travel_log_list

    @travel_log_list.setter
    def travel_log_list(self, value):
        if isinstance(value, list):
            self._travel_log_list = list()
            for i in value:
                if isinstance(i, TransportServiceRecommendTravelLog):
                    self._travel_log_list.append(i)
                else:
                    self._travel_log_list.append(TransportServiceRecommendTravelLog.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.card_no:
            if hasattr(self.card_no, 'to_alipay_dict'):
                params['card_no'] = self.card_no.to_alipay_dict()
            else:
                params['card_no'] = self.card_no
        if self.issue_id:
            if hasattr(self.issue_id, 'to_alipay_dict'):
                params['issue_id'] = self.issue_id.to_alipay_dict()
            else:
                params['issue_id'] = self.issue_id
        if self.location_ciphertext:
            if hasattr(self.location_ciphertext, 'to_alipay_dict'):
                params['location_ciphertext'] = self.location_ciphertext.to_alipay_dict()
            else:
                params['location_ciphertext'] = self.location_ciphertext
        if self.location_key_id:
            if hasattr(self.location_key_id, 'to_alipay_dict'):
                params['location_key_id'] = self.location_key_id.to_alipay_dict()
            else:
                params['location_key_id'] = self.location_key_id
        if self.mtd_amount:
            if hasattr(self.mtd_amount, 'to_alipay_dict'):
                params['mtd_amount'] = self.mtd_amount.to_alipay_dict()
            else:
                params['mtd_amount'] = self.mtd_amount
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        if self.station:
            if hasattr(self.station, 'to_alipay_dict'):
                params['station'] = self.station.to_alipay_dict()
            else:
                params['station'] = self.station
        if self.travel_log_list:
            if isinstance(self.travel_log_list, list):
                for i in range(0, len(self.travel_log_list)):
                    element = self.travel_log_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.travel_log_list[i] = element.to_alipay_dict()
            if hasattr(self.travel_log_list, 'to_alipay_dict'):
                params['travel_log_list'] = self.travel_log_list.to_alipay_dict()
            else:
                params['travel_log_list'] = self.travel_log_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportServiceRecommendModel()
        if 'card_no' in d:
            o.card_no = d['card_no']
        if 'issue_id' in d:
            o.issue_id = d['issue_id']
        if 'location_ciphertext' in d:
            o.location_ciphertext = d['location_ciphertext']
        if 'location_key_id' in d:
            o.location_key_id = d['location_key_id']
        if 'mtd_amount' in d:
            o.mtd_amount = d['mtd_amount']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'station' in d:
            o.station = d['station']
        if 'travel_log_list' in d:
            o.travel_log_list = d['travel_log_list']
        return o


