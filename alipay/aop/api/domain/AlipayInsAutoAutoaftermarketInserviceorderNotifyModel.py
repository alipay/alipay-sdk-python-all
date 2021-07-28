#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RepairItem import RepairItem


class AlipayInsAutoAutoaftermarketInserviceorderNotifyModel(object):

    def __init__(self):
        self._ant_ser_apply_no = None
        self._event_time = None
        self._extra = None
        self._inst_ser_apply_no = None
        self._repair_item = None
        self._status = None

    @property
    def ant_ser_apply_no(self):
        return self._ant_ser_apply_no

    @ant_ser_apply_no.setter
    def ant_ser_apply_no(self, value):
        self._ant_ser_apply_no = value
    @property
    def event_time(self):
        return self._event_time

    @event_time.setter
    def event_time(self, value):
        self._event_time = value
    @property
    def extra(self):
        return self._extra

    @extra.setter
    def extra(self, value):
        self._extra = value
    @property
    def inst_ser_apply_no(self):
        return self._inst_ser_apply_no

    @inst_ser_apply_no.setter
    def inst_ser_apply_no(self, value):
        self._inst_ser_apply_no = value
    @property
    def repair_item(self):
        return self._repair_item

    @repair_item.setter
    def repair_item(self, value):
        if isinstance(value, list):
            self._repair_item = list()
            for i in value:
                if isinstance(i, RepairItem):
                    self._repair_item.append(i)
                else:
                    self._repair_item.append(RepairItem.from_alipay_dict(i))
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.ant_ser_apply_no:
            if hasattr(self.ant_ser_apply_no, 'to_alipay_dict'):
                params['ant_ser_apply_no'] = self.ant_ser_apply_no.to_alipay_dict()
            else:
                params['ant_ser_apply_no'] = self.ant_ser_apply_no
        if self.event_time:
            if hasattr(self.event_time, 'to_alipay_dict'):
                params['event_time'] = self.event_time.to_alipay_dict()
            else:
                params['event_time'] = self.event_time
        if self.extra:
            if hasattr(self.extra, 'to_alipay_dict'):
                params['extra'] = self.extra.to_alipay_dict()
            else:
                params['extra'] = self.extra
        if self.inst_ser_apply_no:
            if hasattr(self.inst_ser_apply_no, 'to_alipay_dict'):
                params['inst_ser_apply_no'] = self.inst_ser_apply_no.to_alipay_dict()
            else:
                params['inst_ser_apply_no'] = self.inst_ser_apply_no
        if self.repair_item:
            if isinstance(self.repair_item, list):
                for i in range(0, len(self.repair_item)):
                    element = self.repair_item[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.repair_item[i] = element.to_alipay_dict()
            if hasattr(self.repair_item, 'to_alipay_dict'):
                params['repair_item'] = self.repair_item.to_alipay_dict()
            else:
                params['repair_item'] = self.repair_item
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
        o = AlipayInsAutoAutoaftermarketInserviceorderNotifyModel()
        if 'ant_ser_apply_no' in d:
            o.ant_ser_apply_no = d['ant_ser_apply_no']
        if 'event_time' in d:
            o.event_time = d['event_time']
        if 'extra' in d:
            o.extra = d['extra']
        if 'inst_ser_apply_no' in d:
            o.inst_ser_apply_no = d['inst_ser_apply_no']
        if 'repair_item' in d:
            o.repair_item = d['repair_item']
        if 'status' in d:
            o.status = d['status']
        return o


