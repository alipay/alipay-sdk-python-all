#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DeliveryInfoVO import DeliveryInfoVO


class DeliveryDetailInfoVO(object):

    def __init__(self):
        self._delivery_list = None
        self._finish_all_delivery = None
        self._status = None
        self._type = None

    @property
    def delivery_list(self):
        return self._delivery_list

    @delivery_list.setter
    def delivery_list(self, value):
        if isinstance(value, list):
            self._delivery_list = list()
            for i in value:
                if isinstance(i, DeliveryInfoVO):
                    self._delivery_list.append(i)
                else:
                    self._delivery_list.append(DeliveryInfoVO.from_alipay_dict(i))
    @property
    def finish_all_delivery(self):
        return self._finish_all_delivery

    @finish_all_delivery.setter
    def finish_all_delivery(self, value):
        self._finish_all_delivery = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.delivery_list:
            if isinstance(self.delivery_list, list):
                for i in range(0, len(self.delivery_list)):
                    element = self.delivery_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.delivery_list[i] = element.to_alipay_dict()
            if hasattr(self.delivery_list, 'to_alipay_dict'):
                params['delivery_list'] = self.delivery_list.to_alipay_dict()
            else:
                params['delivery_list'] = self.delivery_list
        if self.finish_all_delivery:
            if hasattr(self.finish_all_delivery, 'to_alipay_dict'):
                params['finish_all_delivery'] = self.finish_all_delivery.to_alipay_dict()
            else:
                params['finish_all_delivery'] = self.finish_all_delivery
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DeliveryDetailInfoVO()
        if 'delivery_list' in d:
            o.delivery_list = d['delivery_list']
        if 'finish_all_delivery' in d:
            o.finish_all_delivery = d['finish_all_delivery']
        if 'status' in d:
            o.status = d['status']
        if 'type' in d:
            o.type = d['type']
        return o


