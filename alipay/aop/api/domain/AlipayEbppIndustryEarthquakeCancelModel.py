#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MQTTHeaderParam import MQTTHeaderParam


class AlipayEbppIndustryEarthquakeCancelModel(object):

    def __init__(self):
        self._mqtt_header = None
        self._source = None
        self._source_id = None

    @property
    def mqtt_header(self):
        return self._mqtt_header

    @mqtt_header.setter
    def mqtt_header(self, value):
        if isinstance(value, list):
            self._mqtt_header = list()
            for i in value:
                if isinstance(i, MQTTHeaderParam):
                    self._mqtt_header.append(i)
                else:
                    self._mqtt_header.append(MQTTHeaderParam.from_alipay_dict(i))
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def source_id(self):
        return self._source_id

    @source_id.setter
    def source_id(self, value):
        self._source_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.mqtt_header:
            if isinstance(self.mqtt_header, list):
                for i in range(0, len(self.mqtt_header)):
                    element = self.mqtt_header[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.mqtt_header[i] = element.to_alipay_dict()
            if hasattr(self.mqtt_header, 'to_alipay_dict'):
                params['mqtt_header'] = self.mqtt_header.to_alipay_dict()
            else:
                params['mqtt_header'] = self.mqtt_header
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.source_id:
            if hasattr(self.source_id, 'to_alipay_dict'):
                params['source_id'] = self.source_id.to_alipay_dict()
            else:
                params['source_id'] = self.source_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppIndustryEarthquakeCancelModel()
        if 'mqtt_header' in d:
            o.mqtt_header = d['mqtt_header']
        if 'source' in d:
            o.source = d['source']
        if 'source_id' in d:
            o.source_id = d['source_id']
        return o


