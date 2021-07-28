#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AoiInfoDTO(object):

    def __init__(self):
        self._aoi_name = None
        self._aoi_tag = None
        self._circle_detail_url = None
        self._tribe_id = None

    @property
    def aoi_name(self):
        return self._aoi_name

    @aoi_name.setter
    def aoi_name(self, value):
        self._aoi_name = value
    @property
    def aoi_tag(self):
        return self._aoi_tag

    @aoi_tag.setter
    def aoi_tag(self, value):
        self._aoi_tag = value
    @property
    def circle_detail_url(self):
        return self._circle_detail_url

    @circle_detail_url.setter
    def circle_detail_url(self, value):
        self._circle_detail_url = value
    @property
    def tribe_id(self):
        return self._tribe_id

    @tribe_id.setter
    def tribe_id(self, value):
        self._tribe_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.aoi_name:
            if hasattr(self.aoi_name, 'to_alipay_dict'):
                params['aoi_name'] = self.aoi_name.to_alipay_dict()
            else:
                params['aoi_name'] = self.aoi_name
        if self.aoi_tag:
            if hasattr(self.aoi_tag, 'to_alipay_dict'):
                params['aoi_tag'] = self.aoi_tag.to_alipay_dict()
            else:
                params['aoi_tag'] = self.aoi_tag
        if self.circle_detail_url:
            if hasattr(self.circle_detail_url, 'to_alipay_dict'):
                params['circle_detail_url'] = self.circle_detail_url.to_alipay_dict()
            else:
                params['circle_detail_url'] = self.circle_detail_url
        if self.tribe_id:
            if hasattr(self.tribe_id, 'to_alipay_dict'):
                params['tribe_id'] = self.tribe_id.to_alipay_dict()
            else:
                params['tribe_id'] = self.tribe_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AoiInfoDTO()
        if 'aoi_name' in d:
            o.aoi_name = d['aoi_name']
        if 'aoi_tag' in d:
            o.aoi_tag = d['aoi_tag']
        if 'circle_detail_url' in d:
            o.circle_detail_url = d['circle_detail_url']
        if 'tribe_id' in d:
            o.tribe_id = d['tribe_id']
        return o


