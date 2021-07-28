#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.VehicleMessageInfo import VehicleMessageInfo


class AlipaySecurityProdIfaatamMessagenotifySendModel(object):

    def __init__(self):
        self._biz_type = None
        self._box_did = None
        self._business_id = None
        self._car_info_seq_no = None
        self._partner_id = None
        self._tbox_time = None
        self._vehicle_message_info = None

    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def box_did(self):
        return self._box_did

    @box_did.setter
    def box_did(self, value):
        self._box_did = value
    @property
    def business_id(self):
        return self._business_id

    @business_id.setter
    def business_id(self, value):
        self._business_id = value
    @property
    def car_info_seq_no(self):
        return self._car_info_seq_no

    @car_info_seq_no.setter
    def car_info_seq_no(self, value):
        self._car_info_seq_no = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def tbox_time(self):
        return self._tbox_time

    @tbox_time.setter
    def tbox_time(self, value):
        self._tbox_time = value
    @property
    def vehicle_message_info(self):
        return self._vehicle_message_info

    @vehicle_message_info.setter
    def vehicle_message_info(self, value):
        if isinstance(value, VehicleMessageInfo):
            self._vehicle_message_info = value
        else:
            self._vehicle_message_info = VehicleMessageInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.box_did:
            if hasattr(self.box_did, 'to_alipay_dict'):
                params['box_did'] = self.box_did.to_alipay_dict()
            else:
                params['box_did'] = self.box_did
        if self.business_id:
            if hasattr(self.business_id, 'to_alipay_dict'):
                params['business_id'] = self.business_id.to_alipay_dict()
            else:
                params['business_id'] = self.business_id
        if self.car_info_seq_no:
            if hasattr(self.car_info_seq_no, 'to_alipay_dict'):
                params['car_info_seq_no'] = self.car_info_seq_no.to_alipay_dict()
            else:
                params['car_info_seq_no'] = self.car_info_seq_no
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        if self.tbox_time:
            if hasattr(self.tbox_time, 'to_alipay_dict'):
                params['tbox_time'] = self.tbox_time.to_alipay_dict()
            else:
                params['tbox_time'] = self.tbox_time
        if self.vehicle_message_info:
            if hasattr(self.vehicle_message_info, 'to_alipay_dict'):
                params['vehicle_message_info'] = self.vehicle_message_info.to_alipay_dict()
            else:
                params['vehicle_message_info'] = self.vehicle_message_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityProdIfaatamMessagenotifySendModel()
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'box_did' in d:
            o.box_did = d['box_did']
        if 'business_id' in d:
            o.business_id = d['business_id']
        if 'car_info_seq_no' in d:
            o.car_info_seq_no = d['car_info_seq_no']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'tbox_time' in d:
            o.tbox_time = d['tbox_time']
        if 'vehicle_message_info' in d:
            o.vehicle_message_info = d['vehicle_message_info']
        return o


