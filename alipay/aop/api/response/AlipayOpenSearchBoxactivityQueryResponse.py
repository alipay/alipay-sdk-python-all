#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.DeliveryTargetRegion import DeliveryTargetRegion
from alipay.aop.api.domain.SearchBoxActivityVideoInfo import SearchBoxActivityVideoInfo


class AlipayOpenSearchBoxactivityQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenSearchBoxactivityQueryResponse, self).__init__()
        self._box_activity_id = None
        self._box_id = None
        self._end_time = None
        self._fail_reason = None
        self._gmt_modified = None
        self._material_type = None
        self._material_url = None
        self._run_status = None
        self._start_time = None
        self._status = None
        self._target_appid = None
        self._target_appname = None
        self._target_regions = None
        self._title = None
        self._video_info = None

    @property
    def box_activity_id(self):
        return self._box_activity_id

    @box_activity_id.setter
    def box_activity_id(self, value):
        self._box_activity_id = value
    @property
    def box_id(self):
        return self._box_id

    @box_id.setter
    def box_id(self, value):
        self._box_id = value
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
    @property
    def fail_reason(self):
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, value):
        self._fail_reason = value
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def material_type(self):
        return self._material_type

    @material_type.setter
    def material_type(self, value):
        self._material_type = value
    @property
    def material_url(self):
        return self._material_url

    @material_url.setter
    def material_url(self, value):
        self._material_url = value
    @property
    def run_status(self):
        return self._run_status

    @run_status.setter
    def run_status(self, value):
        self._run_status = value
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
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

    def parse_response_content(self, response_content):
        response = super(AlipayOpenSearchBoxactivityQueryResponse, self).parse_response_content(response_content)
        if 'box_activity_id' in response:
            self.box_activity_id = response['box_activity_id']
        if 'box_id' in response:
            self.box_id = response['box_id']
        if 'end_time' in response:
            self.end_time = response['end_time']
        if 'fail_reason' in response:
            self.fail_reason = response['fail_reason']
        if 'gmt_modified' in response:
            self.gmt_modified = response['gmt_modified']
        if 'material_type' in response:
            self.material_type = response['material_type']
        if 'material_url' in response:
            self.material_url = response['material_url']
        if 'run_status' in response:
            self.run_status = response['run_status']
        if 'start_time' in response:
            self.start_time = response['start_time']
        if 'status' in response:
            self.status = response['status']
        if 'target_appid' in response:
            self.target_appid = response['target_appid']
        if 'target_appname' in response:
            self.target_appname = response['target_appname']
        if 'target_regions' in response:
            self.target_regions = response['target_regions']
        if 'title' in response:
            self.title = response['title']
        if 'video_info' in response:
            self.video_info = response['video_info']
