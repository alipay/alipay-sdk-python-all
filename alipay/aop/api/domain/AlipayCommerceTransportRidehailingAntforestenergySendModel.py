#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceTransportRidehailingAntforestenergySendModel(object):

    def __init__(self):
        self._ant_forest_order_id = None
        self._car_no = None
        self._ride_hailing_app_id = None
        self._ride_hailing_order_id = None
        self._ride_hailing_partner_id = None
        self._trade_no = None

    @property
    def ant_forest_order_id(self):
        return self._ant_forest_order_id

    @ant_forest_order_id.setter
    def ant_forest_order_id(self, value):
        self._ant_forest_order_id = value
    @property
    def car_no(self):
        return self._car_no

    @car_no.setter
    def car_no(self, value):
        self._car_no = value
    @property
    def ride_hailing_app_id(self):
        return self._ride_hailing_app_id

    @ride_hailing_app_id.setter
    def ride_hailing_app_id(self, value):
        self._ride_hailing_app_id = value
    @property
    def ride_hailing_order_id(self):
        return self._ride_hailing_order_id

    @ride_hailing_order_id.setter
    def ride_hailing_order_id(self, value):
        self._ride_hailing_order_id = value
    @property
    def ride_hailing_partner_id(self):
        return self._ride_hailing_partner_id

    @ride_hailing_partner_id.setter
    def ride_hailing_partner_id(self, value):
        self._ride_hailing_partner_id = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.ant_forest_order_id:
            if hasattr(self.ant_forest_order_id, 'to_alipay_dict'):
                params['ant_forest_order_id'] = self.ant_forest_order_id.to_alipay_dict()
            else:
                params['ant_forest_order_id'] = self.ant_forest_order_id
        if self.car_no:
            if hasattr(self.car_no, 'to_alipay_dict'):
                params['car_no'] = self.car_no.to_alipay_dict()
            else:
                params['car_no'] = self.car_no
        if self.ride_hailing_app_id:
            if hasattr(self.ride_hailing_app_id, 'to_alipay_dict'):
                params['ride_hailing_app_id'] = self.ride_hailing_app_id.to_alipay_dict()
            else:
                params['ride_hailing_app_id'] = self.ride_hailing_app_id
        if self.ride_hailing_order_id:
            if hasattr(self.ride_hailing_order_id, 'to_alipay_dict'):
                params['ride_hailing_order_id'] = self.ride_hailing_order_id.to_alipay_dict()
            else:
                params['ride_hailing_order_id'] = self.ride_hailing_order_id
        if self.ride_hailing_partner_id:
            if hasattr(self.ride_hailing_partner_id, 'to_alipay_dict'):
                params['ride_hailing_partner_id'] = self.ride_hailing_partner_id.to_alipay_dict()
            else:
                params['ride_hailing_partner_id'] = self.ride_hailing_partner_id
        if self.trade_no:
            if hasattr(self.trade_no, 'to_alipay_dict'):
                params['trade_no'] = self.trade_no.to_alipay_dict()
            else:
                params['trade_no'] = self.trade_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportRidehailingAntforestenergySendModel()
        if 'ant_forest_order_id' in d:
            o.ant_forest_order_id = d['ant_forest_order_id']
        if 'car_no' in d:
            o.car_no = d['car_no']
        if 'ride_hailing_app_id' in d:
            o.ride_hailing_app_id = d['ride_hailing_app_id']
        if 'ride_hailing_order_id' in d:
            o.ride_hailing_order_id = d['ride_hailing_order_id']
        if 'ride_hailing_partner_id' in d:
            o.ride_hailing_partner_id = d['ride_hailing_partner_id']
        if 'trade_no' in d:
            o.trade_no = d['trade_no']
        return o


