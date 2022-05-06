#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DeliveryTargetRegion import DeliveryTargetRegion
from alipay.aop.api.domain.SearchBoxActivityVideoInfo import SearchBoxActivityVideoInfo


class AlipayOpenSearchBoxactivityModifyModel(object):

    def __init__(self):
        self._action_url = None
        self._box_activity_id = None
        self._end_time = None
        self._material_id = None
        self._material_type = None
        self._merchant_id = None
        self._start_time = None
        self._target_appid = None
        self._target_appname = None
        self._target_regions = None
        self._title = None
        self._video_info = None

    @property
    def action_url(self):
        return self._action_url

    @action_url.setter
    def action_url(self, value):
        self._action_url = value
    @property
    def box_activity_id(self):
        return self._box_activity_id

    @box_activity_id.setter
    def box_activity_id(self, value):
        self._box_activity_id = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def material_id(self):
        return self._material_id

    @material_id.setter
    def material_id(self, value):
        self._material_id = value
    @property
    def material_type(self):
        return self._material_type

    @material_type.setter
    def material_type(self, value):
        self._material_type = value
    @property
    def merchant_id(self):
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, value):
        self._merchant_id = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def target_appid(self):
        return self._target_appid

    @target_appid.setter
    def target_appid(self, value):
        self._target_appid = value
    @property
    def target_appname(self):
        return self._target_appname

    @target_appname.setter
    def target_appname(self, value):
        self._target_appname = value
    @property
    def target_regions(self):
        return self._target_regions

    @target_regions.setter
    def target_regions(self, value):
        if isinstance(value, list):
            self._target_regions = list()
            for i in value:
                if isinstance(i, DeliveryTargetRegion):
                    self._target_regions.append(i)
                else:
                    self._target_regions.append(DeliveryTargetRegion.from_alipay_dict(i))
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
    @property
    def video_info(self):
        return self._video_info

    @video_info.setter
    def video_info(self, value):
        if isinstance(value, SearchBoxActivityVideoInfo):
            self._video_info = value
        else:
            self._video_info = SearchBoxActivityVideoInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.action_url:
            if hasattr(self.action_url, 'to_alipay_dict'):
                params['action_url'] = self.action_url.to_alipay_dict()
            else:
                params['action_url'] = self.action_url
        if self.box_activity_id:
            if hasattr(self.box_activity_id, 'to_alipay_dict'):
                params['box_activity_id'] = self.box_activity_id.to_alipay_dict()
            else:
                params['box_activity_id'] = self.box_activity_id
        if self.end_time:
            if hasattr(self.end_time, 'to_alipay_dict'):
                params['end_time'] = self.end_time.to_alipay_dict()
            else:
                params['end_time'] = self.end_time
        if self.material_id:
            if hasattr(self.material_id, 'to_alipay_dict'):
                params['material_id'] = self.material_id.to_alipay_dict()
            else:
                params['material_id'] = self.material_id
        if self.material_type:
            if hasattr(self.material_type, 'to_alipay_dict'):
                params['material_type'] = self.material_type.to_alipay_dict()
            else:
                params['material_type'] = self.material_type
        if self.merchant_id:
            if hasattr(self.merchant_id, 'to_alipay_dict'):
                params['merchant_id'] = self.merchant_id.to_alipay_dict()
            else:
                params['merchant_id'] = self.merchant_id
        if self.start_time:
            if hasattr(self.start_time, 'to_alipay_dict'):
                params['start_time'] = self.start_time.to_alipay_dict()
            else:
                params['start_time'] = self.start_time
        if self.target_appid:
            if hasattr(self.target_appid, 'to_alipay_dict'):
                params['target_appid'] = self.target_appid.to_alipay_dict()
            else:
                params['target_appid'] = self.target_appid
        if self.target_appname:
            if hasattr(self.target_appname, 'to_alipay_dict'):
                params['target_appname'] = self.target_appname.to_alipay_dict()
            else:
                params['target_appname'] = self.target_appname
        if self.target_regions:
            if isinstance(self.target_regions, list):
                for i in range(0, len(self.target_regions)):
                    element = self.target_regions[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.target_regions[i] = element.to_alipay_dict()
            if hasattr(self.target_regions, 'to_alipay_dict'):
                params['target_regions'] = self.target_regions.to_alipay_dict()
            else:
                params['target_regions'] = self.target_regions
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        if self.video_info:
            if hasattr(self.video_info, 'to_alipay_dict'):
                params['video_info'] = self.video_info.to_alipay_dict()
            else:
                params['video_info'] = self.video_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenSearchBoxactivityModifyModel()
        if 'action_url' in d:
            o.action_url = d['action_url']
        if 'box_activity_id' in d:
            o.box_activity_id = d['box_activity_id']
        if 'end_time' in d:
            o.end_time = d['end_time']
        if 'material_id' in d:
            o.material_id = d['material_id']
        if 'material_type' in d:
            o.material_type = d['material_type']
        if 'merchant_id' in d:
            o.merchant_id = d['merchant_id']
        if 'start_time' in d:
            o.start_time = d['start_time']
        if 'target_appid' in d:
            o.target_appid = d['target_appid']
        if 'target_appname' in d:
            o.target_appname = d['target_appname']
        if 'target_regions' in d:
            o.target_regions = d['target_regions']
        if 'title' in d:
            o.title = d['title']
        if 'video_info' in d:
            o.video_info = d['video_info']
        return o


