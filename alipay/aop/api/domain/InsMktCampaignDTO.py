#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InsMktCouponConfigDTO import InsMktCouponConfigDTO
from alipay.aop.api.domain.InsMktObjectDTO import InsMktObjectDTO


class InsMktCampaignDTO(object):

    def __init__(self):
        self._campaign_id = None
        self._circulation = None
        self._coupon_config = None
        self._end_time = None
        self._memo = None
        self._mkt_objects = None
        self._name = None
        self._send_algorithm = None
        self._send_frqnc_type = None
        self._send_frqnc_value = None
        self._start_time = None
        self._status = None

    @property
    def campaign_id(self):
        return self._campaign_id

    @campaign_id.setter
    def campaign_id(self, value):
        self._campaign_id = value
    @property
    def circulation(self):
        return self._circulation

    @circulation.setter
    def circulation(self, value):
        self._circulation = value
    @property
    def coupon_config(self):
        return self._coupon_config

    @coupon_config.setter
    def coupon_config(self, value):
        if isinstance(value, InsMktCouponConfigDTO):
            self._coupon_config = value
        else:
            self._coupon_config = InsMktCouponConfigDTO.from_alipay_dict(value)
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def mkt_objects(self):
        return self._mkt_objects

    @mkt_objects.setter
    def mkt_objects(self, value):
        if isinstance(value, list):
            self._mkt_objects = list()
            for i in value:
                if isinstance(i, InsMktObjectDTO):
                    self._mkt_objects.append(i)
                else:
                    self._mkt_objects.append(InsMktObjectDTO.from_alipay_dict(i))
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def send_algorithm(self):
        return self._send_algorithm

    @send_algorithm.setter
    def send_algorithm(self, value):
        self._send_algorithm = value
    @property
    def send_frqnc_type(self):
        return self._send_frqnc_type

    @send_frqnc_type.setter
    def send_frqnc_type(self, value):
        self._send_frqnc_type = value
    @property
    def send_frqnc_value(self):
        return self._send_frqnc_value

    @send_frqnc_value.setter
    def send_frqnc_value(self, value):
        self._send_frqnc_value = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.campaign_id:
            if hasattr(self.campaign_id, 'to_alipay_dict'):
                params['campaign_id'] = self.campaign_id.to_alipay_dict()
            else:
                params['campaign_id'] = self.campaign_id
        if self.circulation:
            if hasattr(self.circulation, 'to_alipay_dict'):
                params['circulation'] = self.circulation.to_alipay_dict()
            else:
                params['circulation'] = self.circulation
        if self.coupon_config:
            if hasattr(self.coupon_config, 'to_alipay_dict'):
                params['coupon_config'] = self.coupon_config.to_alipay_dict()
            else:
                params['coupon_config'] = self.coupon_config
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.mkt_objects:
            if isinstance(self.mkt_objects, list):
                for i in range(0, len(self.mkt_objects)):
                    element = self.mkt_objects[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.mkt_objects[i] = element.to_alipay_dict()
            if hasattr(self.mkt_objects, 'to_alipay_dict'):
                params['mkt_objects'] = self.mkt_objects.to_alipay_dict()
            else:
                params['mkt_objects'] = self.mkt_objects
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.send_algorithm:
            if hasattr(self.send_algorithm, 'to_alipay_dict'):
                params['send_algorithm'] = self.send_algorithm.to_alipay_dict()
            else:
                params['send_algorithm'] = self.send_algorithm
        if self.send_frqnc_type:
            if hasattr(self.send_frqnc_type, 'to_alipay_dict'):
                params['send_frqnc_type'] = self.send_frqnc_type.to_alipay_dict()
            else:
                params['send_frqnc_type'] = self.send_frqnc_type
        if self.send_frqnc_value:
            if hasattr(self.send_frqnc_value, 'to_alipay_dict'):
                params['send_frqnc_value'] = self.send_frqnc_value.to_alipay_dict()
            else:
                params['send_frqnc_value'] = self.send_frqnc_value
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InsMktCampaignDTO()
        if 'campaign_id' in d:
            o.campaign_id = d['campaign_id']
        if 'circulation' in d:
            o.circulation = d['circulation']
        if 'coupon_config' in d:
            o.coupon_config = d['coupon_config']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'memo' in d:
            o.memo = d['memo']
        if 'mkt_objects' in d:
            o.mkt_objects = d['mkt_objects']
        if 'name' in d:
            o.name = d['name']
        if 'send_algorithm' in d:
            o.send_algorithm = d['send_algorithm']
        if 'send_frqnc_type' in d:
            o.send_frqnc_type = d['send_frqnc_type']
        if 'send_frqnc_value' in d:
            o.send_frqnc_value = d['send_frqnc_value']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'status' in d:
            o.status = d['status']
        return o


