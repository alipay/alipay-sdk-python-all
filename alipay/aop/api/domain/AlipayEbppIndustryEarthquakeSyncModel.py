#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.MQTTHeaderParam import MQTTHeaderParam


class AlipayEbppIndustryEarthquakeSyncModel(object):

    def __init__(self):
        self._ad_code = None
        self._epi_depth = None
        self._epi_intensity = None
        self._epi_lat = None
        self._epi_lon = None
        self._event_type = None
        self._loc_name = None
        self._magnitude = None
        self._mqtt_header = None
        self._ori_time = None
        self._source = None
        self._source_id = None
        self._warning_level = None

    @property
    def ad_code(self):
        return self._ad_code

    @ad_code.setter
    def ad_code(self, value):
        self._ad_code = value
    @property
    def epi_depth(self):
        return self._epi_depth

    @epi_depth.setter
    def epi_depth(self, value):
        self._epi_depth = value
    @property
    def epi_intensity(self):
        return self._epi_intensity

    @epi_intensity.setter
    def epi_intensity(self, value):
        self._epi_intensity = value
    @property
    def epi_lat(self):
        return self._epi_lat

    @epi_lat.setter
    def epi_lat(self, value):
        self._epi_lat = value
    @property
    def epi_lon(self):
        return self._epi_lon

    @epi_lon.setter
    def epi_lon(self, value):
        self._epi_lon = value
    @property
    def event_type(self):
        return self._event_type

    @event_type.setter
    def event_type(self, value):
        self._event_type = value
    @property
    def loc_name(self):
        return self._loc_name

    @loc_name.setter
    def loc_name(self, value):
        self._loc_name = value
    @property
    def magnitude(self):
        return self._magnitude

    @magnitude.setter
    def magnitude(self, value):
        self._magnitude = value
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
    def ori_time(self):
        return self._ori_time

    @ori_time.setter
    def ori_time(self, value):
        self._ori_time = value
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
    @property
    def warning_level(self):
        return self._warning_level

    @warning_level.setter
    def warning_level(self, value):
        self._warning_level = value


    def to_alipay_dict(self):
        params = dict()
        if self.ad_code:
            if hasattr(self.ad_code, 'to_alipay_dict'):
                params['ad_code'] = self.ad_code.to_alipay_dict()
            else:
                params['ad_code'] = self.ad_code
        if self.epi_depth:
            if hasattr(self.epi_depth, 'to_alipay_dict'):
                params['epi_depth'] = self.epi_depth.to_alipay_dict()
            else:
                params['epi_depth'] = self.epi_depth
        if self.epi_intensity:
            if hasattr(self.epi_intensity, 'to_alipay_dict'):
                params['epi_intensity'] = self.epi_intensity.to_alipay_dict()
            else:
                params['epi_intensity'] = self.epi_intensity
        if self.epi_lat:
            if hasattr(self.epi_lat, 'to_alipay_dict'):
                params['epi_lat'] = self.epi_lat.to_alipay_dict()
            else:
                params['epi_lat'] = self.epi_lat
        if self.epi_lon:
            if hasattr(self.epi_lon, 'to_alipay_dict'):
                params['epi_lon'] = self.epi_lon.to_alipay_dict()
            else:
                params['epi_lon'] = self.epi_lon
        if self.event_type:
            if hasattr(self.event_type, 'to_alipay_dict'):
                params['event_type'] = self.event_type.to_alipay_dict()
            else:
                params['event_type'] = self.event_type
        if self.loc_name:
            if hasattr(self.loc_name, 'to_alipay_dict'):
                params['loc_name'] = self.loc_name.to_alipay_dict()
            else:
                params['loc_name'] = self.loc_name
        if self.magnitude:
            if hasattr(self.magnitude, 'to_alipay_dict'):
                params['magnitude'] = self.magnitude.to_alipay_dict()
            else:
                params['magnitude'] = self.magnitude
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
        if self.ori_time:
            if hasattr(self.ori_time, 'to_alipay_dict'):
                params['ori_time'] = self.ori_time.to_alipay_dict()
            else:
                params['ori_time'] = self.ori_time
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
        if self.warning_level:
            if hasattr(self.warning_level, 'to_alipay_dict'):
                params['warning_level'] = self.warning_level.to_alipay_dict()
            else:
                params['warning_level'] = self.warning_level
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppIndustryEarthquakeSyncModel()
        if 'ad_code' in d:
            o.ad_code = d['ad_code']
        if 'epi_depth' in d:
            o.epi_depth = d['epi_depth']
        if 'epi_intensity' in d:
            o.epi_intensity = d['epi_intensity']
        if 'epi_lat' in d:
            o.epi_lat = d['epi_lat']
        if 'epi_lon' in d:
            o.epi_lon = d['epi_lon']
        if 'event_type' in d:
            o.event_type = d['event_type']
        if 'loc_name' in d:
            o.loc_name = d['loc_name']
        if 'magnitude' in d:
            o.magnitude = d['magnitude']
        if 'mqtt_header' in d:
            o.mqtt_header = d['mqtt_header']
        if 'ori_time' in d:
            o.ori_time = d['ori_time']
        if 'source' in d:
            o.source = d['source']
        if 'source_id' in d:
            o.source_id = d['source_id']
        if 'warning_level' in d:
            o.warning_level = d['warning_level']
        return o


