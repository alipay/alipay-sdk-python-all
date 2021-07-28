#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiServindustryReservationLeadsModifyModel(object):

    def __init__(self):
        self._gmt_arrived = None
        self._gmt_reserve = None
        self._memo = None
        self._reservation_record_id = None
        self._status_mark = None

    @property
    def gmt_arrived(self):
        return self._gmt_arrived

    @gmt_arrived.setter
    def gmt_arrived(self, value):
        self._gmt_arrived = value
    @property
    def gmt_reserve(self):
        return self._gmt_reserve

    @gmt_reserve.setter
    def gmt_reserve(self, value):
        self._gmt_reserve = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
    @property
    def reservation_record_id(self):
        return self._reservation_record_id

    @reservation_record_id.setter
    def reservation_record_id(self, value):
        self._reservation_record_id = value
    @property
    def status_mark(self):
        return self._status_mark

    @status_mark.setter
    def status_mark(self, value):
        self._status_mark = value


    def to_alipay_dict(self):
        params = dict()
        if self.gmt_arrived:
            if hasattr(self.gmt_arrived, 'to_alipay_dict'):
                params['gmt_arrived'] = self.gmt_arrived.to_alipay_dict()
            else:
                params['gmt_arrived'] = self.gmt_arrived
        if self.gmt_reserve:
            if hasattr(self.gmt_reserve, 'to_alipay_dict'):
                params['gmt_reserve'] = self.gmt_reserve.to_alipay_dict()
            else:
                params['gmt_reserve'] = self.gmt_reserve
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
        if self.reservation_record_id:
            if hasattr(self.reservation_record_id, 'to_alipay_dict'):
                params['reservation_record_id'] = self.reservation_record_id.to_alipay_dict()
            else:
                params['reservation_record_id'] = self.reservation_record_id
        if self.status_mark:
            if hasattr(self.status_mark, 'to_alipay_dict'):
                params['status_mark'] = self.status_mark.to_alipay_dict()
            else:
                params['status_mark'] = self.status_mark
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiServindustryReservationLeadsModifyModel()
        if 'gmt_arrived' in d:
            o.gmt_arrived = d['gmt_arrived']
        if 'gmt_reserve' in d:
            o.gmt_reserve = d['gmt_reserve']
        if 'memo' in d:
            o.memo = d['memo']
        if 'reservation_record_id' in d:
            o.reservation_record_id = d['reservation_record_id']
        if 'status_mark' in d:
            o.status_mark = d['status_mark']
        return o


