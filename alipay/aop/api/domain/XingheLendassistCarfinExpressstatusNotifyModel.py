#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CarfinCourier import CarfinCourier
from alipay.aop.api.domain.CarfinExpressFile import CarfinExpressFile


class XingheLendassistCarfinExpressstatusNotifyModel(object):

    def __init__(self):
        self._alert_reason = None
        self._courier_info = None
        self._estimated_delivery_date = None
        self._express_no = None
        self._file_list = None
        self._notify_type = None
        self._out_express_no = None
        self._status = None

    @property
    def alert_reason(self):
        return self._alert_reason

    @alert_reason.setter
    def alert_reason(self, value):
        self._alert_reason = value
    @property
    def courier_info(self):
        return self._courier_info

    @courier_info.setter
    def courier_info(self, value):
        if isinstance(value, CarfinCourier):
            self._courier_info = value
        else:
            self._courier_info = CarfinCourier.from_alipay_dict(value)
    @property
    def estimated_delivery_date(self):
        return self._estimated_delivery_date

    @estimated_delivery_date.setter
    def estimated_delivery_date(self, value):
        self._estimated_delivery_date = value
    @property
    def express_no(self):
        return self._express_no

    @express_no.setter
    def express_no(self, value):
        self._express_no = value
    @property
    def file_list(self):
        return self._file_list

    @file_list.setter
    def file_list(self, value):
        if isinstance(value, list):
            self._file_list = list()
            for i in value:
                if isinstance(i, CarfinExpressFile):
                    self._file_list.append(i)
                else:
                    self._file_list.append(CarfinExpressFile.from_alipay_dict(i))
    @property
    def notify_type(self):
        return self._notify_type

    @notify_type.setter
    def notify_type(self, value):
        self._notify_type = value
    @property
    def out_express_no(self):
        return self._out_express_no

    @out_express_no.setter
    def out_express_no(self, value):
        self._out_express_no = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.alert_reason:
            if hasattr(self.alert_reason, 'to_alipay_dict'):
                params['alert_reason'] = self.alert_reason.to_alipay_dict()
            else:
                params['alert_reason'] = self.alert_reason
        if self.courier_info:
            if hasattr(self.courier_info, 'to_alipay_dict'):
                params['courier_info'] = self.courier_info.to_alipay_dict()
            else:
                params['courier_info'] = self.courier_info
        if self.estimated_delivery_date:
            if hasattr(self.estimated_delivery_date, 'to_alipay_dict'):
                params['estimated_delivery_date'] = self.estimated_delivery_date.to_alipay_dict()
            else:
                params['estimated_delivery_date'] = self.estimated_delivery_date
        if self.express_no:
            if hasattr(self.express_no, 'to_alipay_dict'):
                params['express_no'] = self.express_no.to_alipay_dict()
            else:
                params['express_no'] = self.express_no
        if self.file_list:
            if isinstance(self.file_list, list):
                for i in range(0, len(self.file_list)):
                    element = self.file_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.file_list[i] = element.to_alipay_dict()
            if hasattr(self.file_list, 'to_alipay_dict'):
                params['file_list'] = self.file_list.to_alipay_dict()
            else:
                params['file_list'] = self.file_list
        if self.notify_type:
            if hasattr(self.notify_type, 'to_alipay_dict'):
                params['notify_type'] = self.notify_type.to_alipay_dict()
            else:
                params['notify_type'] = self.notify_type
        if self.out_express_no:
            if hasattr(self.out_express_no, 'to_alipay_dict'):
                params['out_express_no'] = self.out_express_no.to_alipay_dict()
            else:
                params['out_express_no'] = self.out_express_no
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
        o = XingheLendassistCarfinExpressstatusNotifyModel()
        if 'alert_reason' in d:
            o.alert_reason = d['alert_reason']
        if 'courier_info' in d:
            o.courier_info = d['courier_info']
        if 'estimated_delivery_date' in d:
            o.estimated_delivery_date = d['estimated_delivery_date']
        if 'express_no' in d:
            o.express_no = d['express_no']
        if 'file_list' in d:
            o.file_list = d['file_list']
        if 'notify_type' in d:
            o.notify_type = d['notify_type']
        if 'out_express_no' in d:
            o.out_express_no = d['out_express_no']
        if 'status' in d:
            o.status = d['status']
        return o


