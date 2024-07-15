#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ETCTripItemDto import ETCTripItemDto


class AlipayCommerceTransportEtcSettlementApplyModel(object):

    def __init__(self):
        self._biz_agreement_no = None
        self._car_type = None
        self._end_station_name = None
        self._end_time = None
        self._etc_trip_item_list = None
        self._memo = None
        self._out_order_id = None
        self._plate_color = None
        self._plate_no = None
        self._replenish_deduct = None
        self._seller_id = None
        self._start_station_name = None
        self._start_time = None
        self._sub_scene = None
        self._sub_type = None
        self._subject = None
        self._total_amount = None

    @property
    def biz_agreement_no(self):
        return self._biz_agreement_no

    @biz_agreement_no.setter
    def biz_agreement_no(self, value):
        self._biz_agreement_no = value
    @property
    def car_type(self):
        return self._car_type

    @car_type.setter
    def car_type(self, value):
        self._car_type = value
    @property
    def end_station_name(self):
        return self._end_station_name

    @end_station_name.setter
    def end_station_name(self, value):
        self._end_station_name = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def etc_trip_item_list(self):
        return self._etc_trip_item_list

    @etc_trip_item_list.setter
    def etc_trip_item_list(self, value):
        if isinstance(value, list):
            self._etc_trip_item_list = list()
            for i in value:
                if isinstance(i, ETCTripItemDto):
                    self._etc_trip_item_list.append(i)
                else:
                    self._etc_trip_item_list.append(ETCTripItemDto.from_alipay_dict(i))
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def out_order_id(self):
        return self._out_order_id

    @out_order_id.setter
    def out_order_id(self, value):
        self._out_order_id = value
    @property
    def plate_color(self):
        return self._plate_color

    @plate_color.setter
    def plate_color(self, value):
        self._plate_color = value
    @property
    def plate_no(self):
        return self._plate_no

    @plate_no.setter
    def plate_no(self, value):
        self._plate_no = value
    @property
    def replenish_deduct(self):
        return self._replenish_deduct

    @replenish_deduct.setter
    def replenish_deduct(self, value):
        self._replenish_deduct = value
    @property
    def seller_id(self):
        return self._seller_id

    @seller_id.setter
    def seller_id(self, value):
        self._seller_id = value
    @property
    def start_station_name(self):
        return self._start_station_name

    @start_station_name.setter
    def start_station_name(self, value):
        self._start_station_name = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def sub_scene(self):
        return self._sub_scene

    @sub_scene.setter
    def sub_scene(self, value):
        self._sub_scene = value
    @property
    def sub_type(self):
        return self._sub_type

    @sub_type.setter
    def sub_type(self, value):
        self._sub_type = value
    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, value):
        self._subject = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_agreement_no:
            if hasattr(self.biz_agreement_no, 'to_alipay_dict'):
                params['biz_agreement_no'] = self.biz_agreement_no.to_alipay_dict()
            else:
                params['biz_agreement_no'] = self.biz_agreement_no
        if self.car_type:
            if hasattr(self.car_type, 'to_alipay_dict'):
                params['car_type'] = self.car_type.to_alipay_dict()
            else:
                params['car_type'] = self.car_type
        if self.end_station_name:
            if hasattr(self.end_station_name, 'to_alipay_dict'):
                params['end_station_name'] = self.end_station_name.to_alipay_dict()
            else:
                params['end_station_name'] = self.end_station_name
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.etc_trip_item_list:
            if isinstance(self.etc_trip_item_list, list):
                for i in range(0, len(self.etc_trip_item_list)):
                    element = self.etc_trip_item_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.etc_trip_item_list[i] = element.to_alipay_dict()
            if hasattr(self.etc_trip_item_list, 'to_alipay_dict'):
                params['etc_trip_item_list'] = self.etc_trip_item_list.to_alipay_dict()
            else:
                params['etc_trip_item_list'] = self.etc_trip_item_list
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.out_order_id:
            if hasattr(self.out_order_id, 'to_alipay_dict'):
                params['out_order_id'] = self.out_order_id.to_alipay_dict()
            else:
                params['out_order_id'] = self.out_order_id
        if self.plate_color:
            if hasattr(self.plate_color, 'to_alipay_dict'):
                params['plate_color'] = self.plate_color.to_alipay_dict()
            else:
                params['plate_color'] = self.plate_color
        if self.plate_no:
            if hasattr(self.plate_no, 'to_alipay_dict'):
                params['plate_no'] = self.plate_no.to_alipay_dict()
            else:
                params['plate_no'] = self.plate_no
        if self.replenish_deduct:
            if hasattr(self.replenish_deduct, 'to_alipay_dict'):
                params['replenish_deduct'] = self.replenish_deduct.to_alipay_dict()
            else:
                params['replenish_deduct'] = self.replenish_deduct
        if self.seller_id:
            if hasattr(self.seller_id, 'to_alipay_dict'):
                params['seller_id'] = self.seller_id.to_alipay_dict()
            else:
                params['seller_id'] = self.seller_id
        if self.start_station_name:
            if hasattr(self.start_station_name, 'to_alipay_dict'):
                params['start_station_name'] = self.start_station_name.to_alipay_dict()
            else:
                params['start_station_name'] = self.start_station_name
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.sub_scene:
            if hasattr(self.sub_scene, 'to_alipay_dict'):
                params['sub_scene'] = self.sub_scene.to_alipay_dict()
            else:
                params['sub_scene'] = self.sub_scene
        if self.sub_type:
            if hasattr(self.sub_type, 'to_alipay_dict'):
                params['sub_type'] = self.sub_type.to_alipay_dict()
            else:
                params['sub_type'] = self.sub_type
        if self.subject:
            if hasattr(self.subject, 'to_alipay_dict'):
                params['subject'] = self.subject.to_alipay_dict()
            else:
                params['subject'] = self.subject
        if self.total_amount:
            if hasattr(self.total_amount, 'to_alipay_dict'):
                params['total_amount'] = self.total_amount.to_alipay_dict()
            else:
                params['total_amount'] = self.total_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceTransportEtcSettlementApplyModel()
        if 'biz_agreement_no' in d:
            o.biz_agreement_no = d['biz_agreement_no']
        if 'car_type' in d:
            o.car_type = d['car_type']
        if 'end_station_name' in d:
            o.end_station_name = d['end_station_name']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'etc_trip_item_list' in d:
            o.etc_trip_item_list = d['etc_trip_item_list']
        if 'memo' in d:
            o.memo = d['memo']
        if 'out_order_id' in d:
            o.out_order_id = d['out_order_id']
        if 'plate_color' in d:
            o.plate_color = d['plate_color']
        if 'plate_no' in d:
            o.plate_no = d['plate_no']
        if 'replenish_deduct' in d:
            o.replenish_deduct = d['replenish_deduct']
        if 'seller_id' in d:
            o.seller_id = d['seller_id']
        if 'start_station_name' in d:
            o.start_station_name = d['start_station_name']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'sub_scene' in d:
            o.sub_scene = d['sub_scene']
        if 'sub_type' in d:
            o.sub_type = d['sub_type']
        if 'subject' in d:
            o.subject = d['subject']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        return o


